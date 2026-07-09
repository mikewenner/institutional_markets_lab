# Institutional Markets Lab Glossary

This glossary is a working desk-style reference for Institutional Markets Lab.

It focuses on institutional derivatives, index volatility, book risk, financing, relative value, Greeks, hedging, and P&L attribution. The goal is not to define elementary options terms. The goal is to connect each concept to how a trader, desk analyst, market maker, or risk manager might actually think about it.

---

## Volatility Surface and Index Volatility

### Volatility Surface

The volatility surface is the map of implied volatility across strike and expiration.

Why it matters:

A desk does not simply trade “volatility.” It trades specific parts of the surface: short-dated downside skew, longer-dated Vega, event vol, upside call demand, calendar spreads, and relative value across strikes and maturities.

Example:

SPX 1-month 5% OTM puts may trade at a much higher implied volatility than 1-month ATM options. A trader selling those puts is not just short volatility; they are short downside skew, short convexity, and exposed to spot/vol correlation if the market sells off.

---

### Skew

Skew refers to the difference in implied volatility across strikes.

Why it matters:

In index options, downside puts often trade at higher implied volatility because institutions demand protection against equity drawdowns. Skew is a major risk factor, not a footnote.

Example:

A desk sells a 95% strike SPX put and buys an ATM put. Even if total Vega looks small, the position may still lose money if downside skew steepens during a selloff.

---

### Term Structure

Term structure refers to how implied volatility changes across expirations.

Why it matters:

Short-dated volatility, event volatility, and longer-dated volatility can move very differently. A book can be long front-end vol and short back-end vol, or vice versa.

Example:

Before a major CPI print, 1-week implied volatility may rise sharply while 3-month volatility barely moves. A calendar spread can make or lose money based on that relative movement, even if spot does not move much.

---

### Forward Volatility

Forward volatility is the implied volatility for a future period between two expirations.

Why it matters:

Forward volatility helps isolate what the market is pricing after a near-term event window.

Example:

If 1-week implied volatility is 24 and 1-month implied volatility is 18 because of an FOMC meeting this week, the implied volatility for the period after the meeting may be much lower than the headline 1-month number suggests.

---

### Volatility Risk Premium

Volatility risk premium is the difference between implied volatility sold upfront and realized volatility experienced later.

Why it matters:

It is central to volatility selling, structured product supply, variance risk premium, and index option carry. But it is not free money; it compensates sellers for crash, gap, convexity, and liquidity risk.

Example:

A desk sells 1-month SPX variance at an implied level of 19 vol. If realized volatility over the month is 13, the trade likely benefits. But if the market gaps down 5% and realized volatility spikes to 35, the premium collected may be overwhelmed.

---

### Spot/Vol Correlation

Spot/vol correlation describes the tendency for equity markets and implied volatility to move together or inversely.

Why it matters:

In equity index markets, spot usually falls when implied volatility rises. This relationship is central to Vanna, skew, downside hedging, and stress P&L.

Example:

A desk short downside puts may lose from Delta as SPX falls, from Gamma as the move accelerates, from Vega as implied vol rises, and from skew as downside options reprice richer.

---

### Vol-of-Vol

Vol-of-vol is the volatility of implied volatility itself.

Why it matters:

Options on volatility, VIX products, and convex volatility books are sensitive not just to the level of volatility but to how unstable volatility is.

Example:

If VIX moves from 15 to 25 and then swings between 20 and 35, a book with convex exposure to volatility may behave very differently than a simple short-Vega book.

---

## Greeks and Higher-Order Risk

### Delta

Delta measures directional exposure to the underlying.

Why it matters:

Delta is the first hedge, but it is not the whole risk. On an options desk, Delta changes constantly because of Gamma, Vanna, Charm, skew movement, and time decay.

Example:

A book starts the morning with $0 Delta. After SPX drops 1%, the book may become short $50 million Delta because short puts have moved closer to the money.

---

### Gamma

Gamma measures how Delta changes as spot moves.

Why it matters:

Gamma determines how aggressively a book’s directional exposure changes. It drives hedging needs and can create nonlinear P&L.

Example:

A short-Gamma desk may need to sell futures as SPX falls and buy futures as SPX rises. In a fast market, this can turn hedging into a source of realized loss.

---

### Vega

Vega measures sensitivity to changes in implied volatility.

Why it matters:

Vega must be understood by strike, expiry, and surface bucket. A book that appears flat total Vega may still be exposed to skew steepening or front-end volatility repricing.

