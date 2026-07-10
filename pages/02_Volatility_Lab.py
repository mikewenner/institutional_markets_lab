
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from src.volatility import calculate_realized_volatility

def subtle_divider() -> None:
    """Render a faint Bloomberg-style divider line."""
    st.markdown(
        """
        <hr style="
            border: none;
            border-top: 1px solid rgba(180, 180, 180, 0.22);
            margin: 0.75rem 0;
        ">
        """,
        unsafe_allow_html=True,
    )

st.set_page_config(
    page_title="Volatility Lab | Institutional Markets Lab",
    page_icon="📊",
    layout="wide",
)

st.title("SPX / VIX Volatility Lab")
st.caption(
    "A real-market volatility workstation for SPX realized volatility, "
    "VIX-implied volatility, volatility risk premium, and index-volatility regime analysis."
)

st.markdown(
    """
    The Volatility Lab studies the relationship between **SPX index movement**
    and **VIX-implied volatility**.

    The core objective is to understand what volatility regime SPX is currently
    realizing, what VIX is implying about forward index volatility, and whether
    the market is pricing calm, protection demand, event risk, or stress.

    This page focuses on market-level volatility regime analysis. Detailed SPX
    option-chain structure, skew, term structure, and volatility-surface analytics
    will live in the SPX Options Lab.
    """
)

st.divider()

left_col, right_col = st.columns([2, 1])

with left_col:
    st.subheader("Core Questions")

    st.markdown(
        """
        This module is built around several institutional volatility questions:

        1. What volatility regime is SPX currently realizing?
        2. Is SPX realized volatility accelerating or calming down across short- and medium-term windows?
        3. How do 5-day, 10-day, 20-day, and 60-day SPX realized volatility compare?
        4. What is VIX implying about forward SPX volatility?
        5. Is VIX elevated or depressed relative to recent SPX realized volatility?
        6. Is the realized/implied spread widening or narrowing?
        7. Is the market pricing calm, protection demand, event risk, or stress?
        8. What is the desk-level interpretation of the current SPX/VIX volatility setup?
        """
    )

with right_col:
    st.info("Module shell created")
    st.info("Realized volatility function implemented")
    st.warning("Real SPX/VIX data not yet connected")
    st.warning("Implied-vs-realized analytics not yet implemented")
    st.warning("Desk interpretation layer not yet implemented")

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

st.subheader("Temporary Mechanics Demo")

st.markdown(
    """
    This first analytics demo calculates rolling annualized realized volatility
    from a synthetic price series.

    The goal is to connect the concept of realized volatility to the underlying
    price path, the selected return window, and reusable code in the
    `src/volatility/` analytics package.
    """
)

np.random.seed(42)

dates = pd.date_range(
    start="2024-01-01",
    periods=252,
    freq="B",
)

daily_returns = np.random.normal(
    loc=0.0003,
    scale=0.012,
    size=len(dates),
)

prices = pd.Series(
    100 * (1 + pd.Series(daily_returns, index=dates)).cumprod(),
    index=dates,
    name="Synthetic Index",
)

controls_col, chart_col = st.columns([1, 2.4])

with controls_col:
    st.markdown("### Controls")

    window_mode = st.radio(
        "Window selection mode",
        options=[
            "Latest rolling window",
            "Custom date range",
        ],
        index=0,
        help="Choose whether realized volatility is calculated from the latest rolling window or a custom historical date range.",
    )
    window = st.slider(
        "Rolling volatility window",
        min_value=5,
        max_value=60,
        value=20,
        step=1,
        help="Number of trading days used to calculate rolling realized volatility.",
    )

    if window_mode == "Custom date range":
        custom_start_date = st.date_input(
            "Custom start date",
            value=prices.index[-window].date(),
            min_value=prices.index[0].date(),
            max_value=prices.index[-1].date(),
        )

        custom_end_date = st.date_input(
            "Custom end date",
            value=prices.index[-1].date(),
            min_value=prices.index[0].date(),
            max_value=prices.index[-1].date(),
        )

    annualization_factor = st.number_input(
        "Annualization factor",
        min_value=1,
        max_value=365,
        value=252,
        help="For daily market data, 252 is the standard trading-day annualization factor.",
    )

    #subtle_divider()
# Synthetic data for the first demo.
# Later, this can be replaced with real SPX/SPY/VIX data.


realized_vol = calculate_realized_volatility(
    prices=prices,
    window=window,
    annualization_factor=annualization_factor,
)

latest_realized_vol = realized_vol.dropna().iloc[-1]

latest_price = prices.iloc[-1]
starting_price = prices.iloc[0]
total_return = latest_price / starting_price - 1

daily_return_series = prices.pct_change()
latest_daily_return = daily_return_series.iloc[-1]

