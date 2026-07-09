import streamlit as st

st.set_page_config(
    page_title="Dealer Positioning Lab | Institutional Markets Lab",
    page_icon="🧭",
    layout="wide",
)

st.title("Dealer Positioning Lab")
st.caption("A module for studying dealer hedging, Gamma exposure, positioning, and market impact.")

st.markdown(
    """
    The Dealer Positioning Lab will explore how option dealer inventory and hedging behavior
    can influence market dynamics.

    This module will focus on intuition first: how dealers become long or short Gamma,
    how they hedge, and why positioning can matter for intraday market behavior.
    """
)

st.divider()

left_col, right_col = st.columns([2, 1])

with left_col:
    st.subheader("Core Questions")

    st.markdown(
        """
        This module will be built around several core questions:

        1. What does it mean for a dealer to be long or short Gamma?
        2. How does dealer hedging change as spot moves?
        3. Why can short-Gamma environments amplify market moves?
        4. Why can long-Gamma environments dampen realized volatility?
        5. How do options flows affect dealer inventory?
        6. How should positioning be interpreted without overstating precision?
        """
    )

with right_col:
    st.subheader("Build Status")

    st.info("Module shell created")
    st.warning("Gamma examples not yet implemented")
    st.warning("Scenario charts not yet implemented")
    st.warning("Data inputs not yet connected")

st.divider()

st.subheader("Planned Topics")

topic_cols = st.columns(3)

with topic_cols[0]:
    st.markdown(
        """
        **Gamma Exposure**

        How convexity changes Delta as spot moves.
        """
    )

with topic_cols[1]:
    st.markdown(
        """
        **Dealer Hedging**

        How inventory can require buying or selling the underlying.
        """
    )

with topic_cols[2]:
    st.markdown(
        """
        **Market Impact**

        How positioning may affect realized volatility and intraday flows.
        """
    )

st.divider()

st.subheader("Institutional Framing")

st.markdown(
    """
    Dealer positioning should be treated as a risk framework, not a magic market signal.

    The goal of this module is to understand the mechanics of hedging behavior, the limits
    of positioning estimates, and how options inventory can interact with liquidity,
    volatility, and client flow.
    """
)