Example:

A desk is long 6-month ATM Vega but short 1-month downside Vega. The total Vega report may look balanced, but the book can still lose in a short-dated downside volatility spike.

---

### Theta

Theta measures sensitivity to the passage of time.

Why it matters:

Theta is carry, but carry is not automatically good. Positive Theta often comes from being short optionality, short Gamma, or short Vega.

Example:

A short put spread may earn positive Theta each day the market is calm. But one large selloff can erase weeks of decay income.

---

### Vanna

Vanna measures the sensitivity of Delta to changes in implied volatility, or equivalently the sensitivity of Vega to changes in spot.

Why it matters:

Vanna is critical in equity index options because spot and vol are linked. When spot falls and vol rises, Delta can change for both reasons at once.

Example:

A trader is short downside puts. SPX falls and implied vol rises. The position becomes more short Delta not only because spot moved, but also because higher vol changes the option’s Delta. That additional Delta change is Vanna-related risk.

---

### Charm

Charm measures the sensitivity of Delta to the passage of time.

Why it matters:

Charm can matter a lot in short-dated and near-expiration options. A book’s Delta can drift even if spot does not move.

Example:

On expiration day, a large near-the-money put position may experience meaningful Delta changes between 10:00 AM and 2:00 PM even if SPX is almost unchanged. The hedge requirement changes because time is passing.

---

### Volga / Vomma

Volga, also called Vomma, measures how Vega changes as implied volatility changes.

Why it matters:

A book’s exposure to volatility is not always linear. During volatility shocks, Vega itself can expand or contract.

Example:

A long option position may have positive Vega at 18 implied vol, but if implied vol jumps to 30, the position’s Vega may change materially. The trader is exposed not just to vol, but to convexity in vol.

---

### Veta

Veta measures how Vega changes as time passes.

Why it matters:

Vega exposure decays and migrates across the term structure. This matters for calendar spreads and expiry buckets.

Example:

A desk long 3-month Vega and short 1-month Vega may see the risk profile change significantly after two weeks, even if spot and implied vol are unchanged.

---

### Speed

Speed measures how Gamma changes as spot moves.

Why it matters:

Gamma is not static. Around strikes and near expiration, Gamma can increase or collapse quickly.

Example:

A short-dated option book may look manageable when SPX is 20 points away from a large strike. If SPX moves closer to that strike, Gamma can increase rapidly, creating much larger hedge requirements.

---

### Color

Color measures how Gamma changes as time passes.

Why it matters:

Near expiration, Gamma profiles can intensify or decay quickly. This matters for intraday risk and expiration-day hedging.

Example:

A dealer short near-the-money options may have moderate Gamma exposure in the morning, but as expiration approaches and spot remains near the strike, Gamma can become more concentrated.

---

### Zomma

Zomma measures how Gamma changes when implied volatility changes.

Why it matters:

Gamma exposure is affected by volatility levels. A volatility shock can change the convexity of the book.

Example:

A book that appears short a certain amount of Gamma at 15 implied vol may have a different Gamma profile if implied vol jumps to 25 during a selloff.

---

### Cross-Gamma

Cross-Gamma measures how the Delta of one instrument changes with respect to movement in another related instrument.

Why it matters:

Important for index versus components, dispersion, ETF/index relationships, and multi-asset books.

Example:

A desk trading index options and single-name options may be exposed to how SPX Delta changes when a major component like Apple or Nvidia moves sharply.

---

## Book Risk and Desk Positioning

### Book Risk

Book risk is the aggregate exposure across all positions, not the risk of one isolated trade.

Why it matters:

A trade that looks attractive alone may be bad for the book if it adds to an existing concentration.

Example:

A client wants to buy downside puts from the desk. Selling them may be attractive at the quoted volatility, but if the desk is already short downside Gamma and short skew, the trade may worsen the book’s stress profile.

---

### Risk Warehousing

Risk warehousing means keeping risk on the book instead of immediately offsetting it.

Why it matters:

This is central to market making and client facilitation. A desk gets paid to intermediate risk, but it must decide which risk is worth holding.

Example:

A client sells a large block of upside calls. The desk buys them at an attractive level and chooses to warehouse some long upside Vega rather than immediately offsetting, because the price includes sufficient edge.

---

### Inventory

Inventory is the accumulated risk created by prior trades and client flow.

Why it matters:

Inventory shapes pricing. A desk may quote differently depending on whether a new trade helps or hurts the existing book.

