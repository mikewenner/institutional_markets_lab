import streamlit as st

st.set_page_config(
    page_title="Home | Institutional Markets Lab",
    page_icon="🏛️",
    layout="wide",
)

st.title("Institutional Markets Lab")
st.caption("A Streamlit-based institutional markets analytics workstation.")

st.markdown(
    """
    Institutional Markets Lab is a long-term learning and software development project
    focused on equity derivatives, index options, volatility, dealer positioning,
    financing, market microstructure, and desk-style analytics.

    The goal is to build a professional, modular application that supports deeper
    institutional markets understanding while also demonstrating clean Python,
    Streamlit, and software development practices.
    """
)

st.divider()

left_col, right_col = st.columns([2, 1])

with left_col:
    st.subheader("Project Mission")

    st.markdown(
        """
        Build a polished institutional markets workstation that connects:

        - Market concepts
        - Data and visualization
        - Derivatives intuition
        - Risk management thinking
        - Professional software development
        """
    )

    st.subheader("Current Development Focus")

    st.markdown(
        """
        The project is currently in the foundation phase:

        1. Create the repo and README
        2. Build the Streamlit app shell
        3. Create the Home Dashboard
        4. Begin the Volatility Lab
        5. Add SPX options and Greeks modules
        """
    )

with right_col:
    st.subheader("Build Status")

    st.success("README complete")
    st.success("Repo structure created")
    st.success("Streamlit app shell running")
    st.info("Home Dashboard in progress")
    st.warning("Analytics modules not yet built")

st.divider()

st.subheader("Core Modules")

module_cols = st.columns(3)

with module_cols[0]:
    st.markdown(
        """
        **Volatility Lab**  
        Implied volatility, realized volatility, skew, term structure, and volatility surfaces.
        """
    )

    st.markdown(
        """
        **SPX Options Lab**  
        Payoffs, put-call parity, synthetic positions, box spreads, and Greeks.
        """
    )

with module_cols[1]:
    st.markdown(
        """
        **Dealer Positioning Lab**  
        Gamma exposure, hedging intuition, spot/vol dynamics, and risk concentration.
        """
    )

    st.markdown(
        """
        **Financing Lab**  
        Box spread rates, synthetic financing, funding markets, and relative value.
        """
    )

with module_cols[2]:
    st.markdown(
        """
        **Market Microstructure Lab**  
        Order lifecycle, liquidity, bid/ask spreads, execution, and market makers.
        """
    )

    st.markdown(
        """
        **Learning Journal**  
        Research notes, open questions, desk-style observations, and concept summaries.
        """
    )

st.divider()

st.subheader("Long-Term Capstone Idea")

st.markdown(
    """
    A future module may include an **SPX Trader Simulation Lab** where the user is
    walked through a simulated trading day on an index options desk.

    The simulation could present client orders, market flow, volatility changes,
    and book-level risk decisions. The app would track simplified Greeks, inventory,
    hedging decisions, and estimated P&L while explaining the desk-style reasoning
    behind each choice.
    """
)

st.divider()

st.subheader("Development Philosophy")

st.markdown(
    """
    This project follows a simple workflow:

    **Learn the market concept → prototype the logic → build reusable Python modules → add the Streamlit interface → document the intuition.**

    Jupyter notebooks may be used for exploration, but durable logic should move into
    reusable Python modules under `src/`.
    """
)