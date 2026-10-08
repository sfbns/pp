"""Standalone toy design-matrix diagnostics; not a BLP-identification test.

Default execution prints JSON only. --out opts into writing one JSON file.
No imports or rewrites of the original numerical_design_checks.py are needed.
"""

import argparse
import json
import warnings
from pathlib import Path

import numpy as np


def _validated_matrix(values):
    try:
        # Test BEFORE conversion: numpy otherwise drops ndarray imaginary parts
        # with a ComplexWarning, even when those parts are all exactly zero.
        inferred = np.asarray(values)
        if np.iscomplexobj(values) or (inferred.dtype.kind == "O" and any(np.iscomplexobj(item) for item in inferred.flat)):
            raise ValueError("complex values/dtypes are not real-valued input")
        matrix = np.asarray(values, dtype=np.float64)
    except (TypeError, ValueError, OverflowError) as error:
        raise ValueError("matrix must be a rectangular real numeric array") from error
    if matrix.ndim != 2 or min(matrix.shape, default=0) == 0:
        raise ValueError("matrix must be a nonempty two-dimensional array")
    if not np.isfinite(matrix).all():
        raise ValueError("matrix must contain only finite values; NaN/Inf rejected")
    return matrix


def _svd_summary(matrix, relative_tolerance):
    # Uniform rescaling preserves geometry and avoids overflow of finite-input
    # singular values near float64 limits. Rank/ratios use the bounded system;
    # unrepresentable raw-unit magnitudes are explicitly null, never Infinity.
    scale = float(np.max(np.abs(matrix)))
    bounded = matrix / scale if scale else matrix
    singular_values = np.linalg.svd(bounded, compute_uv=False)
    if not np.isfinite(singular_values).all():
        raise ValueError("SVD returned nonfinite values after uniform scaling")
    largest = float(singular_values[0])
    threshold = largest * relative_tolerance
    rank = int(np.count_nonzero(singular_values > threshold))
    smallest = float(singular_values[-1])
    ratio = smallest / largest if largest else 0.0
    # A rank-deficient design has no finite full-column-rank condition number.
    full_column_rank = rank == matrix.shape[1]
    condition = largest / smallest if full_column_rank and smallest else None
    def raw_units(value):
        converted = float(value) * scale
        return converted if np.isfinite(converted) else None
    return {
        "singular_values": [raw_units(x) for x in singular_values],
        "uniform_scale_factor": scale,
        "singular_values_divided_by_scale": singular_values.tolist(),
        "raw_unit_magnitudes_all_representable": all(raw_units(x) is not None for x in singular_values),
        "relative_tolerance": relative_tolerance,
        "absolute_threshold": raw_units(threshold),
        "threshold_divided_by_scale": threshold,
        "rank_computed_in_uniformly_scaled_coordinates": True,
        "rank": rank,
        "full_column_rank": full_column_rank,
        "smallest_to_largest_ratio": ratio,
        "condition_number_if_full_column_rank": condition,
    }


