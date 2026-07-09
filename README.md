# Institutional Markets Lab

**Institutional Markets Lab** is a Streamlit-based analytics workstation for studying and visualizing institutional market concepts across equity derivatives, index options, volatility, market microstructure, dealer positioning, and financing.

The project is designed as both a learning platform and a professional portfolio artifact. Its purpose is to help bridge the gap between data science work in financial services and institutional markets roles such as equity derivatives, index derivatives, volatility analytics, options market making, electronic execution, risk, and trading-adjacent analytics.

---

## Why This Project Exists

I currently work in financial services analytics, using Python, SQL, and data visualization to analyze large-scale customer, deposits, payments, spend, liquidity, and transaction datasets. Over time, my strongest professional interest has moved toward markets: derivatives, volatility, index flow, market structure, execution, financing, and risk.

Institutional Markets Lab is my long-term effort to build that knowledge in public through code, research, visualization, and structured learning.

The goal is not to build a retail trading tool or a directional signal generator. The goal is to understand how institutional market participants think about pricing, risk, positioning, flows, funding, and relative value.

---

## Project Objectives

The project has four main objectives:

1. **Build institutional markets knowledge**

   * Learn the core mechanics behind derivatives, volatility, financing, and market structure.
   * Focus on concepts used by trading desks, market makers, hedge funds, and institutional risk teams.

2. **Develop a professional analytics workstation**

   * Build a polished Streamlit application with modular pages, clean architecture, and reusable analytics components.
   * Treat the project like a real internal desk tool or research platform.

3. **Strengthen software development skills**

   * Use VS Code as the primary development environment.
   * Improve project organization, modular Python development, Git/GitHub workflow, testing discipline, and code readability.
   * Use Jupyter notebooks where appropriate for research, exploration, and prototyping, then migrate durable logic into reusable Python modules.

4. **Create a portfolio artifact for career transition**

   * Demonstrate technical ability, market curiosity, and institutional thinking.
   * Build something that can eventually be shared with mentors, traders, hiring managers, and market professionals.

---

## What the App Will Do

Institutional Markets Lab will eventually provide interactive modules for exploring:

* Volatility surfaces
* SPX and index options
* Put-call parity
* Synthetic positions
* Box spreads
* Conversion and reversal arbitrage
* Dealer gamma and positioning
* Index and volatility flows
* VIX and variance products
* Financing, funding, and implied rates
* Market microstructure
* Execution concepts
* Relative value frameworks
* Learning notes and research journals

The app will prioritize clarity, intuition, and institutional relevance over complexity for its own sake.

---

## Target Users

This project is built for four audiences:

1. **Current self**

   * To learn institutional markets deeply and actively through code.

2. **Future self**

   * To serve as a durable reference library and analytics platform.

3. **Interviewers and hiring managers**

   * To demonstrate practical market understanding, technical skill, and initiative.

4. **Institutional market professionals**

   * To make the project credible enough that traders, desk analysts, and mentors can understand the thought process behind it.

---

## Core Design Principles

### 1. Learning Before Coding

Each module should start with a market question before any code is written.

Examples:

* What does a volatility surface tell us that a single implied volatility number does not?
* How does put-call parity connect options, forwards, rates, and synthetic financing?
* What does a box spread imply about funding?
* How can dealer gamma exposure affect intraday market behavior?
* How do execution, liquidity, and order flow shape market outcomes?

### 2. Institutional Framing

The project should avoid retail trading language, chart-pattern commentary, and simple directional predictions.

The focus should be on:

* Pricing
* Risk
* Hedging
* Flow
* Liquidity
* Financing
* Market structure
* Relative value
* Positioning

### 3. Modular Architecture

Each major topic should eventually become its own Streamlit module or page.

The long-term goal is a clean, modular application where notebooks are used for exploration and Python modules power the production app.

### 4. Professional Presentation

The project should be built as if it could eventually be shown to a trader, desk analyst, quantitative researcher, or hiring manager.

That means:

* Clear README
* Clean folder structure
* Descriptive commit history
* Documented assumptions
* Well-labeled charts
* Minimal clutter
* Reproducible examples
* Thoughtful explanations

---

## Initial MVP Scope

The first version of Institutional Markets Lab will focus on building a polished foundation rather than covering every possible topic.

### MVP Modules

1. **Home Dashboard**

   * Project overview
   * Market focus areas
   * Current development status
   * Navigation to core modules

2. **Volatility Lab**

   * Implied volatility basics
   * Volatility term structure
   * Skew
   * Volatility surface concepts
   * Realized vs implied volatility

3. **SPX Options Lab**

   * Option payoff diagrams
   * Put-call parity
   * Synthetic forwards
   * Box spreads
   * Conversion/reversal concepts

