import streamlit as st

st.set_page_config(
    page_title="Volatility Lab | Institutional Markets Lab",
    page_icon="📊",
    layout="wide",
)

st.title("Volatility Lab")
st.caption("A module for studying implied volatility, realized volatility, skew, term structure, and volatility surfaces.")

st.markdown(
    """
    The Volatility Lab will explore how volatility is observed, priced, and interpreted
    in institutional markets.

    This module is intentionally starting with clear explanations before advanced analytics.
    The first goal is to build intuition around what volatility means, why implied volatility
    differs from realized volatility, and how traders think about volatility across strikes
    and expirations.
    """
)

st.divider()

left_col, right_col = st.columns([2, 1])

with left_col:
    st.subheader("Core Questions")

    st.markdown(
        """
        This module will be built around several core questions:

        1. What is realized volatility?
        2. What is implied volatility?
        3. Why does implied volatility usually differ from realized volatility?
        4. What does the volatility term structure tell us?
        5. What is skew, and why does it matter in index options?
        6. How does a volatility surface summarize market pricing across strikes and expirations?
        """
    )

with right_col:
    st.subheader("Build Status")

    st.info("Module shell created")
    st.warning("Analytics not yet implemented")
    st.warning("Charts not yet implemented")
    st.warning("Data inputs not yet connected")

st.divider()

st.subheader("Volatility Concepts")

concept_cols = st.columns(3)

with concept_cols[0]:
    st.markdown(
        """
        **Realized Volatility**

        Realized volatility measures how much the underlying asset actually moved
        over a historical period.
        """
    )

with concept_cols[1]:
    st.markdown(
        """
        **Implied Volatility**

        Implied volatility is the volatility level embedded in option prices. It reflects
        the market price of optionality, uncertainty, supply/demand, and risk premium.
        """
    )

with concept_cols[2]:
    st.markdown(
        """
        **Volatility Risk Premium**

        Implied volatility is often higher than subsequently realized volatility because
        option sellers usually require compensation for bearing volatility and tail risk.
        """
    )

st.divider()

st.subheader("Future Analytics")

st.markdown(
    """
    Future versions of this page may include:

    - Realized volatility calculator
    - Implied vs realized volatility comparison
    - Volatility term structure chart
    - Skew visualization
    - Simplified volatility surface
    - SPX/VIX relationship notes
    - Desk-style interpretation of volatility regimes
    """
)

st.divider()

st.subheader("Institutional Framing")

st.markdown(
    """
    Volatility is not just a statistical measure. On an options desk, volatility connects
    directly to pricing, hedging, risk limits, client demand, market stress, and P&L.

    The purpose of this module is to move from textbook definitions toward desk-style
    interpretation:

    - Is implied volatility rich or cheap relative to realized volatility?
    - Is the market paying up for downside protection?
    - Is short-dated volatility elevated because of event risk?
    - Is skew steepening or flattening?
    - How would a trader think about owning or selling this volatility?
    """
)