Example:

If the desk is already long downside puts, it may be more willing to sell downside protection to a client because that trade reduces existing inventory rather than adding to it.

---

### Concentration Risk

Concentration risk is exposure clustered in a specific strike, expiry, scenario, product, or risk factor.

Why it matters:

A book can look diversified in total notional but still be vulnerable to one market outcome.

Example:

A desk may be roughly flat total Vega but heavily short 1-week 5% OTM put Vega. If the market gaps lower, that one bucket can dominate P&L.

---

### Stress Loss

Stress loss is estimated P&L under a severe but plausible scenario.

Why it matters:

Trading desks care not only about daily Greeks but also about how the book behaves under shocks.

Example:

A risk report may ask: what happens if SPX drops 4%, implied vol rises 8 points, and skew steepens sharply? A short downside options book may show a much larger loss than Delta alone suggests.

---

### Risk Limits

Risk limits define how much exposure a desk can carry.

Why it matters:

Limits force discipline around Delta, Gamma, Vega, stress loss, notional, liquidity, concentration, and product exposure.

Example:

Even if a trader likes selling 1-month downside puts, the desk may be unable to add more because the short-Gamma or stress-loss limit is already near capacity.

---

### Hedge Slippage

Hedge slippage is the difference between intended hedge economics and actual hedge execution.

Why it matters:

A theoretical hedge may look clean, but real markets involve spreads, timing, liquidity, and market impact.

Example:

A trader intends to hedge short Gamma by selling futures as SPX falls. In a fast selloff, fills are worse than expected, and hedge slippage becomes a major source of loss.

---

## P&L Attribution

### P&L Explain

P&L explain is the process of breaking profit and loss into drivers such as Delta, Gamma, Vega, Theta, skew, rates, carry, and execution.

Why it matters:

A trader needs to know why the book made or lost money. Without P&L explain, there is no learning loop.

Example:

The book loses $750k. The explain shows $250k from Delta, $300k from Vega expansion, $150k from skew steepening, and $50k from hedge slippage. That tells a very different story than simply saying “the market went down.”

---

### Delta P&L

Delta P&L is the portion of P&L explained by directional exposure.

Why it matters:

Separates market direction from volatility, convexity, and carry effects.

Example:

If the book is long $20 million Delta and SPX rises 1%, the directional component should be positive before considering options repricing and hedges.

---

### Gamma P&L

Gamma P&L is the P&L generated by convexity and realized movement.

Why it matters:

Long Gamma can benefit from movement if hedged well. Short Gamma can lose when realized volatility is high.

Example:

A long-Gamma book buys futures after a selloff and sells after a rebound. The rebalancing can generate positive Gamma scalping P&L.

---

### Vega P&L

Vega P&L is the P&L from changes in implied volatility.

Why it matters:

Volatility repricing can dominate directional moves, especially in index options.

Example:

A desk short $100k per vol point of Vega loses roughly $500k if implied volatility rises 5 points, before considering changes in skew, Gamma, and spot.

---

### Skew P&L

Skew P&L is the P&L from changes in relative implied volatility across strikes.

Why it matters:

A book can be flat parallel Vega but exposed to the shape of the surface.

Example:

A trader is long ATM vol and short downside vol. If downside skew steepens while ATM vol is unchanged, the book can lose even though total implied volatility did not move much.

---

### Theta P&L

Theta P&L is the P&L from time passing.

Why it matters:

Theta can look attractive, but it often compensates for being short optionality.

Example:

A short option book earns $40k of Theta on a quiet day. But if the book is short Gamma, that carry must be judged against potential loss in a large move.

---

### Residual P&L

Residual P&L is the portion of P&L not explained by the main Greeks or known drivers.

Why it matters:

Residuals can reveal model limitations, stale marks, missing risk factors, bad data, or unexplained execution effects.

Example:

A desk explains most of the day’s loss through Delta and Vega, but $100k remains unexplained. That residual may prompt review of volatility marks, dividends, rates, or trade booking.

---

## Financing, Carry, and Relative Value

### Carry

Carry is the expected P&L from holding a position if market conditions remain broadly unchanged.

Why it matters:

Positive carry can be attractive, but it often comes with hidden exposure to gap risk, funding risk, convexity risk, or liquidity risk.

Example:

Selling index volatility may generate positive carry most days. But the trade can lose sharply when realized volatility spikes or implied volatility gaps higher.

---

