## IMPORT LIBRARIES
import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config("[Feature Testing Environment]")
st.title("Sandbox")

# --- IMPORT EXPENSES

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

expense_costs['Credit'] = expense_costs['Credit'].astype(float)
expense_costs['Debit'] = expense_costs['Debit'].astype(float)
expense_costs['Discover'] = expense_costs['Discover'].astype(float)


# --- MONTHLY EXPESE CALCULATIONS

monthly_costs = expense_costs

weekly = monthly_costs['Due'].astype('string').str.len().eq(3).fillna(False)
monthly_costs.loc[weekly, 'Debit'] = monthly_costs.loc[weekly, 'Debit'] * 4

salary = monthly_costs['Due'].astype('string').str.len().eq(3).fillna(False)
monthly_costs.loc[salary, 'Credit'] = monthly_costs.loc[salary, 'Credit'] * 2

monthly_costs = monthly_costs.dropna(subset = ['Due'])

st.dataframe(monthly_costs)


monthly_costs['budget'] = monthly_costs['Credit'] - monthly_costs['Debit']

st.write("Monthly budget")
st.write("")


budget = monthly_costs[['Person', 'budget']].dropna()
budget = budget.groupby('Person')['budget'].sum()

st.dataframe(budget)



# --- ANNUALIZE SALARY

monthly_costs_ann = monthly_costs
monthly_costs_ann['budget'] = monthly_costs_ann['Credit'].div(24).mul(26)

st.write("Annualized budget")
st.write("")

budget_ann = monthly_costs_ann[['Person', 'budget']].dropna()
budget_ann = budget_ann.groupby('Person')['budget'].sum()

st.dataframe(budget_ann)

st.dataframe(monthly_costs_ann)












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
