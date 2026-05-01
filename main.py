import argparse
from client import BinanceFuturesClient

def validate_args(args):
    if args.side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    if args.type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")

    if args.quantity <= 0:
        raise ValueError("Quantity must be positive")

    if args.type == "LIMIT" and args.price is None:
        raise ValueError("Price is required for LIMIT orders")

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

    parser.add_argument("symbol", required=True, help="e.g. BTCUSDT")
    parser.add_argument("side", required=True, help="BUY or SELL")
    parser.add_argument("type", required=True, help="MARKET or LIMIT")
    parser.add_argument("quantity", type=float, required=True)
    parser.add_argument("price", type=float, required=False)

    args = parser.parse_args()

    try:
        validate_args(args)

        print("\n Order Request Summary")
        print(f"Symbol: {args.symbol}")
        print(f"Side: {args.side}")
        print(f"Type: {args.type}")
        print(f"Quantity: {args.quantity}")
        if args.price:
            print(f"Price: {args.price}")

        client = BinanceFuturesClient()
        response = client.place_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )

        print("\n Order Successful!")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Avg Price: {response.get('avgPrice', 'N/A')}")

    except Exception as e:
        print("\n Order Failed")
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
