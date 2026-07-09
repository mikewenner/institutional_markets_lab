import streamlit as st

st.set_page_config(
    page_title="SPX Options Lab | Institutional Markets Lab",
    page_icon="📈",
    layout="wide",
)

st.title("SPX Options Lab")
st.caption("A module for studying index options, payoffs, parity, synthetics, Greeks, and box spreads.")

st.markdown(
    """
    The SPX Options Lab will focus on the mechanics and institutional use cases of index options.

    This module will eventually connect option payoff intuition, put-call parity, synthetic positions,
    box spreads, Greeks, and book-level risk thinking.
    """
)

st.divider()

left_col, right_col = st.columns([2, 1])

with left_col:
    st.subheader("Core Questions")

    st.markdown(
        """
        This module will be built around several core questions:

        1. How do calls and puts create nonlinear payoff profiles?
        2. What does put-call parity reveal about forwards, rates, and synthetic positions?
        3. How do traders use options to create synthetic long or short exposure?
        4. What is a box spread, and why does it imply a financing rate?
        5. How do Delta, Gamma, Vega, and Theta affect the risk of an options book?
        6. How does SPX options flow differ from single-name options flow?
        """
    )

with right_col:
    st.subheader("Build Status")

    st.info("Module shell created")
    st.warning("Payoff charts not yet implemented")
    st.warning("Greeks not yet implemented")
    st.warning("Box spread calculator not yet implemented")

st.divider()

st.subheader("Planned Topics")

topic_cols = st.columns(3)

with topic_cols[0]:
    st.markdown(
        """
        **Payoff Mechanics**

        Calls, puts, spreads, collars, and combinations.
        """
    )

    st.markdown(
        """
        **Put-Call Parity**

        The relationship between calls, puts, forwards, strikes, rates, and dividends.
        """
    )

with topic_cols[1]:
    st.markdown(
        """
        **Synthetic Positions**

        Using options and cash to replicate equity, forwards, borrowing, or lending.
        """
    )

    st.markdown(
        """
        **Box Spreads**

        A structure that can be interpreted as synthetic lending or borrowing.
        """
    )

with topic_cols[2]:
    st.markdown(
        """
        **Greeks**

        Delta, Gamma, Vega, Theta, and how they shape risk management decisions.
        """
    )

    st.markdown(
        """
        **Book Risk**

        Moving from single-trade payoff diagrams toward portfolio-level risk.
        """
    )

st.divider()

st.subheader("Institutional Framing")

st.markdown(
    """
    Index options are not only tools for directional speculation. On institutional desks,
    they are connected to hedging demand, volatility supply and demand, financing,
    risk transfer, structured products, dealer positioning, and client flow.

    The purpose of this module is to understand options as instruments for pricing,
    hedging, risk warehousing, and relative value.
    """
)