def rank_diagnostics(values, rtol=None, near_ratio=1e-8):
    """Report raw and unit-column-L2 SVD geometry with scale-relative tolerance.

    Default rtol = max(n_rows, n_cols) * float64 epsilon, not an absolute
    cutoff. A nonzero column is normalized in two steps to avoid squaring tiny
    or large entries. Zero columns stay zero without any division by zero.
    Column normalization changes coordinates and is not an identification test.
    """
    matrix = _validated_matrix(values)
    relative_tolerance = (
        max(matrix.shape) * np.finfo(np.float64).eps if rtol is None else float(rtol)
    )
    if not np.isfinite(relative_tolerance) or not 0 < relative_tolerance < 1:
        raise ValueError("rtol must be finite and strictly between zero and one")
    if not np.isfinite(near_ratio) or not 0 < near_ratio < 1:
        raise ValueError("near_ratio must be finite and strictly between zero and one")
    column_max_abs = np.max(np.abs(matrix), axis=0)
    nonzero = column_max_abs > 0
    standardized = np.zeros_like(matrix)
    scaled_l2 = np.zeros(matrix.shape[1], dtype=np.float64)
    if np.any(nonzero):
        bounded = matrix[:, nonzero] / column_max_abs[nonzero]
        scaled_l2[nonzero] = np.linalg.norm(bounded, axis=0)
        standardized[:, nonzero] = bounded / scaled_l2[nonzero]
    raw = _svd_summary(matrix, relative_tolerance)
    scaled = _svd_summary(standardized, relative_tolerance)
    near_collinear = (
        not scaled["full_column_rank"]
        or scaled["smallest_to_largest_ratio"] <= near_ratio
    )
    return {
        "shape": list(matrix.shape),
        "raw": raw,
        "standardized": scaled,
        "column_standardization": {
            "method": "nonzero columns -> unit L2 norm; no centering",
            "max_abs": column_max_abs.tolist(),
            "l2_after_max_abs_division": scaled_l2.tolist(),
            "zero_column_indices": np.flatnonzero(~nonzero).tolist(),
            "zero_columns_kept_zero": True,
        },
        "geometry_diagnostic": {
            "near_collinear_or_rank_deficient": bool(near_collinear),
            "near_ratio_threshold": float(near_ratio),
            "threshold_is_descriptive_not_economic": True,
            "economic_identification_certified": False,
        },
    }


def legacy_absolute_rank(values, tol=1e-10):
    """Original algorithm reproduced only to demonstrate its known scale defect."""
    a = [list(map(float, row)) for row in values]
    n, m, r = len(a), len(a[0]), 0
    for c in range(m):
        i = next((i for i in range(r, n) if abs(a[i][c]) > tol), None)
        if i is None:
            continue
        a[r], a[i] = a[i], a[r]
        pivot = a[r][c]
        a[r] = [v / pivot for v in a[r]]
        for i in range(n):
            if i != r:
                factor = a[i][c]
                a[i] = [x - factor * y for x, y in zip(a[i], a[r])]
        r += 1
        if r == n:
            break
    return r


