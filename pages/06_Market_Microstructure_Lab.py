import streamlit as st

st.set_page_config(
    page_title="Market Microstructure Lab | Institutional Markets Lab",
    page_icon="⚙️",
    layout="wide",
)

st.title("Market Microstructure Lab")
st.caption("A module for studying liquidity, execution, order flow, market makers, and trading infrastructure.")

st.markdown(
    """
    The Market Microstructure Lab will explore how markets actually function beneath
    the price chart: order books, liquidity, spreads, execution, market makers,
    electronic trading, and order lifecycle.

    This module connects directly to trading operations, electronic execution,
    and desk-adjacent market workflows.
    """
)

st.divider()

left_col, right_col = st.columns([2, 1])

with left_col:
    st.subheader("Core Questions")

    st.markdown(
        """
        This module will be built around several core questions:

        1. What is the order lifecycle?
        2. What is the difference between liquidity, volume, and market depth?
        3. Why do bid/ask spreads widen or tighten?
        4. What does a market maker do?
        5. How does electronic execution route and monitor orders?
        6. How do microstructure frictions affect trading decisions?
        """
    )

with right_col:
    st.subheader("Build Status")

    st.info("Module shell created")
    st.warning("Order lifecycle examples not yet implemented")
    st.warning("Liquidity visuals not yet implemented")
    st.warning("Execution scenarios not yet implemented")

st.divider()

st.subheader("Planned Topics")

topic_cols = st.columns(3)

with topic_cols[0]:
    st.markdown(
        """
        **Order Lifecycle**

        From order creation to routing, execution, fill, allocation, and post-trade processing.
        """
    )

with topic_cols[1]:
    st.markdown(
        """
        **Liquidity and Spreads**

        How depth, volatility, uncertainty, and inventory risk affect transaction costs.
        """
    )

with topic_cols[2]:
    st.markdown(
        """
        **Market Makers**

        How market makers provide liquidity, manage inventory, and respond to flow.
        """
    )

st.divider()

st.subheader("Institutional Framing")

st.markdown(
    """
    Market microstructure is the bridge between theoretical prices and real execution.

    A model may say what something is worth, but microstructure determines whether a desk
    can actually trade it, hedge it, scale it, and manage the resulting risk.
    """
)