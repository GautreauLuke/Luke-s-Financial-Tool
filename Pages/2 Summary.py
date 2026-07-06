## IMPORT LIBRARIES
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title = "Monthly Cost Summary",
    layout = "wide"
    )

st.title("Let's see your expense summary.")
st.title("")


expense_costs = pd.read_csv("assets\ExpenseCosts.csv")

## expense_costs['Debit'] = expense_costs['Debit'].str.replace(["$" , ","],"")      -- For some reason, broken. Individual replaces below work just fine.

expense_costs['Debit'] = expense_costs['Debit'].str.replace("," , "")
expense_costs['Debit'] = expense_costs['Debit'].str.replace("$" , "")
expense_costs['Debit'] = expense_costs['Debit'].fillna(0)
expense_costs['Credit'] = expense_costs['Credit'].str.replace("," , "")
expense_costs['Credit'] = expense_costs['Credit'].str.replace("$" , "")
expense_costs['Credit'] = expense_costs['Credit'].fillna(0)
expense_costs['Discover'] = expense_costs['Discover'].str.replace("," , "")
expense_costs['Discover'] = expense_costs['Discover'].str.replace("$" , "")
expense_costs['Discover'] = expense_costs['Discover'].fillna(0)

tabs,sunbs = st.columns(2)

# --- SUNBURST CHART
sunburst_expenses = px.sunburst(
    expense_costs,
    path=['Person','Type','Description'],
    values = 'Debit',
    color = 'Type'
)

sunburst_expenses.update_layout(height = 700)

#st.plotly_chart(sunburst_expenses, use_container_width=True)


# --- TABULAR BREAKDOWN
expense_costs['Debit'] = expense_costs['Debit'].astype(float)

expense_agg = expense_costs.groupby(['Person', 'Type'])['Debit'].sum()

#st.dataframe(data = expense_agg, height = "content")

with tabs:
    st.dataframe(data = expense_agg, height = "content")
with sunbs:
    st.plotly_chart(sunburst_expenses, use_container_width=True)