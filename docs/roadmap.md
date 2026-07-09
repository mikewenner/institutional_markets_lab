# Institutional Markets Lab Roadmap

This roadmap tracks the planned development path for Institutional Markets Lab.

The goal is to build a polished, modular Streamlit-based institutional markets workstation focused on derivatives, volatility, index options, financing, dealer positioning, market microstructure, and desk-style analytics.

---

## Current Status

The project is in the initial shell phase.

Completed:

- Initial README
- Project folder structure
- Virtual environment setup
- Basic Streamlit app shell
- Home Dashboard page
- Volatility Lab placeholder
- SPX Options Lab placeholder
- Dealer Positioning Lab placeholder
- Financing Lab placeholder
- Market Microstructure Lab placeholder
- Learning Journal placeholder

Next focus:

- Improve documentation
- Create module-specific concept notes
- Begin the first real analytics build inside the Volatility Lab

---

## Phase 0: Foundation

Goal: create the basic repository, app structure, and development workflow.

Completed:

- Create GitHub repository
- Add README
- Open project in VS Code
- Create virtual environment
- Add dependencies
- Create Streamlit app shell
- Create initial multipage app structure
- Commit and push initial project milestones

---

## Phase 1: App Shell and Navigation

Goal: create a clickable workstation shell that communicates the full project vision.

Completed:

- Main app entry point
- Home Dashboard
- Placeholder pages for all initial modules

Modules currently represented:

1. Home Dashboard
2. Volatility Lab
3. SPX Options Lab
4. Dealer Positioning Lab
5. Financing Lab
6. Market Microstructure Lab
7. Learning Journal

---

## Phase 2: Volatility Lab

Goal: build the first true analytics module.

Planned features:

- Realized volatility calculator
- Simple return series example
- Annualized volatility explanation
- Implied vs realized volatility comparison
- Volatility term structure visualization
- Skew explanation
- Simplified volatility surface concept
- Desk-style interpretation of volatility regimes

Core learning questions:

- What is realized volatility?
- What is implied volatility?
- Why does implied volatility often differ from realized volatility?
- What does term structure tell us?
- What is skew?
- How do traders think about volatility across strike and expiry?

---

## Phase 3: SPX Options Lab

Goal: build a desk-quality SPX options module that goes beyond retail options education.

This module should frame SPX options as institutional products used for:

- Risk transfer
- Hedging
- Volatility exposure
- Financing
- Index flow
- Book-level risk management
- Relative value
- Client facilitation

Important future topics:

- SPX vs SPY vs ES options
- Index hedging demand
- Client flow and dealer response
- Put-call parity
- Synthetic forwards
- Box spreads and implied financing
- Conversion and reversal intuition
- Volatility surface, skew, and term structure
- Greeks at the portfolio/book level
- Dealer inventory and hedging
- Structured product flow
- Liquidity and execution considerations
- Dispersion and index/single-name relationships
- P&L and risk attribution

Note:

The current SPX Options Lab page is only a placeholder. When developed further, it should be upgraded into a more institutional, desk-style module rather than a generic options education page.

---

## Phase 4: Dealer Positioning Lab

Goal: explain dealer hedging behavior and positioning frameworks.

Planned features:

- Long gamma vs short gamma intuition
- Delta hedging examples
- Spot move scenario analysis
- Dealer hedge direction examples
- Gamma exposure visualizations
- Caveats around positioning estimates
- Relationship between options inventory, liquidity, and realized volatility

Core learning questions:

- What does it mean for a dealer to be long or short gamma?
- How does hedging behavior change as spot moves?
- Why can short-gamma conditions amplify market moves?
- Why can long-gamma conditions dampen moves?
- What are the limits of dealer positioning analysis?

---

## Phase 5: Financing Lab

Goal: connect options pricing to financing, funding, and relative value.

Planned features:

- Box spread payoff example
- Implied financing calculator
- Comparison to Treasury or money market rates
- Synthetic borrowing/lending explanation
- Put-call parity connection
- Margin and collateral discussion
- Implementation risks

Core learning questions:

- How can options imply a financing rate?
- Why is a box spread similar to lending or borrowing?
- How do rates, forwards, and options connect?
- What real-world risks remain after the payoff is defined?

---

## Phase 6: Market Microstructure Lab

Goal: build intuition around execution, liquidity, and trading infrastructure.

Planned features:

- Order lifecycle explanation
- Bid/ask spread examples
- Liquidity vs volume vs depth
- Market maker role
- Electronic execution workflow
- Connectivity and order monitoring concepts
- Slippage and transaction cost examples

Core learning questions:

- What happens between order creation and execution?
- Why do spreads widen?
- What does liquidity actually mean?
- How do market makers manage inventory?
- Why does execution matter even when valuation is correct?

---

## Phase 7: Learning Journal

Goal: make the learning process visible, structured, and durable.

Planned features:

- Research notes
- Open questions
- Glossary links
- Module-specific concept notes
- Desk-style observations
- Interview preparation notes
- Lessons learned while building
- Software development notes

---

## Future Capstone: SPX Trader Simulation Lab

Goal: create an interactive simulation that walks the user through a day on an SPX/index options desk.

This would be a capstone module after the foundational topics are built.

Potential features:

- Simulated trading day
- Client orders and market flow
- User decisions around pricing, hedging, passing, or warehousing risk
- Book-level tracking of Delta, Gamma, Vega, Theta, inventory, and estimated P&L
- Market events such as spot moves, volatility changes, liquidity changes, and event risk
- Desk-style feedback after each decision
- Teaching commentary explaining what happened and why
- Potential free-text user responses instead of only multiple choice
- Potential AI/API integration for interactive coaching and feedback

Example scenario:

A client asks for a market on SPX downside puts during a weak open. The simulated desk is already short gamma. The user must decide whether to show aggressively, widen the market, pass, trade smaller size, or hedge immediately.

The app would then explain:

- How the decision changes the book
- What happens to Greeks
- What risks were added or reduced
- What P&L drivers matter next
- How a desk might think about the trade in real life

This module should not be started until the project has stronger foundations in:

- Options mechanics
- Greeks
- Volatility
- Skew
- Term structure
- Dealer hedging
- Financing
- Market microstructure
- Book-level risk
- P&L attribution

---

## Development Principles

1. Learn the market concept before coding the feature.
2. Keep pages clean and readable.
3. Move reusable logic into `src/`.
4. Use notebooks for exploration, not final app logic.
5. Commit after each logical milestone.
6. Prefer institutional framing over retail trading language.
7. Document assumptions clearly.
8. Build toward something credible enough to show to traders, mentors, and hiring managers.

---

## Near-Term Build Order

The likely near-term sequence is:

1. Finalize app shell
2. Add roadmap and glossary docs
3. Create first real Volatility Lab calculation
4. Add realized volatility function under `src/volatility/`
5. Add a simple interactive volatility calculator to Streamlit
6. Add first chart
7. Document the concept in the Learning Journal or docs
8. Commit the first real analytics feature