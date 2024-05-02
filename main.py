import streamlit as st


# def formula(p, d, o, c, m, t):
#     total = (p * m) + (round(d / t[0], 2)) + (round(o / t[1], 2)) + (round(c / t[2], 2))
#     total = total / 12
#     return total

def formula(p,d,o,c,m,t):
    total = (p*m) + (d/t[0]) + (o/t[1]) + (c/t[2])
    return total

st.header("Health Insurance calculator")

st.write("Premium")
premium = st.number_input(label="The Ammount You Pay Per Month")

st.write("Deductables")
deduct = st.number_input(label="The Ammount You Pay For Your Insurance To 'Kick In ")
d_time = st.number_input(label="times you pay per month")

st.write("Out of pockets")
oop = st.number_input("Expensenses not covered by insurance ")
o_time = st.number_input(label="times you pay per month ")

st.write("CoPayments")
copay = st.number_input("Payments For Things Like Meds and ER Visits")
c_time = st.number_input(" times you pay per month")

st.write("Months")
months = st.number_input("NOTE payments are assumed to be payed monthly frequensy boxes coming soon")
go = st.button("Calculate")
times = (d_time, o_time, c_time)
if go:
    st.write(str(formula(premium, deduct, oop, copay, months, times)) + " Per Year (Aprox)")
    st.write(str(formula(premium, deduct, oop, copay, months, times)/12) + " Per month (Aprox)")
