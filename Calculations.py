from datetime import datetime, timezone

def create_price_volume_list(candlestick_data):
    for dp in candlestick_data:
        dp['date'] = datetime.fromtimestamp(dp['date'], tz=timezone.utc)
        dp['avg_price'] = (dp['low'] + dp['high'] + dp['close'])/3
    return candlestick_data

def calc_vwap(price_volume_list):
    pvl = create_price_volume_list(price_volume_list)
    pvl = calc_cumulative_price(pvl)
    pvl = calc_cumulative_volume(pvl)
    for dp in pvl:
        dp['vwap'] = dp['cumulative_price']/dp['cumulative_volume']
    return pvl

def calc_cumulative_price(price_volume_list):
    for i,dp in enumerate(price_volume_list):
        if i == 0:
            dp['cumulative_price'] = dp['avg_price']*dp['volume']
        else:
            dp['cumulative_price'] = (dp['avg_price']*dp['volume']) + price_volume_list[i-1]['cumulative_price']
    return price_volume_list

def calc_cumulative_volume(price_volume_list):
    for i,dp in enumerate(price_volume_list):
        if i == 0:
            dp['cumulative_volume'] = dp['volume']
        else:
            dp['cumulative_volume'] = dp['volume'] + price_volume_list[i-1]['cumulative_volume']
    return price_volume_list
