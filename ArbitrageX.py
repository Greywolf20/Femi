import ccxt
import time

# Set up the exchanges
exchange1 = ccxt.binance({'apiKey': 'YOUR_API_KEY', 'secret': 'YOUR_SECRET'})
exchange2 = ccxt.coinbasepro({'apiKey': 'YOUR_API_KEY', 'secret': 'YOUR_SECRET'})

# Parameters
symbol = 'BTC/USDT'
amount = 0.001  # Adjust based on your risk tolerance and funds
threshold = 0.5  # Minimum percentage gain to execute arbitrage

# Arbitrage Bot
while True:
    try:
        # Fetch prices
        price1 = get_price(exchange1, symbol)
        price2 = get_price(exchange2, symbol)
        
        # Check for arbitrage
        action = check_arbitrage(price1, price2, threshold)
        
        # Execute trade if an opportunity is found
        if action:
            if action == 'buy_exchange1':
                execute_trade(exchange1, exchange2, symbol, amount)
            else:
                execute_trade(exchange2, exchange1, symbol, amount)
                
        time.sleep(10)  # Sleep to avoid rate limit issues
    except Exception as e:
        print(f"Error in bot loop: {e}")