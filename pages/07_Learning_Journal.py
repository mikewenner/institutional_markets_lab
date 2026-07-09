import streamlit as st

st.set_page_config(
    page_title="Learning Journal | Institutional Markets Lab",
    page_icon="📓",
    layout="wide",
)

st.title("Learning Journal")
st.caption("A module for research notes, open questions, desk-style observations, and concept summaries.")

st.markdown(
    """
    The Learning Journal will track the research, questions, insights, and open threads
    that emerge while building Institutional Markets Lab.

    This page is intended to make the learning process visible, structured, and durable.
    """
)

st.divider()

left_col, right_col = st.columns([2, 1])

with left_col:
    st.subheader("Purpose")

    st.markdown(
        """
        The Learning Journal will eventually include:

        - Research notes
        - Definitions
        - Open questions
        - Desk-style observations
        - Interview preparation notes
        - Concepts to revisit
        - Module-specific learning summaries
        """
    )

with right_col:
    st.subheader("Build Status")

    st.info("Module shell created")
    st.warning("Journal entries not yet implemented")
    st.warning("Search/filter not yet implemented")
    st.warning("Markdown note system not yet implemented")

st.divider()

st.subheader("Initial Learning Themes")

theme_cols = st.columns(3)

with theme_cols[0]:
    st.markdown(
        """
        **Derivatives Mechanics**

        Payoffs, parity, synthetics, Greeks, and volatility.
        """
    )

with theme_cols[1]:
    st.markdown(
        """
        **Desk Thinking**

        Flow, risk warehousing, hedging, client demand, and P&L attribution.
        """
    )

with theme_cols[2]:
    st.markdown(
        """
        **Software Development**

        VS Code, Git, modular Python, Streamlit, documentation, and app architecture.
        """
    )

st.divider()

st.subheader("Future Capstone Note")

st.markdown(
    """
    A future SPX Trader Simulation Lab may use the concepts from this project to walk
    through simulated desk decisions involving client flow, hedging, book risk, and P&L.

    The Learning Journal can serve as the research base for that future simulation module.
    """
)