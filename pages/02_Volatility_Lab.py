
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st

from src.volatility import calculate_realized_volatility
from src.data import load_spx_vix_vvix_data

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
    st.subheader("Build Status")

    st.success("Module shell created")
    st.success("Realized volatility function implemented")
    st.success("Real SPX / VIX / VVIX data connected")
    st.info("Implied-vs-realized analytics in progress")
    st.info("Desk interpretation layer in progress")
    st.warning("Volatility surface analytics live in SPX Options Lab")

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

st.subheader("SPX / VIX / VVIX Market Snapshot")

st.markdown(
    """
    This section displays the latest available SPX, VIX, and VVIX market snapshot from the real-data feed.
    
    **SPX** represents the underlying index movement, **VIX** represents the
    market's implied-volatility benchmark for SPX, and **VVIX** represents
    volatility-of-volatility context.
    """
)

try:
    market_data = load_spx_vix_vvix_data(period="1y")

    latest_row = market_data.iloc[-1]
    previous_row = market_data.iloc[-2]

    latest_date = market_data.index[-1]
    start_date = market_data.index[0]

    spx_latest_return = (
        latest_row["spx_close"] / previous_row["spx_close"] - 1
    )
    vix_latest_change = latest_row["vix_close"] - previous_row["vix_close"]
    vvix_latest_change = latest_row["vvix_close"] - previous_row["vvix_close"]

    spx_prices = market_data["spx_close"]

    with st.expander("How to read the SPX / VIX / VVIX snapshot"):
        st.markdown(
            """
            **SPX Close** is the latest available closing level of the S&P 500 index.
            The daily change shown underneath is the latest close-to-close SPX return.

            **VIX Close** is the market's implied-volatility benchmark for SPX.
            A VIX level of 16 means the market is pricing roughly **16% annualized
            implied volatility** for forward SPX movement.

            **VVIX Close** measures implied volatility on VIX options. In simple terms,
            it is a market gauge of **volatility-of-volatility**. A rising VVIX can
            suggest that the market is becoming more uncertain about volatility itself,
            not just about the level of SPX.

            Desk framing:

            - **SPX** tells us what the index is doing.
            - **VIX** tells us what the options market is implying about future SPX volatility.
            - **VVIX** gives context on whether the volatility market itself is becoming more unstable.
            """
        )

    realized_vol_windows = {
        "5d": 5,
        "10d": 10,
        "20d": 20,
        "60d": 60,
    }

    latest_realized_vols = {}

    for label, window_size in realized_vol_windows.items():
        realized_vol_series = calculate_realized_volatility(
            prices=spx_prices,
            window=window_size,
            annualization_factor=252,
        )

        latest_realized_vols[label] = realized_vol_series.dropna().iloc[-1]

    vix_implied_vol = latest_row["vix_close"] / 100

    vix_realized_comparisons = {}

    for label, realized_vol_value in latest_realized_vols.items():
        spread = vix_implied_vol - realized_vol_value
        ratio = vix_implied_vol / realized_vol_value

        vix_realized_comparisons[label] = {
            "realized_vol": realized_vol_value,
            "spread": spread,
            "ratio": ratio,
        }
    
    short_realized_vol = latest_realized_vols["5d"]
    medium_realized_vol = latest_realized_vols["20d"]
    longer_realized_vol = latest_realized_vols["60d"]

    if short_realized_vol > medium_realized_vol and medium_realized_vol > longer_realized_vol:
        realized_vol_read = (
            "SPX realized volatility is accelerating across the curve, with short-term "
            "realized volatility above both the 20-day and 60-day baselines."
        )
        realized_vol_regime = "Accelerating realized volatility"

    elif short_realized_vol < medium_realized_vol and medium_realized_vol < longer_realized_vol:
        realized_vol_read = (
            "SPX realized volatility is calming, with short-term realized volatility "
            "below the 20-day and 60-day baselines."
        )
        realized_vol_regime = "Cooling realized volatility"

    elif short_realized_vol > medium_realized_vol:
        realized_vol_read = (
            "Short-term SPX realized volatility is running above the 20-day baseline, "
            "suggesting recent index movement has picked up."
        )
        realized_vol_regime = "Short-term realized vol pickup"

    else:
        realized_vol_read = (
            "Short-term SPX realized volatility is not materially above the 20-day "
            "baseline, suggesting recent index movement is relatively contained."
        )
        realized_vol_regime = "Contained short-term realized volatility"


    vix_20d_ratio = vix_realized_comparisons["20d"]["ratio"]
    vix_20d_spread = vix_realized_comparisons["20d"]["spread"]

    if vix_20d_ratio >= 1.50:
        implied_vol_read = (
            "VIX is trading at an elevated premium to SPX 20-day realized volatility. "
            "The market is pricing meaningfully more forward volatility than SPX has "
            "recently delivered."
        )
        implied_vol_regime = "Elevated implied-vol premium"

    elif vix_20d_ratio >= 1.15:
        implied_vol_read = (
            "VIX is trading at a moderate premium to SPX 20-day realized volatility. "
            "This suggests the market is pricing some forward uncertainty, protection "
            "demand, or volatility risk premium."
        )
        implied_vol_regime = "Moderate implied-vol premium"

    elif vix_20d_ratio >= 0.95:
        implied_vol_read = (
            "VIX is trading close to SPX 20-day realized volatility. Implied volatility "
            "is broadly in line with the recent realized movement baseline."
        )
        implied_vol_regime = "Implied near realized"

    else:
        implied_vol_read = (
            "VIX is trading below SPX 20-day realized volatility. Recent SPX movement "
            "has been running ahead of what the implied-volatility benchmark is pricing."
        )
        implied_vol_regime = "Realized vol above implied"


    vvix_level = latest_row["vvix_close"]

    if vvix_level >= 120:
        vvix_read = (
            "VVIX is elevated, suggesting the volatility market itself is pricing "
            "higher uncertainty around volatility outcomes."
        )
        vvix_regime = "Elevated vol-of-vol"

    elif vvix_level >= 95:
        vvix_read = (
            "VVIX is moderately elevated, suggesting some demand for volatility convexity "
            "or uncertainty around the VIX path."
        )
        vvix_regime = "Moderate vol-of-vol"

    else:
        vvix_read = (
            "VVIX is relatively contained, suggesting volatility-of-volatility is not "
            "showing acute stress."
        )
        vvix_regime = "Contained vol-of-vol"
        def classify_implied_vs_realized(spread: float, ratio: float) -> tuple[str, str]:
            """Classify VIX richness/cheapness versus realized volatility."""

            if ratio >= 1.50:
                return "Elevated Premium", "rgba(140, 70, 20, 0.45)"

            if ratio >= 1.15:
                return "Moderate Premium", "rgba(120, 110, 35, 0.38)"

            if ratio >= 0.95:
                return "Near Realized", "rgba(80, 80, 80, 0.42)"

            return "Realized > Implied", "rgba(120, 35, 35, 0.45)"

    realized_vol_chart_data = pd.DataFrame(
        {
            "SPX": market_data["spx_close"],
            "VIX Implied Vol": market_data["vix_close"] / 100,
            "SPX 5d Realized Vol": calculate_realized_volatility(
                prices=spx_prices,
                window=5,
                annualization_factor=252,
            ),
            "SPX 10d Realized Vol": calculate_realized_volatility(
                prices=spx_prices,
                window=10,
                annualization_factor=252,
            ),
            "SPX 20d Realized Vol": calculate_realized_volatility(
                prices=spx_prices,
                window=20,
                annualization_factor=252,
            ),
            "SPX 60d Realized Vol": calculate_realized_volatility(
                prices=spx_prices,
                window=60,
                annualization_factor=252,
            ),
        }
    ).dropna()

    metric_cols = st.columns(3)

    with metric_cols[0]:
        st.metric(
            "SPX Close",
            f"{latest_row['spx_close']:,.2f}",
            f"{spx_latest_return:.2%}",
        )

    with metric_cols[1]:
        st.metric(
            "VIX Close",
            f"{latest_row['vix_close']:.2f}",
            f"{vix_latest_change:+.2f} pts",
        )

    with metric_cols[2]:
        st.metric(
            "VVIX Close",
            f"{latest_row['vvix_close']:.2f}",
            f"{vvix_latest_change:+.2f} pts",
        )

    st.markdown("#### SPX Realized Volatility")

    realized_vol_cols = st.columns(4)

    with realized_vol_cols[0]:
        st.metric("5d Realized Vol", f"{latest_realized_vols['5d']:.2%}")

    with realized_vol_cols[1]:
        st.metric("10d Realized Vol", f"{latest_realized_vols['10d']:.2%}")

    with realized_vol_cols[2]:
        st.metric("20d Realized Vol", f"{latest_realized_vols['20d']:.2%}")

    with realized_vol_cols[3]:
        st.metric("60d Realized Vol", f"{latest_realized_vols['60d']:.2%}")

    with st.expander("How to read SPX realized volatility"):
        st.markdown(
            """
            **Realized volatility** measures how much SPX actually moved over a
            historical window. The values shown here are annualized.

            The windows give different views of the market:

            - **5d realized vol**: very recent realized movement.
            - **10d realized vol**: short-term movement.
            - **20d realized vol**: roughly one trading month.
            - **60d realized vol**: medium-term realized-volatility regime.

            Desk framing:

            If 5d and 10d realized volatility are above 20d and 60d realized
            volatility, SPX realized volatility may be **accelerating**.

            If 5d and 10d realized volatility are below 20d and 60d realized
            volatility, SPX realized volatility may be **calming down**.

            This matters because option P&L depends not only on where implied
            volatility is priced, but also on how much the underlying actually moves.
            """
        )

    st.markdown("#### Implied vs Realized Volatility")

    #st.metric("VIX Implied Vol", f"{vix_implied_vol:.2%}")

    comparison_cols = st.columns(4)

    for column, label in zip(
        comparison_cols,
        ["5d", "10d", "20d", "60d"],
    ):
        comparison = vix_realized_comparisons[label]
        regime_label, background_color = classify_implied_vs_realized(
            spread=comparison["spread"],
            ratio=comparison["ratio"],
        )

        with column:
            st.markdown(
                f"""
                <div style="
                    background: {background_color};
                    border: 1px solid rgba(220, 220, 220, 0.18);
                    border-radius: 10px;
                    padding: 0.85rem;
                    min-height: 150px;
                ">
                    <div style="font-size: 0.85rem; color: #cfcfcf;">
                        VIX vs SPX {label} Realized
                    </div>
                    <div style="font-size: 1.45rem; font-weight: 700; margin-top: 0.25rem;">
                        {comparison["spread"]:.2%}
                    </div>
                    <div style="font-size: 0.85rem; color: #d8d8d8; margin-top: 0.25rem;">
                        Ratio: {comparison["ratio"]:.2f}x
                    </div>
                    <div style="font-size: 0.80rem; color: #f0f0f0; margin-top: 0.60rem;">
                        {regime_label}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
    
    with st.expander("How to read VIX vs SPX realized volatility"):
        st.markdown(
                """
                This section compares **VIX implied volatility** against SPX realized
                volatility across several lookback windows.

                **VIX - SPX Realized Vol** measures the spread between implied volatility
                and realized volatility.

                Example:

                If VIX is 16% and SPX 20d realized volatility is 11%, then:

                ```text
                VIX - SPX 20d realized = +5%
                VIX / SPX 20d realized = 1.45x
                ```

                That means the options market is pricing more forward volatility than
                SPX has recently delivered.

                Desk framing:

                - **VIX above realized vol** may suggest volatility risk premium,
                protection demand, event risk, or uncertainty.
                - **VIX near realized vol** suggests implied volatility is close to the
                recent movement baseline.
                - **VIX below realized vol** suggests SPX has recently moved more than
                the implied-volatility benchmark is pricing.

                The comparison across windows matters:

                - Rich versus **5d/10d** but not **60d** can mean recent realized movement
                is calm, but the broader vol regime still carries uncertainty.
                - Rich versus **all windows** can suggest the market is pricing protection
                or event risk beyond what SPX has recently delivered.
                - Cheap versus **short windows** can suggest realized movement is outrunning
                implied volatility.
                """
            )
    st.markdown("#### SPX / VIX Desk Read")

    st.markdown(
        f"""
        <div style="
            background: rgba(35, 35, 35, 0.72);
            border: 1px solid rgba(220, 220, 220, 0.18);
            border-radius: 12px;
            padding: 1rem 1.1rem;
            margin-top: 0.5rem;
            margin-bottom: 0.75rem;
        ">
            <div style="font-size: 0.90rem; color: #cfcfcf; margin-bottom: 0.35rem;">
                Current Regime Summary
            </div>
            <div style="font-size: 1.05rem; font-weight: 700; margin-bottom: 0.70rem;">
                {realized_vol_regime} | {implied_vol_regime} | {vvix_regime}
            </div>
            <div style="font-size: 0.92rem; line-height: 1.55; color: #eeeeee;">
                <strong>Realized vol read:</strong> {realized_vol_read}<br><br>
                <strong>Implied vol read:</strong> {implied_vol_read}<br><br>
                <strong>VVIX read:</strong> {vvix_read}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.expander("Desk so what"):
        st.markdown(
            f"""
            This read connects SPX realized volatility, VIX implied volatility, and
            VVIX volatility-of-volatility into one desk-style interpretation.

            **Current setup:**

            - SPX 5d realized vol: **{latest_realized_vols["5d"]:.2%}**
            - SPX 20d realized vol: **{latest_realized_vols["20d"]:.2%}**
            - SPX 60d realized vol: **{latest_realized_vols["60d"]:.2%}**
            - VIX implied vol: **{vix_implied_vol:.2%}**
            - VIX minus SPX 20d realized: **{vix_20d_spread:.2%}**
            - VIX / SPX 20d realized: **{vix_20d_ratio:.2f}x**
            - VVIX level: **{vvix_level:.2f}**

            For an SPX/VIX/index-options flow desk, the key question is whether
            realized SPX movement is strong enough to justify the implied-volatility
            premium, and whether VVIX is signaling instability in the volatility
            market itself.

            If implied volatility remains above realized volatility while SPX movement
            stays contained, short-vol carry may look attractive but remains exposed
            to event risk and volatility spikes. If realized volatility accelerates
            and VVIX rises, the desk may focus more on convexity demand, hedging
            pressure, and risk to short-gamma or short-vol positions.
            """
        )
    
    st.markdown("#### SPX / VIX Volatility Regimes")

    vol_regime_fig = make_subplots(
        rows=2,
        cols=2,
        shared_xaxes=True,
        vertical_spacing=0.12,
        horizontal_spacing=0.08,
        specs=[
            [{"secondary_y": True}, {"secondary_y": True}],
            [{"secondary_y": True}, {"secondary_y": True}],
        ],
        subplot_titles=[
            "VIX vs SPX 5d Realized Vol",
            "VIX vs SPX 10d Realized Vol",
            "VIX vs SPX 20d Realized Vol",
            "VIX vs SPX 60d Realized Vol",
        ],
    )

    chart_windows = [
        ("5d", "SPX 5d Realized Vol", 1, 1),
        ("10d", "SPX 10d Realized Vol", 1, 2),
        ("20d", "SPX 20d Realized Vol", 2, 1),
        ("60d", "SPX 60d Realized Vol", 2, 2),
    ]

    for label, realized_column, row, col in chart_windows:
        vol_regime_fig.add_trace(
            go.Scatter(
                x=realized_vol_chart_data.index,
                y=realized_vol_chart_data["VIX Implied Vol"],
                mode="lines",
                name="VIX Implied Vol",
                legendgroup="VIX",
                showlegend=(label == "5d"),
                line=dict(color="#f5b041", width=2.2),
                hovertemplate="Date: %{x}<br>VIX Implied Vol: %{y:.2%}<extra></extra>",
            ),
            row=row,
            col=col,
            secondary_y=False,
        )

        vol_regime_fig.add_trace(
            go.Scatter(
                x=realized_vol_chart_data.index,
                y=realized_vol_chart_data[realized_column],
                mode="lines",
                name=realized_column,
                legendgroup=realized_column,
                showlegend=True,
                line=dict(color="#5dade2", width=1.9),
                hovertemplate=(
                    f"Date: %{{x}}<br>{realized_column}: %{{y:.2%}}<extra></extra>"
                ),
            ),
            row=row,
            col=col,
            secondary_y=False,
        )

        vol_regime_fig.add_trace(
            go.Scatter(
                x=realized_vol_chart_data.index,
                y=realized_vol_chart_data["SPX"],
                mode="lines",
                name="SPX Index Level",
                legendgroup="SPX",
                showlegend=(label == "5d"),
                yaxis="y2",
                line=dict(color="rgba(220, 220, 220, 0.22)", width=1.1),
                hovertemplate="Date: %{x}<br>SPX: %{y:,.2f}<extra></extra>",
            ),
            row=row,
            col=col,
            secondary_y=True,
        )

    vol_regime_fig.update_layout(
        title=dict(
            text="VIX Implied Vol, SPX Realized Volatility Windows, and SPX Index Level",
            x=0.01,
            xanchor="left",
            font=dict(size=18, color="#f5f5f5"),
        ),
        template="plotly_dark",
        height=600,
        margin=dict(l=40, r=50, t=75, b=40),
        paper_bgcolor="#111111",
        plot_bgcolor="#111111",
        showlegend=False,
        hovermode="x unified",
    )

    for row in [1, 2]:
        for col in [1, 2]:
            vol_regime_fig.update_xaxes(
                gridcolor="rgba(180, 180, 180, 0.18)",
                zeroline=False,
                row=row,
                col=col,
            )

            vol_regime_fig.update_yaxes(
                title_text=None,
                tickformat=".0%",
                gridcolor="rgba(180, 180, 180, 0.18)",
                zeroline=False,
                row=row,
                col=col,
                secondary_y=False,
            )

            vol_regime_fig.update_yaxes(
                title_text=None,
                showgrid=False,
                zeroline=False,
                color="rgba(220, 220, 220, 0.45)",
                row=row,
                col=col,
                secondary_y=True,
            )

    st.plotly_chart(vol_regime_fig, use_container_width=True)

    with st.expander("Desk so what: SPX / VIX volatility regime chart pack"):
        st.markdown(
            f"""
            This chart pack compares **VIX implied volatility** against multiple
            SPX realized-volatility windows, while keeping the SPX index level in
            the background for price-path context.

            Each panel asks a slightly different desk question:

            - **VIX vs 5d realized vol:** Is implied volatility high or low versus
            the very recent SPX movement?
            - **VIX vs 10d realized vol:** Is implied volatility high or low versus
            short-term realized movement?
            - **VIX vs 20d realized vol:** Is implied volatility high or low versus
            the standard one-month realized-volatility baseline?
            - **VIX vs 60d realized vol:** Is implied volatility high or low versus
            the broader realized-volatility regime?

            **Current read:**

            - VIX implied vol: **{vix_implied_vol:.2%}**
            - SPX 5d realized vol: **{latest_realized_vols["5d"]:.2%}**
            - SPX 10d realized vol: **{latest_realized_vols["10d"]:.2%}**
            - SPX 20d realized vol: **{latest_realized_vols["20d"]:.2%}**
            - SPX 60d realized vol: **{latest_realized_vols["60d"]:.2%}**

            **Desk interpretation:**

            A desk is not just asking whether VIX is above or below one realized-vol
            number. It is asking **which realized-volatility baseline VIX is rich or
            cheap against**.

            If VIX is above the 5d and 10d realized-volatility windows, but closer to
            the 20d or 60d windows, recent SPX movement may have calmed even though
            the market is still carrying broader volatility premium.

            If VIX is above all four realized-volatility windows, the market may be
            pricing protection demand, event risk, or volatility risk premium beyond
            what SPX has recently delivered.

            If short-window realized volatility is above VIX, recent SPX movement is
            outrunning the implied-volatility benchmark. That can matter for desks
            exposed to short gamma, short volatility, or hedging flows that become
            more sensitive when realized movement picks up.

            The faint SPX line helps connect volatility behavior to the underlying
            index path. Sharp drawdowns, reversals, or unstable rallies can explain
            why VIX and short-window realized volatility move differently.
            """
        )    
    st.caption(
        """
        **How to read Implied vs Realized**

        This row compares what SPX has recently **realized** against what the
        volatility market is **implying** through VIX. Is the options market 
        pricing more movement than SPX has actually been realizing?

        - **VIX - SPX 20d Realized** measures the spread between implied volatility
        and recent realized volatility.
        - **VIX / SPX 20d Realized** shows how large implied volatility is relative
        to the recent realized-volatility baseline.

        A positive implied-vs-realized spread means VIX is pricing more forward
        volatility than SPX has recently delivered. This may reflect volatility risk
        premium, protection demand, event risk, or uncertainty around future index
        movement.
        """
    )

    st.markdown("#### VVIX / Vol-of-Vol Stress")

    vvix_series = market_data["vvix_close"].dropna()

    vvix_current = vvix_series.iloc[-1]
    vvix_percentile = (vvix_series <= vvix_current).mean()

    vvix_20d_average = vvix_series.rolling(window=20).mean().iloc[-1]
    vvix_60d_average = vvix_series.rolling(window=60).mean().iloc[-1]

    vvix_5d_change = vvix_current - vvix_series.iloc[-6]
    vvix_20d_change = vvix_current - vvix_series.iloc[-21]

    vix_current = latest_row["vix_close"]
    vix_percentile = (market_data["vix_close"].dropna() <= vix_current).mean()

    if vvix_percentile >= 0.80:
        vvix_regime_label = "Elevated vol-of-vol"
        vvix_regime_color = "rgba(120, 35, 35, 0.45)"
        vvix_regime_read = (
            "VVIX is high versus its recent history, suggesting the market is pricing "
            "greater uncertainty around volatility outcomes."
        )

    elif vvix_percentile >= 0.60:
        vvix_regime_label = "Firm vol-of-vol"
        vvix_regime_color = "rgba(140, 90, 25, 0.42)"
        vvix_regime_read = (
            "VVIX is moderately firm versus its recent history, suggesting some demand "
            "for volatility convexity or uncertainty around the VIX path."
        )

    else:
        vvix_regime_label = "Contained vol-of-vol"
        vvix_regime_color = "rgba(45, 90, 65, 0.42)"
        vvix_regime_read = (
            "VVIX is contained versus its recent history, suggesting volatility-of-volatility "
            "is not showing acute stress."
        )


    if vix_percentile >= 0.70 and vvix_percentile >= 0.70:
        vix_vvix_read = (
            "Both VIX and VVIX are elevated versus recent history. This points to a more "
            "stressed volatility environment where the market is pricing higher SPX volatility "
            "and greater uncertainty around volatility itself."
        )

    elif vix_percentile >= 0.70 and vvix_percentile < 0.70:
        vix_vvix_read = (
            "VIX is elevated, but VVIX is not equally stressed. The market may be pricing "
            "higher SPX volatility without a major increase in vol-of-vol stress."
        )

    elif vix_percentile < 0.70 and vvix_percentile >= 0.70:
        vix_vvix_read = (
            "VVIX is elevated while VIX is less stressed. This may suggest demand for convexity "
            "or uncertainty around future volatility outcomes even if spot VIX is not extreme."
        )

    else:
        vix_vvix_read = (
            "Both VIX and VVIX are relatively contained versus recent history. The volatility "
            "market does not appear to be pricing acute index-volatility stress or vol-of-vol stress."
        )

    vvix_chart_data = pd.DataFrame(
        {
            "VVIX": market_data["vvix_close"],
            "SPX": market_data["spx_close"],
        }
    ).dropna()

    vvix_fig = go.Figure()

    vvix_fig.add_trace(
        go.Scatter(
            x=vvix_chart_data.index,
            y=vvix_chart_data["VVIX"],
            mode="lines",
            name="VVIX",
            line=dict(color="#af7ac5", width=2.3),
            hovertemplate="Date: %{x}<br>VVIX: %{y:.2f}<extra></extra>",
        )
    )

    vvix_fig.add_trace(
        go.Scatter(
            x=vvix_chart_data.index,
            y=vvix_chart_data["SPX"],
            mode="lines",
            name="SPX Index Level",
            yaxis="y2",
            line=dict(color="rgba(220, 220, 220, 0.16)", width=1.0),
            hovertemplate="Date: %{x}<br>SPX: %{y:,.2f}<extra></extra>",
        )
    )

    vvix_fig.update_layout(
        title=dict(
            text="VVIX Vol-of-Vol Stress with SPX Context",
            x=0.01,
            xanchor="left",
            font=dict(size=18, color="#f5f5f5"),
        ),
        template="plotly_dark",
        height=360,
        margin=dict(l=40, r=55, t=55, b=40),
        paper_bgcolor="#111111",
        plot_bgcolor="#111111",
        xaxis=dict(
            title="Date",
            gridcolor="rgba(180, 180, 180, 0.18)",
            zeroline=False,
        ),
        yaxis=dict(
            title="VVIX Level",
            gridcolor="rgba(180, 180, 180, 0.18)",
            zeroline=False,
        ),
        yaxis2=dict(
            title="SPX",
            overlaying="y",
            side="right",
            showgrid=False,
            zeroline=False,
            color="rgba(220, 220, 220, 0.45)",
        ),
        hovermode="x unified",
        showlegend=False,
    )

    st.plotly_chart(vvix_fig, use_container_width=True)

    vvix_cols = st.columns(4)

    with vvix_cols[0]:
        st.metric("Current VVIX", f"{vvix_current:.2f}")

    with vvix_cols[1]:
        st.metric(
            "VVIX Percentile",
            f"{vvix_percentile:.0%}",
            help="Percentile rank of the latest VVIX level versus the loaded history.",
        )

    with vvix_cols[2]:
        st.metric(
            "VVIX 5d Change",
            f"{vvix_5d_change:+.2f} pts",
        )

    with vvix_cols[3]:
        st.metric(
            "VVIX 20d Change",
            f"{vvix_20d_change:+.2f} pts",
        )

    st.markdown(
        f"""
        <div style="
            background: {vvix_regime_color};
            border: 1px solid rgba(220, 220, 220, 0.18);
            border-radius: 12px;
            padding: 1rem 1.1rem;
            margin-top: 0.5rem;
            margin-bottom: 0.75rem;
        ">
            <div style="font-size: 0.90rem; color: #cfcfcf; margin-bottom: 0.35rem;">
                VVIX Regime
            </div>
            <div style="font-size: 1.05rem; font-weight: 700; margin-bottom: 0.60rem;">
                {vvix_regime_label}
            </div>
            <div style="font-size: 0.92rem; line-height: 1.55; color: #eeeeee;">
                {vvix_regime_read}<br><br>
                <strong>VIX / VVIX read:</strong> {vix_vvix_read}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.expander("Desk so what: VVIX / vol-of-vol stress"):
        st.markdown(
            f"""
            **VVIX** measures implied volatility on VIX options. It is often described
            as volatility-of-volatility.

            In desk terms, VIX gives a read on the market price of forward SPX
            volatility. VVIX gives a read on how uncertain the market is about the
            volatility path itself.

            **Current read:**

            - Current VVIX: **{vvix_current:.2f}**
            - VVIX percentile versus loaded history: **{vvix_percentile:.0%}**
            - VVIX 20d average: **{vvix_20d_average:.2f}**
            - VVIX 60d average: **{vvix_60d_average:.2f}**
            - VVIX 5d change: **{vvix_5d_change:+.2f} pts**
            - VVIX 20d change: **{vvix_20d_change:+.2f} pts**

            **Why this matters to a VIX/options flow desk:**

            A VIX options trader is not only watching the level of VIX. They also care
            about the market's demand for optionality on volatility itself.

            Elevated or rising VVIX can suggest stronger demand for convexity, greater
            uncertainty around the VIX path, or more stress in volatility products.
            That can matter for pricing, risk limits, hedging, and how a desk thinks
            about flow in VIX options.

            **Possible reads:**

            - **VIX up, VVIX up:** market is pricing higher SPX volatility and more
            uncertainty around volatility outcomes.
            - **VIX up, VVIX contained:** implied SPX volatility is higher, but vol-of-vol
            stress may be more controlled.
            - **VIX contained, VVIX up:** spot VIX is not extreme, but the options market
            may be paying for convexity or future volatility uncertainty.
            - **VIX contained, VVIX contained:** volatility markets look calmer from both
            the SPX implied-vol and vol-of-vol perspective.
            """
        )

    subtle_divider()

    st.caption(
        f"Latest available market data as of {latest_date.date()} "
        f"| 1-year history loaded for volatility calculations "
        f"| Source: Yahoo Finance via yfinance"
    )

except Exception as error:
    st.error("Unable to load SPX / VIX / VVIX market data.")
    st.caption(f"Data error: {error}")

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