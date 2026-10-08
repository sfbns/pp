"""BLP random-coefficients demand skeleton."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

from econ_model_agent.structural.counterfactual import CounterfactualResult
from econ_model_agent.structural.gmm import (
    GMMResult,
    GMMStandardErrors,
    OptimizerDiagnostics,
    finite_difference_jacobian,
    gmm_sandwich_standard_errors,
)


@dataclass
class BLPConfig:
    """Configuration for a BLP demand skeleton."""

    market_id: str
    product_id: str
    share: str
    price: str
    product_characteristics: list[str]
    demand_instruments: list[str]
    random_coefficients: list[str]
    firm_id: str | None = None


class BLPModelSkeleton:
    """Describe BLP objects without doing full numerical estimation."""

    def describe_model(self, config: BLPConfig) -> str:
        """Return a model description."""

        chars = ", ".join(config.product_characteristics)
        rc = ", ".join(config.random_coefficients)
        return (
            "BLP skeleton: 数据应是产品-市场层面，每行由 "
            f"{config.market_id} 和 {config.product_id} 唯一识别，并包含市场份额 {config.share}、价格 {config.price}。"
            f"消费者效用可写为 u_ijm = delta_jm + mu_ijm + epsilon_ijm，其中 delta_jm 包含价格和产品特征({chars})，"
            f"mu_ijm 允许消费者对 {rc} 存在随机系数偏好。市场份额方程把模型预测份额与观察份额匹配。"
            "价格通常内生，因为未观测产品质量同时影响价格和需求。"
        )

    def moment_conditions(self, config: BLPConfig) -> str:
        """Return GMM moment conditions."""

        instruments = ", ".join(config.demand_instruments)
        return (
            f"需求侧工具变量 Z = [{instruments}] 用于处理价格内生性。"
            "BLP 的 GMM moment conditions 是 E[Z_jm * xi_jm(theta)] = 0，"
            "其中 xi_jm(theta) 是由市场份额反演得到的未观测产品质量。"
            "GMM 目标函数 Q(theta) = g(theta)' W g(theta)，估计后可计算需求弹性、替代矩阵和福利变化。"
        )

    def python_code(self, config: BLPConfig) -> str:
        """Return built-in lightweight code plus an optional pyblp skeleton."""

        chars = " + ".join(config.product_characteristics)
        rc_terms = " + ".join(config.random_coefficients)
        instruments = ", ".join(repr(name) for name in config.demand_instruments)
        firm_line = f'product_data["firm_ids"] = product_data["{config.firm_id}"]' if config.firm_id else "# Optional: add firm_ids for supply-side pricing."
        return f'''# Built-in lightweight logit/BLP-style IV-GMM estimator.
# This is useful for toy data, diagnostics, and report scaffolding.
from econ_model_agent.structural.blp import (
    BLPConfig,
    MicroMoment,
    RandomCoefficientsDemandEstimator,
    SimpleLogitDemandEstimator,
    SupplySideBertrandSolver,
)

config = BLPConfig(
    market_id="{config.market_id}",
    product_id="{config.product_id}",
    share="{config.share}",
    price="{config.price}",
    product_characteristics={config.product_characteristics!r},
    demand_instruments={config.demand_instruments!r},
    random_coefficients={config.random_coefficients!r},
    firm_id={config.firm_id!r},
)
estimate = SimpleLogitDemandEstimator(config).fit(df)
print(estimate.summary())
print(estimate.elasticities().head())
subsidy_cf = estimate.simulate_price_counterfactual(df, subsidy=1.0, scenario="unit subsidy")
print(subsidy_cf.summary())

# Nonlinear random-coefficients GMM with optional micro moments.
micro_moments = []
# Example:
# micro_moments = [MicroMoment(name="avg_range", variable="range", target=450.0, weight=1.0)]
rc_estimate = RandomCoefficientsDemandEstimator(config, n_draws=100, seed=123, micro_moments=micro_moments).fit(df)
print(rc_estimate.summary())

# Supply side: recover markups/marginal costs and solve a Bertrand pricing counterfactual.
if config.firm_id is not None:
    supply = SupplySideBertrandSolver().recover_marginal_costs(estimate)
    equilibrium = SupplySideBertrandSolver().solve_equilibrium_prices(estimate, supply.marginal_costs)
    print(equilibrium.summary())

# Optional full pyblp route for production-grade random-coefficients demand.
try:
    import pyblp
except ImportError:
    pyblp = None

if pyblp is not None:
    product_data = df.copy()
    product_data["market_ids"] = product_data["{config.market_id}"]
    product_data["product_ids"] = product_data["{config.product_id}"]
    product_data["shares"] = product_data["{config.share}"]
    product_data["prices"] = product_data["{config.price}"]
    {firm_line}
    for idx, name in enumerate([{instruments}], start=1):
        product_data[f"demand_instruments{{idx}}"] = product_data[name]

    formulations = (
        pyblp.Formulation("0 + prices + {chars}"),
        pyblp.Formulation("0 + {rc_terms}"),
    )
    problem = pyblp.Problem(formulations, product_data)
    # sigma and optimization settings should be chosen after scale checks and instrument diagnostics.
    # results = problem.solve(sigma=np.eye(len({config.random_coefficients!r})))
    # print(results)
'''

    def counterfactual_interface(self, config: BLPConfig) -> str:
        """Return a counterfactual API sketch."""

        return (
            "counterfactual_price_or_subsidy(policy_df): 输入新的价格、补贴或产品特征，"
            "用估计的需求参数重新预测市场份额、需求弹性、企业定价和消费者剩余。"
            "补贴反事实应明确补贴传导到价格的规则，并标注外推到样本外价格区间的风险。"
        )


@dataclass
class ContractionResult:
    """Mean-utility contraction output."""

    delta: np.ndarray
    predicted_shares: np.ndarray
    converged: bool
    iterations: int
    max_error: float


class BLPContractionSolver:
    """Solve BLP-style mean utilities by market-share contraction."""

    def solve(
        self,
        observed_shares: np.ndarray,
        market_ids: np.ndarray,
        mu: np.ndarray | None = None,
        initial_delta: np.ndarray | None = None,
        max_iter: int = 10_000,
        tol: float = 1e-10,
    ) -> ContractionResult:
        """Find mean utilities that match observed shares."""

        observed = np.asarray(observed_shares, dtype=float)
        markets = np.asarray(market_ids)
        self._validate_shares(observed, markets)
        delta = np.zeros_like(observed) if initial_delta is None else np.asarray(initial_delta, dtype=float).copy()
        predicted = self.predict_shares(delta, markets, mu)
        max_error = np.inf
        converged = False
        iterations = 0

        for iterations in range(1, max_iter + 1):
            predicted = np.clip(self.predict_shares(delta, markets, mu), 1e-300, 1.0)
            max_error = float(np.max(np.abs(np.log(observed) - np.log(predicted))))
            if max_error < tol:
                converged = True
                break
            delta += np.log(observed) - np.log(predicted)

        predicted = self.predict_shares(delta, markets, mu)
        return ContractionResult(
            delta=delta,
            predicted_shares=predicted,
            converged=converged,
            iterations=iterations,
            max_error=max_error,
        )

    def predict_shares(
        self,
        delta: np.ndarray,
        market_ids: np.ndarray,
        mu: np.ndarray | None = None,
    ) -> np.ndarray:
        """Predict market shares from mean utility and optional draw utilities."""

        delta_arr = np.asarray(delta, dtype=float)
        markets = np.asarray(market_ids)
        mu_arr = np.zeros((delta_arr.size, 1)) if mu is None else np.asarray(mu, dtype=float)
        if mu_arr.ndim == 1:
            mu_arr = mu_arr[:, None]
        if mu_arr.shape[0] != delta_arr.size:
            raise ValueError("mu must have one row per product-market observation.")

        shares = np.zeros(delta_arr.size)
        for market in pd.unique(markets):
            idx = np.flatnonzero(markets == market)
            utilities = delta_arr[idx, None] + mu_arr[idx, :]
            max_utility = np.maximum(0.0, utilities.max(axis=0))
            exp_utilities = np.exp(utilities - max_utility)
            denominator = np.exp(-max_utility) + exp_utilities.sum(axis=0)
            shares[idx] = (exp_utilities / denominator).mean(axis=1)
        return shares

    @staticmethod
    def _validate_shares(shares: np.ndarray, market_ids: np.ndarray) -> None:
        if np.any(shares <= 0):
            raise ValueError("Observed shares must be strictly positive.")
        for market in pd.unique(market_ids):
            total = float(shares[market_ids == market].sum())
            if total >= 1:
                raise ValueError(f"Observed inside shares in market {market!r} sum to {total}, not below one.")


@dataclass
class BLPDemandResults:
    """Results from the lightweight logit/BLP-style demand estimator."""

    config: BLPConfig
    data: pd.DataFrame
    coefficients: pd.Series
    xi: pd.Series
    fitted_delta: pd.Series
    fitted_shares: pd.Series
    moments: pd.Series
    objective: float
    weighting_matrix: np.ndarray
    diagnostics: dict[str, float | int | bool]
    standard_errors: pd.Series | None = None

    @property
    def price_coefficient(self) -> float:
        """Return the estimated price coefficient."""

        return float(self.coefficients[self.config.price])

    def summary(self) -> str:
        """Return a compact structural-demand summary."""

        coef_lines = ", ".join(f"{key}={value:.4g}" for key, value in self.coefficients.items())
        return (
            "Simple logit IV-GMM demand estimate: "
            f"{coef_lines}; objective={self.objective:.6g}; "
            f"markets={self.diagnostics['n_markets']}; observations={self.diagnostics['n_obs']}."
        )

    def predict_shares(
        self,
        data: pd.DataFrame,
        prices: np.ndarray | pd.Series | None = None,
        include_xi: bool = True,
    ) -> pd.Series:
        """Predict logit shares for a possibly counterfactual dataset."""

        work = data.copy()
        if prices is not None:
            work[self.config.price] = np.asarray(prices, dtype=float)
        estimator = SimpleLogitDemandEstimator(self.config)
        x = estimator.design_matrix(work)
        delta = x @ self.coefficients.to_numpy()
        if include_xi:
            delta = delta + self._matched_xi(work)
        shares = _predict_logit_shares(delta, work[self.config.market_id].to_numpy())
        return pd.Series(shares, index=data.index, name="predicted_share")

    def elasticities(self, data: pd.DataFrame | None = None) -> pd.DataFrame:
        """Return own- and cross-price elasticities for the simple logit model."""

        work = self.data if data is None else data.copy()
        shares = self.predict_shares(work, include_xi=True).to_numpy()
        prices = work[self.config.price].to_numpy(dtype=float)
        markets = work[self.config.market_id].to_numpy()
        products = work[self.config.product_id].to_numpy()
        alpha = self.price_coefficient
        rows: list[dict[str, float | str | bool]] = []

        for market in pd.unique(markets):
            idx = np.flatnonzero(markets == market)
            for row_pos in idx:
                for price_pos in idx:
                    is_own = row_pos == price_pos
                    elasticity = alpha * prices[price_pos] * (
                        (1.0 if is_own else 0.0) - shares[price_pos]
                    )
                    rows.append(
                        {
                            self.config.market_id: market,
                            self.config.product_id: products[row_pos],
                            "price_product_id": products[price_pos],
                            "elasticity": float(elasticity),
                            "own": is_own,
                        }
                    )
        return pd.DataFrame(rows)

    def simulate_price_counterfactual(
        self,
        data: pd.DataFrame,
        price_shift: float = 0.0,
        price_multiplier: float | None = None,
        subsidy: float | dict[str, float] | pd.Series = 0.0,
        scenario: str = "price counterfactual",
    ) -> CounterfactualResult:
        """Simulate demand and consumer-surplus changes after price/subsidy changes."""

        work = data.copy()
        old_prices = work[self.config.price].astype(float)
        new_prices = old_prices + price_shift
        if price_multiplier is not None:
            new_prices = new_prices * price_multiplier
        new_prices = new_prices - self._subsidy_vector(work, subsidy)

        base_delta = self._delta_for_counterfactual(work, old_prices)
        cf_delta = self._delta_for_counterfactual(work, new_prices)
        base_shares = pd.Series(
            _predict_logit_shares(base_delta, work[self.config.market_id].to_numpy()),
            index=work.index,
        )
        cf_shares = pd.Series(
            _predict_logit_shares(cf_delta, work[self.config.market_id].to_numpy()),
            index=work.index,
        )
        result_frame = work[[self.config.market_id, self.config.product_id]].copy()
        result_frame["old_price"] = old_prices
        result_frame["new_price"] = new_prices
        result_frame["base_share"] = base_shares
        result_frame["counterfactual_share"] = cf_shares
        result_frame["share_change"] = cf_shares - base_shares

        cs_change = self._consumer_surplus_change(work, base_delta, cf_delta)
        notes = [
            "Holds unobserved product quality fixed unless the user supplies a new model.",
            "This is a partial-equilibrium demand counterfactual; supply-side price equilibrium is not solved.",
        ]
        if self.price_coefficient >= 0:
            notes.append("Estimated price coefficient is non-negative, so consumer-surplus interpretation is not reliable.")
        return CounterfactualResult(
            scenario=scenario,
            results=result_frame,
            aggregate_effects={
                "total_share_change": float(result_frame["share_change"].sum()),
                "mean_price_change": float((new_prices - old_prices).mean()),
                "consumer_surplus_change": float(cs_change),
            },
            notes=notes,
            metadata={"price_coefficient": self.price_coefficient},
        )

    def _delta_for_counterfactual(self, data: pd.DataFrame, prices: pd.Series) -> np.ndarray:
        work = data.copy()
        work[self.config.price] = prices.to_numpy(dtype=float)
        estimator = SimpleLogitDemandEstimator(self.config)
        return estimator.design_matrix(work) @ self.coefficients.to_numpy() + self._matched_xi(work)

    def _matched_xi(self, data: pd.DataFrame) -> np.ndarray:
        xi_frame = self.data[[self.config.market_id, self.config.product_id]].copy()
        xi_frame["_xi"] = self.xi.to_numpy()
        merged = data[[self.config.market_id, self.config.product_id]].merge(
            xi_frame,
            on=[self.config.market_id, self.config.product_id],
            how="left",
        )
        return merged["_xi"].fillna(0.0).to_numpy(dtype=float)

    def _consumer_surplus_change(
        self,
        data: pd.DataFrame,
        base_delta: np.ndarray,
        cf_delta: np.ndarray,
    ) -> float:
        alpha = self.price_coefficient
        if alpha >= 0:
            return float("nan")
        markets = data[self.config.market_id].to_numpy()
        change = 0.0
        for market in pd.unique(markets):
            idx = np.flatnonzero(markets == market)
            change += (_logsum(cf_delta[idx]) - _logsum(base_delta[idx])) / (-alpha)
        return float(change)

    def _subsidy_vector(
        self,
        data: pd.DataFrame,
        subsidy: float | dict[str, float] | pd.Series,
    ) -> pd.Series:
        if isinstance(subsidy, dict):
            return data[self.config.product_id].map(subsidy).fillna(0.0).astype(float)
        if isinstance(subsidy, pd.Series):
            return subsidy.reindex(data.index).fillna(0.0).astype(float)
        return pd.Series(float(subsidy), index=data.index)


class SimpleLogitDemandEstimator:
    """Estimate aggregate logit demand with IV-GMM moments.

    The estimator implements the transparent baseline block behind many BLP
    workflows: invert shares into mean utility, project mean utility on price
    and characteristics, and discipline price endogeneity with instruments.
    """

    def __init__(self, config: BLPConfig) -> None:
        self.config = config

    @property
    def coefficient_names(self) -> list[str]:
        """Names in the linear mean-utility index."""

        return ["Intercept", self.config.price] + list(self.config.product_characteristics)

    @property
    def instrument_names(self) -> list[str]:
        """Excluded and included instruments."""

        names = ["Intercept"] + list(self.config.demand_instruments) + list(self.config.product_characteristics)
        return list(dict.fromkeys(names))

    def fit(self, data: pd.DataFrame) -> BLPDemandResults:
        """Estimate logit demand by IV-GMM."""

        work = data.reset_index(drop=True).copy()
        self._validate_columns(work)
        observed_shares = work[self.config.share].to_numpy(dtype=float)
        outside = _outside_share_vector(work, self.config.market_id, self.config.share)
        if np.any(outside <= 0):
            raise ValueError("Inside market shares must sum to less than one in every market.")
        if np.any(observed_shares <= 0):
            raise ValueError("Observed product shares must be strictly positive.")

        delta = np.log(observed_shares) - np.log(outside)
        x = self.design_matrix(work)
        z = self.instrument_matrix(work)
        n_obs = x.shape[0]
        weight = np.linalg.pinv((z.T @ z) / n_obs)
        zx = (z.T @ x) / n_obs
        zy = (z.T @ delta) / n_obs
        beta = np.linalg.pinv(zx.T @ weight @ zx) @ (zx.T @ weight @ zy)
        xi = delta - x @ beta
        moments_by_obs = z * xi[:, None]
        mean_moments = moments_by_obs.mean(axis=0)
        objective = float(mean_moments.T @ weight @ mean_moments)
        fitted_delta = x @ beta + xi
        fitted_shares = _predict_logit_shares(fitted_delta, work[self.config.market_id].to_numpy())

        diagnostics: dict[str, float | int | bool] = {
            "n_obs": int(n_obs),
            "n_markets": int(work[self.config.market_id].nunique()),
            "n_parameters": int(x.shape[1]),
            "n_moments": int(z.shape[1]),
            "overidentified": bool(z.shape[1] > x.shape[1]),
            "min_outside_share": float(outside.min()),
            "max_share_error": float(np.max(np.abs(fitted_shares - observed_shares))),
        }
        return BLPDemandResults(
            config=self.config,
            data=work,
            coefficients=pd.Series(beta, index=self.coefficient_names),
            xi=pd.Series(xi, index=work.index, name="xi"),
            fitted_delta=pd.Series(fitted_delta, index=work.index, name="delta"),
            fitted_shares=pd.Series(fitted_shares, index=work.index, name="fitted_share"),
            moments=pd.Series(mean_moments, index=self.instrument_names),
            objective=objective,
            weighting_matrix=weight,
            diagnostics=diagnostics,
            standard_errors=self._standard_errors(work, x, z, xi, weight),
        )

    def design_matrix(self, data: pd.DataFrame) -> np.ndarray:
        """Return X: intercept, price, and product characteristics."""

        arrays = [np.ones(len(data)), data[self.config.price].to_numpy(dtype=float)]
        arrays.extend(data[name].to_numpy(dtype=float) for name in self.config.product_characteristics)
        return np.column_stack(arrays)

    def instrument_matrix(self, data: pd.DataFrame) -> np.ndarray:
        """Return Z: intercept, excluded instruments, and included characteristics."""

        arrays: list[np.ndarray] = []
        for name in self.instrument_names:
            if name == "Intercept":
                arrays.append(np.ones(len(data)))
            else:
                arrays.append(data[name].to_numpy(dtype=float))
        return np.column_stack(arrays)

    def _validate_columns(self, data: pd.DataFrame) -> None:
        required = [
            self.config.market_id,
            self.config.product_id,
            self.config.share,
            self.config.price,
            *self.config.product_characteristics,
            *self.config.demand_instruments,
        ]
        missing = [name for name in required if name not in data.columns]
        if missing:
            raise ValueError(f"Missing required BLP columns: {missing}")

    def _standard_errors(
        self,
        data: pd.DataFrame,
        x: np.ndarray,
        z: np.ndarray,
        xi: np.ndarray,
        weight: np.ndarray,
    ) -> pd.Series:
        """Compute linear IV-GMM sandwich standard errors."""

        n_obs = x.shape[0]
        moments = z * xi[:, None]
        jacobian = -(z.T @ x / n_obs)
        centered = moments - moments.mean(axis=0)
        moment_covariance = centered.T @ centered / n_obs
        bread = np.linalg.pinv(jacobian.T @ weight @ jacobian)
        covariance = bread @ (jacobian.T @ weight @ moment_covariance @ weight @ jacobian) @ bread / n_obs
        values = np.sqrt(np.maximum(np.diag(covariance), 0.0))
        return pd.Series(values, index=self.coefficient_names, name="std_error")


@dataclass
class MicroMoment:
    """A simple micro moment that targets a share-weighted product statistic."""

    name: str
    variable: str
    target: float
    weight: float = 1.0


@dataclass
class RandomCoefficientsDemandResults:
    """Results from simulated random-coefficients nonlinear GMM."""

    config: BLPConfig
    data: pd.DataFrame
    nonlinear_params: pd.Series
    linear_coefficients: pd.Series
    delta: pd.Series
    xi: pd.Series
    fitted_shares: pd.Series
    moments: pd.Series
    objective: float
    weighting_matrix: np.ndarray
    draws: np.ndarray
    micro_moments: list[MicroMoment]
    optimizer_result: GMMResult
    standard_errors: pd.Series | None

    @property
    def price_coefficient(self) -> float:
        return float(self.linear_coefficients[self.config.price])

    @property
    def coefficient_names(self) -> list[str]:
        return list(self.nonlinear_params.index) + list(self.linear_coefficients.index)

    def summary(self) -> str:
        nonlinear = ", ".join(f"{key}={value:.4g}" for key, value in self.nonlinear_params.items())
        linear = ", ".join(f"{key}={value:.4g}" for key, value in self.linear_coefficients.items())
        return f"Random-coefficients nonlinear GMM: sigma[{nonlinear}], beta[{linear}], objective={self.objective:.6g}."

    def predict_shares(
        self,
        data: pd.DataFrame,
        prices: np.ndarray | pd.Series | None = None,
        include_xi: bool = True,
    ) -> pd.Series:
        """Predict random-coefficients shares with fixed estimated parameters."""

        work = data.copy()
        if prices is not None:
            work[self.config.price] = np.asarray(prices, dtype=float)
        estimator = RandomCoefficientsDemandEstimator(
            self.config,
            n_draws=self.draws.shape[0],
            seed=123,
            micro_moments=self.micro_moments,
        )
        estimator.draws_ = self.draws
        delta = estimator.design_matrix(work) @ self.linear_coefficients.to_numpy()
        if include_xi:
            delta = delta + self._matched_xi(work)
        mu = estimator.random_utility(work, self.nonlinear_params.to_numpy())
        shares = BLPContractionSolver().predict_shares(delta, work[self.config.market_id].to_numpy(), mu)
        return pd.Series(shares, index=data.index, name="predicted_share")

    def elasticities(self, data: pd.DataFrame | None = None, price_step: float = 1e-4) -> pd.DataFrame:
        """Compute numerical own/cross price elasticities."""

        work = self.data if data is None else data.copy()
        base_prices = work[self.config.price].to_numpy(dtype=float)
        base_shares = self.predict_shares(work).to_numpy()
        markets = work[self.config.market_id].to_numpy()
        products = work[self.config.product_id].to_numpy()
        rows: list[dict[str, float | str | bool]] = []

        for market in pd.unique(markets):
            idx = np.flatnonzero(markets == market)
            for price_pos in idx:
                perturbed = base_prices.copy()
                step = price_step * max(abs(base_prices[price_pos]), 1.0)
                perturbed[price_pos] += step
                new_shares = self.predict_shares(work, prices=perturbed).to_numpy()
                derivative = (new_shares[idx] - base_shares[idx]) / step
                for row_pos, dsdp in zip(idx, derivative):
                    elasticity = dsdp * base_prices[price_pos] / max(base_shares[row_pos], 1e-300)
                    rows.append(
                        {
                            self.config.market_id: market,
                            self.config.product_id: products[row_pos],
                            "price_product_id": products[price_pos],
                            "elasticity": float(elasticity),
                            "own": row_pos == price_pos,
                        }
                    )
        return pd.DataFrame(rows)

    def simulate_price_counterfactual(
        self,
        data: pd.DataFrame,
        price_shift: float = 0.0,
        price_multiplier: float | None = None,
        subsidy: float | dict[str, float] | pd.Series = 0.0,
        scenario: str = "random-coefficients price counterfactual",
    ) -> CounterfactualResult:
        """Partial-equilibrium counterfactual with random coefficients."""

        work = data.copy()
        old_prices = work[self.config.price].astype(float)
        new_prices = old_prices + price_shift
        if price_multiplier is not None:
            new_prices = new_prices * price_multiplier
        new_prices = new_prices - self._subsidy_vector(work, subsidy)
        base_shares = self.predict_shares(work, prices=old_prices)
        cf_shares = self.predict_shares(work, prices=new_prices)
        frame = work[[self.config.market_id, self.config.product_id]].copy()
        frame["old_price"] = old_prices
        frame["new_price"] = new_prices
        frame["base_share"] = base_shares
        frame["counterfactual_share"] = cf_shares
        frame["share_change"] = cf_shares - base_shares
        return CounterfactualResult(
            scenario=scenario,
            results=frame,
            aggregate_effects={
                "total_share_change": float(frame["share_change"].sum()),
                "mean_price_change": float((new_prices - old_prices).mean()),
            },
            notes=["Partial-equilibrium random-coefficients demand counterfactual."],
        )

    def _matched_xi(self, data: pd.DataFrame) -> np.ndarray:
        xi_frame = self.data[[self.config.market_id, self.config.product_id]].copy()
        xi_frame["_xi"] = self.xi.to_numpy()
        merged = data[[self.config.market_id, self.config.product_id]].merge(
            xi_frame,
            on=[self.config.market_id, self.config.product_id],
            how="left",
        )
        return merged["_xi"].fillna(0.0).to_numpy(dtype=float)

    def _subsidy_vector(
        self,
        data: pd.DataFrame,
        subsidy: float | dict[str, float] | pd.Series,
    ) -> pd.Series:
        if isinstance(subsidy, dict):
            return data[self.config.product_id].map(subsidy).fillna(0.0).astype(float)
        if isinstance(subsidy, pd.Series):
            return subsidy.reindex(data.index).fillna(0.0).astype(float)
        return pd.Series(float(subsidy), index=data.index)


class RandomCoefficientsDemandEstimator(SimpleLogitDemandEstimator):
    """Simulated random-coefficients nonlinear GMM with contraction mapping."""

    def __init__(
        self,
        config: BLPConfig,
        n_draws: int = 100,
        seed: int = 123,
        micro_moments: list[MicroMoment] | None = None,
    ) -> None:
        super().__init__(config)
        self.n_draws = n_draws
        self.seed = seed
        self.micro_moments = micro_moments or []
        self.draws_: np.ndarray | None = None

    @property
    def nonlinear_names(self) -> list[str]:
        return [f"sigma_{name}" for name in self.config.random_coefficients]

    def fit(
        self,
        data: pd.DataFrame,
        initial_sigma: np.ndarray | None = None,
        step_size: float = 0.25,
        max_iter: int = 200,
        tol: float = 1e-7,
    ) -> RandomCoefficientsDemandResults:
        """Estimate nonlinear random-coefficients parameters by GMM."""

        work = data.reset_index(drop=True).copy()
        self._validate_columns(work)
        self._validate_random_coefficients(work)
        self.draws_ = self._draws()
        initial = np.full(len(self.config.random_coefficients), 0.1) if initial_sigma is None else np.asarray(initial_sigma, dtype=float)

        def moments(params: np.ndarray) -> np.ndarray:
            params = np.maximum(params, 0.0)
            block = self._evaluate_sigma(work, params)
            return block["moments_by_obs"]

        optimizer = _BoundedGMMEstimator(lower_bound=0.0)
        result = optimizer.fit(moments, initial, step_size=step_size, max_iter=max_iter, tol=tol)
        sigma = np.maximum(result.params, 0.0)
        block = self._evaluate_sigma(work, sigma)
        stderr = self._standard_errors(work, sigma, block["weight"])
        return RandomCoefficientsDemandResults(
            config=self.config,
            data=work,
            nonlinear_params=pd.Series(sigma, index=self.nonlinear_names),
            linear_coefficients=pd.Series(block["beta"], index=self.coefficient_names),
            delta=pd.Series(block["delta"], index=work.index, name="delta"),
            xi=pd.Series(block["xi"], index=work.index, name="xi"),
            fitted_shares=pd.Series(block["fitted_shares"], index=work.index, name="fitted_share"),
            moments=pd.Series(block["mean_moments"], index=self._moment_names()),
            objective=float(block["objective"]),
            weighting_matrix=block["weight"],
            draws=self.draws_,
            micro_moments=self.micro_moments,
            optimizer_result=result,
            standard_errors=stderr,
        )

    def random_utility(self, data: pd.DataFrame, sigma: np.ndarray) -> np.ndarray:
        """Return product-draw utility deviations mu_jr."""

        draws = self._draws() if self.draws_ is None else self.draws_
        columns = [data[name].to_numpy(dtype=float) for name in self.config.random_coefficients]
        x_random = np.column_stack(columns)
        return (x_random * np.asarray(sigma, dtype=float)) @ draws.T

    def _evaluate_sigma(self, data: pd.DataFrame, sigma: np.ndarray) -> dict[str, np.ndarray | float]:
        observed = data[self.config.share].to_numpy(dtype=float)
        markets = data[self.config.market_id].to_numpy()
        mu = self.random_utility(data, sigma)
        contraction = BLPContractionSolver().solve(observed, markets, mu=mu, max_iter=5_000, tol=1e-9)
        x = self.design_matrix(data)
        z = self.instrument_matrix(data)
        beta, xi, weight = _iv_gmm_beta(contraction.delta, x, z)
        demand_moments = z * xi[:, None]
        micro_values = self._micro_moment_errors(data, contraction.delta, sigma)
        if micro_values.size:
            micro_block = np.tile(micro_values, (len(data), 1))
            moments_by_obs = np.column_stack([demand_moments, micro_block])
        else:
            moments_by_obs = demand_moments
        mean_moments = moments_by_obs.mean(axis=0)
        full_weight = np.eye(mean_moments.size)
        full_weight[: weight.shape[0], : weight.shape[1]] = weight
        objective = float(mean_moments.T @ full_weight @ mean_moments)
        return {
            "beta": beta,
            "xi": xi,
            "delta": contraction.delta,
            "fitted_shares": contraction.predicted_shares,
            "moments_by_obs": moments_by_obs,
            "mean_moments": mean_moments,
            "weight": full_weight,
            "objective": objective,
        }

    def _micro_moment_errors(self, data: pd.DataFrame, delta: np.ndarray, sigma: np.ndarray) -> np.ndarray:
        if not self.micro_moments:
            return np.array([])
        shares = BLPContractionSolver().predict_shares(delta, data[self.config.market_id].to_numpy(), self.random_utility(data, sigma))
        inside_share = max(float(shares.sum()), 1e-300)
        errors = []
        for moment in self.micro_moments:
            predicted = float(np.sum(data[moment.variable].to_numpy(dtype=float) * shares) / inside_share)
            errors.append(moment.weight * (predicted - moment.target))
        return np.asarray(errors)

    def _standard_errors(
        self,
        data: pd.DataFrame,
        sigma: np.ndarray,
        weighting_matrix: np.ndarray,
    ) -> pd.Series | None:
        def all_moments(params: np.ndarray) -> np.ndarray:
            sigma_params = np.maximum(params[: len(self.nonlinear_names)], 0.0)
            block = self._evaluate_sigma(data, sigma_params)
            # Linear params are profiled out in this lightweight implementation,
            # so the reported SEs cover nonlinear parameters only.
            return block["moments_by_obs"]

        try:
            se = gmm_sandwich_standard_errors(all_moments, sigma, weighting_matrix)
        except np.linalg.LinAlgError:
            return None
        return pd.Series(se.standard_errors, index=self.nonlinear_names, name="std_error")

    def _draws(self) -> np.ndarray:
        if self.draws_ is None:
            rng = np.random.default_rng(self.seed)
            self.draws_ = rng.normal(size=(self.n_draws, len(self.config.random_coefficients)))
        return self.draws_

    def _moment_names(self) -> list[str]:
        return self.instrument_names + [moment.name for moment in self.micro_moments]

    def _validate_random_coefficients(self, data: pd.DataFrame) -> None:
        missing = [name for name in self.config.random_coefficients if name not in data.columns]
        if missing:
            raise ValueError(f"Missing random coefficient columns: {missing}")


@dataclass
class SupplySideResults:
    """Bertrand supply-side recovered markups and marginal costs."""

    data: pd.DataFrame
    markups: pd.Series
    marginal_costs: pd.Series
    ownership_matrix: dict[str, np.ndarray]
    diagnostics: dict[str, float | int | bool]


class SupplySideBertrandSolver:
    """Recover and simulate multi-product Bertrand pricing."""

    def recover_marginal_costs(
        self,
        demand_results: BLPDemandResults | RandomCoefficientsDemandResults,
        data: pd.DataFrame | None = None,
    ) -> SupplySideResults:
        """Recover marginal costs from prices, shares, and demand derivatives."""

        work = demand_results.data.copy() if data is None else data.copy()
        prices = work[demand_results.config.price].to_numpy(dtype=float)
        shares = demand_results.predict_shares(work).to_numpy()
        markets = work[demand_results.config.market_id].to_numpy()
        markups = np.zeros(len(work))
        ownership_by_market: dict[str, np.ndarray] = {}
        for market in pd.unique(markets):
            idx = np.flatnonzero(markets == market)
            derivative = self._derivative_matrix(demand_results, work, idx)
            ownership = self._ownership_matrix(demand_results.config, work.iloc[idx])
            ownership_by_market[str(market)] = ownership
            omega = ownership * derivative
            markups[idx] = -np.linalg.pinv(omega) @ shares[idx]
        marginal_costs = prices - markups
        diagnostics = {
            "n_markets": int(work[demand_results.config.market_id].nunique()),
            "mean_markup": float(markups.mean()),
            "min_marginal_cost": float(marginal_costs.min()),
        }
        return SupplySideResults(
            data=work,
            markups=pd.Series(markups, index=work.index, name="markup"),
            marginal_costs=pd.Series(marginal_costs, index=work.index, name="marginal_cost"),
            ownership_matrix=ownership_by_market,
            diagnostics=diagnostics,
        )

    def solve_equilibrium_prices(
        self,
        demand_results: BLPDemandResults | RandomCoefficientsDemandResults,
        marginal_costs: pd.Series | np.ndarray,
        data: pd.DataFrame | None = None,
        max_iter: int = 500,
        tol: float = 1e-8,
        damping: float = 0.5,
    ) -> CounterfactualResult:
        """Solve a fixed-point Bertrand price equilibrium."""

        work = demand_results.data.copy() if data is None else data.copy()
        costs = np.asarray(marginal_costs, dtype=float)
        prices = work[demand_results.config.price].to_numpy(dtype=float).copy()
        markets = work[demand_results.config.market_id].to_numpy()
        converged = False
        max_error = np.inf
        iterations = 0
        for iterations in range(1, max_iter + 1):
            new_prices = prices.copy()
            work[demand_results.config.price] = prices
            shares = demand_results.predict_shares(work, prices=prices).to_numpy()
            for market in pd.unique(markets):
                idx = np.flatnonzero(markets == market)
                derivative = self._derivative_matrix(demand_results, work, idx)
                ownership = self._ownership_matrix(demand_results.config, work.iloc[idx])
                omega = ownership * derivative
                markup = -np.linalg.pinv(omega) @ shares[idx]
                new_prices[idx] = costs[idx] + markup
            max_error = float(np.max(np.abs(new_prices - prices)))
            prices = damping * new_prices + (1.0 - damping) * prices
            if max_error < tol:
                converged = True
                break
        frame = work[[demand_results.config.market_id, demand_results.config.product_id]].copy()
        frame["equilibrium_price"] = prices
        frame["marginal_cost"] = costs
        frame["markup"] = prices - costs
        return CounterfactualResult(
            scenario="Bertrand equilibrium pricing",
            results=frame,
            aggregate_effects={
                "mean_equilibrium_price": float(prices.mean()),
                "mean_markup": float((prices - costs).mean()),
                "max_price_error": float(max_error),
            },
            notes=["Solves a damped fixed point using recovered demand derivatives."],
            metadata={"converged": converged, "iterations": iterations},
        )

    def _derivative_matrix(
        self,
        demand_results: BLPDemandResults | RandomCoefficientsDemandResults,
        data: pd.DataFrame,
        idx: np.ndarray,
        step_scale: float = 1e-5,
    ) -> np.ndarray:
        base_prices = data[demand_results.config.price].to_numpy(dtype=float)
        base_shares = demand_results.predict_shares(data, prices=base_prices).to_numpy()[idx]
        derivative = np.zeros((idx.size, idx.size))
        for col, global_pos in enumerate(idx):
            perturbed = base_prices.copy()
            step = step_scale * max(abs(base_prices[global_pos]), 1.0)
            perturbed[global_pos] += step
            new_shares = demand_results.predict_shares(data, prices=perturbed).to_numpy()[idx]
            derivative[:, col] = (new_shares - base_shares) / step
        return derivative

    @staticmethod
    def _ownership_matrix(config: BLPConfig, data: pd.DataFrame) -> np.ndarray:
        if config.firm_id is None or config.firm_id not in data.columns:
            return np.eye(len(data))
        firms = data[config.firm_id].to_numpy()
        return (firms[:, None] == firms[None, :]).astype(float)


class SMMEstimator:
    """Simulated method of moments estimator for small structural skeletons."""

    def fit(
        self,
        simulator,
        observed_moments: np.ndarray,
        initial_params: np.ndarray,
        weighting_matrix: np.ndarray | None = None,
        step_size: float = 0.25,
        max_iter: int = 500,
        tol: float = 1e-8,
    ) -> GMMResult:
        """Estimate parameters by matching simulated to observed moments."""

        target = np.asarray(observed_moments, dtype=float)

        def moments(params: np.ndarray) -> np.ndarray:
            simulated = np.asarray(simulator(params), dtype=float)
            return simulated - target

        return _BoundedGMMEstimator(lower_bound=None).fit(
            moments,
            np.asarray(initial_params, dtype=float),
            weighting_matrix=weighting_matrix,
            step_size=step_size,
            max_iter=max_iter,
            tol=tol,
        )


class _BoundedGMMEstimator:
    """Coordinate-search GMM with optional lower bound."""

    def __init__(self, lower_bound: float | None = None) -> None:
        self.lower_bound = lower_bound

    def objective(self, params: np.ndarray, moments, weighting_matrix: np.ndarray | None = None) -> float:
        raw = np.asarray(moments(params), dtype=float)
        mean = raw if raw.ndim == 1 else raw.mean(axis=0)
        weight = np.eye(mean.size) if weighting_matrix is None else weighting_matrix
        return float(mean.T @ weight @ mean)

    def fit(
        self,
        moments,
        initial_params: np.ndarray,
        weighting_matrix: np.ndarray | None = None,
        step_size: float = 0.25,
        max_iter: int = 500,
        tol: float = 1e-8,
    ) -> GMMResult:
        params = self._bound(np.asarray(initial_params, dtype=float).copy())
        step = float(step_size)
        best = self.objective(params, moments, weighting_matrix)
        diagnostics = OptimizerDiagnostics(
            objective_history=[best],
            step_history=[step],
            convergence_reason="running",
            evaluations=1,
        )
        converged = False
        iterations = 0
        for iterations in range(1, max_iter + 1):
            improved = False
            for pos in range(params.size):
                for direction in (1.0, -1.0):
                    candidate = params.copy()
                    candidate[pos] += direction * step
                    candidate = self._bound(candidate)
                    value = self.objective(candidate, moments, weighting_matrix)
                    diagnostics.evaluations += 1
                    if value + tol < best:
                        params = candidate
                        best = value
                        improved = True
            if not improved:
                step *= 0.5
            diagnostics.objective_history.append(best)
            diagnostics.step_history.append(step)
            if step < tol:
                converged = True
                diagnostics.convergence_reason = "step_below_tolerance"
                break
        if not converged:
            diagnostics.convergence_reason = "max_iter_reached"
        raw = np.asarray(moments(params), dtype=float)
        mean = raw if raw.ndim == 1 else raw.mean(axis=0)
        weight = np.eye(mean.size) if weighting_matrix is None else weighting_matrix
        try:
            jacobian = finite_difference_jacobian(lambda values: np.asarray(moments(values)).mean(axis=0), params)
            diagnostics.gradient_norm = float(np.linalg.norm(2.0 * jacobian.T @ weight @ mean))
        except Exception:
            diagnostics.warnings.append("Could not compute finite-difference gradient diagnostics.")
        return GMMResult(
            params=params,
            objective=best,
            moments=mean,
            weighting_matrix=weight,
            converged=converged,
            iterations=iterations,
            step_size=step,
            diagnostics=diagnostics,
        )

    def _bound(self, params: np.ndarray) -> np.ndarray:
        if self.lower_bound is None:
            return params
        return np.maximum(params, self.lower_bound)


def _outside_share_vector(data: pd.DataFrame, market_id: str, share: str) -> np.ndarray:
    inside_sum = data.groupby(market_id)[share].transform("sum").to_numpy(dtype=float)
    return 1.0 - inside_sum


def _iv_gmm_beta(delta: np.ndarray, x: np.ndarray, z: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    n_obs = x.shape[0]
    weight = np.linalg.pinv((z.T @ z) / n_obs)
    zx = (z.T @ x) / n_obs
    zy = (z.T @ delta) / n_obs
    beta = np.linalg.pinv(zx.T @ weight @ zx) @ (zx.T @ weight @ zy)
    xi = delta - x @ beta
    return beta, xi, weight


def _predict_logit_shares(delta: np.ndarray, market_ids: np.ndarray) -> np.ndarray:
    values = np.asarray(delta, dtype=float)
    markets = np.asarray(market_ids)
    shares = np.zeros(values.size)
    for market in pd.unique(markets):
        idx = np.flatnonzero(markets == market)
        market_delta = values[idx]
        max_delta = max(0.0, float(np.max(market_delta)))
        exp_delta = np.exp(market_delta - max_delta)
        denominator = np.exp(-max_delta) + exp_delta.sum()
        shares[idx] = exp_delta / denominator
    return shares


def _logsum(delta: np.ndarray) -> float:
    max_delta = max(0.0, float(np.max(delta)))
    return float(max_delta + np.log(np.exp(-max_delta) + np.exp(delta - max_delta).sum()))
