# This is a sample Python script.
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# There are many applications out there that predict stockbassed on price
# Warren Buffet learned from Benjamin Graham how to pick businesses not stocks
# Graham wrote the "Intelligent Investor" where he said that successful stock traders
# don't focus on stock price alone, but they look at the business as well
# This application reads financial statements and gives the business a score
# based on they're business and then compares that score to stock price


ticker = str(input('Please enter the ticker of the business you want to analyze and compare'))
ticker1 = str(input('Please enter another ticker a the business you want to analyze and compare'))

income = pd.read_csv('{}_annual_financials.csv'.format(ticker))
balance = pd.read_csv('{}_annual_balance-sheet.csv'.format(ticker))
cash_flow = pd.read_csv('{}_annual_cash-flow.csv'.format(ticker))
income1 = pd.read_csv('{}_annual_financials.csv'.format(ticker1))
balance1 = pd.read_csv('{}_annual_balance-sheet.csv'.format(ticker1))
cash_flow1 = pd.read_csv('{}_annual_cash-flow.csv'.format(ticker1))


pd.set_option("display.max_rows", None)
print('{}'.format(ticker), balance)
pd.set_option("display.max_rows", None)
print('{}'.format(ticker), income)

pd.set_option("display.max_rows", None)
print('{}'.format(ticker1), balance1)
pd.set_option("display.max_rows", None)
print('{}'.format(ticker1), income1)
pd.set_option("display.max_rows", None)
print('{}'.format(ticker), cash_flow)
pd.set_option("display.max_rows", None)
print('{}'.format(ticker1), cash_flow1)
pd.set_option("display.max_rows", None)


def cash_asset(df):
    cash = df.iloc[[4], [1]]
    return cash


def cash_equivalants_asset(df):
    cash_equivalant = df.loc[5]
    return cash_equivalant


def accounts_recievables_asset(df):
    recievables = df.iloc[[7], [1]]
    return recievables


def prepaid_asset(df):
    prepaid = df.loc[11]
    return prepaid


def noncurrent_asset(df):
    non_current = df.loc[15]
    return non_current


def other_asset(df):
    other = df.loc[14]
    return other


def liabilities(df, row):
    liabilities = df.loc[row]
    return liabilities


def equity(df, row):
    equity = df.loc[row]
    return equity


# Income Statement data
def net_income(df1, row):
    income = df1.loc[row]
    return income


def revenue(df1):
    revenue = df1.loc[0]
    return revenue


def gross_profit(df1):
    profit = df1.loc[3]
    profit = profit.replace(',', '')
    return profit


def expenses(df1):
    exp = df1.loc[32]
    exp = exp.replace(',', '')
    return exp


# cash flow statement
def free_cash_flow(df, row):
    fcf = df.loc[row]
    return fcf


# Ratios
def debt_to_equity_ratio(debt, equity):
    debt = debt.replace(',', '')
    equity = equity.replace(',', '')
    ratio = float(debt) / float(equity)
    return ratio


def return_on_equity(income, equity):
    income = income.replace(',', '')
    equity = equity.replace(',', '')
    roe = float(income) / float(equity)
    return roe


def gross_profit_ratio(sales, gross):
    sales = sales.replace(',', '')
    gross = gross.replace(',', '')
    gpr = float(gross) / float(sales)
    return gpr


def net_profit_ratio(net, sales):
    net = net.replace(',', '')
    sales = sales.replace(',', '')
    npr = float(net) / float(sales)
    return float(npr)


def cashflow_to_debt(fcf, debt):
    fcf = fcf.replace(',', '')
    debt = debt.replace(',', '')
    ctd = float(fcf) / float(debt)
    return ctd

def revenue_growth(r):
    i = 0
    r = r.replace(',', '')

    while i < 10:
        temp = float(r) - float(r[i])
        growth = temp / float(r) *100
        return growth

row_equity = int(input('Enter the row that equities are on for {}'.format(ticker)))
row_liabilities = int(input('Enter the row that liabilities are on for {}'.format(ticker)))
row_income = int(input('Enter the row that income are on for {}'.format(ticker)))
row_free_cash = int(input('Enter the row that free cash flow is on for{}'.format(ticker)))

row_equity1 = int(input('Enter the row that equities are on for {}'.format(ticker1)))
row_liabilities1 = int(input('Enter the row that liabilities are on for {}'.format(ticker1)))
row_income1 = int(input('Enter the row that income are on for {}'.format(ticker1)))
row_free_cash1 = int(input('Enter the row that free cash flow is on for{}'.format(ticker1)))

biz1_ni = net_profit_ratio(net_income(income, row_income)[1], revenue(income)[1])
biz2_ni = net_profit_ratio(net_income(income1, row_income1)[1], revenue(income1)[1])
if biz1_ni > biz2_ni:
    print('{} net profit margin is higher with a net profit margin of: {}'.format(ticker, biz1_ni))
else:
    print('{} net profit margin is higher with a net profit margin of: {}'.format(ticker1, biz2_ni))

biz1_roe = return_on_equity(net_income(income, row_income)[1], equity(balance, row_equity)[1])
biz2_roe = return_on_equity(net_income(income1, row_income1)[1], equity(balance1, row_equity1)[1])

if biz1_roe > biz2_roe:
    print('{} return on equity margin is higher with: {}'.format(ticker, biz1_roe))
else:
    print('{} return on equity is higher with: {}'.format(ticker1, biz2_roe))

biz1_dte = debt_to_equity_ratio(liabilities(balance, row_liabilities)[1], equity(balance, row_equity)[1])
biz2_dte = debt_to_equity_ratio(liabilities(balance1, row_liabilities1)[1], equity(balance1, row_equity1)[1])

if biz1_dte > biz2_dte:
    print('{} has a higher debt ratio wit: {}'.format(ticker, biz1_dte))
else:
    print('{} has a lower debt ratio with: {}'.format(ticker1, biz2_dte))
print(biz1_dte)

biz1_fcd = cashflow_to_debt(free_cash_flow(cash_flow, row_free_cash)[1], liabilities(balance, row_liabilities)[1])
biz2_fcd = cashflow_to_debt(free_cash_flow(cash_flow1,row_free_cash1)[1], liabilities(balance1, row_liabilities1)[1])

if biz1_fcd > biz2_fcd:
    print('{} has a higher debt ratio wit: {}'.format(ticker, biz1_fcd))
else:
    print('{} has a lower debt ratio with: {}'.format(ticker1, biz2_fcd))
print(revenue_growth(revenue(income1)[1]))