## IMPORT LIBRARIES
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config("[Feature testing]")
st.title("Sandbox environment")
st.title("")

expense_costs = pd.read_csv("assets\ExpenseCosts.csv")
expense_costs['Debit'] = expense_costs['Debit'].str.replace("," , "")
expense_costs['Debit'] = expense_costs['Debit'].str.replace("$" , "")
expense_costs['Debit'] = expense_costs['Debit'].fillna(0)
expense_costs['Credit'] = expense_costs['Credit'].str.replace("," , "")
expense_costs['Credit'] = expense_costs['Credit'].str.replace("$" , "")
expense_costs['Credit'] = expense_costs['Credit'].fillna(0)
expense_costs['Discover'] = expense_costs['Discover'].str.replace("," , "")
expense_costs['Discover'] = expense_costs['Discover'].str.replace("$" , "")
expense_costs['Discover'] = expense_costs['Discover'].fillna(0)


expense_costs['Debit'] = expense_costs['Debit'].astype(float)
expense_costs['Credit'] = expense_costs['Credit'].astype(float)


expense_costs['budget'] = expense_costs['Credit'] - expense_costs['Debit']

st.dataframe(expense_costs)

budget = expense_costs[['Person', 'budget']].dropna()
budget = budget.groupby('Person')['budget'].sum()

st.dataframe(budget)














st.title("")
st.title("")
st.title("")
st.title("")
st.title("")
st.title("Feature test archive")
st.title("")



label_cols = st.columns(3)

label_col1 = label_cols[0].container()
label_col2 = label_cols[1].container()
label_col3 = label_cols[2].container()

with label_col1:
    st.write("Income by Account")
with label_col2:
    st.write("Expenses by Account")
with label_col3:
    st.write("Expenses by Category")


# label_col1, label_col2, label_col3 = st.columns(3,
#                                                 width = 'stretch')
# with label_col1:
#     st.write("Income by Account")
# with label_col2:
#     st.write("Expenses by Account")
# with label_col3:
#     st.write("Expenses by Category")