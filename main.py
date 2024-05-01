import streamlit as st


def formula(p, d, o, c, m):
    total = (p * m) + (d) + (o / m) + (c/m)
    total = total / 12
    return total


st.header("Health Insurance calculator")

st.write("Premium")
premium = st.number_input(label="The Ammount You Pay Per Month")

st.write("Deductables")
deduct = st.number_input(label="The Ammount You Pay For Your Insurance To 'Kick In ")

st.write("Out of pockets")
oop = st.number_input("Expensenses not covered by insurance ")

st.write("CoPayments")
copay = st.number_input("Payments For Things Like Meds and ER Visits")

st.write("Months")
months = st.number_input("NOTE payments are assumed to be payed monthly frequensy boxes coming soon")

go = st.button("Calculate")
if go:
    st.write(str(formula(premium, deduct, oop, copay, months)) + " Per month")