### Basis

Basis is the pricing difference between related instruments.

Why it matters:

Basis connects cash, futures, ETFs, swaps, and options. It often reflects funding, dividends, borrow, liquidity, and balance sheet.

Example:

If futures trade rich to fair value relative to cash index pricing, the basis may reflect funding pressure, dividend assumptions, or demand for futures exposure.

---

### Implied Financing

Implied financing is the funding rate embedded in derivative prices.

Why it matters:

Options, forwards, futures, and boxes can all imply financing assumptions. Those assumptions can be compared to alternative funding markets.

Example:

A box spread pays $100 at expiration and costs $97.50 today. The difference implies a financing rate. A trader compares that implied rate to Treasury bills, repo, margin cost, and capital usage.

---

### Box Rate

Box rate is the annualized implied rate from a box spread.

Why it matters:

It turns an options structure into a financing comparison.

Example:

A 6-month SPX box costs $98 and pays $100 at expiration. Ignoring costs, the implied return is roughly 2% over six months, or about 4% annualized. The desk then asks whether margin, execution, and liquidity make that rate real.

---

### Funding Spread

Funding spread is the difference between one funding rate and another relevant benchmark.

Why it matters:

Relative value trades often depend on funding spread, not just asset price movement.

Example:

A desk can finance at SOFR plus 50 bps but a box implies SOFR plus 120 bps. The apparent spread may be attractive, but only if capital, margin, and execution costs do not consume it.

---

### Balance Sheet Usage

Balance sheet usage refers to the capital, leverage, or financing capacity consumed by a trade.

Why it matters:

A trade with attractive theoretical economics may be unattractive after balance sheet costs.

Example:

A relative value trade earns 20 bps of spread but consumes significant balance sheet. The return on capital may be too low compared with other uses of the desk’s capacity.

---

### Collateral Efficiency

Collateral efficiency refers to how effectively a position uses margin or collateral.

Why it matters:

Institutional trades are often judged by return on capital, not just raw P&L.

Example:

Two trades both expect to earn $100k. One requires $1 million of margin, the other requires $10 million. The first trade is much more capital efficient.

---

## Relative Value and Index Structure

### Dispersion

Dispersion compares index volatility to the volatility of the index components.

Why it matters:

Index volatility depends on both single-name volatility and correlation. Dispersion trades isolate that relationship.

Example:

A trader sells index variance and buys variance on the component stocks. If single names move a lot but correlations stay low, the component options may outperform the index option short.

---

### Correlation

Correlation measures how assets move together.

Why it matters:

Index option pricing embeds assumptions about component volatility and correlation. During stress, correlations often rise.

Example:

If all major index components begin falling together, index volatility can rise more than single-name volatility alone would suggest because correlation is increasing.

---

### Index Volatility

Index volatility reflects volatility of the whole basket, including component volatility and correlation.

Why it matters:

Index options are not just an average of single-name options. Correlation and concentration matter.

Example:

If the largest technology stocks dominate index movement, index volatility may rise even if smaller components are quiet.

---

### Correlation Skew

Correlation skew refers to how implied correlation differs across strikes or market scenarios.

Why it matters:

Downside index options often embed higher implied correlation because stocks tend to sell off together in stress.

Example:

A downside SPX put may be expensive not only because single-name vols are high, but because the market prices higher correlation in a crash scenario.

---

### Implied Correlation

Implied correlation is the correlation level inferred from index option prices and component option prices.

Why it matters:

It is central to dispersion and correlation trading.

Example:

If index options are very expensive relative to component options, the market may be implying high correlation. A dispersion trader evaluates whether that implied correlation is too high or too low.

---

## Flow, Events, and Desk Judgment

### Client Flow

Client flow refers to trades or inquiries coming from clients.

Why it matters:

Flow can reveal hedging demand, risk transfer pressure, supply/demand imbalance, or positioning themes.

Example:

Multiple asset managers ask to buy 3-month downside put spreads after a market rally. The desk may infer increased demand for portfolio protection.

---

### Edge

Edge is the compensation a desk believes it earns for taking or facilitating a trade.

Why it matters:

A trade can add risk but still be worth doing if the price is favorable enough.

Example:

A client wants to buy puts in size. The desk sells them only if the implied vol is high enough to compensate for short Gamma, short skew, hedging cost, and stress risk.

---

### Axe

An axe is the risk a desk wants to buy or sell.

Why it matters:

A desk’s inventory affects how aggressively it quotes.

