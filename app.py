import streamlit as st
st.title("SMART EXPENSE TRACKER")
st.write("Track your Expense")
category=st.selectbox("Category",["food","Shopping","Travel","loan","House rent","Vechicle","celebration"])
expense=st.number_input("Expense",min_value=0)
if st.button("Add Expense"):
     data = {category: expense}
     with open("EXPENSE_TRACKER.txt", "a") as a:
        a.write(str(data) + "\n")
        st.success("Saved Successfully!")
if st.button("Total Expense"):
    total=0
    try:
        with open("EXPENSE_TRACKER.txt", "r") as f:
            for line in f:
                 if line.strip() != "":
                    data = eval(line.strip()) 
                    for value in data.values():
                        total += value
        st.write("Total Expense =", total)
    except FileNotFoundError:
        st.warning("No expense addes yet")

    
