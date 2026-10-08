# The Evolution of Market Power in the US Automobile Industry∗ \*

Paul L. E. Grieco† Charles Murry‡ Ali Yurukoglu§

March 9, 2023

## Abstract

We construct measures of industry performance and welfare in the U.S. automobile market from 1980 to 2018. We estimate a demand model using product level data on market shares, prices, and attributes, and consumer level data on demographics, purchases, and stated second choices. We estimate marginal costs assuming Nash-Bertrand pricing. We relate trends in consumer welfare and markups to trends in market structure and the composition of products. Although real prices rose, we find that markups decreased substantially, and the fraction of total surplus accruing to consumers increased. Consumer welfare increased over time due to improved product quality and improved production technology.

JEL Codes: L11, L62, D43

## 1 Introduction

From 1980 to 2018, the U.S. automobile industry experienced numerous technological and regulatory changes and its market structure changed dramatically. The goal of this paper is to examine whether these changes led to discernible changes in industry performance. This work complements a recent academic and policy literature analyzing long-term trends in market power and sales concentration from a macroeconomic perspective (De Loecker et al., 2020; Autor et al., 2020) with an industry-specific approach. Several papers and commentators point to a competition problem where price-cost margins and industry concentration have increased during this time period (Economist, 2016; Covarrubias et al., 2020). We find that, in this industry, the situation for consumers has improved noticeably over time. Our estimates of price-cost margins for this industry differ from those computed using methods and data from the recent macroeconomics literature that indicate declining markups. Furthermore, our approach—in contrast to the recent literature—admits a measure of consumer surplus over time. We find that consumer welfare in the U.S automobile market has increased significantly over this period, primarily due to improvements in product quality and production technology.

To estimate trends in industry performance in the U.S. new car industry, we specify a heterogeneous agent demand system and assume Nash-Bertrand pricing by multi-product automobile manufacturers. The key inputs into the demand estimates are aggregate data on prices, market shares, and vehicle characteristics over time, microdata on the relationship between demographics and car characteristics over time, microdata on consumers’ stated second choices, and the use of the real exchange rate between the US and product origin countries as an instrumental variable for endogenous prices. With the demand system in hand, we infer product level markups from the first order condition of each firm’s profit maximization problem.

We find that median markups as defined by the Lerner index $\begin{array} { r } { ( L = \frac { p - m c } { p } ) } \end{array}$ fell from 0.325 in 1980 to 0.185 by 2018 (Figure VI). However, as we detail below, although markups are useful proxy for market efficiency when products are fixed over time, they are a conceptually unattractive measure over long periods of time when products change. We use our model to consider trends in consumer and producer surplus directly. To quantify changes in welfare over time, we utilize a decomposition from Pakes et al. (1993) to develop a measure of consumer surplus that is robust to changes in the attractiveness of the outside good. This approach leverages continuing products to capture changes in unobserved automobile quality over time. However, it is not influenced by aggregate fluctuations in demand for automobiles e.g., business cycle effects such as monetary policy or changes in alternative transportation options. We find that the fraction of efficient surplus going to consumers went from 0.62 in 1980 to 0.82 by 2018 and that average consumer surplus per household increased by roughly \$8,000 over our sample period.

The increase in consumer surplus is predominantly due to the increasing quality of cars and improved production technology. We confirm the patterns in Knittel (2011) that horsepower, size, and fuel efficiency have improved significantly over this time period. We use the estimated valuations of these car attributes to put a dollar amount on this improvement. Furthermore, we use market shares of continuing products to estimate the combined valuation of improvements in other characteristics such as electronics, safety, or comfort features that are not readily available in common data sets (e.g., audio and entertainment systems, rear-view cameras, driver assistance systems). Improvements on these dimensions are quantitatively large. Additionally, we estimate improved production technology from variation in marginal cost over time controlling for product attributes. Counterfactuals that eliminate the observed increase in import competition or the increase in the number of vehicle models have small to moderate effects on consumer surplus. Counterfactuals that eliminate the increase in automobile quality and the technological improvements in production have the greatest effect on consumer surplus.

A number of caveats are warranted for this analysis. First, our main results assume static Nash-Bertrand pricing each year and rule out changes in conduct, for example via the ability to tacitly collude. However, for robustness, we present a number of alternative assumptions on conduct, all of which indicate declining markups. Second, we do not model the complementary dealer, parts, or financing markets where the behavior of margins or product market efficiency over time may be different than for the automobile manufacturers.

By studying long-run trends in market power and market efficiency using the workhorse toolbox of supply and demand estimation, we provide an alternative perspective on the analysis of the recent literature on the rise in aggregate markups based on production-side modeling and accounting data on revenues and costs, for example De Loecker et al. (2020) and various subsequent studies. This approach infers markups at the firm level under the assumption that firms optimally choose the quantity of variable inputs in production in order to minimize costs. The assumptions of these two approaches are non-nested; we provide a comparison of our markup estimates in the US automobile industry with those constructed by De Loecker et al. (2020) in Section 5.6. Our perspective is rooted in the methods developed in industrial organization that grew out of the critique of the Structure-Conduct-Performance literature, for example Demsetz (1973), and for a historical perspective see Berry et al. (2019). Our approach also allows for an understanding of the mechanisms that contribute to trends in market power and consumer surplus. In particular, we highlight the importance of characterizing consumer welfare, which is only possible by estimating demand curves.

While we focus on a single industry, our results suggest that more work should be done to carefully measure market power and welfare in important industries in order to provide an alternative measurement from the production approach and to identify the mechanisms that drive trends in market power and efficiency. This work thus complements research that raises measurement issues and proposes alternatives within the production paradigm such as Traina (2021), Raval (2022), Demirer (2020), Bond et al. (2021), Doraszelski and Jaumandreu (2021), and Foster et al. (2022).

There are now other recent examples of researchers using demand and supply to characterize trends in markups in specific industries.1 Brand (2020) and Döpper et al. (2021) analyze multiple grocery categories for a selection of retail outlets over the period 2006 to 2017 and 2019, respectively. Miller et al. (2022) analyze the cement industry over the years 1976 to 2016. Ganapati (2021) studies the wholesaling sector over the period 1997 to 2007. Relative to these papers, this paper uses household level data on purchases, demographics, and second choice data to estimate a demand specification with rich heterogeneity and employs standard instrumental variable identification strategies. This paper also compares its markup estimates with production function based estimates as reported in De Loecker et al. (2020) and analyzes the determinants of the change in consumer surplus over time. Bet (2021) compares markup estimates from a demand approach with those from a production approach for domestic airlines and finds that, under Nash-Bertrand pricing, markups from the demand approach are flat for large carriers while under the production approach, markups for large carriers are increasing over the period 2013 to 2019. Relative to these other papers, our work estimates the role of technological progress in improving consumer surplus by decomposing over time changes in demand shocks into improvements in unobservable quality and changes in the value of the outside option. This decomposition is important for interpreting the economics of how changing prices and markups translate into consumer welfare when products and technology change over time.

Our research is also closely related to Hashmi and Biesebroeck (2016) who model dynamic competition and innovation in the world automobile market using a logit model over the period 1982 to 2006. Relative to their work, this paper focuses on analyzing the evolution of consumer surplus and markups rather than modeling dynamic competition in quality. Furthermore, in addition to analyzing a longer time period, this paper uses micro data and second choice data to estimate demand following Bordley (1993) and Berry et al. (2004), uses a different instrumental variable to account for price endogeneity, and decomposes time effects in demand separately into changes in unobservable quality and changes in the value of the outside option.

## 2 Data

We compiled a data set covering 1980 through 2018 consisting of automobile characteristics and market shares, individual consumer choices and demographic information, and consumer survey responses regarding alternate “second choice” products. This section describes the data sources and presents basic descriptive information.

## 2.1 Automobile Market Data

