import streamlit as st
import numpy as np
import numpy_financial as npf

# Streamlit UI
st.title('Real Estate Investment Monte Carlo Simulation')

# User Inputs
initial_investment = st.number_input('Initial Investment', min_value=10000, value=100000)
monthly_payment = st.number_input('Monthly Payment', min_value=500, value=2000)
sale_price = st.number_input('Expected Sale Price at the End of the Period', min_value=10000, value=150000)
rate = st.number_input('Annual Discount Rate (%)', value=5.0)
periods = st.number_input('Investment Period (Months)', min_value=12, value=60)
simulations = st.number_input('Number of Simulations', min_value=100, value=1000)

# Monte Carlo Simulation for IRR
@st.cache(suppress_st_warning=True)
def monte_carlo_irr(initial_investment, monthly_payment, sale_price, rate, periods, simulations):
    np.random.seed(42)  # For reproducible results
    irr_values = []
    for _ in range(simulations):
        # Simulating monthly cash flow variations
        cash_flows = np.random.normal(-monthly_payment, monthly_payment * 0.1, periods)
        cash_flows[0] -= initial_investment  # Initial investment outflow
        cash_flows[-1] += sale_price  # Sale price inflow at the end of the period
        
        # Calculating IRR
        irr = npf.irr(cash_flows)
        irr_values.append(irr)
    return irr_values

if st.button('Run Simulation'):
    irr_results = monte_carlo_irr(initial_investment, monthly_payment, sale_price, rate, periods, simulations)
    irr_mean = np.mean(irr_results)
    st.write(f"Simulation Results: Mean IRR = {irr_mean*100:.2f}%")
    st.hist_chart(irr_results)

# Additional Dependencies
# Note: numpy_financial is used for financial calculations like IRR.
# You may need to install it using pip if it's not already installed:
# pip install numpy-financial
