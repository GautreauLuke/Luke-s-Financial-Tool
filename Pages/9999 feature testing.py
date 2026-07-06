## IMPORT LIBRARIES
import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime


st.set_page_config("[Feature Testing Environment]")
st.title("Sandbox")
st.write(datetime.now().strftime("%H:%M:%S"))

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


#######################################################################################################################################################################################
## --- DEV SPACE

analysis_container = st.container(border = True)

with analysis_container:
    p_cards, t_cards = st.columns(2, border = False)
    with p_cards:
        luke_card = st.container(border=True,vertical_alignment="center")
        with luke_card:
            st.subheader("Luke")
        caitlin_card = st.container(border=True,vertical_alignment="center")
        with caitlin_card:
            st.subheader("Caitlin")
    with t_cards:
        st.subheader("Totals")



sunburst_expenses = px.sunburst(
    expense_costs,
    path=['Person','Type','Description'],
    values = 'Debit'
)

sunburst_expenses.update_layout(height = 900)

st.plotly_chart(sunburst_expenses, use_container_width=True)


#######################################################################################################################################################################################

st.title("")
st.title("")
st.title("")
st.title("")
st.title("")
st.title("Feature test archive")
st.title("")




# --- MONTHLY EXPESE CALCULATIONS

monthly_costs = expense_costs.copy()

weekly = monthly_costs['Due'].astype('string').str.len().eq(3).fillna(False)
monthly_costs.loc[weekly, 'Debit'] = monthly_costs.loc[weekly, 'Debit'] * 4

salary = monthly_costs['Due'].astype('string').str.len().eq(3).fillna(False)
monthly_costs.loc[salary, 'Credit'] = monthly_costs.loc[salary, 'Credit'] * 2

monthly_costs = monthly_costs.dropna(subset = ['Due'])

st.dataframe(monthly_costs.set_index('Description'))


monthly_costs['budget'] = monthly_costs['Credit'] - monthly_costs['Debit']

    ### Add Combined person
#combined_budget = monthly_costs.groupby("Person", as_index = False)["budget"].sum()


st.write("Monthly Budget Remainders")
st.write("")



budget = monthly_costs[['Person', 'budget']].dropna()
budget = budget.groupby('Person', as_index=False)['budget'].sum()
budget.loc[len(budget)] = ["Luke + Caitlin", budget['budget'].sum()]

st.dataframe(budget.set_index('Person'))



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