Our primary source of data is information on sales, manufacturer suggested retail prices (MSRP), and characteristics of all cars and light trucks sold in the U.S. from 1980-2018 that we obtain from Ward’s Automotive. Ward’s keeps digital records of this information from 1988 through the present. To get information from before 1988, we hand collected data from Ward’s Automotive Yearbooks. The information in the yearbooks is non-standard across years and required multiple layers of digitization and re-checking. We supplemented the Ward’s data with additional information, including vehicle country of production, company ownership information, missing and nonstandard product characteristics (e.g. electric vehicle eMPG and driving range, missing MPG, and missing prices), brand country affiliation (e.g. Volkswagen from Germany, Chrysler from the U.S., and model redesign years. Prices in all years are deflated to 2015 USD using the core consumer price index. In order to construct market shares, we define the market size as the number of households in the U.S. divided by 2.5, which reflects the fact that the average household owns nearly two cars and the average tenure of car-ownership during this time period is roughly five years.

Product aggregation Vehicles sold in the U.S. are highly differentiated products. Each brand (or “make”) produces many models and each model can have multiple variants (more commonly called “trims”). Although we have specifications and pricing of individual trims, our sales data is at the make-model level. Similar to other studies of this market, we make use of the sales data by aggregating the trim information to the make-model level, see Berry et al. (1995) Berry et al. (2004), Goldberg (1995), and Petrin (2002). We aggregate price and product characteristics by taking the median across trims.

## [Table 1 about here.]

In Table I we display summary statistics for our sample of vehicles at the make-model-year level. An example of an observation is a 1987 Honda Accord. There are 6,130 cars, 2,243 SUVs, 680 trucks, and 641 vans in our sample.2 The average car has 52,089 sales in a year and the average truck has 140,207 sales. Trucks and vans are more likely to be from U.S. brands and less likely to be assembled outside of the U.S. than cars and SUVs. Two percent of our sample has an electric motor (including hybrid gas-powered and electric only). We present a description of trends in vehicle characteristics in Section 3.

## 2.2 Price Instrument

To identify the price sensitivity of consumers, we rely on an instrumental variable that shifts price while being plausibly uncorrelated with unobserved demand shocks. We employ a cost-shifter related to local production costs where a vehicle is produced. For each automobile in each year, we use the price level of expenditure in the country where the car was manufactured, obtained from the Penn World Tables version 9.1 variable pl_con, lagged by one year to reflect planning horizons. Following Feenstra et al. (2015), we refer to this as the Real Exchange Rate (RXR). RXR is equal to the purchasing power parity (PPP) exchange rate relative to the U.S. divided by the nominal exchange rate relative to the U.S.. RXR varies with two sources that are useful for identifying price sensitivities. First, if wages in the country of manufacture rise, the cost of making the car will rise, which will in turn raise the real exchange rate via the PPP rising. Therefore, the real exchange captures one source of input cost variation through local labor costs. Another source of variation is through the nominal exchange rate. If the nominal exchange rate rises, so that the local currency depreciates relative to the dollar, a firm with market power will have an incentive to lower retail prices in the U.S., thereby providing another avenue of positive covariation between the real exchange rate and retail prices in the U.S.. Exchange rates were employed as instrumental variables for car prices in Goldberg and Verboven (2001), which is focused on the European car market, and in Berry et al. (1999), along with wages. In Figure I, we display the lagged Real XR for the most popular production countries, where the size of the plot marker is proportional to the number of products sold from each country and the black dashed line represents the U.S. price level. Although our measure of RXR is relative to the U.S., U.S. RXR is also changing over time due to U.S. inflation.

## [Figure 1 about here.]

We use a second instrument for price to aid identifying additional time-varying price parameters that we include in some specifications of our model. The second instrument we use is a dummy for whether a particular car is assembled in the country of the brand headquarter, similar to Gandhi and Houde (2019) who use a dummy for when a vehicle’s production is moved to the U.S.. The theoretical justification for this instrument is similar to the RXR instrument in that vehicles whose production is shifted to a new location likely reflects cost advantages of that new location which may not be captured in the RXR. For example, a foreign manufacturer might relocate production to Canada where labor costs are higher than in Mexico, but transportation costs into major markets in the U.S. are lower.

We demonstrate the behavior of the RXR instrumental variable in a simple setup in Table II. We estimate a logit model of demand, as in Berry (1994), first via OLS and then using two-stage least squares with RXR as an instrumental variable for price. We include make fixed effects and year fixed effects. Within make there is variation in real exchange rates both within and across time. Within time variation is due to the fact that different models of the same make are assembled in different countries. For example, BMW assembles vehicles for the U.S. market in Germany and the U.S., General Motors has produced U.S. sold vehicles in Canada, Mexico, and South Korea (among other countries), and many of the Japanese and South Korean brands produce some of their models in the United States, Canada, and Mexico. Lacetera and Sydnor (2015) provide evidence that vehicle manufacturers maintain quality standards when producing vehicles in different countries. The first column in Table II shows the first stage relevance of the instrumental variable. The sign is positive as predicted by the theory with a first stage F-stat of 14.09. We cluster the standard errors at the make level. The first stage implies a pass-through of RXR to prices of 0.117, which is consistent with estimates in the literature (Goldberg and Campa, 2010; Burstein and Gopinath, 2014). The difference in the price coefficient in the last two columns demonstrates that employing the IV moves the coefficient estimate on price in the negative direction, which is expected because the OLS coefficient should be biased in the positive direction if prices positively correlate with unobserved demand shocks conditional on observable characteristics. Comparing the mean own price elasticities between the OLS and IV estimates confirms the importance of controlling for price endogeneity.

[Table 2 about here.]

## 2.3 Consumer Choices and Demographics

We collect individual level data on car purchases and demographics from two data sources: the Consumer Expenditure Survey (CEX) and MRI’s Survey of the American Consumer (MRI). These data sets provide observations on a sample of new car purchasers for each year, including the demographics of the purchaser and the car model purchased. CEX covers the years 1980-2005 with an average of 1,014 observations per year. MRI covers the years 1992-2018 with an average of 2,005 observations per year. We construct micro-moments from these data to use as targets for the heterogeneous agent demand model, following Goldberg (1995), Petrin (2002), and Berry et al. (2004). There are some general patterns from these data that motivate specification choices for the demand model. For example, that the average purchaser of a van having a larger family size suggests families value size more than non-families. That the average price of a car purchased by a high income versus low income buyer suggests higher income buyers are either less sensitive to price or value characteristics that come in higher priced cars more. That rural households are more likely to purchase a truck suggests different preferences for features of trucks by rural households.

In order to approximate the distribution of household demographics, we sample from the CPS, which contains the demographics information from 1980-2018 that we use from the CEX and MRI samples. Average household income (in 2015 dollars) increases from \$55,382 to \$81,375 from 1980 to 2018. Average household age increases from 46 to 51; average household size falls from 1.60 to 1.25; the percent of rural households decreases from 27.9 to 13.4. We will account for these trends by explicitly including evolving consumer heterogeneity in income, family size, and rural status as part of our model.

## 2.4 Second Choices

We obtain data on consumers’ reported second choices from MartizCX, an automobile industry research and marketing firm. MaritzCX surveys recent car purchasers based on new vehicle registrations. The survey includes a question about cars that the respondents considered, but did not purchase. We use the first listed car as the purchaser’s second choice. These data have previously been used, such as in Leard et al. (2017) and Leard (2019), and are similar to the survey data used in Berry et al. (2004).3 After we merge with our sales data, we use second choice data from 1991, 1999, 2005 and 2015, representing 29,396, 20,413, 42,533, and 53,328 purchases, respectively.

In Table III we display information about second choices for many popular cars of different styles and features to give a sense for how strong substitution within vehicle style appears in the data. For each year, we display the modal second choice, the next most common second choice, and the share who report these two cars as second choices over the total responses for that car. For example, in 1991, the the Dodge Ram Pickup is the modal second choice among the respondents who purchased a Ford F Series. The Chevrolet CK Pickup is the second most popular second choice, and together, these two second choices make up 69 percent of reported second choices for the Ford F Series. From this sample of vehicles, second choices tend to be similar types of vehicles (i.e. trucks, cars, SUVs, vans). Also, there is substantial variation in the share that the two most frequent choices represent: for example, in 1991, the F Series and Dodge Ram represent 76 percent of reported second choices for the Chevrolet Silverado in 1999, but the Civic and Corolla only represent 22 percent of second choices for the Ford Focus in 2005. The generally strong substitution towards similar vehicles is crucial for identifying unobserved heterogeneity in the demand model we present in Section 4.

[Table 3 about here.]

## 3 Empirical Description of the New Car Industry, 1980-2018

This section describes trends in the U.S. automobile industry from 1980 to 2018 related to market power and market efficiency. We first discuss changes in prices and market structure. Second, we discuss trends in product characteristics.

## 3.1 Prices and Market Structure

Inflation adjusted average prices in the automobile industry rose from 1980 to 2018. At the same time, concentration decreased. Figure II displays these patterns. In panel (a), we document that the average manufacturer suggested retail price (MSRP) rose from around \$17,000 in 1980 to around \$34,000 in 2018 (in 2015 USD, deflated by the core consumer price index). The bulk of the change in average price occurred before the year 2000, although the upper 25 percent of prices continued to rise after 2000. At the same time, HHI measured at the parent company level fell from over 2500 to around 1200, see panel (b). The C4 index saw a similar decrease over the same time period, from around 0.80 to 0.58. In panel (c), we document the main source of decreasing concentration. While the total number of firms in this industry fell slightly from 1980 to 2018, there were about twice as many products in 2018 as there were in 1980. In 1980, the “Big 3” US manufacturers accounted for a large portion of sales, whereas by 2018, sales were more evenly dispersed among domestic and international firms, consistent with patterns in other manufacturing industries (Amiti and Heise, 2021).

[Figure 2 about here.]

## 3.2 Physical Characteristics of Vehicles

That prices rose while concentration fell might seem counterintuitive at first pass, however prices are also a function of physical characteristics, quality, and production technology. There are two main trends regarding the physical characteristics of cars. The first is the rise of the SUV, which was a nearly non-existent vehicle class in 1980 and by the end of our sample represented roughly half of all sales. Second, cars and trucks have become larger and more powerful without sacrificing fuel efficiency (Knittel, 2011).

The number of products available to consumers increased from 1980 to 2018. A major contribution to this change is the rise of SUV production, particularly smaller SUVs that are designed to compete with sedans. Our SUV category aggregates SUVs (typically larger vehicles built on pickup truck frames, like the Toyota 4Runner) together with CUVs (smaller than SUVs and built on sedan frames, like the Honda CRV). In Figure II(d) we display the number of products by vehicle style over time. In the early 1980’s less than 25 SUVs were available to consumers (typically large truck-like vehicles) and after the year 2000 there were nearly 100 SUVs available in the market.

## [Figure 3 about here.]

Figure III displays selected product attributes over time. Average horsepower and footprint (length times width) increased substantially from 1980 to 2018. Average horsepower more than doubled for cars and roughly tripled for trucks from 1980 to 2018, see Figure IIIa. Cars became larger, SUVs and vans became smaller during the 1980s and then grew, and the average truck size grew substantially from 1980 to 2018. At the same time as horsepower and size increased, average fuel economy remained roughly constant, which largely reflects federal regulatory standards for fleet fuel economy, first enacted in the Energy Policy and Conservation Act of 1975.

Additionally, attributes not related to size and power changed substantially from 1980 to 2018. In Figure IIId, we show the percent of cars (i.e. not trucks, SUVs, or vans) sold with the following features, for years 1980, 1990, 2000, 2010, and 2014: air conditioning, power windows, anti-lock brakes, cassette player stereo system, side airbags, memory seats, and rear camera.4 The percentage of cars with many of these features increased from 1980 to 2018, however, both technology and trends in preferences affected the rate of adoption differently for different features. For example, air conditioning reached near universal adoption by 2000, but rear cameras are a recent addition. Safety features, like side airbags, were quickly adopted through the 1990s as federal safety regulations tightened. The cassette player, once a luxury feature, faded from cars as CDs and streaming services became popular, disappearing by 2010. In our demand model, many of these features will be subsumed into a quality residual which summarizes all characteristics not captured by readily available data like horsepower and vehicle size.

## 4 Model

Our framework is a differentiated product demand and oligopoly pricing model following Berry et al. (1995), which is standard in the industrial organization literature.

## 4.1 Consumers

Consumer i makes a discrete choice among the $J _ { t }$ options in the set $\mathcal { J } _ { t }$ of car models available in year t and an outside “no-purchase” option (indexed 0), choosing the option that delivers the maximum conditional indirect utility.5

Utility is a linear index of a vector of vehicle attributes $\left( \mathbf { x } _ { j t } \right)$ , price $\left( p _ { j t } \right)$ , an unobserved vehicle specific term $( \xi _ { j t } )$ , and an idiosyncratic consumer-vehicle specific term $( \epsilon _ { i j t } )$

$$
u _ { i j t } = \beta _ { i t } { \bf x } _ { j t } + \alpha _ { i t } p _ { j t } + \xi _ { j t } + \epsilon _ { i j t }\tag{1}
$$

The index i denotes an individual in a given year. We specify and estimate parametric distributions of taste parameters $\beta _ { i }$ and $\alpha _ { i }$ across individuals that depend on time-varying demographics and allow for unobservable heterogeneity. In our preferred specification, the parameters governing these distributions are fixed over time, but we also report estimates including time-varying components to parameters of the distribution of $\alpha _ { i }$ and some dimensions of $\beta _ { i }$ . We assume that $\epsilon _ { i j t }$ are independent draws from the standard Gumbel distribution.

Utility of the no-purchase option is $u _ { i 0 t } = \gamma _ { t } + \epsilon _ { i 0 t }$ , where $\gamma _ { t }$ reflects factors that change the utility of the no-purchase option from year to year, including business cycle fluctuations, urbanization, and durability of used automobiles. The average unobserved quality of new automobiles is also changing over time. We denote the mean utility of the choice set in year t relative to the base year as $\tau _ { t }$ so that $\xi _ { j t } = \tau _ { t } + \tilde { \xi } _ { j t }$ and assume that $E [ \tilde { \xi } _ { j t } | { \bf z } _ { j t } ] = 0$ , where $\mathbf { z } _ { j t }$ is a vector of instruments including $\mathbf { x } _ { j t } .$ year dummies, and an instrument for price (i.e., RXR).

It is well known that discrete choice models only identify utility relative to the outside good. Therefore, without further restrictions, we would be unable to separately identify yearly average unobserved quality, $\tau _ { t }$ , and the value of the outside option, $\gamma _ { t }$ . To address this issue, we follow Pakes et al. (1993) and add the restriction that

$$
\forall j \in \mathcal { C } _ { t } : E [ \xi _ { j t } - \xi _ { j t - 1 } ] = E [ ( \tau _ { t } - \tau _ { t - 1 } ) + ( \tilde { \xi } _ { j t } - \tilde { \xi } _ { j t - 1 } ) ] = 0\tag{2}
$$

where $\mathcal { C } _ { t }$ is the set of continuing vehicles offered in both year t and $t - 1$ that have not been redesigned by the manufacturer. Consider a model $j \in \mathcal { C } _ { t }$ as a product nameplate and design generation appearing both in $t - 1$ and $t . ^ { 6 }$ This restriction captures the fact that models within a model generation have substantively the same design from year to year, although it allows for idiosyncratic changes in features, marketing, or consumer taste. That is, while $\xi _ { j t }$ can change from year to year, innovations in $\xi _ { j t }$ are mean zero across years within a model generation. This restriction separately identifies average quality of the choice set, $\tau _ { t } ,$ from the average consumer valuation of the outside good, $\gamma _ { t }$ . Identification follows from a two step argument: First, following the usual logic of discrete choice models, $\tau _ { t } \mathrm { ~ - ~ } \gamma _ { t }$ is identified. Second, given that $\tilde { \xi } _ { j t }$ can be constructed from identified objects, the moment condition over continuing products (2) identifies $\tau _ { t }$ (subject to the normalization that $\tau _ { 0 } = 0 )$ . As this argument for identification is constructive, we will follow it closely when estimating the model below.

Separating average unobserved quality and the value of the outside option is important because we expect that unobserved product attributes change over time as in Figure IIId. It is important for us to incorporate this concept into consumer welfare. Second, the time effects capture aggregate economic conditions that influence the total sales of vehicles, but that are arguably not relevant for assessing the functioning of competition in the industry.

We model consumer heterogeneity by interacting household demographics and unobserved preferences with car attributes. Our baseline specification is:

$$
\alpha _ { i t } = \bar { \alpha } + \sum _ { h } \alpha _ { h } \mathrm { D } _ { i t } ^ { h }\tag{3}
$$

$$
\beta _ { i k } = \bar { \beta } _ { k } + \sum _ { h } \beta _ { k h } \mathrm { D } _ { i t } ^ { h } + \sigma _ { k } \nu _ { i k } ,\tag{4}
$$

where subscript k denotes the kth car characteristic (including a constant) and h indexes dimensions of consumer demographics (e.g., income). Allowing for observed heterogeneity allows substitution patterns to differ by demographics. The distribution of $D _ { i t }$ is taken from the Current Population Survey. In practice, we do not interact every demographic with every car characteristic. See Table VI for a complete listing of demographic - characteristic interactions and unobserved heterogeneity that we include in the model. Allowing for unobserved heterogeneity allows for more flexible substitution patterns. Unobserved taste for automobile characteristics, $\nu _ { i k }$ are assumed to be independent draws from the standard normal distribution.

Our baseline specification holds the parameters underlying the distributions of $\beta _ { i }$ and $\alpha _ { i }$ fixed over time. That said, the distributions themselves can change over time because of changing demographics. For example, increasing income inequality will lead to increasing dispersion in the $\alpha _ { i t }$ distribution over time. We also estimate additional specifications where we allow the mean of these distributions to change over time. That is, we allow for $\bar { \alpha }$ and $\bar { \beta }$ to depend on t. This allows for greater flexibility in the estimation of markups, since consumers’ price sensitivity and other tastes will vary over time, and firms will react to these changes when setting price. However, it will also imply changes in surplus due only to changes in the parameters of the utility function. As we report in Section 5, allowing for time varying parameters does not substantially change our estimates of markups. Therefore our baseline specification maintains stable-over-time parameters with clearer consumer welfare implications.

For a given year, market shares in the model are given by integrating over the distribution of consumers who vary in their demographics, unobserved tastes for characteristics, and idiosyncratic error terms,

$$
s _ { j t } = \int _ { i } \frac { \exp ( \beta _ { i t } { \bf x } _ { j t } + \alpha _ { i t } p _ { j t } + \xi _ { j t } ) } { \exp ( \gamma _ { t } ) + \sum _ { l \in \mathcal { J } _ { t } } \exp ( \beta _ { i t } { \bf x } _ { l t } + \alpha _ { i t } p _ { l t } + \xi _ { l t } ) } d F ( i ) .\tag{5}
$$

Shares conditional on consumer demographics can be computed by replacing the population distribution with the appropriate conditional distribution $F ( i | D _ { i t } \in \cdot )$ . Moreover, second choice shares conditional on a given first choice vehicle can be computed similarly by integrating consumers’ choice probabilities, when the first choice vehicle is removed, over the distribution of consumers, weighted by their probability of making that first choice.

## 4.2 Firms

On the supply side, we assume automobile manufacturers, indexed by m, play a static, full information, simultaneous move pricing game each year. Manufacturers choose the price for all vehicles for all of their brands, $\mathcal { J } _ { t } ^ { m }$ , with the objective of maximizing firm profit. Observed prices form a Nash equilibrium to the pricing game. We assume a constant marginal cost, $c _ { j t }$ , associated with producing a vehicle in a given year. The pricing first order condition for vehicle j is:

$$
s _ { j t } + \sum _ { k \in \mathcal { J } _ { t } ^ { m } } ( p _ { j t } - c _ { j t } ) \frac { \partial s _ { j t } } { \partial p _ { k t } } = 0\tag{6}
$$

These first order conditions will be used in conjunction with the estimated demand system to solve for marginal costs for each product. Marginal costs will then be used to compute markups and for counterfactual analysis. For a subset of counterfactual analysis, we will parameterize marginal costs to depend on vehicle covariates including elements of $\mathbf { x } _ { j t }$ and cost shifters excluded from demand which we describe in detail in Appendix B.2.

Our assumption of Nash-Bertrand pricing to maximize firms’ profits rules out cartels or other changes in conduct over the time period.7 If firms became more or less collusive, then the implied marginal costs inferred by assuming a static Nash equilibrium in prices would be misleading. We will consider alternative conduct assumptions for robustness and analyze alternative models of conduct in counterfactual analysis. However, we do not attempt to measure changes in conduct as in Bresnahan (1982), Lau (1982), or Duarte et al. (2020).

## 5 Estimation and Results

We estimate the model using GMM, closely following the procedures outlined by Petrin (2002) and Berry et al. (2004). Our estimation procedure is implemented in three steps. We briefly outline each step here and relegate a full description to Appendix A.

In the first step, we jointly estimate consumer heterogeneity and the mean consumer valuations. We compute the conditional demographic and second choice moments from the model and construct a GMM estimator matching these to their analogues in the consumer-level choice data. We employ micromoments from two sources: (1) demographic information linked to car purchases from MRI and CEX and (2) second-choice information from the MaritzCX survey. An example of a moment for the first source is the difference between the observed and predicted average price of vehicle purchases for each quintile of the income distribution. For the second source, we match the correlations in car characteristics between the purchased and second-choice cars.8

In the second step, we estimate α¯ and $\beta$ and year fixed effects by regressing the estimated consumer mean valuations on product characteristics, prices, make dummies, and year dummies. Our assumption that $\mathbf { x } _ { j t }$ and the real exchange rate are uncorrelated with product-level demand shocks provides the classic moment conditions for 2SLS. The year fixed effects absorb the structural parameters for annual variation in mean car quality, $\tau _ { t } .$ , and preference for outside good, $\gamma _ { t }$ .

In the third step we use the empirical analogue of the continuing product condition (2) to separately estimate $\tau _ { t }$ and $\gamma _ { t }$ from the estimated year effects.

We compute standard errors using a bootstrap procedure. We re-sample the micro data, including the sampled households in the CEX and MRI surveys as well as the MaritzCX survey, and re-estimate the model following the same three-step procedure. We account for the sampling variation in $\xi _ { j t }$ in the second step of the estimation procedure. In each of the 500 bootstrap draws of the micro data, we employ a nested parametric bootstrap, clustering at the make level, of the second step estimation.

## 5.1 Parameter Estimates

Tables IV, V, and VI present parameter estimates for our demand system. In addition to the estimates presented, we also include brand dummies and year dummies. Later, we present the decomposition of the year effects into unobserved quality and aggregate effects, $\gamma _ { t }$ and $\tau _ { t } .$ , following equation 2. We estimate three specifications of the utility function with varying degrees of temporal flexibility in the “mean” parameters. We do this to separate changing preferences from other reasons market power changes over time.

In Table IV, we present the price sensitivity parameters for the three specifications: (1) the “mean” price sensitivity parameter, α¯, does not change over time; (2) a linear trend in $\bar { \alpha } _ { t } = \alpha ^ { 0 } { + } t \alpha ^ { 1 }$ ; (3) separate $\bar { \alpha } _ { t }$ estimates for five-year intervals. Specifications (2) and (3) additionally allow for a time trend in taste for automobile type (e.g., Van, Truck, SUV). The point estimate for the linear trend specification (column 2) implies a slight (statistically imprecise) negative trend over time. The five-year interval estimates (column 3) do not suggest a strong upward or downward trend.9

As we show later, all three specifications have similar implications for trends in markups over time.

[Table 4 about here.]

Table V reports “mean” parameters on vehicle attributes. We allow for temporal flexibility in the specifications in columns 2 and 3 by interacting vehicle-type dummies with a time trend.

Lastly, Table VI reports the observed (demographic) and unobserved (random coefficients) preference heterogeneity. The demographic estimates are intuitive and match clear patterns in the microdata. Higher-income and older consumers are less price sensitive for the relevant range of incomes. Larger households have stronger preferences for vans and vehicle footprint. Rural households have a stronger preference for trucks. In general, we estimate large and economically meaningful coefficients representing unobserved heterogeneity, which rationalizes very strong substitution patterns observed in the second-choice data. The largest random coefficients appear on vehicle style, suggesting consumers substitute most strongly within vehicle style. The random coefficient on Truck is double the magnitude of the interaction of Truck with a rural consumer dummy variable, suggesting that unobservable taste heterogeneity is quantitatively important. Electric vehicles also have a large estimated random coefficient.

[Table 5 about here.]

## [Table 6 about here.]

Although we fix model parameters over time in the baseline specification (column 1 in Table IV), even in the baseline specification the distribution of price sensitivity and other tastes does change due to the change in the distribution of consumer demographics over time. For example, Figure IV presents the distribution of consumers’ price sensitivity, $\alpha _ { i } ,$ in 1985, 2000, and 2015. Over the data period, there has been a shift in the mean distribution towards less price sensitivity, which is a reflection of higher incomes and an older population. This, together with changes in the product set, drives changes in the elasticity of demand.

Our estimates of own-price elasticities for the earlier years in our sample are similar to BLP, Goldberg (1995), and Petrin (2002). The average own-price elasticity across out entire sample is -6.16. Table VII displays elasticities for the aggregate market and for a group of parent companies. Berry et al. (2004), on the suggestion of analysts at General Motors, calibrate their model by targeting an aggregate price elasticity of -1 for 1993. Our estimates are roughly validate this assumption. Demand elasticities became more elastic over time in each of these categories with most of the change from 1985 to 1995.

[Figure 4 about here.]

[Table 7 about here.]

## 5.2 Decomposition of Time Effects

The restriction in (2) decomposes the time effects into average improvements in unobservable car quality and relative movements in the utility of the outside good over time—potentially due to business cycle factors or changes in the utility of not purchasing a new car.

Figure V displays the results of this decomposition. We find that unobservable vehicle quality is steadily increasing, roughly linearly, by a cumulative total of about \$25,000. The value of the outside option also generally increases over the time period with noticeable deviations from trend during the 1990-1991 and 2007-2009 recessions.

Our model points to a substantial improvement in the quality of automobiles over the sample period, equal to approximately the mean price of a new car in the early part of the sample period. The economic meaning of this increase is that a consumer faced with the choice between two new automobiles of the same observable characteristics (e.g., size, horsepower, fuel economy) but with average unobserved quality (e.g., airbags, sound system, durability) of 1980 versus 2018 would place a significantly higher value on the 2018 vehicle. To quantitatively assess the plausibility of the estimated unobserved quality component, we manually collected data from the Kelly Blue Book website in 2021 for mint condition used automobiles produced every five years between 1992 and 2017. We then regressed the Kelly Blue Book private party transaction value against characteristics and dummy variables for the year of production. The year of production dummy variables should capture the average unobserved product differences across years of production. The full specification is presented in Appendix B.4. We find that the year of production dummies rise by \$19,638.88 between 1992 and 2017, which is nearly the increase we estimate for the value of unobserved product improvements, suggesting the estimate is not implausibly large.

A number of narratives also support such large increases. Automobiles have become safer through features such as improved airbag technology, body construction, rear-view cameras, and blind spot sensors. According to the National Highway Traffic Safety Administration (NHTSA), fatalities not involving alcohol impairment per vehicle miles traveled (VMT) have decreased 40 percent between 1982 and 2019 from 1.27 per hundred million VMT to 0.74 per hundred million VMT.10 Unobserved comfort improvements include power steering, durable interior materials, and electronic features such as Bluetooth audio systems and power or heated seats. Many of these features had not even been invented at the start of the sample.

## [Figure 5 about here.]

Finally, car durability is likely an important aspect for both the increased quality of new cars and the value of the outside good (which includes driving used cars). We would expect increased car durability to increase the value of a car. Between 1980 and 2018, data from the NHTSA implies that the average time a consumer keeps a new car has risen from 3.9 to 5.9 years, consistent with increased durability. This is part of the improvement in unobserved quality captured by our quality adjustment, $\tau _ { t } ,$ along with improvements in safety, comfort, and electronics. However, as cars become more durable, households will replace them less often, which has the effect of making the outside option appear more attractive. We expect this effect to be captured in the outside good part of the time effect, $\gamma _ { t }$ . The outside option series is broader than durability, however. In addition to improvements in the attributes of used cars, the outside option is also influenced by alternative transportation methods such as public transport or ride-sharing, or changes in the commuting needs of the population. It will also be affected by business cycle fluctuations or monetary policy which may lead consumers to accelerate or postpone new car purchases.

## 5.3 Model Fit

We target correlations between the attributes of purchased cars and stated second choices for survey years 1991, 1999, 2005, and 2015. The first column of Table VIII presents the average correlation across years for each attribute we target. These correlations suggest strong substitution patterns among vehicles with similar characteristics. As seen in the second column of Table VIII, our estimated model is able to match these moments well. To emphasize the importance of observed and unobserved consumer heterogeneity in our model, we compare our fit to a series of more restrictive models. In column 3, we present the implied correlations from a model with only demographic heterogeneity and a random coefficient on footprint. This model is roughly able to match the second choice correlation on footprint, but understates the remaining second choice correlations, even those one would expect to be highly correlated with footprint (e.g., horsepower, miles per gallon, and truck). Column 4 drops the random coefficient on footprint. Surprisingly, this model achieves essentially none of the second choice correlations reported in the data. This is despite the fact that it matches demographic patterns well, as reported in Table X in Appendix B. Indeed, it is only a slightly improved fit for second choices over the logit model in Column 5, which restricts substitution by assuming independence of irrelevant alternatives. We conclude that observable heterogeneity alone is insufficient to generate substitution patterns implied by the second-choice survey data. Table XI of Appendix B shows that the model matches the second-choice correlations separately in each year that we have second-choice data. Table X displays the fit of all of the demographic moments we match.

[Table 8 about here.]

## 5.4 Markup Estimates

We infer marginal costs of each vehicle using the first-order conditions in (6) at the estimated demand parameters. Table XII in Appendix B.2 displays the coefficient estimates from projecting inferred marginal costs on vehicle attributes and cost shifters. Together with the observed vehicle prices, we use the marginal costs to calculate vehicle markups. Figure VIa presents the median Lerner index over time for our three demand specifications. Each specification differs in the temporal flexibility of the average price sensitivity parameter, corresponding to the three columns in

Table IV, which leads to differences in elasticities and, thus, markups. Across all three specifications, average markups decrease substantially over time.11 Because the markup trends are not sensitive to flexibility in the price sensitivity parameter, we restrict the rest of our analysis to the specification where α¯ is constant over time.

In Figure VIb we display the median markups in terms of the Lerner index over time, as well as the 10th, 25th, 75th, and 90th percentiles. There is variation in markups across vehicles, and the entire distribution falls from 1980 to 2018.

## [Figure 6 about here.]

In Figure VII, we display median markups by vehicle style in panel (a) and by import status in panel (b). The decline in markups occurs across all vehicle styles and for both imported and domestically produced vehicles. Starting with panel (a), truck markups were higher than other vehicles at the beginning of our sample but fell more steeply throughout the 1990’s. This is likely due to two factors, a steeper increase in the quality and price of trucks and slightly greater competition as the popularity of foreign-manufactured trucks increased. This specific pattern is consistent with the move by Toyota and Nissan to produce trucks in the US to avoid the so-called “chicken tax.” Markups for SUVs also experienced a sharp fall during the 1990s, likely due to the massive increase in competition in this segment. The number of SUVs available nearly tripled during this time, and our demand estimates imply strong within-category substitution. Turning to panel (b) in Figure VII, overall, imported vehicles have lower markups than domestically produced vehicles, where our classification is based on the country of production, not the headquarters country of the product. However, domestically produced vehicles experienced a much greater fall in markups over our sample period.

## [Figure 7 about here.]

To assess sampling variability in the estimated markup trend, we utilize a bootstrap procedure accounting for sampling variability in the demand estimates, demographic data, and the $\xi _ { j t }$ residuals. In our baseline results, only a single product out of 9,694 has inelastic demand and all consumer price sensitivities are negative. However, in some of our bootstrap samples, some products have positive elasticities due to some consumers having positive price sensitivities. In these cases, which comprise 5.6 percent of products over all bootstrap draws, the Nash pricing condition cannot be satisfied and there is no inversion from observed prices to marginal costs.12 This occurs for at least one firm in 14.2 percent of year and bootstrap combinations. In all bootstrap samples where the inversion is well defined for all firms in 1980 and 2018, we find that median markups decrease over the sample period.

## 5.4.1 Explaining the Evolution of Markups

What drives the decline in markups? In the model, the exogenous forces which can change markups are changes in the ownership configuration, product entry and exit and associated changes in product characteristics, changes in the value of the outside option, and changes in consumer demographics or preferences. In our data and estimates, all of these forces are active throughout the time period.

An intermediate observation to understand the estimated change in markups is that the trend is similar if we infer markups assuming single product firms, as seen in Figure VIIIa. Assuming single product firms is a good approximation if vehicles manufactured by the same parent are not strong substitutes for each other. In the single product firm case, the Lerner index is equal to the inverse elasticity of the product:

$$
{ \frac { p - m c } { p } } = { \frac { 1 } { \mathrm { e l a s } } } = { \frac { s } { p } } \times { \frac { 1 } { \frac { d s } { d p } } }\tag{7}
$$

In the remaining panels of Figure VIII, we plot average prices (panel b), average market shares (c) and average derivatives of share with respect to price (d), noting that some intuition about the drivers of markups over time can be gleaned despite each of these being both an average and an endogenous function of the underlying preference, technology, and ownership structure primitives. During the period 1980 to 1999, when estimated markups decreased, average market shares and the average of their derivatives with respect to price are stable while average prices increased. This combination suggests that markups decrease according to equation 7. The economic reason why prices are increasing without shares decreasing and without changes in the derivative of share with respect to price is that vehicle quality is increasing. In the period 2000 to 2019, markups are stable as average market shares are decreasing, the average of their derivatives with respect to price are increasing, and average prices are roughly stable. In this latter period, although quality is still increasing steadily, the outside option also experiences substantial growth which can explain the flattened average price trend and offsetting the decline in average shares and increase in the average of their derivative with respect to price. Under the logic of equation 7, this combination leads to flat markups.

## [Figure 8 about here.]

In order to study which primitive factors explain the estimated decline in markups, we turn to counterfactual simulations. To consider the impact of concentration, the first counterfactual we perform adjusts the ownership matrix in each year to remove the impact of the growth of competition from foreign brands since 1980. To consider the impact of product product proliferation, our second counterfactual holds the number of products fixed over time at the level of 1980. These counterfactual are described in full in Section 6.2 as Mechanisms 1 and 2. These changes to primitives do not eliminate the decrease in markups we observed in our baseline results. We display the results in Figure XVIII in the appendix. Next, we simulate a counterfactual where the observable characteristics of vehicles in each year are scaled down to match the distribution of characteristics from 1980. Specifically, if a vehicle is in a certain percentile of a characteristic in a given year, we assign the same percentile from the 1980 distribution of that characteristic. As a result of this change, which shifts the distribution of products towards lighter, lower horsepower vehicles, the increase in marginal costs over time estimated by our model is effectively eliminated, as shown in IXa. The reason marginal costs are flat despite an estimated downward technological trend is that there is an offsetting upward time trend in the RXR, see XII in Appendix B.2. Other primitives, like the number of products and the market structure, are allowed to evolve as they do in the data. This counterfactual, which effectively eliminates the growth in observed product quality, does eliminate the fall in markups, as shown in Figure IXb. The main takeaway of this exercise is that a major driver of the decline in markups is is that increasing observable quality of vehicles results in increasing marginal costs which are less than fully passed through to consumer prices.

The importance of vehicle quality in driving markup trends highlights the fact that markups are not conceptually attractive proxies for welfare when the product set is changing.13 This fact motivates our focus on the model’s measures of welfare and surplus over time to assess industry performance in Section 6.

[Figure 9 about here.]

## 5.5 Robustness to Conduct Assumption

In this section, we compare markup estimates under alternative assumptions of conduct. To summarize the results, while there is a disparity in the level of markups, these alternatives all point towards declining markups over the sample period, as in the base case of Nash-Bertrand pricing. In the first case, we assume the Big Three US auto manufacturers (G.M., Ford, and Chrysler) collude on prices for our entire sample.14 Markups are much higher than our baseline case in the 1980s, but then become closer to our baseline case throughout time. This is consistent with the decline in the dominance of the Big-3 firms over time. Notably, markups at the end of the sample under the assumption that the Big-3 collude are lower than the Nash-Bertrand markups at the start of the sample. Therefore, under the assumption that the Big-3 were competing in 1980 and organized a pricing cartel in response to import competition after 1980, we would still find a decline in markups between 1980 and 2018. In the second case, we consider markups that are implied if all of the firms colluded on prices. In this case, markups are much higher. However, there is still a decrease in markups over the time period.

Figure X establishes that markups decline over time under a variety of constant conduct assumptions. However, it is possible that a cartel could have formed during our sample period. We now ask how large such a cartel would need to be to have held markups constant over the period. To quantify this, we consider different size cartels in 2018 to measure how many cartel members it would take for a cartel in 2018 to achieve the baseline non-collusive level of markups found in 1980. Specifically, we form cartels with the largest (by sales) manufacturers, adding one manufacturer at a time. The results are in Table IX. One change in conduct from Nash-Bertrand that would produce estimated increases in markups would involve a cartel of the six largest parent companies (“Top 5 + Nissan”) forming during our sample. Overall, it seems that a price-fixing cartel on the scale needed to keep markups at their 1980 level would be unlikely to escape the notice of antitrust authorities.

[Table 9 about here.]

## 5.6 Comparison to production-based approach

De Loecker et al. (2020) use financial data from Compustat to estimate markups.15 This approach uses a model of firm production and data on input expenditures and output revenue to estimate price over marginal cost ratios. In their baseline results, they estimate an increase in the sales weighted average price to marginal cost ratio (across all sectors) from 1.21 to 1.61 from 1980 to 2016. In addition to aggregate results, De Loecker et al. (2020) report estimates for specific industries, including the US auto industry. Figure XIa displays the time series of average price to marginal cost ratio from their work together with our own measure. We also include an estimate from Berry et al. (1995), which reports an average price to marginal cost ratio from 1971-1990. Both the level and trends in the price to marginal cost ratio differ from the estimates we derive, though both series are relatively flat from 1995 onward. In the right panel, we plot our estimates for total variable profits, which is the sum of price minus marginal cost multiplied by quantity sold over models in a year. Quantity thus enters directly into the right panel, but does not enter directly in our estimates in the left panel. Our estimates for total variable profits share some patterns with the De Loecker et al. (2020) estimates for markups, including an increase in the 1980’s, a dip and recovery in the 1990’s, and a dip and recovery around the Great Recession.

$$
[ \mathrm { F i g u r e ~ 1 1 ~ a b o u t ~ h e r e . } ]
$$

The two markup estimates rely on different underlying data and non-nested sets of assumptions. The approach for our estimates relies on a credible demand system and an assumption of static Nash pricing conduct by the manufacturers.16 The De Loecker et al. (2020) approach relies on an assumption of cost minimization with respect to a fully flexible input and credible production function estimation to measure the elasticity of output with respect to the flexible input.

There are a number of potential issues in implementing the production approach which may lead to inaccurate estimates in this context. First, if the input used to obtain marginal costs is not freely chosen by the firm (e.g., if it contains any fixed rather than variable costs), the static first-order condition at the heart of the approach does not apply. The flexible input employed in De Loecker et al. (2020) is Cost of Goods Sold (COGS) reported in Compustat at the firm-year level. In the context of auto manufacturing, COGS includes some marginal costs such as the additional material or labor costs associated with producing additional vehicles, but it also includes, by Generally Accepted Accounting Principles (GAAP), fixed overhead associated with manufacturing. That is, manufacturers are required to allocate fixed overhead costs as part of COGS. In this sense, COGS contains capital expenditures and thus may not satisfy the requirements as a flexible input.17 In practice, including fixed costs in the flexible input can lead to over time variation in the estimated markups even when the true price over marginal cost is fixed simply due to fluctuating quantities. Being driven by quantity sold rather than the true price to marginal cost ratio is one potential reason why the DLEU series shares some patterns with our estimates of total variable profits over time in the right panel of Figure XIb.

A second set of challenges are due to the estimation of output elasticities. Ideally, output elasticities would be estimated as part of a production function relating quantities of output to quantities of input accounting for endogenous input choices on the part of firms. There are three practical challenges with estimating output elasticities using Compustat data that may contribute to differences in the estimated series. Compustat reports total revenues at the firm-year level whereas a traditional output elasticity would be estimated using quantity instead of revenue (Bond et al., 2021). Second, observing revenue at the firm-year level leads to abstracting away from the multiproduct nature of production, with unknown consequences for the interpretation of the resulting output elasticity used to estimate markups. Third, there is the question of allowing for cross-firm heterogeneity in output elasticities, which can be challenging since Compustat contains only public firms. To address this, De Loecker et al. (2020) pool firms in the same two digit NAICS code to estimate output elasticities which for example pools auto manufacturers in NAICS code 33 with a wide range of manufacturing segments including computer manufacturing, ship building, furniture manufacturing, and many others. Using the Annual Survey of Manufacturers, Foster et al. (2022) estimate output elasticities allowing for flexibility across firms in the same industry and finds, in some specifications, decreasing average manufacturing markups for the period 1977 to 2012.

Finally, differences in the data sample may account for discrepancies between the two series. The demand approach uses price and quantity data of products available in a given market— the US new car market in our case. The production approach is applied to a collection of firms assumed to have a similar production technology with no explicit assumption on conduct. In the case of the Compustat data used by De Loecker et al. (2020), the firms included are primarily those publicly listed on US stock exchanges. Consequently, the data does not include some important auto manufacturers who sell in the US (e.g. Volkswagen, BMW, Hyundai-Kia, Nissan, Mazda, and Mitsubishi) in certain years. For example, Nissan enters the Compustat data in 1989 and Volkswagen enters in 2001, even though both were selling in the US market prior to these dates. BMW, Hyundai-Kia, Mazda and Mitsubishi never appear in the dataset. Moreover, Compustat includes additional revenue streams outside of automobile manufacturing such as any vertically integrated parts manufacturing, consumer financing operations, or manufacturing of other products. Finally, the revenue information in Compustat will include sales of vehicles outside of the U.S. market, which may have very different markups than autos sold inside the U.S. market.

Census or industry-specific production data sets can alleviate some of these concerns. For example, the US Census of Manufacturers includes inputs such as materials and energy which are arguably closer to flexible. It also contains quantity data for select industries. However, only the Census of Manufacturers (as opposed to other parts of the Economic Census) is well suited to the estimation of output elasticities and even for manufacturing there is little information on multiproduct production.18 Moreover, such data would contain information only on products produced in the United States. Compared to our data set, this excludes the substantial number of imported automobiles, and incorrectly includes automobiles that are exported.

Given these difficulties with estimating markups via the production approach in practice, we believe the approach of estimating markups using detailed demand data and conduct assumptions is a useful alternative. This approach does have the downside of requiring detailed industry-specific data sets and tailored modeling to each market under study. While resource intensive, this research is feasible. Indeed, in some cases, the two approaches may agree. De Loecker and Scott (2016) examine production and demand based estimates for beer and find both approaches find plausibly similar markup estimates. An important advantage of the demand side approach is that it provides direct measures of consumer surplus which are not available without an estimated demand system and accounts for changing product quality over time. For the remainder of the paper, we will use our estimates to go beyond markups and analyze the welfare trends of the US automobile industry.

## 6 The Evolution of Welfare

What are the implications of our estimates for assessing the performance of the industry over time? It may seem natural to evaluate concentration and markups as proxies for welfare, and we documented that both concentration and markups have fallen. However, it is well known that the relationship between concentration and welfare is theoretically ambiguous (Demsetz, 1973). Above we show that the relationship between markups and welfare is ambiguous if the product set is changing and that our markup estimates are largely driven by the changing cost and quality of cars. This section directly examines welfare trends over time.

## 6.1 Consumer surplus, producer surplus, and deadweight loss over time.

We first define a consumer surplus measure appropriate for our context. Typically, studies use the compensating variation of the product set relative to only the outside good being available to consumers. While this approach is straightforward, it is sensitive to changes in the valuation of the outside good over time. For example, suppose consumers choose to delay buying cars during a macroeconomic downturn. Then, in the down year the value of the outside good, $\gamma _ { t } ,$ will be high as more consumers choose not to purchase. Similarly, suppose there is a significant improvement in public transit over time, this again is reflected in an increase in $\gamma _ { t }$ which will cause a decline in consumer surplus. Both of these cases will affect the standard consumer surplus measure, even when the quality of automobiles and their prices are held fixed. We construct a measure of consumer surplus that captures the attractiveness of the choice set and is straightforward to compare across years. For each year, instead of using the value of the outside option associated with that year, we average the compensating differential overall all of the 39 (1980-2018) estimated values of outside options.

To make things concrete, consider the compensating variation of a consumer being offered the inside product bundle in year t with the outside good valued at $\gamma$ relative to receiving only the option to purchase this hypothetical outside good. Given our model assumptions, this is,

$$
C S _ { t } ( \gamma ) = \int _ { i } \frac { 1 } { \alpha _ { i t } } \left[ \log \left( \exp ( \gamma ) + \sum _ { j \in \mathcal { J } _ { t } } \exp ( \beta _ { i t } \mathbf { x } _ { j t } + \alpha _ { i t } p _ { j t } ^ { ( \gamma ) } + \xi _ { j t } ) \right) - \gamma \right] d F _ { t } ( i ) .\tag{8}
$$

In this calculation, $\mathbf { p } _ { t } ^ { ( \gamma ) }$ represents the equilibrium vector of prices when firms face an outside good valued at γ.

The traditional consumer surplus measure is simply $C S _ { t } ( \gamma _ { t } )$ —the compensating variation that would make consumers in year t indifferent between the product bundle they face and only the outside good from that bundle. However we can also examine how the inside product bundle in year t would have been valued against the the outside good in other years, enabling a direct comparison of product sets across years. Our preferred surplus measure removes the influence of changes in the outside good over time by averaging over the outside good across all years in the sample,

$$
\widetilde { C S } _ { t } = \frac { 1 } { T } \sum _ { v = 0 } ^ { T } C S _ { t } ( \gamma _ { v } ) .
$$

We can compute producer surplus and deadweight loss measures analogously.

$$
[ \mathrm { F i g u r e ~ 1 2 ~ a b o u t ~ h e r e . } ]
$$

In Figure XII we plot estimated consumer surplus $( \widetilde { C S } _ { t } )$ , producer surplus, and deadweight loss over the sample period. These components sum to total efficient surplus, which we measure by computing surplus when prices equal marginal costs. Surplus is displayed as per U.S. household. Total surplus rises roughly \$10,000 per household, from around a little less than \$2,000 to roughly \$11,000. Overall, the market is very efficient, with deadweight loss representing a small portion of total efficient surplus. This finding is reminiscent of Bresnahan and Reiss (1991) who estimate that most of the increase in competition comes with the entry of the second and third firms on their sample of retailers in multiple industries. The U.S. automobile market typically features four or more parent companies producing each specific style of vehicle.19

The more common measurement of consumer surplus in the industrial organization literature simply compares the value of the choice set to the current year’s estimated value of the outside option, or $C S _ { t } ( \gamma _ { t } )$ in our notation. This is a more static approach, which may be appropriate when the researcher does not have a long time series with a drastically changing outside option. However, we prefer our measure of consumer surplus because it captures the welfare impacts of industry developments separately from external effects such as changes in macroeconomic conditions or developments in substitute products represented in the outside option, such as public transit.

Figure XIIIa displays both measures of consumer surplus. Under the traditional measure, consumer surplus is relatively flat over the period with marked troughs in the early 1980s, early 1990s, and 2009, corresponding to the three major economic downturns in our sample period. Clearly, this measure confounds the value of the set of available products with the value of the outside option when comparing across years. The difference between these panels is intuitive given the significant changes in our estimates of the value of the outside good over time, as shown in Figure V. Figure XIIIb plots the share of consumer surplus of total efficient surplus. We do this for our baseline measure of consumer surplus, as well as for the traditional measure. In both cases, consumers’ share of available surplus is increasing from 1980 to 2018. For our baseline measure, consumers’ share of surplus rises from 0.62 to 0.82.

[Figure 13 about here.]

## 6.2 Why does consumer surplus rise?

We now investigate the economic primitives driving the increase in consumer surplus over time. There are many plausible reasons for this increase. There has been a significant change in market structure; foreign brands now offer a larger proportion of products relative to the 1980s. The number of products available has also increased dramatically which benefits consumers due to increased variety and strong competition between models. Products have changed in terms of characteristics in numerous ways: Today, there are many SUVs available, whereas they were a negligible part of the market in 1980. Automobiles are larger, more powerful, more efficient and offer greater comfort and reliability than in the past. Finally, production has become more efficient. We propose a series of counterfactuals where we isolate these industry trends and recompute equilibrium outcomes to determine the main drivers of consumer surplus growth.

Mechanism 1: Increased competitive pressure form foreign brands. It is possible that the increase in foreign brands competing in the US led to downward pressure on prices that benefited consumers.20 To understand this mechanism, we simulate an alternative scenario where we assume all vehicles sold by foreign brands in our data are instead owned by the Big 3 US car manufacturers (General Motors, Ford, and Chrysler), so that these manufacturers internalize the competitive pressure of the increase in foreign-owned products over our time period. To implement this, we randomly assign ownership of foreign brand vehicles to one of the Big 3 firms and recompute the pricing equilibrium. We do this ten times and take an average of the outcomes across the random assignments. Chrysler itself experiences ownership changes, so we track the ultimate owner of the Chrysler brand and treat that company as a Big 3 firm. While this exercise captures the effect of competition on prices, it holds fixed product design or quality and productivity. It is possible that improvements in product quality or marginal costs may ultimately be due to increased pressure from foreign competition.

The results, in terms of consumer surplus, are presented in the left panel of Figure XIV. Throughout this section, the solid line in the figures corresponds to our baseline consumer surplus, and the dashed line corresponds to a counterfactual. Our estimates indicate that, had foreign brands been owned by domestic firms, consumer surplus would still have increased substantially. We conclude that the competitive pricing pressure from foreign brands was not a primary driver of the rise in consumer surplus. Again, this is consistent with competition constraining market power with only a few competitors within clusters of similar products.

## [Figure 14 about here.]

We benchmark the result against two alternatives to emphasize this point. In the middle panel, we plot a counterfactual where the Big 3 coordinate pricing for the entire period without owning imports, and in the right panel we show a case where all firms enter into a cartel to maximize joint profits. Only in the the full cartel case is the gain in consumer surplus dampened substantially. In other words, by changing the ownership structure, the model is able to deliver outcomes where consumer surplus is greatly reduced, but the ownership configuration which eliminates foreign-brand competition does not achieve this.

## [Figure 15 about here.]

Mechanism 2: Product proliferation. Another potential reason for the increase in consumer surplus is the increase in the number of available products. Consumer welfare increases with the number of products for two reasons. First, consumers are heterogeneous and thus benefit from variety, all else equal. Second, additional products in the choice set crowds the characteristics space and adds to competitive pressure.

To quantify this mechanism, we simulate an alternate market where we restrict the number of active products to be at the 1980 level of 165 available products.21 The results are presented in the left panel of Figure XV. There is not much gap between the counterfactual consumer surplus and the estimated baseline path of consumer surplus. This is particularly striking considering that there were over 314 products in 2018, so the choice set was reduced by more than half. This suggests that product proliferation was not a significant driver of the consumer surplus increase. The intuition behind this result is that even though many products are eliminated from the choice set, consumers are able to substitute towards similar products. The rich substitution patterns of our demand system are important to capturing this effect. Indeed, under the logit model— which assumes symmetric unobserved product differentiation (Ackerberg and Rysman, 2005)—the increase in welfare over the 1980-2018 is roughly 5 times larger than under our model, largely as a result of product proliferation.

Another major development related to product proliferation is the rise in the the number of SUV’s available to consumers, as we documented in Figure IId. SUVs today represent a popular segment of the automobile market that was essentially unavailable in 1980. We estimate significant heterogeneity in taste for SUVs, which suggests the possibility of the introduction of SUV to generate large consumer surplus gains. In the right panel of Figure XV, displays a counterfactual where we eliminate all SUVs from the choice set. As expected, this has a larger effect in the later years of the sample, when SUVs are more numerous. However, while consumer surplus is lower than baseline, the difference is modest and only explains a small portion of the rise in consumer surplus between 1980 and 2018.

Mechanism 3: Changing product attributes. We now turn to changes in product characteristics. A notable trend in the industry has been the general growth in car characteristics such as size and horsepower, as we documented in Figure III. To see how these improvements affected consumer surplus, we scale the distribution of horsepower, MPG, footprint, height, and curb weight for each year in the sample to match the mean and variance of these characteristics in the 1980 choice set. This exercise affects consumer utility holding marginal cost fixed for all products. The results are displayed in the left panel of Figure XVI.

$$
[ \mathrm { F i g u r e ~ 1 6 ~ a b o u t ~ h e r e } . ]
$$

In addition to improvements in observable characteristics, we documented a steady rise in unobservable quality (see Figure V). In the right panel of Figure XVI, we simulate a counterfactual where the unobservable mean vehicle quality is fixed at 1980 levels. Specifically, since the rise in ξ is captured by the quality adjustment term τ in (2), we set $\tau _ { t } = 0 \ \forall t$ . In this case, the counterfactual delivers substantially lower increases in consumer surplus between 1980 and 2018. This comparison suggests that a large portion of the increased surplus enjoyed by consumers is due to improvements to vehicles that are outside our observed set of characteristics, such as safety features like airbags and rear view cameras, reliability improvements, and improved electronics like Bluetooth audio and navigation.

[Figure 17 about here.]

Mechanism 4: Decreasing costs. As we report in Appendix B.2, our results indicate that marginal costs of producing a car with fixed characteristics has experienced a steady decline of 1.4% per year over the sample period. To investigate the welfare implications of these technological improvements in production, the left panel of Figure XVII eliminates the downward trend in marginal costs. We find that welfare increases by about half as much as in the baseline. Thus, technological progress in production is also a significant driver of the measured increase in consumer surplus.

Finally, in the right panel of Figure XVII, we combine the improvement in marginal costs and the improvement in vehicle quality (from the right panel of Figure XVI) and simulate a world where neither the unobservable product quality increases nor do marginal costs fall. This combination almost entirely eliminates the measured increase in consumer surplus.

## 7 Conclusion

Antitrust policy has come under scrutiny in the U.S. in recent years. Critics argue that weak antitrust enforcement from the 1980’s onward has led to an increasingly tight grip of large firms over product markets to the detriment of consumers. In this paper, we focus on the new automobile market over nearly forty years. Employing a supply and demand industry oligopoly model with detailed microdata, we find that concentration has decreased, markups have decreased (in contrast to findings in studies estimating markups using production data), and consumer welfare has increased. The fraction of efficient surplus accruing to consumers has also increased.

We attribute the increase in consumer surplus primarily to increasing product quality and decreasing marginal costs. Specifically, we find that unobservable attributes—those that are not measured by specifications such as size, horsepower, and fuel efficiency—have increased significantly. These attributes include safety, reliability, comfort, and improved electronics. We find that competition was healthy enough that benefits from these improvements mostly accrued to consumers. However, our simulations indicate that had competition been significantly weaker, for example under a monopoly, then consumer benefits would have been offset through higher prices.

Our analysis makes a number of important assumptions. We consider specific models of firm conduct to infer marginal costs. Testing different models of firm conduct to detect changes over time would be a useful direction for future research. Moreover, we do not analyze adjacent markets such as the market for financing, parts suppliers, labor, or retail dealerships. Profits and firm behavior in these markets are linked and could be offsetting the changes we measure here. We largely abstract away from the used car market except as it appears in a time-varying outside option for consumers in our model. More detailed modelling of the joint dynamics of new and used cars could lead to more precise measurements of consumer welfare.

Most importantly, to speak to the broader question of the performance of antitrust and industry regulation, more long term studies of specific industries are necessary. While broad based studies using accounting or production data are important and attractive due to their feasibility, specific industry studies are useful to validate measurements. Furthermore, as proxies for welfare such as concentration or markups can be misleading in an environment where products are improving over time, specific industry studies often lend themselves to direct welfare calculations thereby avoiding the use of proxy measurements.

## References

Ackerberg, Daniel and Marc Rysman, “Unobserved Product Diferentiation in Discrete-Choice Models: Estimating Elasticities and Welfare Effects,” RAND Journal of Economics, 2005, 36 (4), 771–788.

Amiti, Mary and Sebastian Heise, “US Market Concentration and Import Competition,” 2021.

Autor, David, David Dorn, Lawrence F Katz, Christina Patterson, and John Van Reenen, “The Fall of the Labor Share and the Rise of Superstar Firms,” The Quarterly Journal of Economics, 02 2020, 135 (2), 645–709.

Berry, Steven and Panle Jia, “Tracing the Woes: An Empirical Analysis of the Airline Industry,” American Economic Journal: Microeconomics, 2010, 2 (3), 1–43.

, James Levinsohn, and Ariel Pakes, “Automobile Prices in Market Equilibrium,” Econometrica: Journal of the Econometric Society, 1995, pp. 841–890.

, , and , “Voluntary Export Restraints on Automobiles: Evaluating a Trade Policy,” American Economic Review, 1999, 89 (3), 400–430.

, , and , “Differentiated Products Demand Systems from a Combination of Micro and Macro data: The New Car Market,” Journal of Political Economy, 2004, 112 (1), 68–105.

, Martin Gaynor, and Fiona Scott Morton, “Do Increasing Markups Matter? Lessons from Empirical Industrial Organization,” Journal of Economic Perspectives, 2019, 33 (3), 44–68.

Berry, Steven T, “Estimating Discrete-choice Models of Product Differentiation,” The RAND Journal of Economics, 1994, pp. 242–262.

Bet, Germán, “Market Power in the US Airline Industry,” Available at SSRN 3913695, 2021.

Bond, Steve, Arshia Hashemi, Greg Kaplan, and Piotr Zoch, “Some Unpleasant Markup Arithmetic: Production Function Elasticities and Their Estimation from Production Data,” Journal of Monetary Economics, 2021, 121, 1–14.

Bordley, Robert F, “Estimating Automotive Elasticities from Segment Elasticities and First Choice/Second Choice Data,” The Review of Economics and Statistics, 1993, pp. 455–462.

Brand, James, “Differences in Differentiation: Rising Variety and Markups in Retail Food Stores,” Available at SSRN 3712513, 2020.

Bresnahan, Timothy F, “The Oligopoly Solution Concept is Identified,” Economics Letters, 1982, 10 (1-2), 87–92.

and Peter C Reiss, “Entry and Competition in Concentrated Markets,” Journal of Political Economy, 1991, 99 (5), 977–1009.

Burstein, Ariel and Gita Gopinath, “International Prices and Exchange Rates,” in “Handbook of international economics,” Vol. 4, Elsevier, 2014, pp. 391–451.

Covarrubias, Matias, Germán Gutiérrez, and Thomas Philippon, “From Good to Bad Concentration? US Industries over the past 30 years,” NBER Macroeconomics Annual, 2020, 34 (1), 1–46.

Demirer, Mert, “Production Function Estimation with Factor-augmenting Technology: An Application to Markups,” Technical Report, MIT working paper 2020.

Demsetz, Harold, “Industry Structure, Market Rivalry, and Public Policy,” Journal of Law and Economics, 1973, 16 (1), 1–9.

Döpper, Hendrik, Alexander MacKay, Nathan Miller, and Joel Stiebale, “Rising Markups and the Role of Consumer Preferences,” Available at SSRN 3939126, 2021.

Doraszelski, Ulrich and Jordi Jaumandreu, “Reexamining the De Loecker & Warzynski (2012) Method for Estimating Markups,” 2021.

Duarte, Marco, Lorenzo Magnolfi, and Christopher Sullivan, “Testing Firm Conduct,” 2020.

Economist, The, “Corporate Concentration: The creep of consolidation across America’s corporate landscape,” Technical Report 2016.

Feenstra, Robert C, Robert Inklaar, and Marcel P Timmer, “The Next Generation of the Penn World Table,” American Economic Review, 2015, 105 (10), 3150–82.

Foster, Lucia S, John C Haltiwanger, and Cody Tuttle, “Rising Markups or Changing Technology?,” Technical Report, National Bureau of Economic Research 2022.

Ganapati, Sharat, “The Modern Wholesaler: Global Sourcing, Domestic Distribution, and Scale Economies,” Technical Report 2021.

Gandhi, Amit and Jean-François Houde, “Measuring Substitution Patterns in Differentiatedproducts Industries,” NBER Working Paper, 2019, (w26375).

Gillingham, Kenneth, “The Economics of Fuel Economy Standards versus Feebates,” Manuscript: Yale University, 2013.

Goldberg, Linda S and José Manuel Campa, “The Sensitivity of the CPI to Exchange Rates: Distribution Margins, Imported Inputs, and Trade Exposure,” The Review of Economics and Statistics, 2010, 92 (2), 392–407.

Goldberg, Pinelopi Koujianou, “Product Differentiation and Oligopoly in International Markets: The Case of the US Automobile Industry,” Econometrica: Journal of the Econometric Society, 1995, pp. 891–951.

, “The Effects of the Corporate Average Fuel Economy Standards in the US,” Journal of Industrial Economics, 1998, 46 (1), 1–33.

and Frank Verboven, “The Evolution of Price Dispersion in the European Car Market,” The Review of Economic Studies, 2001, 68 (4), 811–848.

Hashmi, Aamir Rafique and Johannes Van Biesebroeck, “The Relationship Between Market Structure and Innovation in Industry Equilibrium: A Case Study of the Global Automobile Industry,” Review of Economics and Statistics, 2016, 98 (1), 192–208.

Knittel, Christopher R, “Automobiles on Steroids: Product Attribute Trade-offs and Technological Progress in the Automobile Sector,” American Economic Review, 2011, 101 (7), 3368–99.

Lacetera, Nicola and Justin Sydnor, “Would You Buy a Honda Made in the United States? The Impact of Production Location on Manufacturing Quality,” The Review of Economics and Statistics, 2015, 97 (4), 855–876.

Lau, Lawrence J, “On Identifying the Degree of Competitiveness from Industry Price and Output Data,” Economics Letters, 1982, 10 (1-2), 93–99.

Leard, Benjamin, “Estimating Consumer Substitution Between New and Used Passenger Vehicles,” 2019.

, Joshua Linn, and Y Zhou, “How Much Do Consumers Value Fuel Economy and Performance. Evidence from Technology Adoption,” Resources for the Future Report, 2017, pp. 1–37.

Loecker, Jan De and Paul T Scott, “Estimating Market Power: Evidence from the US Brewing Industry,” Technical Report, National Bureau of Economic Research 2016.

, Jan Eeckhout, and Gabriel Unger, “The Rise of Market Power and the Macroeconomic Implications,” The Quarterly Journal of Economics, 2020, 135 (2), 561–644.

Miller, Nathan, Matthew Osborne, Gloria Sheu, and Gretchen Sileo, “The Evolution of Concentration and Markups in the United States Cement Industry,” Available at SSRN, 2022.

Pakes, Ariel and David Pollard, “Simulation and the Aymptotics of Optimization Estimators,” Econometrica, 1989, 57 (5), 1027–1057.

, Steven Berry, and James A Levinsohn, “Applications and Limitations of Some Recent Advances in Empirical Industrial Organization: Price Indexes and the Analysis of Environmental Change,” The American Economic Review, 1993, 83 (2), 240–246.

Petrin, Amil, “Quantifying the Benefits of New Products: The Case of the Minivan,” Journal of Political Economy, 2002, 110 (4), 705–729.

Raval, Devesh, “Testing the Production Approach to Markup Estimation,” Review of Economic Studies, 2022.

Traina, James, “Is Aggregate Market power Increasing? Production Trends using Financial Statements,” 2021.

## A Demand Estimation Procedure

In this appendix, we detail the three steps of our demand estimation procedure.

## A.1 Unobserved Heterogeneity and Mean Valuation

Following Berry et al. (1995) we can decompose a consumer utility net of taste for the outside good into a vertical component $\delta _ { j t }$ and horizontal components,22

$$
u _ { i j t } - \gamma _ { t } = \delta _ { j t } + \mu _ { i j t } ( \theta ) + \epsilon _ { i j t } .
$$

Where the vertical component is

$$
\delta _ { j t } = \bar { \beta } \mathbf { x } _ { j t } + \bar { \alpha } p _ { j t } + \xi _ { j t } - \gamma _ { t }\tag{9}
$$

and the heterogeneity term is

$$
\mu _ { i j t } ( \theta ) = \sum _ { k } \sum _ { h } \beta _ { k h } x _ { j t } ^ { k } D _ { i t } ^ { h } + \sum _ { h } \alpha _ { h } p _ { j } D _ { i t } ^ { h } + \sum _ { k } \sigma _ { k } x _ { j t } ^ { k } \nu _ { i k } ,\tag{10}
$$

where $x _ { j t } ^ { k }$ is the kth element of $\mathbf { x } _ { j t }$ and we collect the heterogeneity parameters into the vector $\theta = ( \{ \beta _ { k h } \} , \{ \alpha _ { h } \} , \sigma )$

Our goal in this step is to estimate (θ, δ). For any consumer i, the conditional choice probability as a function of parameters is

$$
\begin{array} { l } { { \displaystyle { \mathcal { S } } _ { i j t } ( \theta , \delta ) = \frac { \exp \big ( \delta _ { j t } + \mu _ { i j t } ( \theta ) \big ) } { 1 + \sum _ { k \in J _ { t } } \exp \big ( \delta _ { k t } + \mu _ { i k t } ( \theta ) \big ) } . } } \end{array}\tag{11}
$$

Integrating these choice probabilities over the distribution of consumers gives us the market shares. Since there is a one-to-one mapping between δ and market shares, we can solve for mean valuations as a function of θ by matching model predicted shares to the market share data,

$$
s _ { j t } = \int \mathcal { s } _ { i j } ( \theta , \delta ( \theta ) ) d F _ { t } ( i ) .
$$

We can now construct the moments for our estimator of θ. Let $s _ { i j } ( \theta ) \ = \ s _ { i j } ( \theta , \delta ( \theta ) )$ . For readability, we drop t from the notation from the rest of this section and let $y _ { i }$ be the observed purchase of consumer i

Our first set of moments rely on microdata where we observe consumers’ automobile choice as well as their demographic characteristics, so we observe a random sample $\{ y _ { i } , \mathbf { D } _ { i } \}$ . We use this information to match product characteristics conditional on consumer demographics. Specifically,

we construct moments of the form23

$$
{ \bf g } _ { 1 } ( \theta ) = E [ \widehat { \bf x } _ { ( y _ { i } ) } | i \in \mathcal { H } ] - \int \sum _ { j } { \bf x } _ { j } \smallskip \mathcal { S } _ { i j } ( \theta ) \ d F ( i | i \in \mathcal { H } ) ,\tag{12}
$$

where $\mathcal { H }$ describes a set of consumers identifiable based on demographics, $\mathbf { x } _ { ( y _ { i } }$ is the characteristic vector of the product purchased by i and $E [ \mathbf { x } _ { \left( y _ { i } \right) } ^ { \left( \begin{array} { l } { \left| i \right. } \end{array} \right) } |$ is an estimate from the microdata. In ： practice, we match differences and ratios of $E [ \mathbf { x } _ { ( y _ { i } ) } | i \in \mathcal { H } ]$ across alternative demographic sets, $\mathcal { H }$ Table X lists the demographic moments we target and the associated model fit.

Our second set of moments relies on microdata for which we observe the consumers first and second choices of products. That is, the data is a random sample $\{ y _ { i } , z _ { i } \}$ , where $z _ { i }$ is the stated second choice of consumer i. Conditional on purchasing an automobile, our model predicts the first and second choices of consumer i,24

$$
\begin{array} { r } { \mathsf { \Gamma } _ { \mathcal { S } _ { i ( j , k ) } \left( \theta \right) } = \frac { \exp \left( \delta _ { j } ( \theta ) + \mu _ { i j } ( \theta ) \right) } { \sum _ { \ell \in J } \exp \left( \delta _ { \ell } + \mu _ { i \ell } ( \theta ) \right) } \cdot \frac { \exp \left( \delta _ { k } ( \theta ) + \mu _ { i k } ( \theta ) \right) } { \sum _ { \ell \in J \backslash j } \exp \left( \delta _ { \ell } + \mu _ { i \ell } ( \theta ) \right) } . } \end{array}\tag{13}
$$

We construct moments based on the correlation of product characteristics of first and second choices,

$$
{ \bf g } _ { 2 } ( \theta ) = E [ { \widehat { \bf x } } _ { ( y _ { i } ) } \circ { \bf x } _ { ( z _ { i } ) } ] - \int \sum _ { j , k } ( { \bf x } _ { j } \circ { \bf x } _ { k } ) \mathscr { s } _ { i ( j , k ) } ( \theta ) d F ( i )\tag{14}
$$

where ◦ denotes element-wise multiplication and $E [ \mathbf { x } _ { ( y _ { i } ) } ^ { \widehat { \mathbf { \xi } } } \circ \mathbf { x } _ { ( z _ { i } ) } ]$ is an estimate based on the microdata. Table VIII displays the second choice correlations we target and the model fit.

We stack these two sets of moments and estimate θ via simulated GMM. We use a weight matrix based on the inverse variance matrix of the data moments. Simulation over the distribution of consumers follows Pakes and Pollard (1989). Given ${ \hat { \theta } } ,$ our estimate of mean valuations is $\hat { \delta } = \delta ( \hat { \theta } )$

## A.2 Mean Taste for Characteristics

With the estimates of mean valuations from the previous step, we can now estimate mean tastes for product characteristics. We use the following regression equation,

$$
\delta _ { j t } = \bar { \beta } \mathbf { x } _ { j t } + \bar { \alpha } p _ { j t } + \iota _ { t } + \tilde { \xi } _ { j t } ,\tag{15}
$$

where $\iota _ { t } = \tau _ { t } - \gamma _ { t }$ absorbs the effect of the average utility of the outside good and the average car quality in year t. We use our first stage estimate $\hat { \delta }$ as a proxy for $\delta$ and employ a simple (IV) regression where the real exchange rate is our instrument for price. The extension to allow for variation in mean preference parameters over time is straightforward.

## A.3 Mean Quality over Time

Our final step estimates τ and $\gamma$ separately using the continuing product condition (2). The empirical analogue of this condition can be rewritten as an estimator of $\tau _ { t }$ using the residuals from our second step,

$$
\hat { \tau } _ { t } = \hat { \tau } _ { t - 1 } + \sum _ { j \in \mathcal { C } _ { t } } ( \hat { \tilde { \xi } } _ { j t - 1 } - \hat { \tilde { \xi } } _ { j t } ) ,\tag{16}
$$

with $\tau _ { 0 }$ normalized to 0. Finally, we can estimate $\hat { \gamma } _ { t } = \hat { \iota _ { t } } - \hat { \tau _ { t } }$

## B Additional Results and Analysis

## B.1 Model Fit

In this section, we report model fit for all of the moments used in estimation. Fit for the demographic interaction moments, for both the MRI and CEX samples, are reported in Table X. Table XI reports the second choice moments we match in demand estimation. An aggregated (averaged across the four sample years) version of these moments appears in the body of the paper (Table VIII).

$$
[ \mathrm { T a b l e ~ 1 0 ~ a b o u t ~ h e r e . } ]
$$

[Table 11 about here.]

## B.2 Determinants of Marginal Cost

In a subset of the counterfactual exercises, we consider scenarios that alter the marginal cost of products. To do ${ \mathrm { s o } } ,$ we estimate a parsimonious model of the determinants of marginal cost, relating them to observable characteristics, the real exchange rate, and a linear time trend to capture technological innovation.

$$
l o g ( c _ { j t } ) = \mu \mathbf { x } _ { j t } + \psi \cdot \mathrm { R X R } _ { j t } + \rho \cdot t + \omega _ { j t } ,\tag{17}
$$

Where $\mathbf { x } _ { j t }$ is the characteristic set used in utility and $\mathrm { R X R } _ { j t }$ is the real exchange rate (our cost instrument).25 The coefficient estimates for this estimation are provided in Table XII.

For the exercises in counterfactual Mechanism 4, which are reported in Figure XVII, we compute counterfactual marginal costs by eliminating the technological improvements represented by the time trend (i.e., setting $\rho = 0 )$ while holding all other cost elements fixed (including the residuals). We then solve for a new price equilibrium and compute the resulting consumer surplus.

$$
[ \mathrm { T a b l e ~ 1 2 ~ a b o u t ~ h e r e . } ]
$$

## B.3 Additional Markup Counterfactuals

In this section we report plots for additional markup counterfactuals mentioned in Section 5.4.1. In Figure XVIIIa, we display median markups after assigning all foreign brands to be owned by one of the Big 3 U.S. manufacturers. Markups are slightly higher throughout the time period, but the downward trend remains. In Figure XVIIIb, we display median markups after (randomly) limiting the number of products offered each year to match the number of offerings in 1980. Median markups have a similar trend in this case as the the baseline.

[Figure 18 about here.]

## B.4 Used Car Analysis

We manually collected data from the Kelly Blue Book website in December 2021 for mint condition, the best possible option, which KBB reflects 1-2% of the vehicles they evaluate, used automobiles with a total of 500 miles driven produced every five years between 1992 and 2017. Our query asked for the private party transaction value of the top five vehicles in each of the years for each of cars, SUV’s, vans, and trucks. We then regressed the midpoint of Kelly Blue Book private party transaction value range against characteristics and dummy variables for the year of production. The year of production dummy variables should capture the unobserved product differences across years of production. Table XIII reports the results, which indicate a steady increase in product quality over time which is consistent with the results of our demand estimation.

[Table 13 about here.]

![](images/af09d79415f664221e58878596d4ac97cfc0a8f23f2cb5bd248225995f76e9c5.jpg)  
Figure I: Real Exchange Rates

Note: Lagged real exchange rates from Penn World Table 9.1. Size of dots corresponds to the relative number of sales by production country, except for U.S.A.

![](images/1e990f5ba3676e30848e3f602835b46b83487f2e84ac13419057b3e510d7e3fa.jpg)  
(a) Prices

![](images/d62ea24c4b97fcbd1086e223219f23dd45850a7e8d456e8b053d09e1e0798112.jpg)  
(b) Measures of Concentration

![](images/c871b849862505c52f89fa61ab66b7b4d9c7d04d21a92a414139000a6c41c8dc.jpg)  
(c) Products and Manufacturers

![](images/74f894130fd24c0d2890d6913cdca337e1723b261e582874d9b1774a582a1912.jpg)  
(d) Count of Products by Styles  
Figure II: Prices and Market Structure, 1980-2018

Notes: Panel (a) displays share-weighted average price along with the interquartile range. Panel (b): HHI (bold line and left scale) and C4 (dashed line and right scale) are defined at the parent company level, e.g. Honda is the parent company of the Honda and Acura brands. In Panel (c), the number of products corresponds to a model available in a given year in our sample. The style definitions referred to in Panel (d) are described in the text. Data is from Wards Automotive Yearbooks and the sample selection is described in the text.

![](images/cae32d003139a0f918857d0d9a731e4ab05223260e55a522118fe2577ecb6ca3.jpg)  
(a) Horsepower

![](images/2e0343cdfecc56d6b39a6f938761f84d82b34d2f14f519926956e874bdbfdfe0.jpg)  
(b) Footprint (length × width)

![](images/4b87decdb3d90be31d82a52f99468d5f984db8494290f001b8ce7d6fc144298a.jpg)  
(c) Fuel Economy

![](images/85328d4dc8bbdc0a21613f48a7175312cd2a34e695d3c969ab87aeed12555264.jpg)  
(d) Additional Factory Installed Features  
Figure III: Physical Vehicle Characteristics, 1980-2018

Notes: Panels (a)-(c) display average characteristics for available models in our sample. Panel (d) is the percent of each feature installed on total “cars” sold (i.e. not trucks, SUVs, or vans). Factory installed features were compiled from Wards Automotive Yearbooks from various years. For example, in 1980 61% of “cars” sold had air conditioning.

![](images/2b487e500bf1344e3be422c6d617f717243495ee0fb59d6889888564879543f6.jpg)  
Figure IV: Distribution of Price Sensitivity

Note: Plot displays smoothed kernel regression of 10,000 draws from the estimated distribution of $\alpha _ { i }$ , by year, for the baseline specification with constant α¯ over time.

![](images/f2c75dc46ec67147044aae42714b942c83ad7713f1e888089474013f99dd6b65.jpg)  
Figure V: Quality and Aggregate Components of Time Effects

Notes: Average unobserved quality, $\tau _ { t } ,$ and value of outside good, $\gamma _ { t } ,$ in dollars. See text for estimation details.

![](images/5f18aeb5b1b5165728c9ec5e4386e6c2a40d90d4869ebdfd999e134dbd4d5cec.jpg)  
(a) Markups, Three Specifications

![](images/d49b945026a398d2ac56d20e2bf27e5a90969918ef5e9728969f41c47f2b8ea6.jpg)  
(b) Distribution of Markups  
Figure VI: Markups

Notes: Panel (a) displays the median markup over time for three specifications of demand. Refer to Tables 4, 5, and 6 for demand estimates. Panel (b) displays the distribution of markups, over time, for demand specification (1).

![](images/e41b6806276dbd2a5a934f990f497fd0966b636b751452faa15dc369b586db10.jpg)  
(a) Markups by Vehicle Style

![](images/f955f23f117a398f795e8964effb43f31885a5381bf9851187d0e07b171127da.jpg)  
(b) Markups by Import Status  
Figure VII: Markups over Time by Vehicle Style and Import Status

Note: Median markups across all vehicles. Vehicle style defined in the text. “Domestic” are those cars produced in the U.S., regardless of brand headquarters.

![](images/1ee726c1ccef5e4d7a71acd44981062c1d54ca2c38d9ce05b49f33ceb1ff4418.jpg)  
(a) Average Markups

![](images/9a7f21af7bb880630dec05532d5b54162471685dadc3693cafc49d14b776e9d3.jpg)  
(b) Average Price

![](images/1e137d254ff3ed699910f4769043e4ec0990acd755c5a206ef79e4e1b53f4cab.jpg)  
(c) Average Share

![](images/5a032fddf8609a76109cf66c2de1c9d24c8d969636651b912877b2c7d81772cf.jpg)  
(d) Average Own-price Derivative  
Figure VIII: Markups, Prices, and Shares

Notes: The top-left panel displays share-weighted mean markups for our baseline model and a model that assumes each product’s price is set independently of all other products. In the top-right panel, average prices are in 2015 USD.

![](images/f86ce1dfce1b56733fb52beeb486621063bc0be74e70cd7938e8c6f4ef760b6a.jpg)  
(a) Marginal Cost: Baseline vs. Counterfactual

![](images/47665a563a3da9aad9b16218e2175edbb71d45c32767421cecdf933bc9385b86.jpg)  
(b) Markups: Baseline vs. Counterfactual  
Figure IX: Counterfactual Markups, 1980 Distribution of Characteristics

Note: For each vehicle in each year, we assign the same percentile from the 1980 distribution of each characteristic, recompute marginal costs, which are plotted in panel (a), and recompute the pricing equilibrium and markups which are plotted in panel (b).

![](images/c2829e77dbbaaae2adfa717e771602ab36834130b0879fc0404f92dfb8557758.jpg)  
Figure X: Markups: Alternative Conduct Assumptions

Notes: Estimated median markups for Nash Bertrand pricing by parent companies (“Baseline”), the Big 3 U.S. automobile manufacturers colluding for every year in our sample (“Big 3 Collusion”), and joint price setting by every parent company in our sample (“Full Collusion”).

![](images/81d57d8705f719836150544967a8baecde75d42b09fb15219c240b9fd4741f16.jpg)  
(a) Price over Marginal Cost

![](images/5cd4e9558c4f19d99dc30a9aa08743aabcfb7262655861726271acc15880a4f8.jpg)  
(b) Total Variable Profits  
Figure XI: Comparison to De Loecker et al. (2020)

Notes: Panel (a) displays share-weighted mean price over marginal cost in our estimates, the estimate for share-weighted mean price over marginal cost in the U.S. automobile industry from De Loecker et al. (2020), and the average estimate across 1971-1990 from Berry et al. (1995). Panel (b) displays our estimate of total variable profits, quantity sold multiplied by margins, summed across all products.

![](images/c6aa2f77b9c9b7b12f56ce6fae6543caedc8b4ce833ee87109dee740c89f14a6.jpg)  
Figure XII: Consumer Surplus, Producer Surplus, and Deadweight Loss

Notes: Consumer surplus, producer surplus and deadweight loss. Consumer surplus in the compensating variation procedure detailed in the text. Deadweight loss is computed by netting consumer and producer surplus form efficient surplus, defined as the surplus available when prices equal marginal costs. Surplus measured in 2015 dollars.

![](images/c007477e4e49f7dc391102c2bc18e32949d22b848dfb552342834f8f72e60666.jpg)  
(a) Consumer Surplus Comparison

![](images/264a7f407c4010f96eaaa6497d8b94e68445f11925c8ddc715194efcedf1e8e5.jpg)  
(b) CS as a Share of Total Available Surplus  
Figure XIII: Consumer Surplus Comparison

Notes: Panel (a) displays consumer surplus computed two ways: the baseline definition described in the text, and consumer surplus computed as the compensating variation to the current year outside good. Panel (b) displays the ratio of consumer surplus to total efficient surplus using both approached presented in panel (a), where efficient surplus is computed as consumer surplus when prices equal estimated marginal costs of production, vehicle by vehicle.

![](images/7a4c4045c16201286dd7fe7be7b1d0095f538a39ab0066379728a74497e5d7c1.jpg)

![](images/59b4c7594aba57928452500c07f3be6e1dc25200d10340bc233e28635ade27bc.jpg)

![](images/99539e954277c251501dfdfc1525c75b177d436cd96edd635ff43a1014e3c81b.jpg)  
Notes: Vertical axis represents consumer surplus per U.S. household in 2015 dollars. In the first panel, we simulate the market equilibrium if all vehicles produced by foreign brands were owned by the Big 3 U.S. car manufacturers (randomly assigning new ownership). In the second panel, we simulate market equilibrium if the Big 3 jointly set prices. In the third panel, we simulate market equilibrium if all firms jointly set prices.

Figure XIV: Consumer Surplus: Alternative Product Ownership

![](images/6b86dd621aa023b2b1bda9c3c3b11e8ee158d791aef21c93d009b351e857bf6b.jpg)

![](images/7ac10f0b61caed6e6a55424420172af4180fe3b16148ff702ae1dbda2f833a8b.jpg)  
Figure XV: Consumer Welfare, Product Proliferation

Notes: Vertical axis represents consumer surplus per U.S. household in 2015 dollars. In the first panel, we simulate the market equilibrium if we eliminate (randomly) products in every year so that the number of products in the choice set is the same as in 1980. In the second panel we eliminate all SUVs from our sample and simulate market the equilibrium.

![](images/dcffc6563d36737d23a24ff69cd3493a0eeb60a4a981fd00739651c9a58f34b3.jpg)

![](images/64b442baf744ac231cd2941a5d5abeda2e7df421137e81a5c2b30472122b4a52.jpg)  
Figure XVI: Consumer Welfare, Changes in Attributes

Notes: Vertical axis represents consumer surplus per U.S. household in 2015 dollars. In the first panel, we simulate the market equilibrium if, in each year, we re-scale the distribution of footprint, horsepower, MPG, curbweight, and height, to match the 1980 distribution. In the second panel we eliminate the improvements to average unobserved quality, $\xi _ { j t }$ over time.

![](images/93dea6f256de47e0101cef3a9cfb0e8b2fabbf98c586b2fb881b6fd293f66a68.jpg)

![](images/d407b8e00b061c1d1e0dd0a9a2b4b71c94e5002f764af6b927faae592bdf9232.jpg)  
Figure XVII: Consumer Welfare, Changes in Production Efficiency

Notes: Vertical axis represents consumer surplus per U.S. household in 2015 dollars. In the first panel, we simulate the market equilibrium if, in each year, we eliminate the production efficiency trend estimated in Table XII. In the second panel, we eliminate both the changes in production efficiency and unobserved quality (from Figure ??).

![](images/09d883f29153f5f327d3aba37f33b6698983e7322c3c2d5435cfd2474948979a.jpg)  
(a) Markup Counterfactual: Foreign Ownership

![](images/c151bb54cc469cd53ede2e0992cbe4af3f733e4609d0d6400154dfda6dfac35b.jpg)  
(b) Markup Counterfactual: 1980 Product Count  
Figure XVIII: Additional Counterfactual Markups

Note: Panel (a) displays counterfactual median markups for the counterfactual described in Mechanism 1 in Section 6.2. Panel (b) displays median markups for the counterfactual described in Mechanism 2 in Section 6.2.

Table I: Summary Statistics
<table><tr><td></td><td>Mean</td><td>Std.Dev.</td><td>Min</td><td>Max</td><td></td><td>Mean</td><td>Std.Dev.</td><td>Min</td><td>Max</td></tr><tr><td>Cars,N=6,130</td><td colspan="9">SUVs,N=2,243</td></tr><tr><td>Sales</td><td>52,088.60</td><td>72,750.83</td><td>10.00</td><td>473108.00</td><td>Sales</td><td>51,629.61</td><td>66,932.79</td><td>10.00</td><td>753064.00</td></tr><tr><td>Price</td><td>35.85</td><td>18.76</td><td>11.14</td><td>99.99</td><td>Price</td><td>40.41</td><td>14.94</td><td>12.75</td><td>96.94</td></tr><tr><td>MPG</td><td>22.67</td><td>6.82</td><td>10.00</td><td>50.00</td><td>MPG</td><td>18.01</td><td>4.98</td><td>10.00</td><td>50.00</td></tr><tr><td>Horsepower</td><td>178.21</td><td>83.41</td><td>48.00</td><td>645.00</td><td>Horsepower</td><td>232.33</td><td>74.92</td><td>63.00</td><td>510.00</td></tr><tr><td>Height</td><td>55.76</td><td>4.21</td><td>43.50</td><td>107.50</td><td>Height</td><td>69.01</td><td>4.38</td><td>53.00</td><td>90.00</td></tr><tr><td>Footprint</td><td>12,870.08</td><td>1,710.41</td><td>6,514.54</td><td>21,821.86</td><td>Width</td><td>13,790.90</td><td>1,785.69</td><td>8,127.00</td><td>18,136.00</td></tr><tr><td>Curbweight</td><td>3,181.94</td><td>639.51</td><td>1,488.00</td><td>6,765.00</td><td>Curbweight</td><td>4,246.05</td><td>854.30</td><td>2,028.00</td><td>7,230.00</td></tr><tr><td>US Brand</td><td>0.40</td><td>0.49</td><td>0.00</td><td>1.00</td><td>US Brand</td><td>0.40</td><td>0.49</td><td>0.00</td><td>1.00</td></tr><tr><td>Import</td><td>0.59</td><td>0.49</td><td>0.00</td><td>1.00</td><td>Import</td><td>0.59</td><td>0.49</td><td>0.00</td><td>1.00</td></tr><tr><td>Electric</td><td>0.02</td><td>0.14</td><td>0.00</td><td>1.00</td><td>Electric</td><td>0.01</td><td>0.12</td><td>0.00</td><td>1.00</td></tr><tr><td>Trucks,N=680</td><td colspan="9">Vans,N=641</td></tr><tr><td>Sales</td><td>140207.22</td><td>184123.33</td><td>12.00</td><td>891482.00</td><td>Sales</td><td>59,103.39</td><td>86,940.25</td><td>10.00</td><td>891482.00</td></tr><tr><td>Price</td><td>27.81</td><td>9.82</td><td>12.02</td><td>69.43</td><td>Price</td><td>36.05</td><td>17.13</td><td>11.14</td><td>99.99</td></tr><tr><td>MPG</td><td>17.83</td><td>4.36</td><td>10.00</td><td>50.00</td><td>MPG</td><td>20.94</td><td>6.58</td><td>10.00</td><td>50.00</td></tr><tr><td>Horsepower</td><td>189.17</td><td>90.31</td><td>44.00</td><td>403.00</td><td>Horsepower</td><td>192.18</td><td>83.88</td><td>44.00</td><td>645.00</td></tr><tr><td>Height</td><td>68.39</td><td>6.33</td><td>51.80</td><td>81.00</td><td>Height</td><td>60.95</td><td>8.41</td><td>43.50</td><td>107.50</td></tr><tr><td>Footprint</td><td>15,086.14</td><td>2,478.91</td><td>8,437.30</td><td>20,000.00</td><td>Footprint</td><td>13,392.63</td><td>1,968.92</td><td>6,514.54</td><td>21,821.86</td></tr><tr><td>Curbweight</td><td>4,043.42</td><td>1,114.94</td><td>1,113.00</td><td>7,178.00</td><td>Curbweight</td><td>3,561.21</td><td>897.77</td><td>1,113.00</td><td>8,550.00</td></tr><tr><td>US Brand</td><td>0.65</td><td>0.48</td><td>0.00</td><td>1.00</td><td>US Brand</td><td>0.44</td><td>0.50</td><td>0.00</td><td>1.00</td></tr><tr><td>Import</td><td>0.35</td><td>0.48</td><td>0.00</td><td>1.00</td><td>Import</td><td>0.55</td><td>0.50</td><td>0.00</td><td>1.00</td></tr><tr><td>Electric</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>Electric</td><td>0.02</td><td>0.13</td><td>0.00</td><td>1.00</td></tr></table>

Notes: An observation is a make-model-year, aggregated by taking the median across trims in a given year. Statistics are not sales weighted. Prices are in 2015 000’s USD. Physical dimensions are in inches and curbweight is in pounds.

Table II: Logit Demand
<table><tr><td></td><td>First Stage</td><td>Reduced Form</td><td></td><td>OLS</td><td>IV</td></tr><tr><td>Price</td><td></td><td></td><td>-0.334</td><td>4 (0.042)</td><td>-1.696 (0.598)</td></tr><tr><td>RXR</td><td>0.411 (0.110)</td><td>-0.697 (0.232)</td><td></td><td></td><td></td></tr><tr><td>Height</td><td>-0.199 (0.048)</td><td>-0.064 (0.066)</td><td></td><td>-0.120 (0.069)</td><td>-0.401 (0.161)</td></tr><tr><td>Footprint</td><td>-0.117 7(0.066)</td><td>0.348 (0.081)</td><td>0.318</td><td>3(0.082)</td><td>0.149 (0.149)</td></tr><tr><td>Horsepower</td><td>0.768 (0.116)</td><td>-0.097 (0.070)</td><td>0.149</td><td>(0.067)</td><td>1.206 (0.472)</td></tr><tr><td>MPG</td><td>0.113 (0.036)</td><td>-0.062 (0.057)</td><td>-0.018</td><td>(0.062)</td><td>0.130 (0.116)</td></tr><tr><td>Curbweight</td><td>0.803 (0.111)</td><td>-0.493 (0.142)</td><td>-0.233</td><td>(0.140)</td><td>0.868 (0.541)</td></tr><tr><td>Num.of Trims</td><td>-0.115 (0.020)</td><td>1.097 (0.045)</td><td>1.060</td><td>(0.044)</td><td>0.902 (0.091)</td></tr><tr><td>Release Year</td><td>-0.081 (0.040)</td><td>-0.173 (0.054)</td><td>-0.195</td><td>(0.056)</td><td>-0.311 (0.091)</td></tr><tr><td>Yrs. Since Design</td><td>0.000 (0.012)</td><td>-0.145( (0.017)</td><td>-0.145</td><td>5 (0.017)</td><td>-0.144 (0.024)</td></tr><tr><td>Sport</td><td>0.480 (0.090)</td><td>-0.679 (0.105)</td><td>-0.523</td><td>(0.102)</td><td>0.134 (0.323)</td></tr><tr><td>Electric</td><td>0.765 (0.176)</td><td>-1.031 (0.255)</td><td>-0.791</td><td>(0.245)</td><td>0.267 (0.560)</td></tr><tr><td>Truck</td><td>-0.416 (0.154)</td><td>-0.485 (0.099)</td><td>-0.631</td><td>1 (0.107)</td><td>-1.190 (0.359)</td></tr><tr><td>SUV</td><td>-0.111 (0.117)</td><td>0.561 (0.100)</td><td>0.515</td><td>(0.105)</td><td>0.372 (0.214)</td></tr><tr><td>Van</td><td>-0.268 (0.161)</td><td>0.037 (0.126)</td><td>-0.060</td><td>(0.143)</td><td>-0.417 (0.330)</td></tr><tr><td>Mean Own Price Elas. Implied Pass-through</td><td>0.117 (0.032) 14.09</td><td></td><td></td><td>-1.20</td><td>-6.11</td></tr></table>

Notes: Unit of observations: year-make-model, from 1980 to 2018. Number of observations: 9,694. All specifications include year and make fixed effects. Standard errors clustered by make in parentheses. All continuous car characteristics are in logs and price is in 2015 \$10,000. Variables are logged and standardized.

Table III: Second Choices, Selected Examples
<table><tr><td>Model and Year</td><td>Modal Second Choice</td><td>Next Second Choice</td><td>(Modal + Next)/n</td></tr><tr><td colspan="4">1991 (N=29,436)</td></tr><tr><td>FordF Series</td><td>Dodge Ram Pickup</td><td>Chevrolet Ck Pickup</td><td>0.35</td></tr><tr><td>Honda Accord</td><td>Toyota Camry</td><td>Nissan Maxima</td><td>0.19</td></tr><tr><td>Dodge Caravan</td><td>Ford Aerostar</td><td>Plymouth Voyager</td><td>0.15</td></tr><tr><td>Mercedes-benz Mercedes E Class</td><td>Bmw 5 Series</td><td>Lexus Ls</td><td>0.17</td></tr><tr><td>Toyota 4runner</td><td>Ford Explorer</td><td>Nissan Pathfinder</td><td>0.34</td></tr><tr><td>Nissan 300zx</td><td>Alfa Romeo Alfa Romeo 164</td><td>Chevrolet Corvette</td><td>0.20</td></tr><tr><td colspan="4">1999 (N=20,413)</td></tr><tr><td>Chevrolet Silverado</td><td>FordFSeries</td><td>Dodge Ram Pickup</td><td>0.76</td></tr><tr><td>Toyota Camry</td><td>Honda Accord</td><td>Nissan Maxima</td><td>0.38</td></tr><tr><td>Plymouth Voyager</td><td>Ford Windstar</td><td>Dodge Caravan</td><td>0.42</td></tr><tr><td>Audi A6</td><td>Bmw 5 Series</td><td>Volvo 80</td><td>0.28</td></tr><tr><td>Chevrolet Tahoe</td><td>Ford Expedition</td><td>Dodge Durango</td><td>0.36</td></tr><tr><td>Bmw Z3</td><td>Porsche Boxster</td><td>Mazda Mx-5 Miata</td><td>0.42</td></tr><tr><td colspan="4">2005 (N=42.977)</td></tr><tr><td>Toyota Tacoma</td><td>Nissan Frontier</td><td>FordF Series</td><td>0.35</td></tr><tr><td>Ford Focus</td><td>Toyota Corolla</td><td>Honda Civic</td><td>0.22</td></tr><tr><td>Honda Odyssey</td><td>Toyota Sienna</td><td>Chrysler Town &amp; Country</td><td>0.71</td></tr><tr><td>Lincoln Town Car</td><td>Cadillac Deville</td><td>Chrysler 300 Series</td><td>0.44</td></tr><tr><td>Honda Cr-v</td><td>Toyota Rav4</td><td>Ford Escape</td><td>0.38</td></tr><tr><td>Porsche Cayenne</td><td>Bmw X5</td><td>Land Rover Range Rover</td><td>0.43</td></tr><tr><td colspan="4">2015 (N=53.391)</td></tr><tr><td>FordF Series</td><td>Chevrolet Silverado</td><td>Ram Pickup</td><td>0.64</td></tr><tr><td>Toyota Prius</td><td>Honda Accord Hybrid</td><td>Honda Cr-v</td><td>0.11</td></tr><tr><td>Toyota Sienna</td><td>Honda Odyssey</td><td>Chrysler Town&amp; Country</td><td>0.64</td></tr><tr><td>Volvo 60</td><td>Bmw 3 Series</td><td> Audi A4</td><td>0.16</td></tr><tr><td>Nissan Frontier</td><td>Toyota Tacoma</td><td>Chevrolet Colorado</td><td>0.69</td></tr><tr><td>Chevrolet Camaro</td><td>Ford Mustang</td><td>Dodge Challenger</td><td>0.46</td></tr><tr><td>Toyota Prius Phev</td><td>Chevrolet Volt</td><td>Nissan Leaf</td><td>0.32</td></tr></table>

Notes: Data from Maritz CX surveys in 1991, 1999, 2005, and 2015. Vehicles selected are high selling vehicles that represent a range of styles and attributes. The last column displays diversion to the two most popular second choices, conditional on diversion to any vehicle.

Table IV: “Mean” price parameters for different specifications
<table><tr><td></td><td>(1) Baseline</td><td>(2) Linear Trend</td><td>(3) 5-year Breaks</td></tr><tr><td>Price</td><td>-3.112</td><td>-2.839</td><td></td></tr><tr><td>Trend X Price</td><td>(1.122)</td><td>(0.737) -0.018</td><td></td></tr><tr><td>1980-1984</td><td></td><td>(0.02)</td><td>-1.933</td></tr><tr><td>1985-1989</td><td></td><td></td><td>(0.521) -3.05</td></tr><tr><td>1990-1994</td><td></td><td></td><td>(1.3) -2.682</td></tr><tr><td>1995-1999</td><td></td><td></td><td>(0.791) -2.722</td></tr><tr><td>2000-2004</td><td></td><td></td><td>(0.617) -2.57</td></tr><tr><td>2005-2009</td><td></td><td></td><td>(0.571) -3.222</td></tr><tr><td>2010-2014</td><td></td><td></td><td>(0.847)</td></tr><tr><td>2015-2018</td><td></td><td></td><td>-3.65 (0.839) -3.312</td></tr></table>

Notes: Brand and year dummies included. Standard errors account for correlation within make of realizations of $\xi _ { j t }$ and are bootstrapped over the entire estimation procedure, so they account for sampling error in the survey data. Price is in 2015 \$10,000.

Table V: “Mean” attribute parameters for different specifications
<table><tr><td></td><td>(1) Baseline</td><td>(2) Linear Trend</td><td>(3） 5-year Breaks</td></tr><tr><td rowspan="2">Height</td><td></td><td>-1.696</td><td>-1.631</td></tr><tr><td>-1.788</td><td></td><td></td></tr><tr><td rowspan="2">Footprint</td><td>(0.317)</td><td>(0.263)</td><td>(0.253) 0.502</td></tr><tr><td>0.534</td><td>0.409</td><td></td></tr><tr><td rowspan="2">Horsepower</td><td>(0.26) 1.018</td><td>(0.253) 1.24</td><td>(0.237) 1.189</td></tr><tr><td>(0.955)</td><td>(0.689)</td><td>(0.766)</td></tr><tr><td rowspan="2">MPG</td><td>-0.965</td><td>-0.957</td><td>-0.971</td></tr><tr><td>(0.212)</td><td>(0.207)</td><td>(0.196)</td></tr><tr><td rowspan="2">Curbweight</td><td>0.339</td><td>0.454</td><td>0.088</td></tr><tr><td>(0.932)</td><td>(0.671)</td><td>(0.629)</td></tr><tr><td rowspan="2">Num.of Trims</td><td>1.118</td><td>1.108</td><td>1.153</td></tr><tr><td>(0.142)</td><td>(0.081)</td><td>(0.08)</td></tr><tr><td rowspan="2">Release Year</td><td>-0.238</td><td>-0.296</td><td>-0.234</td></tr><tr><td>(0.16)</td><td>(0.133)</td><td>(0.129)</td></tr><tr><td rowspan="2">Yrs. Since Design</td><td>-0.214</td><td>-0.22</td><td>-0.221</td></tr><tr><td>(0.025)</td><td>(0.023)</td><td>(0.021)</td></tr><tr><td rowspan="2">Sport</td><td>-3.046</td><td>-3.039</td><td>-3.203</td></tr><tr><td>(0.549)</td><td>(0.381)</td><td>(0.418)</td></tr><tr><td rowspan="2">Electric</td><td>-5.549</td><td>-5.244</td><td>-5.261</td></tr><tr><td>(1.403)</td><td>(1.171)</td><td>(1.233)</td></tr><tr><td rowspan="2">Truck</td><td>-7.463</td><td>-6.885</td><td>-6.387</td></tr><tr><td>(0.892)</td><td>(0.9)</td><td>(0.836)</td></tr><tr><td rowspan="2">SUV</td><td>-0.079</td><td>-2.727</td><td>-2.604</td></tr><tr><td>(0.338)</td><td>(0.625)</td><td>(0.676)</td></tr><tr><td rowspan="2">Van</td><td>-7.614</td><td>-5.942</td><td>-5.701</td></tr><tr><td>(0.599)</td><td>(0.657)</td><td>(0.6)</td></tr><tr><td rowspan="2">Van Trend</td><td></td><td>-0.099</td><td>-0.106</td></tr><tr><td></td><td>(0.018)</td><td>(0.02)</td></tr><tr><td rowspan="2">SUV Trend</td><td></td><td>0.093</td><td>0.092</td></tr><tr><td></td><td>(0.033)</td><td>(0.028)</td></tr><tr><td rowspan="2">Truck Trend</td><td></td><td>-0.042</td><td>-0.058</td></tr><tr><td></td><td>(0.021)</td><td>(0.018)</td></tr></table>

Notes: Brand and year dummies included. Brand and year dummies included. Standard errors account for correlation within make of realizations of $\xi _ { j t }$ and are bootstrapped over the entire estimation procedure, so they account for sampling error in the survey data. Footprint is vehicle length times height in square inches. All continuous physical attributes are logged and standardized.

Table VI: Coefficient Estimates: Unobserved and Observed Heterogeneity
<table><tr><td></td><td></td><td colspan="8">Demographic Interactions</td></tr><tr><td>Price</td><td>0</td><td>Income 0.094</td><td>Inc. Sq. -0.462</td><td>Age 2.065</td><td>Rural</td><td></td><td>Fam.Size 2</td><td>FS 3-4</td><td>FS 5+</td></tr><tr><td>Van</td><td>5.538</td><td>(0.01)</td><td>(0.133)</td><td></td><td>(0.122)</td><td></td><td>1.737</td><td>3.681 (0.176)</td><td>5.84</td></tr><tr><td>SUV</td><td>(0.133) 3.617</td><td></td><td></td><td></td><td></td><td></td><td>(0.165)</td><td></td><td>(0.223)</td></tr><tr><td>Truck</td><td>(0.087) 6.309</td><td></td><td></td><td></td><td></td><td>3.007</td><td></td><td></td><td></td></tr><tr><td>Footprint</td><td>(0.31) 1.873</td><td></td><td></td><td></td><td></td><td>(0.34)</td><td>0.481 (0.053)</td><td>0.459 (0.054)</td><td>0.636 (0.07)</td></tr><tr><td>Horsepower</td><td>(0.118) 1.246</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Miles/Gal.</td><td>(0.361) 1.645</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Luxury</td><td>(0.151) 2.624</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Sport</td><td>(0.047) 2.617</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EV</td><td>(0.075) 3.798</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Euro.Brand</td><td>(0.511) 1.921</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>US Brand</td><td>(0.054) 2.141</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Constant</td><td>(0.048)</td><td>0.362 (0.034)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Notes: Brand and year dummies included. Standard errors are constructed by bootstrapping the microdata. All continuous car characteristics are in logs and standardized, and price is in 2015 \$10,000. Footprint is vehicle length times height in square inches. Income is normalized to have zero mean and unit variance.

Table VII: Selected Elasticities
<table><tr><td rowspan="2"></td><td colspan="3">Year</td></tr><tr><td>1985</td><td>1995</td><td>2005 2015</td></tr><tr><td>Average Own-price Elasticity</td><td>-4.23</td><td>-5.30</td><td>-5.78 -5.36</td></tr><tr><td>Market Elasticity</td><td>-1.07</td><td>-1.44</td><td>-1.38 -1.29</td></tr><tr><td>Ford</td><td>-3.51</td><td>-4.21</td><td>-5.29 -4.75</td></tr><tr><td>GM</td><td>-2.64</td><td>-3.75 -4.60</td><td>-4.72</td></tr><tr><td>Toyota</td><td>-3.40</td><td>-5.06 -4.67</td><td>-4.40</td></tr><tr><td>Volkswagen</td><td>-4.15</td><td>-5.42</td><td>-5.54 -5.45</td></tr><tr><td>Hyundai</td><td>1</td><td>-3.43 -3.93</td><td>-4.11</td></tr></table>

Notes: “Average Own-price Elasticity” is the percent change in sales for a one percent increase in price, averaged across each available product (shareweighted). “Market Elasticity” is the percentage change in the sales of all vehicles for a one percent increase in the price of all vehicles. Manufacturer-specific elasticities represent the percent change in sales for all cars of that manufacturer for a one percent increase in price for all cars of that manufacturer.

Table VIII: Attribute Correlation between First and Second Choice
<table><tr><td></td><td></td><td></td><td colspan="3">Alternative Specifications</td></tr><tr><td></td><td>Data</td><td>Model</td><td>Only Dem.&amp; Footprint RC</td><td>Only Demographics</td><td>Logit</td></tr><tr><td>Van</td><td>0.720</td><td>0.729</td><td>0.048</td><td>0.008</td><td>-0.008</td></tr><tr><td>SUV</td><td>0.642</td><td>0.636</td><td>0.018</td><td>-0.007</td><td>-0.010</td></tr><tr><td>Truck</td><td>0.843</td><td>0.797</td><td>0.246</td><td>-0.013</td><td>-0.024</td></tr><tr><td>Footprint</td><td>0.710</td><td>0.695</td><td>0.666</td><td>-0.003</td><td>-0.018</td></tr><tr><td>Horsepower</td><td>0.599</td><td>0.589</td><td>0.385</td><td>0.009</td><td>-0.012</td></tr><tr><td>MPG</td><td>0.647</td><td>0.657</td><td>0.363</td><td>0.003</td><td>-0.013</td></tr><tr><td>Luxury</td><td>0.484</td><td>0.499</td><td>0.031</td><td>0.005</td><td>-0.005</td></tr><tr><td>Sport</td><td>0.277</td><td>0.293</td><td>0.001</td><td>-0.004</td><td>-0.004</td></tr><tr><td>Electric</td><td>0.373</td><td>0.182</td><td>0.002</td><td>-0.001</td><td>-0.001</td></tr><tr><td>Euro Brand</td><td>0.336</td><td>0.347</td><td>0.019</td><td>0.000</td><td>-0.003</td></tr><tr><td>US Brand</td><td>0.479</td><td>0.471</td><td>0.120</td><td>-0.010</td><td>-0.012</td></tr></table>

Notes: Data from MaritzCX survey, 1991, 1999, 2005, 2015. The numbers are the average across these four years. “Model” column represents the predictions from the model presented in Table VI, and column 1 of Tables IV and V. The “Logit” column contains model predictions from a simple logit demand specification, with no observed or unobserved heterogeneity. The “Only Demographics” column contains model predictions from a model with the same demographic interactions as our main specification, but without any unobserved heterogeneity. “Logit” and “Only Demographics” are estimated without moments on second choices.

Table IX: Average Markups with Different Cartel Assumptions
<table><tr><td></td><td>Median Markup</td><td>HHI</td></tr><tr><td>1980 Baseline</td><td>0.32</td><td>2661</td></tr><tr><td>2018 Baseline</td><td>0.19</td><td>1132</td></tr><tr><td>2018 Hypothetical Cartel Membership</td><td></td><td></td></tr><tr><td>GM + Ford + Toyota</td><td>0.22</td><td>2546</td></tr><tr><td>Top 3+Fiat</td><td>0.23</td><td>3724</td></tr><tr><td>Top 4+ Honda</td><td>0.26</td><td>4819</td></tr><tr><td>Top 5 + Nissan</td><td>0.32</td><td>6000</td></tr></table>

Notes: Computed median markups and HHI with simulated collusion in 2018 for various manufacturer cartels. Note: Fiat is the parent company of Chrysler in 2018.

<table><tr><td></td><td></td><td></td><td colspan="3">MRI</td><td colspan="3">CEX</td></tr><tr><td>Demographic</td><td></td><td>Car Attribute</td><td>Data</td><td>Model</td><td>Only Demos</td><td>Data</td><td>Model</td><td>Only Demos</td></tr><tr><td> $\mathbb { E } [ x | I n c o m e Q _ { 5 } ] - \mathbb { E } [ x | I n c o m e Q _ { 1 } ]$ </td><td></td><td>Price</td><td>0.215</td><td>0.383</td><td>0.363</td><td>0.603</td><td>0.4</td><td>0.421</td></tr><tr><td> $\mathbb { E } \{ x | I n c o m e Q _ { 4 } \} - \mathbb { E } \{ x | I n c o m e Q _ { 1 } \}$ </td><td></td><td>Price</td><td>0.016</td><td>0.229</td><td>0.215</td><td>0.356</td><td>0.266</td><td>0.268</td></tr><tr><td> $\mathbb { E } [ x | I n c o m e Q _ { 3 } ] - \mathbb { E } [ x | I n c o m e Q _ { 1 } ]$ </td><td></td><td>Price</td><td>-0.08</td><td>0.131</td><td>0.121</td><td>0.189</td><td>0.149</td><td>0.15</td></tr><tr><td> $\mathbb { E } [ x | I n c o m e Q _ { 2 } ] - \mathbb { E } [ x | I n c o m e Q _ { 1 } ]$ </td><td></td><td>Price</td><td>-0.146</td><td>0.068</td><td>0.062</td><td>0.069</td><td>0.078</td><td>0.075</td></tr><tr><td> $\mathbb { E } [ x | A g e > 6 0 ] - E [ x | A g e < 3 0 ]$ </td><td></td><td>Price</td><td>0.518</td><td>0.369</td><td>0.328</td><td>0.257</td><td>0.344</td><td>0.342</td></tr><tr><td> ${ \mathbb E } [ x | A g e 5 0 - 6 0 ] - E [ x | A g e < 3 0 ]$ </td><td></td><td>Price</td><td>0.388</td><td>0.34</td><td>0.33</td><td>0.239</td><td>0.291</td><td>0.316</td></tr><tr><td> $\mathbb { E } [ x | A g e 4 0 - 5 0 ] - E [ x | A g e < 3 0 ]$ </td><td></td><td>Price</td><td>0.329</td><td>0.294</td><td>0.295</td><td>0.265</td><td>0.236</td><td>0.246</td></tr><tr><td> $\mathbb { E } [ x | A g e 3 0 - 4 0 ] - E [ x | A g e < 3 0 ]$ </td><td></td><td>Price</td><td>0.266</td><td>0.146</td><td>0.148</td><td>0.265</td><td>0.135</td><td>0.139</td></tr><tr><td></td><td> $\mathbb { E } [ x | F a m i l y = 2 ] - \mathbb { E } [ x | F a m i l y = 1 ]$ </td><td>Van</td><td>0.025</td><td>0.022</td><td>0.022</td><td>0.02</td><td>0.021</td><td>0.021</td></tr><tr><td></td><td> $\mathbb { E } [ x | F a m i l y = 3 / 4 ] - \mathbb { E } [ x | F a m i l y = 1 ]$ </td><td>Van</td><td>0.063</td><td>0.062</td><td>0.061</td><td>0.058</td><td>0.059</td><td>0.059</td></tr><tr><td></td><td> $\mathbb { E } [ x | F a m i l y = 5 + ] - \mathbb { E } [ x | F a m i l y = 1 ]$ </td><td>Van</td><td>0.132</td><td>0.131</td><td>0.126</td><td>0.12</td><td>0.121</td><td>0.122</td></tr><tr><td> $\mathbb { E } [ x | F a m i l y = 2 ] - \mathbb { E } [ x | F a m i l y = 1 ]$ </td><td></td><td>Footprint</td><td>0.036</td><td>0.027</td><td>0.026</td><td>0.026</td><td>0.027</td><td>0.027</td></tr><tr><td></td><td> $\mathbb { E } [ x | F a m i l y = 3 / 4 ] - \mathbb { E } [ x | F a m i l y = 1 ]$ </td><td>Footprint</td><td>0.018</td><td>0.024</td><td>0.023</td><td>0.026</td><td>0.025</td><td>0.025</td></tr><tr><td></td><td> $\mathbb { E } [ x | F a m i l y = 5 + ] - \mathbb { E } [ x | F a m i l y = 1 ]$ </td><td>Footprint</td><td>0.03</td><td>0.035</td><td>0.033</td><td>0.036</td><td>0.036</td><td>0.036</td></tr><tr><td> $\mathbb { E } [ x | R u r a l ] - \mathbb { E } [ x | N o t R u r a l ]$ </td><td></td><td>Truck</td><td>-0.103</td><td>-0.098</td><td>-0.101</td><td></td><td></td><td></td></tr><tr><td> $\mathbb { E } [ x | I n c o m e Q _ { 2 } ] / \mathbb { E } [ x | I n c o m e Q _ { 1 } ]$ </td><td></td><td>PurchaseProb</td><td></td><td></td><td></td><td>7.813</td><td>9.239</td><td>9.091</td></tr><tr><td> $\mathbb { E } \{ x | I n c o m e Q _ { 3 } \} / \mathbb { E } \{ x | I n c o m e Q _ { 1 } \}$ </td><td></td><td>PurchaseProb</td><td></td><td></td><td></td><td>5.466</td><td>5.077</td><td>5.246</td></tr><tr><td> $\mathbb { E } [ x | I n c o m e Q _ { 4 } ] / \mathbb { E } [ x | I n c o m e Q _ { 1 } ]$ </td><td></td><td>PurchaseProb</td><td></td><td></td><td></td><td>3.641</td><td>2.706</td><td>2.866</td></tr><tr><td></td><td> $\mathbb { E } [ x | I n c o m e Q _ { 5 } ] / \mathbb { E } [ x | I n c o m e Q _ { 1 } ]$ </td><td>PurchaseProb</td><td></td><td></td><td></td><td>2.265</td><td>1.66</td><td>1.684</td></tr></table>

Notes: Moments from the consumer samples that we target in estimation, along with the analog from our model at the estimated parameters. For the demographic moments, our data comes from two surveys, the Consumer Expenditure Survey (CEX) covering years 1980-2005 and MRI covering years 1992-2018. The "Only Demos" column correspond to a specification where we include all of the demographic interactions but none of the random coefficients.

Table X: Moments and Model Fit: Demographic Interactions

<table><tr><td></td><td colspan="2">1991</td><td colspan="2">1999</td><td colspan="2">2005</td><td colspan="2">2015</td></tr><tr><td>Attribute</td><td>Data</td><td>Model</td><td>Data</td><td>Model</td><td>Data</td><td>Model</td><td>Data</td><td>Model</td></tr><tr><td>Van</td><td>0.688</td><td>0.734</td><td>0.735</td><td>0.739</td><td>0.735</td><td>0.719</td><td>0.72</td><td>0.696</td></tr><tr><td>SUV</td><td>0.605</td><td>0.58</td><td>0.652</td><td>0.639</td><td>0.623</td><td>0.665</td><td>0.69</td><td>0.663</td></tr><tr><td>Truck</td><td>0.84</td><td>0.792</td><td>0.83</td><td>0.79</td><td>0.828</td><td>0.805</td><td>0.872</td><td>0.799</td></tr><tr><td>Footprint</td><td>0.638</td><td>0.665</td><td>0.68</td><td>0.684</td><td>0.739</td><td>0.713</td><td>0.782</td><td>0.714</td></tr><tr><td>Horsepower</td><td>0.512</td><td>0.542</td><td>0.567</td><td>0.559</td><td>0.643</td><td>0.611</td><td>0.674</td><td>0.636</td></tr><tr><td>MPG</td><td>0.627</td><td>0.647</td><td>0.686</td><td>0.667</td><td>0.664</td><td>0.664</td><td>0.611</td><td>0.641</td></tr><tr><td>Luxury</td><td>0.426</td><td>0.514</td><td>0.438</td><td>0.469</td><td>0.521</td><td>0.499</td><td>0.55</td><td>0.476</td></tr><tr><td>Sport</td><td>0.229</td><td>0.266</td><td>0.217</td><td>0.244</td><td>0.314</td><td>0.267</td><td>0.348</td><td>0.338</td></tr><tr><td>Electric</td><td>一</td><td>1</td><td>1</td><td>0.003</td><td>一</td><td>1</td><td>0.373</td><td>0.371</td></tr><tr><td>Euro Brand</td><td>0.186</td><td>0.276</td><td>0.337</td><td>0.359</td><td>0.409</td><td>0.368</td><td>0.413</td><td>0.363</td></tr><tr><td>US Brand</td><td>0.468</td><td>0.453</td><td>0.475</td><td>0.471</td><td>0.51</td><td>0.474</td><td>0.464</td><td>0.48</td></tr></table>

Notes: Moments from the Maritz second choice survey that we target in estimation and the analog from our model at the estimated parameters.  
Table XI: Moments and Model Fit: Second Choice Moments

Table XII: Marginal Cost Function Estimates
<table><tr><td></td><td>Coefficient</td><td>S.E.</td></tr><tr><td>Trend</td><td>-0.014</td><td>(0.002)</td></tr><tr><td>RXR</td><td>0.211</td><td>(0.030)</td></tr><tr><td>Height</td><td>-0.839</td><td>(0.133)</td></tr><tr><td>Footprint</td><td>-0.289</td><td>(0.122)</td></tr><tr><td>HP</td><td>0.552</td><td>(0.049)</td></tr><tr><td>MPG</td><td>0.096</td><td>(0.042)</td></tr><tr><td>Curbweight</td><td>1.280</td><td>(0.125)</td></tr><tr><td>Trims</td><td>-0.032</td><td>(0.007)</td></tr><tr><td>Release Year</td><td>-0.012</td><td>(0.013)</td></tr><tr><td>SUV</td><td>0.025</td><td>(0.026)</td></tr><tr><td>Truck</td><td>-0.124</td><td>(0.037)</td></tr><tr><td>Van</td><td>0.042</td><td>(0.029)</td></tr><tr><td>EV</td><td>0.313</td><td>(0.066)</td></tr><tr><td>Sport</td><td>0.110</td><td>(0.019)</td></tr><tr><td>Design Years</td><td>-0.000</td><td>(0.003)</td></tr><tr><td colspan="3">Brand Effect 厂</td></tr></table>

Notes: Dependent variable is log marginal costs recovered from the first-order conditions. All continuous attributes are logged. Standard errors are clustered by brand.

Table XIII: KBB Price Regression
<table><tr><td></td><td>Coefficient</td><td>S.E.</td></tr><tr><td>Height</td><td>26058.27</td><td>(5244.96)</td></tr><tr><td>Footprint</td><td>12470.29</td><td>(6862.72)</td></tr><tr><td>Horsepower</td><td>600.47</td><td>(2407.91)</td></tr><tr><td>MPG</td><td>-258.53</td><td>(4450.29)</td></tr><tr><td>Weight</td><td>-9710.17</td><td>(5279.84)</td></tr><tr><td>No. Trims</td><td>-2.65</td><td>(11.90)</td></tr><tr><td>Years Since Redesign</td><td>-99.44</td><td>(100.48)</td></tr><tr><td>Truck</td><td>-1809.78</td><td>(1403.22)</td></tr><tr><td>SUV</td><td>421.12</td><td>(1223.43)</td></tr><tr><td>Van</td><td>-1124.60</td><td>(1101.78)</td></tr><tr><td>Year 1997</td><td>-586.04</td><td>(951.43)</td></tr><tr><td>Year 2002</td><td>395.62</td><td>(1251.81)</td></tr><tr><td>Year 2007</td><td>3424.69</td><td>(1506.16)</td></tr><tr><td>Year 2012</td><td>10224.18</td><td>(1485.64)</td></tr><tr><td>Year 2017</td><td>19638.88</td><td>(1956.91)</td></tr><tr><td></td><td></td><td></td></tr></table>

Notes: Unit of observations: year make-model, from 1980 to 2018. Number of observations: 72. Specification include make fixed effects. Car characteristics in logs.