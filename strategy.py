import pandas as pd

def calculate_rsi(data, period=14):
    delta = data['close'].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))

def generate_signal(data):
    data['rsi'] = calculate_rsi(data)
    latest = data.iloc[-1]
    if latest['rsi'] < 30:
        return {"action": "BUY", "reason": "RSI below 30"}
    elif latest['rsi'] > 70:
        return {"action": "SELL", "reason": "RSI above 70"}
    else:
        return {"action": "HOLD", "reason": "RSI in neutral"}
