# Python's Standard Library Imports
import csv

# Third-party Library Imports
import yfinance as yf


def get_ticker_list():
    stocks = []
    with open("stocks.csv") as stocks_list:
        for row in csv.reader(stocks_list):
            stocks.append(row[0])
    print(f"Stocks read in from stocks.csv -  {stocks}")
    return stocks


def get_industry(ticker):
    stock = yf.Ticker(ticker)
    stock_informaton = stock.info

    sector = stock_informaton["sector"]
    industry = stock_informaton["industry"]
    print(f"{ticker} is part of {industry}, within {sector}")


def main():
    for ticker in get_ticker_list():
        get_industry(ticker)


if __name__ == "__main__":
    main()
