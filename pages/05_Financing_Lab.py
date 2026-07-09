import streamlit as st

st.set_page_config(
    page_title="Financing Lab | Institutional Markets Lab",
    page_icon="💵",
    layout="wide",
)

st.title("Financing Lab")
st.caption("A module for studying implied financing, box spreads, funding markets, and relative value.")

st.markdown(
    """
    The Financing Lab will explore how derivatives can embed financing rates,
    funding assumptions, collateral considerations, and relative value opportunities.

    The initial focus will be on understanding box spreads as synthetic borrowing
    or lending instruments.
    """
)

st.divider()

left_col, right_col = st.columns([2, 1])

with left_col:
    st.subheader("Core Questions")

    st.markdown(
        """
        This module will be built around several core questions:

        1. How can options imply a financing rate?
        2. Why can a box spread be interpreted as lending or borrowing?
        3. How does put-call parity connect options to rates and forwards?
        4. How do funding, margin, and collateral affect relative value?
        5. How do Treasury, repo, and derivatives markets connect?
        6. What risks remain even when a structure appears arbitrage-like?
        """
    )

with right_col:
    st.subheader("Build Status")

    st.info("Module shell created")
    st.warning("Box spread calculator not yet implemented")
    st.warning("Rate comparison not yet implemented")
    st.warning("Funding assumptions not yet connected")

st.divider()

st.subheader("Planned Topics")

topic_cols = st.columns(3)

with topic_cols[0]:
    st.markdown(
        """
        **Box Spreads**

        Using options to create synthetic borrowing or lending exposure.
        """
    )

with topic_cols[1]:
    st.markdown(
        """
        **Implied Rates**

        Extracting a financing rate from option structures.
        """
    )

with topic_cols[2]:
    st.markdown(
        """
        **Relative Value**

        Comparing implied financing to alternative funding or investment rates.
        """
    )

st.divider()

st.subheader("Institutional Framing")

st.markdown(
    """
    Financing is central to institutional markets. Trades that look attractive on payoff
    alone may depend heavily on margin, collateral, funding rates, taxes, execution costs,
    liquidity, and balance sheet constraints.

    The purpose of this module is to connect options pricing to capital efficiency,
    funding markets, and real-world implementation.
    """
)