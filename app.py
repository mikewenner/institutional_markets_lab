import streamlit as st

st.set_page_config(
    page_title="Institutional Markets Lab",
    page_icon="📈",
    layout="wide",
)

st.title("Institutional Markets Lab")

st.markdown(
    """
    Institutional Markets Lab is a Streamlit-based analytics workstation for studying
    institutional market concepts across equity derivatives, index options, volatility,
    dealer positioning, financing, and market microstructure.

    This project is in early development. The initial focus is building a clean app
    foundation, then adding one module at a time.
    """
)

st.divider()

st.subheader("Current Build Status")

st.markdown(
    """
    - README created
    - Initial project structure created
    - Streamlit app shell in progress
    - Home Dashboard coming next
    - Volatility Lab will be the first major analytics module
    """
)

st.subheader("Core Modules")

st.markdown(
    """
    1. Home Dashboard  
    2. Volatility Lab  
    3. SPX Options Lab  
    4. Dealer Positioning Lab  
    5. Financing Lab  
    6. Market Microstructure Lab  
    7. Learning Journal  
    """
)