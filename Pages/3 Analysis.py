## IMPORT LIBRARIES
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Here's a breakdown of your incomes and expenses.")
st.write("")

##
## IMPORT ANALYSIS DATA

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


# --- MONTHLY EXPESE CALCULATIONS

monthly_costs = expense_costs.copy()

weekly = monthly_costs['Due'].astype('string').str.len().eq(3).fillna(False)
monthly_costs.loc[weekly, 'Debit'] = monthly_costs.loc[weekly, 'Debit'] * 4

salary = monthly_costs['Due'].astype('string').str.len().eq(3).fillna(False)
monthly_costs.loc[salary, 'Credit'] = monthly_costs.loc[salary, 'Credit'] * 2

monthly_costs = monthly_costs.dropna(subset = ['Due'])

#st.dataframe(monthly_costs.set_index('Description'))


monthly_costs['budget'] = monthly_costs['Credit'] - monthly_costs['Debit']

    ### Add Combined person
#combined_budget = monthly_costs.groupby("Person", as_index = False)["budget"].sum()


st.write("Monthly Budget Remainders")
st.write("")



budget = monthly_costs[['Person', 'budget']].dropna()
budget = budget.groupby('Person', as_index=False)['budget'].sum()
budget.loc[len(budget)] = ["Luke + Caitlin", budget['budget'].sum()]

st.dataframe(budget.set_index('Person'))

st.write("")


##
## DATA VISUALIZATION

# # LABEL COLUMNS
# label_cols = st.columns(3,
#                         width = 'stretch')

# label_col1 = label_cols[0]
# label_col2 = label_cols[1]
# label_col3 = label_cols[2]

# with label_col1:
#     st.write("Income by Source")
# with label_col2:
#     st.write("Expenses by Account")
# with label_col3:
#     st.write("Expenses by Category")

# PIE CHART COLUMNS
pie_cols = st.columns(3,
                      width = 'stretch',
                      border = True)

pie_col1 = pie_cols[0]
pie_col2 = pie_cols[1]
pie_col3 = pie_cols[2]

income_account = px.pie(expense_costs[expense_costs['Credit'] > 0.01],
                   values = 'Credit',
                   names = 'Description',
                   width = 200,
                   color = 'Description',
                   color_discrete_map = 
                        {"Unum" : "#0070C0",
                        "DCFSA Reimbursement" : "#489FD5",
                        "Williamson": "#E18686"})
income_account.update_layout(showlegend = False)

expense_account = px.pie(expense_costs,
                   values = 'Debit',
                   names = 'Person',
                   width = 200)
expense_account.update_layout(showlegend = False)


expense_type = px.pie(expense_costs,
                      values = 'Debit',
                      names = 'Type',
                      width = 200)
expense_type.update_layout(showlegend = False)


with pie_col1:
    st.subheader("Income by Source")
    st.write("")
    st.write("")
    
    pie_part1, table_part1 = st.columns(2,
                                        vertical_alignment = "top"
                                        )

    with pie_part1:
        st.plotly_chart(income_account)
    with table_part1:
        income_account_desc = expense_costs[expense_costs['Credit'] > 0.01]
        income_account_desc = income_account_desc.groupby('Description')['Credit'].sum().dropna().sort_values(ascending = False)  
        st.dataframe(income_account_desc)      

with pie_col2:
    st.subheader("Expenses by Account")
    st.write("")
    st.write("")

    pie_part2, table_part2 = st.columns(2,
                                        vertical_alignment = "top"
                                        )

    with pie_part2:
        st.plotly_chart(expense_account)
    with table_part2:
        expense_account_desc = expense_costs[expense_costs['Debit'] != 0]
        expense_account_desc = expense_account_desc.groupby('Person')['Debit'].sum().dropna().sort_values(ascending = False)
        st.dataframe(expense_account_desc)  

with pie_col3:
    st.subheader("Expenses by Category")  
    st.write("")
    st.write("")

    pie_part3, table_part3 = st.columns(2,
                                        vertical_alignment = "top"
                                        )

    with pie_part3:  
        st.plotly_chart(expense_type)
    with table_part3:
        expense_type_desc = expense_costs[expense_costs['Debit'] != 0]
        expense_type_desc = expense_type_desc.groupby('Type')['Debit'].sum().dropna().sort_values(ascending = False)
        st.dataframe(expense_type_desc)  

st.write("")


##
## DATA DESCRIPTIONS 

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

# detail_tab1, detail_tab2 = st.tabs(['Breakdown', 'Details'])

# with detail_tab1:
#     data_col1, data_col2, data_col3 = st.columns(3)

#     with data_col1:
#         st.dataframe(income_account_desc)
#     with data_col2:
#         st.dataframe(expense_account_desc)
#     with data_col3:
#         st.dataframe(expense_type_desc)
# with detail_tab2:
#     detail = st.selectbox("Detail",
#                  expense_costs['Type'].drop_duplicates().dropna().sort_values())
#     st.dataframe(expense_costs[expense_costs['Type'] == detail].set_index('Description'))


detail = st.selectbox("Detail",
                    expense_costs['Type'].drop_duplicates().dropna().sort_values())
st.dataframe(expense_costs[expense_costs['Type'] == detail].set_index('Description'))
