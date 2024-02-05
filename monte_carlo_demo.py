import streamlit as st
import numpy as np

# Streamlit UI
st.title('Monte Carlo Simulation Demo')

# User Inputs
initial_investment = st.number_input('Initial Investment', min_value=1000, value=10000)
annual_return = st.number_input('Expected Annual Return (%)', value=7.0)
volatility = st.number_input('Annual Volatility (%)', value=15.0)
years = st.number_input('Investment Period (Years)', min_value=1, value=10)
simulations = st.number_input('Number of Simulations', min_value=100, value=1000)

# Monte Carlo Simulation
@st.cache(suppress_st_warning=True)
def monte_carlo(initial_investment, annual_return, volatility, years, simulations):
    np.random.seed(42)  # For reproducible results
    final_values = []
    for _ in range(simulations):
        returns = np.random.normal(annual_return / 100, volatility / 100, years)
        value = initial_investment
        for r in returns:
            value += value * r
        final_values.append(value)
    return final_values

if st.button('Run Simulation'):
    results = monte_carlo(initial_investment, annual_return, volatility, years, simulations)
    st.write(f"Simulation Results: Mean = ${np.mean(results):,.2f}, Median = ${np.median(results):,.2f}")
    st.line_chart(results)