Example:

If the desk is too short downside Vega, it may have an axe to buy downside options. A client selling puts may receive a tighter/better market because that flow helps the book.

---

### Event Vol

Event vol is implied volatility specifically associated with a known catalyst.

Why it matters:

Events can concentrate volatility into a narrow time window.

Example:

Short-dated options expiring after CPI may trade at elevated implied vol. Options expiring before CPI may not reflect the same event premium.

---

### Gap Risk

Gap risk is the risk of a large move occurring before a position can be hedged.

Why it matters:

Dynamic hedging assumes the ability to trade as markets move. Gaps break that assumption.

Example:

A desk short weekend options cannot hedge while the market is closed. If futures open sharply lower Sunday night, the book may realize a large loss before any hedge can be adjusted.

---

### Liquidity Regime

Liquidity regime describes the current state of market depth, transaction cost, and ability to move risk.

Why it matters:

The same position can be manageable in normal liquidity and dangerous in stressed liquidity.

Example:

Selling $500 million notional of futures may be easy during normal hours in calm markets but costly during a volatility shock.

---

## Modeling, Marks, and Assumptions

### Mark-to-Market

Mark-to-market is the process of valuing positions using current market prices or model-derived fair values.

Why it matters:

Daily P&L depends on marks. Illiquid strikes, wide markets, and surface assumptions can affect reported value.

Example:

A far OTM put has no recent trade and a wide market. The desk must mark it using a surface model, and that mark can materially affect P&L.

---

### Model Risk

Model risk is the risk that the pricing or risk model is wrong or incomplete.

Why it matters:

Greeks and valuations depend on model assumptions. A clean model output can hide bad assumptions.

Example:

A model assumes smooth volatility surface behavior, but during a selloff, downside skew reprices discontinuously. The model underestimates risk.

---

### Surface Marking

Surface marking is the process of setting implied volatility levels across strikes and expirations for valuation and risk.

Why it matters:

Options books are often marked from surfaces, not from every option trading actively.

Example:

If downside skew is marked 1 vol point higher across short maturities, a desk short downside puts may show a significant loss even if spot is unchanged.

---

### Scenario Analysis

Scenario analysis estimates book behavior under hypothetical market moves.

Why it matters:

Greeks are local. Scenario analysis helps evaluate nonlinear and stressed outcomes.

Example:

A trader shocks SPX down 3%, front-end vol up 6 points, and skew steeper. The scenario shows the book loses more than Delta and Vega alone implied.

---

### Local Risk

Local risk refers to small-move sensitivity around current market levels.

Why it matters:

Greeks are local risk measures. They are useful but incomplete.

Example:

A book may show modest Delta and Vega for a small spot move, but under a 5% selloff, Gamma, Vanna, skew, and liquidity effects can dominate.

---

### Path Dependency

Path dependency means the final P&L depends on the sequence of market moves, not just the endpoint.

Why it matters:

Options hedging and realized volatility strategies are path-dependent.

Example:

SPX starts and ends the week unchanged. A long-Gamma trader may make money if the market moved around enough intraday and hedges were executed well.

---

## Expiration and Short-Dated Options

### 0DTE

0DTE refers to options expiring the same day.

Why it matters:

Short-dated options can have intense Gamma, Charm, and intraday hedging sensitivity.

Example:

A large 0DTE position near the money can move from low Delta to high Delta very quickly as SPX approaches the strike in the final hour.

---

### Pinning

Pinning describes the tendency for the underlying to trade near a strike with large open interest or hedging sensitivity, though it should not be assumed mechanically.

Why it matters:

Expiration dynamics can affect hedging flows and intraday behavior.

Example:

SPX trades near a large strike into the close. Dealers hedging near-expiration options may need to adjust futures repeatedly as spot moves around the strike.

---

### Strike Magnet

Strike magnet is informal language for the idea that certain strikes may attract attention because of positioning, hedging, or open interest.

Why it matters:

It is a market-color concept, not a law. It should be treated carefully.

Example:

A large amount of open interest sits at the 5,500 strike. Traders may watch how spot behaves near that level, but they should not assume it must pin there.

---

### Expiry Roll-Off

Expiry roll-off is the disappearance of option exposure as contracts expire.

Why it matters:

Dealer positioning and Gamma exposure can change sharply after expiration.

Example:

A large amount of short-dated Gamma expires on Friday. On Monday, the market may have a different hedging profile because that exposure has rolled off.
