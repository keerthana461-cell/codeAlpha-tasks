


import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# 1. Define portfolio holdings (Ticker: Quantity)
portfolio = {
    'AAPL': 50,  # 50 shares of Apple
    'TSLA': 30   # 30 shares of Tesla
}

# 2. Function to fetch data and calculate value
def track_portfolio(portfolio):
    data = []
    total_value = 0
    
    for ticker, quantity in portfolio.items():
        stock = yf.Ticker(ticker)
        # Fetch latest closing price
        price = stock.history(period="1d")['Close'].iloc[-1]
        value = price * quantity
        total_value += value
        data.append([ticker, quantity, price, value])
        
    # Create DataFrame
    df = pd.DataFrame(data, columns=['Ticker', 'Quantity', 'Current Price', 'Current Value'])
    return df, total_value

# 3. Get Portfolio Results
portfolio_df, total_value = track_portfolio(portfolio)

# 4. Calculate Percentage Allocation
portfolio_df['Allocation %'] = (portfolio_df['Current Value'] / total_value) * 100

# 5. Output Results
print("--- Portfolio Performance ---")
print(portfolio_df.to_string(index=False))
print(f"\nTotal Portfolio Value: ${total_value:,.2f}")

# 6. Visualization: Portfolio Allocation
plt.figure(figsize=(8, 6))
plt.pie(portfolio_df['Current Value'], labels=portfolio_df['Ticker'], autopct='%1.1f%%', startangle=140)
plt.title("Portfolio Allocation")
plt.show()