if window_mode == "Latest rolling window":
    selected_prices = prices.tail(window)
    selected_window_label = f"Last {window} Days"

else:
    selected_start = pd.Timestamp(custom_start_date)
    selected_end = pd.Timestamp(custom_end_date)

    selected_prices = prices.loc[
        (prices.index >= selected_start) & (prices.index <= selected_end)
    ]

    selected_window_label = (
        f"{selected_start.date()} to {selected_end.date()}"
    )

selected_start_date = selected_prices.index[0]
selected_end_date = selected_prices.index[-1]

selected_starting_price = selected_prices.iloc[0]
selected_end_price = selected_prices.iloc[-1]
selected_return = selected_end_price / selected_starting_price - 1

selected_daily_returns = daily_return_series.loc[selected_prices.index].dropna()
selected_average_daily_return = selected_daily_returns.mean()

selected_realized_vol = selected_daily_returns.std() * np.sqrt(
    annualization_factor
)

with controls_col:
    st.markdown(
        """
        <hr style="border: 0.5px solid rgba(180, 180, 180, 0.25); margin: 0.75rem 0;">
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### Price Path Context")

    st.markdown(
        f"""
        <div style="font-size: 0.82rem; line-height: 1.45; margin-bottom: 0.9rem;">
            <div><b>Starting Price:</b> {starting_price:,.2f}</div>
            <div><b>Latest Price:</b> {latest_price:,.2f}</div>
            <div><b>Total Return:</b> {total_return:.2%}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <hr style="border: 0.5px solid rgba(180, 180, 180, 0.25); margin: 0.75rem 0;">
        """,
        unsafe_allow_html=True,
    )
    
    #subtle_divider()

    st.markdown("### Selected Window")

    st.markdown(
        f"""
        <div style="
            border: 1px solid rgba(180, 180, 180, 0.28);
            border-radius: 0.35rem;
            padding: 0.75rem;
            background-color: rgba(20, 20, 20, 0.65);
            font-size: 0.82rem;
            line-height: 1.45;
        ">
            <div style="font-size: 0.75rem; opacity: 0.75; margin-bottom: 0.15rem;">
                Selected Period Realized Volatility
            </div>
            <div style="font-size: 1.65rem; font-weight: 700; color: #f5b041; margin-bottom: 0.65rem;">
                {selected_realized_vol:.2%}
            </div>
            <div><b>Selected Period:</b> {selected_window_label}</div>
            <div><b>Period Return:</b> {selected_return:.2%}</div>
            <div><b>Avg Daily Return:</b> {selected_average_daily_return:.2%}</div>
            <div><b>Latest Daily Return:</b> {latest_daily_return:.2%}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    subtle_divider()

    st.caption(
        "The shaded chart region is the selected period used to calculate "
        "the realized volatility estimate."
    )

with chart_col:
    #st.markdown("**Synthetic Index Price Path**")

    price_fig = go.Figure()

    price_fig.add_trace(
        go.Scatter(
            x=prices.index,
            y=prices.values,
            mode="lines",
            name="Synthetic Index",
            line=dict(color="#f5b041", width=2),
            hovertemplate="Date: %{x}<br>Index Level: %{y:.2f}<extra></extra>",
    )
)

    price_fig.add_vrect(
        x0=selected_start_date,
        x1=selected_end_date,
        fillcolor="rgba(180, 180, 180, 0.35)",
        opacity=0.35,
        layer="below",
        line_width=0,
        annotation_text="Selected realized vol window",
        annotation_position="top left",
    )

    price_fig.update_layout(
        title=dict(
            text="Synthetic Index Price Path",
            x=0.01,
            xanchor="left",
            font=dict(size=18, color="#f5f5f5"),
        ),
        template="plotly_dark",
        height=520,
        margin=dict(l=40, r=40, t=55, b=40),
        paper_bgcolor="#111111",
        plot_bgcolor="#111111",
        xaxis=dict(
            title="Date",
            gridcolor="rgba(180, 180, 180, 0.22)",
            zeroline=False,
        ),
        yaxis=dict(
            title="Index Level",
            gridcolor="rgba(180, 180, 180, 0.22)",
            zeroline=False,
        ),
        hovermode="x unified",
)

    st.plotly_chart(price_fig, use_container_width=True)

    st.caption(
        f"The selected {window}-day window produced a {selected_return:.2%} return "
        f"with an average daily return of {selected_average_daily_return:.2%}. "
        f"The realized volatility estimate annualizes the dispersion of daily returns "
        f"over that same window, resulting in {selected_realized_vol:.2%} realized volatility."
    )

    st.markdown("**Rolling Annualized Realized Volatility**")

    st.caption(
        "Realized volatility is shown as an annualized percentage. "
        "Institutionally, this would often be compared against implied volatility "
        "to evaluate whether options are pricing rich or cheap versus recent movement."
    )

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