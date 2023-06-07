import streamlit as st
import retirement as rt

st.title('Retirement Readiness')

rt.current_age = st.number_input("Input Current Age", value=40, min_value=0, max_value=100)
rt.retirement_age = st.number_input("Input Retirement Age", value=50, min_value=0, max_value=100)
rt.current_annual_income = st.number_input("Input Current Annual Income", value=2000000)
rt.savings_per_month = st.number_input("How much you can save per Month", value=10000)
rt.current_savings_bal = st.number_input("How much you have saved so far", value=1000000)
rt.monthly_pension = st.number_input("Monthly Income through pension post Retirement", value=0)
rt.other_income_post_ret = st.number_input("Other Monthly income (like rentals)", value=45000)
rt.corpus_from_wealth_dilution = st.number_input("Value of any asset that you can convert to cash for retirement", value=8000000)
rt.retire_income_per_month = st.number_input("Expected Retirement income per Month", value=(rt.current_annual_income/12)*0.7)

if st.button('Calculate Retriment Readiness'):
    st.write('hello there')
    rt.certainity = rt.simulate_income_post_ret(100)
    st.write('As per above plan there is {} chance of meeting your monthly retirement income goal of {}%'\
             .format(rt.certainity*100, rt.retire_income_per_month))

