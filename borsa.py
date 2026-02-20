import yfinance as yf

def get_stock_price(symbol):
    """
    Fetches the latest closing price for a given stock symbol.
    Example: 'THYAO.IS' for Borsa Istanbul.
    """
    ticker = yf.Ticker(symbol)
    data = ticker.history(period="1d")
    return data['Close'].iloc[-1] if not data.empty else None

if __name__ == "__main__":
    symbol = "THYAO.IS"
    price = get_stock_price(symbol)
    if price:
        print(f"{symbol} current price: {price:.2f}")
