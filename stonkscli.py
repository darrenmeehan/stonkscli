import yfinance as yf


def get_industry(ticker):
    stock = yf.Ticker(ticker)
    stock_informaton = stock.info

    sector = stock_informaton["sector"]
    industry = stock_informaton["industry"]
    print(f"{ticker} is part of {industry}, within {sector}")

def main():
    TICKERS = [
        "GME",
        "AAPL",
    ]
    for ticker in TICKERS:
        get_industry(ticker)

if __name__ == "__main__":
    main()
