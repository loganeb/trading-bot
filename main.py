import Calculations
from Coinbase import PRODUCT_URL, get_coinbase_product_candles, coinbase_convert_to_dicts
import plotly.graph_objects as go

SYMBOL = 'ETH-USDT'

candles = get_coinbase_product_candles(PRODUCT_URL, SYMBOL)
candles = coinbase_convert_to_dicts(candles)
candles = Calculations.calc_vwap(candles)


def plot_vwap(candlestick_data):
    dates = [dp['date'] for dp in candlestick_data]
    opens =  [dp['open'] for dp in candlestick_data]
    highs = [dp['high'] for dp in candlestick_data]
    lows = [dp['low'] for dp in candlestick_data]
    closes = [dp['close'] for dp in candlestick_data]
    vwap = [dp['vwap'] for dp in candlestick_data]
    fig = go.Figure()
    fig.add_trace(go.Candlestick(x=dates,open=opens, high=highs, low=lows,close=closes, name=SYMBOL))
    fig.add_trace(go.Scatter(x=dates, y=vwap, mode='lines', name='VWAP'))
    fig.show()

plot_vwap(candles)
