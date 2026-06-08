## IMPORT LIBRARIES
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title = "Expense Costs",
    layout = "wide"
    )

st.title("Here are your expense costs.")
st.title("")


expense_costs = pd.read_csv("assets\ExpenseCosts.csv")

print(expense_costs)

dynamic_table = st.data_editor(
    expense_costs, 
    width="content", 
    height="auto", 
    use_container_width=None, 
    hide_index=None, 
    column_order=None, 
    column_config=None, 
    num_rows="dynamic", 
    disabled=False, 
    key=None, 
    on_change=None, 
    args=None, 
    kwargs=None, 
    row_height=None, 
    placeholder=None
    )

if st.button("Save changes"):
    dynamic_table.to_csv(r"C:\Users\pc\Documents\GitHub\Luke's Financial Tool\assets\ExpenseCosts.csv", index = False)
    st.success("Changes saved!")