def run_checks():
    base = np.array([[1, .2], [2, .1], [3, .7], [4, .3]], dtype=np.float64)
    fixtures = [("supported_base", base, 2)]
    for scale in (1e-12, -1e-12, 1e12, -1e12):
        fixtures.append(("overall_scale_" + format(scale, ".0e"), base * scale, 2))
    for name, scales in (
        ("mixed_small_large", [1e-12, 1e12]),
        ("mixed_large_small", [1e12, 1e-12]),
        ("mixed_signed", [-1e-12, 1e12]),
    ):
        mixed = base * np.array(scales)
        fixtures.append((name, mixed, 2))
        for scale in (1e-12, -1e-12, 1e12, -1e12):
            fixtures.append((name + "_overall_" + format(scale, ".0e"), mixed * scale, 2))
    first = base[:, 0]
    fixtures.extend([
        ("duplicate_columns", np.column_stack((first, first)), 1),
        ("zero_column", np.column_stack((first, np.zeros(4))), 1),
        ("zero_matrix", np.zeros((4, 2)), 0),
        ("near_collinear_full_rank", np.column_stack((first, first + 1e-10 * np.array([1., -1., 1., -1.]))), 2),
        ("finite_near_float64_upper_limit", np.array([[1e308,1e308],[1e308,-1e308],[1e308,0],[1e308,1e308]]), 2),
        ("finite_near_float64_lower_limit", base * 1e-308, 2),
        ("wide_full_row_rank", np.array([[1.,0.,1.],[0.,1.,1.]]), 2),
    ])
    checks = []
    for name, matrix, expected_rank in fixtures:
        diagnostics = rank_diagnostics(matrix)
        observed_rank = diagnostics["standardized"]["rank"]
        expected_raw_rank = 1 if name.startswith("mixed_") else expected_rank
        passed = (
            observed_rank == expected_rank
            and diagnostics["raw"]["rank"] == expected_raw_rank
        )
        if name == "near_collinear_full_rank":
            passed = passed and diagnostics["geometry_diagnostic"]["near_collinear_or_rank_deficient"]
        if name == "zero_column":
            passed = passed and diagnostics["column_standardization"]["zero_column_indices"] == [1]
        if name == "zero_matrix":
            passed = passed and diagnostics["standardized"]["absolute_threshold"] == 0.0
        if name == "finite_near_float64_upper_limit":
            passed = passed and diagnostics["raw"]["singular_values"][0] is None and not diagnostics["raw"]["raw_unit_magnitudes_all_representable"]
        # This serializability check is part of the actual regression, not a
        # print-time repair that would hide an earlier Infinity/NaN result.
        json.dumps(diagnostics, allow_nan=False)
        checks.append({
            "name": name,
            "passed": bool(passed),
            "expected_standardized_rank": expected_rank,
            "expected_raw_rank": expected_raw_rank,
            "input": matrix.tolist(),
            "diagnostics": diagnostics,
        })
    invalid_cases = [
        ("nan_rejected", [[1., float("nan")], [2., 3.]]),
        ("positive_inf_rejected", [[1., float("inf")], [2., 3.]]),
        ("negative_inf_rejected", [[1., -float("inf")], [2., 3.]]),
        ("empty_rejected", []),
        ("ragged_rejected", [[1.], [2., 3.]]),
        ("complex_ndarray_positive_imaginary_rejected", np.array([[1.+2.j, 2.], [3., 4.]], dtype=np.complex128)),
        ("complex_ndarray_zero_imaginary_rejected", np.array([[1.+0.j, 2.], [3., 4.]], dtype=np.complex128)),
        ("complex_list_positive_imaginary_rejected", [[1.+2.j, 2.], [3., 4.]]),
        ("complex_list_zero_imaginary_rejected", [[1.+0.j, 2.], [3., 4.]]),
        ("complex_numpy_scalar_in_object_array_rejected", np.array([[np.complex128(1.+2.j), 2.], [3., 4.]], dtype=object)),
    ]
    for name, values in invalid_cases:
        try:
            rank_diagnostics(values)
        except ValueError as error:
            checks.append({"name": name, "passed": True, "rejected_with": str(error)})
        else:
            checks.append({"name": name, "passed": False, "rejected_with": None})
    legacy = {
        "original_absolute_tolerance": 1e-10,
        "unscaled_rank": legacy_absolute_rank(base),
        "scaled_1e_minus_12_rank": legacy_absolute_rank(base * 1e-12),
        "exact_rank_for_both_toy_matrices": 2,
        "original_script_and_original_eight_results_unchanged": "verified separately by byte hashes",
    }
    legacy_ok = legacy["unscaled_rank"] == 2 and legacy["scaled_1e_minus_12_rank"] == 0
    near = next(row for row in checks if row["name"] == "near_collinear_full_rank")
    return {
        "status": "PASS" if legacy_ok and all(row["passed"] for row in checks) else "FAIL",
        "scope": "toy design-matrix numerical geometry only; no real BLP moment Jacobian, instrument exclusion, weak-identification inference or Agent-quality certification",
        "numpy_version": np.__version__,
        "default_rtol_formula": "max(n_rows, n_cols) * np.finfo(np.float64).eps",
        "legacy_defect_reproduced": legacy,
        "summary": {
            "matrix_checks": len(fixtures),
            "invalid_input_rejections": len(invalid_cases),
            "all_standardized_ranks_match_toy_expectations": all(row["passed"] for row in checks),
            "near_collinear_full_rank_flagged": near["diagnostics"]["geometry_diagnostic"]["near_collinear_or_rank_deficient"],
            "near_collinear_does_not_certify_strong_economic_identification": True,
            "raw_relative_svd_not_assumed_invariant_to_individual_column_units": True,
        },
        "checks": checks,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, help="optional explicit JSON output; absent means stdout only")
    args = parser.parse_args()
    with warnings.catch_warnings(record=True) as observed_warnings:
        warnings.simplefilter("always")
        result = run_checks()
    result["captured_warnings"] = [{"category": item.category.__name__, "message": str(item.message)}
                                   for item in observed_warnings]
    result["summary"]["no_warning_promoted_to_success"] = not observed_warnings
    if observed_warnings:
        result["status"] = "FAIL"
    if args.out is not None:
        args.out.write_text(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf8")
    print(json.dumps(result, ensure_ascii=False, separators=(",", ":"), allow_nan=False))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