4. **Dealer Positioning Lab**

   * Gamma exposure concepts
   * Dealer hedging intuition
   * Spot/vol relationship
   * Market impact scenarios

5. **Financing Lab**

   * Implied financing
   * Box spread rates
   * Synthetic borrowing/lending
   * Treasury/repo connections

6. **Market Microstructure Lab**

   * Order lifecycle
   * Liquidity
   * Bid/ask spreads
   * Market makers
   * Electronic execution concepts

7. **Learning Journal**

   * Notes from research
   * Open questions
   * Desk-style observations
   * Concept explanations

---

## Technology Stack

### Core Tools

* **Python**
* **Streamlit**
* **Pandas**
* **NumPy**
* **Matplotlib / Plotly**
* **SQL**
* **Git / GitHub**
* **VS Code**
* **Jupyter Notebook**

### Development Philosophy

VS Code will be the primary development environment for the project. Jupyter notebooks may be used for research, early exploration, and concept testing, but reusable logic should eventually be moved into structured Python files.

The intended workflow is:

1. Explore concept in notes or notebook.
2. Build a small prototype.
3. Refactor logic into Python modules.
4. Add the concept to the Streamlit app.
5. Document the market intuition and assumptions.
6. Commit cleanly to GitHub.

---

## Planned Project Structure

```text
institutional-markets-lab/
│
├── README.md
├── requirements.txt
├── app.py
│
├── pages/
│   ├── 01_Home.py
│   ├── 02_Volatility_Lab.py
│   ├── 03_SPX_Options_Lab.py
│   ├── 04_Dealer_Positioning_Lab.py
│   ├── 05_Financing_Lab.py
│   ├── 06_Market_Microstructure_Lab.py
│   └── 07_Learning_Journal.py
│
├── src/
│   ├── options/
│   ├── volatility/
│   ├── financing/
│   ├── microstructure/
│   ├── dealer_positioning/
│   └── utils/
│
├── notebooks/
│   ├── volatility_research.ipynb
│   ├── spx_options_research.ipynb
│   └── financing_research.ipynb
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── sample/
│
├── docs/
│   ├── concepts/
│   ├── roadmap.md
│   └── glossary.md
│
└── tests/
```

---

## Development Roadmap

### Phase 0: Foundation

* Define project purpose
* Create README
* Set up GitHub repo
* Set up VS Code project
* Create initial folder structure
* Create basic Streamlit app shell

### Phase 1: Home Dashboard

* Build landing page
* Add project mission
* Add module navigation
* Add development status
* Add market themes

### Phase 2: Volatility Lab

* Add realized vs implied volatility examples
* Add term structure visualizations
* Add skew examples
* Add volatility surface explanation

### Phase 3: SPX Options Lab

* Add payoff diagrams
* Add put-call parity walkthrough
* Add synthetic forward example
* Add box spread example
* Add implied financing calculation

### Phase 4: Financing and Relative Value

* Expand box spread analytics
* Add implied borrowing/lending rate examples
* Connect options pricing to rates, funding, and capital efficiency

### Phase 5: Dealer Positioning and Market Microstructure

* Add dealer gamma intuition
* Add hedging scenario examples
* Add liquidity and execution concepts
* Add order lifecycle explanations

### Phase 6: Polish and External Readiness

* Improve UI/UX
* Add documentation
* Add examples
* Clean codebase
* Prepare for GitHub sharing
* Prepare project walkthrough for networking and interviews

---

## Learning Philosophy

This project is not about pretending to already be an expert. It is about building expertise through deliberate study, implementation, and explanation.

The process matters as much as the final app.

Each module should answer three questions:

1. **What is the market concept?**
2. **Why does it matter institutionally?**
3. **How can it be represented with data, code, or visualization?**

---

## Current Status

This project is in early development.

The initial focus is on:

* Setting up the repository
* Building the README
* Creating the project structure
* Developing the first Streamlit app shell
* Starting with a clean Home Dashboard and Volatility Lab

---

## Disclaimer

This project is for education, research, and professional development only.

It is not investment advice, trading advice, or a recommendation to buy or sell any security, derivative, or financial product. Any examples are simplified for learning purposes and may omit real-world considerations such as transaction costs, margin requirements, liquidity, taxes, funding constraints, execution risk, and model risk.

---

## Long-Term Vision

The long-term vision for Institutional Markets Lab is to become a polished, modular institutional markets workstation that demonstrates:

* Strong Python and analytics capability
* Practical software development discipline
* Institutional derivatives understanding
* Curiosity about market structure and risk
* Ability to turn complex market concepts into clear analytical tools

The project should eventually be strong enough to support career conversations with traders, desk analysts, quantitative researchers, market makers, and hiring managers.

