## IMPORT LIBRARIES
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Here's a breakdown of your incomes and expenses.")
st.title("")


##
## IMPORT ANALYSIS DATA
##
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

##
## DATA VISUALIZATION
##

# LABEL COLUMNS
label_cols = st.columns(3,
                        width = 'stretch')

label_col1 = label_cols[0]
label_col2 = label_cols[1]
label_col3 = label_cols[2]

with label_col1:
    st.write("Income by Account")
with label_col2:
    st.write("Expenses by Account")
with label_col3:
    st.write("Expenses by Category")

# PIE CHART COLUMNS
pie_cols = st.columns(3,
                      width = 'stretch')

pie_col1 = pie_cols[0]
pie_col2 = pie_cols[1]
pie_col3 = pie_cols[2]

income_account = px.pie(expense_costs,
                   values = 'Credit',
                   names = 'Description',
                   width = 200)

expense_account = px.pie(expense_costs,
                   values = 'Debit',
                   names = 'Person',
                   width = 200)

expense_type = px.pie(expense_costs,
                      values = 'Debit',
                      names = 'Type',
                      width = 200)


with pie_col1:
    st.plotly_chart(income_account)

with pie_col2:
    st.plotly_chart(expense_account)

with pie_col3:
    st.plotly_chart(expense_type)


##
## DATA DESCRIPTIONS 
##
# data_col1, data_col2, data_col3 = st.columns(3)

income_account_desc = expense_costs[expense_costs['Credit'] > 0.01]
income_account_desc = income_account_desc.groupby('Description')['Credit'].sum().dropna().sort_values(ascending = False)

expense_account_desc = expense_costs[expense_costs['Debit'] != 0]
expense_account_desc = expense_account_desc.groupby('Person')['Debit'].sum().dropna().sort_values(ascending = False)

expense_type_desc = expense_costs[expense_costs['Debit'] != 0]
expense_type_desc = expense_type_desc.groupby('Type')['Debit'].sum().dropna().sort_values(ascending = False)


##
## DETAILED ANALYSIS
##

detail_tab1, detail_tab2 = st.tabs(['Breakdown', 'Details'])

with detail_tab1:
    data_col1, data_col2, data_col3 = st.columns(3)

    with data_col1:
        st.dataframe(income_account_desc)
    with data_col2:
        st.dataframe(expense_account_desc)
    with data_col3:
        st.dataframe(expense_type_desc)
with detail_tab2:
    detail = st.selectbox("Detail",
                 expense_costs['Type'].drop_duplicates().dropna().sort_values())
    st.dataframe(expense_costs[expense_costs['Type'] == detail].reset_index(drop = True))
