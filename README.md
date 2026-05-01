Binance Futures Trading Bot

->Project Description

This is a simple Python trading bot that places orders on Binance Futures Testnet using CLI input.

-> Features

* Supports BUY and SELL orders
* Supports MARKET and LIMIT orders
* Command line input (symbol, side, type, quantity, price)
* Logging of API requests and errors

->Setup Instructions

1. Install required packages:
   pip install python-binance python-dotenv

2.Create a .env file and add your API keys:
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_secret_key
-> How to Run
Market Order:
python main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

Limit Order:
python main.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 60000

Output

* Displays order details such as orderId, status, executed quantity, and price
Logs

* Logs are saved in bot.log file

 Note

* This project uses Binance Futures Testnet (no real money involved)
* Do not share your API keys publicly
