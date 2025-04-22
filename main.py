from signals.strategy import generate_signal
from utils.binance_fetch import fetch_binance_data
import json
import os

def save_signal(signal):
    os.makedirs("output", exist_ok=True)
    with open("output/last_signal.json", "w") as f:
        json.dump(signal, f)

def main():
    data = fetch_binance_data("BTCUSDT", "15m", 100)
    signal = generate_signal(data)
    print("Signal:", signal)
    save_signal(signal)

if __name__ == "__main__":
    main()
