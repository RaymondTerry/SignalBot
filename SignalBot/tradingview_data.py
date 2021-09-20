from tradingview_ta import *
import sms_api
import sms_auth
import math

# High end of portfolio
EOS = "EOSUSD"
XRP = "XRPUSD"
BCH = "BCHUSD"
DASH = "DASHUSD"

#Rest of portfolio
BTC = "BTCUSD"
ETH = "ETHUSD"
XLM = "XLMUSD"
LINK = "LINKUSD"
#et cetera and so forth...


    

#''' Evaluates various TA targets to determine buy/sell indications '''


def buy_or_sell_eos():

    handler = TA_Handler(
        symbol=EOS,
        screener="crypto",
        exchange="COINBASE",
        interval=Interval.INTERVAL_1_DAY
    )

    analysis = handler.get_analysis()

    blue_line = analysis.indicators["MACD.macd"] #BLUE LINE
    orange_line = analysis.indicators["MACD.signal"] #ORANGE LINE
    rsi = analysis.indicators["RSI"]
    ema_200 = analysis.indicators["EMA200"]
    ema_20 = analysis.indicators["EMA20"]
    ema_50 = analysis.indicators["EMA50"]
    price = analysis.indicators['close']
    daily_change = analysis.indicators['change']
    

    if blue_line < orange_line and blue_line <= 0 and orange_line <= 0 and math.isclose(blue_line, orange_line, abs_tol = 0.04) == True and price < ema_200 and rsi < 50:
        print("GOOD TIME TO DCA EOS")
        sms_api.send_buy_eos_sms()
    else: pass
    
    if blue_line < orange_line and blue_line <= 0 and orange_line <= 0 and math.isclose(blue_line, orange_line, abs_tol = 0.04) == True and price > ema_200:
        print("GOOD TIME TO ENTER TRADE")
        sms_api.send_buy_eos_sms()
    else: pass
    
    if blue_line < orange_line and blue_line <= 0.200 and orange_line > 0 and math.isclose(blue_line, orange_line, abs_tol = 0.04) == True and price > ema_200:
        print("GOOD TIME TO ENTER TRADE EOS")
        sms_api.send_buy_eos_sms()
    else: pass
    
    if blue_line > orange_line and blue_line > 0.240 and orange_line > 0 and math.isclose(blue_line, orange_line, abs_tol = 0.04) == True and price > ema_200:
        print("GOOD TIME TO TAKE PROFIT EOS")
        sms_api.send_sell_eos_sms()
    else: pass

    if math.isclose(ema_20, ema_50, abs_tol = 0.08) == True:
        print("GOLDEN CROSS OR BEAR CROSS")
        sms_api.send_eos_ema_sms()
    else: pass

    if daily_change <= -17.0000:
        print("Decent dip to DCA EOS")
        sms_api.send_buy_eos_sms()
    else: pass
    
    if daily_change >= 17.0000:
        print("Decent spike to take profit EOS")
        sms_api.send_sell_eos_sms()
    else: pass

    



def buy_or_sell_xrp():

    handler = TA_Handler(
        symbol=XRP,
        screener="crypto",
        exchange="BITFINEX",
        interval=Interval.INTERVAL_1_DAY
    )

    analysis = handler.get_analysis()

    blue_line = analysis.indicators["MACD.macd"] #BLUE LINE
    orange_line = analysis.indicators["MACD.signal"] #ORANGE LINE
    rsi = analysis.indicators["RSI"]
    ema_200 = analysis.indicators["EMA200"]
    ema_20 = analysis.indicators["EMA20"]
    ema_50 = analysis.indicators["EMA50"]
    price = analysis.indicators['close']
    daily_change = analysis.indicators['change']
    
    if blue_line < orange_line and blue_line <= 0 and orange_line <= 0 and math.isclose(blue_line, orange_line, abs_tol = 0.009) == True and price < ema_200 and rsi < 50:
        print("GOOD TIME TO DCA XRP")
        sms_api.send_buy_xrp_sms()
    else: pass
    
    if blue_line < orange_line and blue_line <= 0 and orange_line <= 0 and math.isclose(blue_line, orange_line, abs_tol = 0.009) == True and price > ema_200:
        print("GOOD TIME TO ENTER TRADE")
        sms_api.send_buy_xrp_sms()
    else: pass
    
    if blue_line < orange_line and blue_line <= 0.100 and orange_line > 0 and math.isclose(blue_line, orange_line, abs_tol = 0.009) == True and price > ema_200:
        print("GOOD TIME TO ENTER TRADE XRP")
        sms_api.send_buy_xrp_sms()
    else: pass

    if blue_line > orange_line and blue_line > 0.100 and orange_line > 0 and math.isclose(blue_line, orange_line, abs_tol = 0.009) == True and price > ema_200:
        print("GOOD TIME TO TAKE PROFIT XRP")
        sms_api.send_sell_xrp_sms()
    else: pass

    if math.isclose(ema_20, ema_50, abs_tol = 0.08) == True:
        print("GOLDEN CROSS OR BEAR CROSS ON XRP")
        sms_api.send_xrp_ema_sms()
    else: pass

    if daily_change <= -17.0000:
        print("Decent dip to DCA XRP")
        sms_api.send_buy_xrp_sms()
    else: pass
    
    if daily_change >= 17.0000:
        print("Decent spike to take profit XRP")
        sms_api.send_sell_xrp_sms()
    else: pass


def buy_or_sell_bch():

    handler = TA_Handler(
        symbol=BCH,
        screener="crypto",
        exchange="COINBASE",
        interval=Interval.INTERVAL_1_DAY
    )

    analysis = handler.get_analysis()

    blue_line = analysis.indicators["MACD.macd"] #BLUE LINE
    orange_line = analysis.indicators["MACD.signal"] #ORANGE LINE
    rsi = analysis.indicators["RSI"]
    ema_200 = analysis.indicators["EMA200"]
    ema_20 = analysis.indicators["EMA20"]
    ema_50 = analysis.indicators["EMA50"]
    price = analysis.indicators['close']
    daily_change = analysis.indicators['change']
    
    if blue_line <= 0 and orange_line <= 0 and math.isclose(blue_line, orange_line, abs_tol = 0.90) == True and price < ema_200 and rsi < 50:
        print("GOOD TIME TO DCA BCH")
        sms_api.send_buy_bch_sms()
    else: pass
    
    if blue_line <= 0 and orange_line <= 0 and math.isclose(blue_line, orange_line, abs_tol = 0.90) == True > ema_200:
        print("GOOD TIME TO ENTER TRADE BCH")
        sms_api.send_buy_bch_sms()
    else: pass
    
    if blue_line > 30 and orange_line > 0 and math.isclose(blue_line, orange_line, abs_tol = 1.00) == True and price > ema_200:
        print("GOOD TIME TO TAKE PROFIT BCH")
        sms_api.send_sell_bch_sms()
    else: pass

    if math.isclose(ema_20, ema_50, abs_tol = 3.00) == True:
        print("GOLDEN CROSS OR BEAR CROSS ON BCH")
        sms_api.send_bch_ema_sms()
    else: pass

    if daily_change <= -17.0000:
        print("Decent dip to DCA BCH")
        sms_api.send_buy_bch_sms()
    else: pass
    
    if daily_change >= 17.0000:
        print("Decent spike to take profit BCH")
        sms_api.send_sell_bch_sms()
    else: pass


def buy_or_sell_dash():

    handler = TA_Handler(
        symbol=DASH,
        screener="crypto",
        exchange="COINBASE",
        interval=Interval.INTERVAL_1_DAY
    )

    analysis = handler.get_analysis()

    blue_line = analysis.indicators["MACD.macd"] #BLUE LINE
    orange_line = analysis.indicators["MACD.signal"] #ORANGE LINE
    rsi = analysis.indicators["RSI"]
    ema_200 = analysis.indicators["EMA200"]
    ema_20 = analysis.indicators["EMA20"]
    ema_50 = analysis.indicators["EMA50"]
    price = analysis.indicators['close']
    daily_change = analysis.indicators['change']
    
    if blue_line < orange_line and blue_line <= 0 and orange_line <= 0 and math.isclose(blue_line, orange_line, abs_tol = 0.20) == True and price < ema_200 and rsi < 50:
        print("GOOD TIME TO DCA DASH")
        sms_api.send_buy_dash_sms()
    else: pass
    
    if blue_line < orange_line and blue_line <= 0 and orange_line <= 0 and math.isclose(blue_line, orange_line, abs_tol = 0.20) == True and price > ema_200:
        print("GOOD TIME TO ENTER DASH")
        sms_api.send_buy_dash_sms()
    else: pass
    
    if blue_line < orange_line and blue_line <= 17 and orange_line > 0 and math.isclose(blue_line, orange_line, abs_tol = 0.20) == True and price > ema_200:
        print("GOOD TIME TO ENTER TRADE DASH")
        sms_api.send_buy_dash_sms()
    else: pass
    
    if blue_line > orange_line and blue_line > 17 and orange_line > 0 and math.isclose(blue_line, orange_line, abs_tol = 0.20) == True and price > ema_200:
        print("GOOD TIME TO TAKE PROFIT DASH")
        sms_api.send_sell_dash_sms()
    else: pass

    if math.isclose(ema_20, ema_50, abs_tol = 3.00) == True:
        print("GOLDEN CROSS OR BEAR CROSS ON DASH")
        sms_api.send_dash_ema_sms()
    else: pass

    if daily_change <= -17.0000:
        print("Decent dip to DCA DASH")
        sms_api.send_buy_dash_sms()
    else: pass
    
    if daily_change >= 17.0000:
        print("Decent spike to take profit DASH")
        sms_api.send_sell_dash_sms()
    else: pass


def buy_or_sell_xlm():

    handler = TA_Handler(
        symbol=XLM,
        screener="crypto",
        exchange="COINBASE",
        interval=Interval.INTERVAL_1_DAY
    )

    analysis = handler.get_analysis()

    blue_line = analysis.indicators["MACD.macd"] #BLUE LINE
    orange_line = analysis.indicators["MACD.signal"] #ORANGE LINE
    rsi = analysis.indicators["RSI"]
    ema_200 = analysis.indicators["EMA200"]
    ema_20 = analysis.indicators["EMA20"]
    ema_50 = analysis.indicators["EMA50"]
    price = analysis.indicators['close']
    daily_change = analysis.indicators['change']
    
    if blue_line < orange_line and blue_line <= 0 and orange_line <= 0 and math.isclose(blue_line, orange_line, abs_tol = 0.0009) == True and price < ema_200 and rsi < 50:
        print("GOOD TIME TO DCA XLM")
        sms_api.send_buy_xlm_sms()
    else: pass
    
    if blue_line < orange_line and blue_line <= 0 and orange_line <= 0 and math.isclose(blue_line, orange_line, abs_tol = 0.0009) == True and price > ema_200:
        print("GOOD TIME TO ENTER XLM")
        sms_api.send_buy_xlm_sms()
    else: pass
    
    if blue_line < orange_line and blue_line <= 0.0180 and orange_line > 0 and math.isclose(blue_line, orange_line, abs_tol = 0.0009) == True and price > ema_200:
        print("GOOD TIME TO ENTER TRADE XLM")
        sms_api.send_buy_xlm_sms()
    else: pass
    
    if blue_line > orange_line and blue_line > 0.0180 and orange_line > 0 and math.isclose(blue_line, orange_line, abs_tol = 0.0009) == True and price > ema_200:
        print("GOOD TIME TO TAKE PROFIT XLM")
        sms_api.send_sell_xlm_sms()
    else: pass

    if math.isclose(ema_20, ema_50, abs_tol = 0.006) == True:
        print("GOLDEN CROSS OR BEAR CROSS ON XLM")
        sms_api.send_xlm_ema_sms()
    else: pass

    if daily_change <= -17.0000:
        print("Decent dip to DCA XLM")
        sms_api.send_buy_xlm_sms()
    else: pass
    
    if daily_change >= 17.0000:
        print("Decent spike to take profit XLM")
        sms_api.send_sell_xlm_sms()
    else: pass


def buy_or_sell_btc():

    handler = TA_Handler(
        symbol=BTC,
        screener="crypto",
        exchange="COINBASE",
        interval=Interval.INTERVAL_1_DAY
    )

    analysis = handler.get_analysis()

    blue_line = analysis.indicators["MACD.macd"] #BLUE LINE
    orange_line = analysis.indicators["MACD.signal"] #ORANGE LINE
    rsi = analysis.indicators["RSI"]
    ema_200 = analysis.indicators["EMA200"]
    ema_20 = analysis.indicators["EMA20"]
    ema_50 = analysis.indicators["EMA50"]
    price = analysis.indicators['close']
    daily_change = analysis.indicators['change']
    
    if blue_line < orange_line and blue_line <= 0 and orange_line <= 0 and math.isclose(blue_line, orange_line, abs_tol = 12.00) == True and price < ema_200 and rsi < 50:
        print("GOOD TIME TO DCA BTC")
        sms_api.send_buy_btc_sms()
    else: pass
    
    if blue_line < orange_line and blue_line <= 0 and orange_line <= 0 and math.isclose(blue_line, orange_line, abs_tol = 12.00) == True and price > ema_200:
        print("GOOD TIME TO ENTER TRADE")
        sms_api.send_buy_btc_sms()
    else: pass
    
    if blue_line < orange_line and blue_line > 700 and orange_line > 0 and math.isclose(blue_line, orange_line, abs_tol = 12.00) == True and price > ema_200:
        print("GOOD TIME TO TAKE PROFIT BTC")
        sms_api.send_sell_btc_sms()
    else: pass

    if math.isclose(ema_20, ema_50, abs_tol = 14.00) == True:
        print("GOLDEN CROSS OR BEAR CROSS ON BTC")
        sms_api.send_btc_ema_sms()
    else: pass

    if daily_change <= -17.0000:
        print("Decent dip to DCA BTC")
        sms_api.send_buy_btc_sms()
    else: pass
    
    if daily_change >= 17.0000:
        print("Decent spike to take profit BTC")
        sms_api.send_sell_btc_sms()
    else: pass


def buy_or_sell_eth():

    handler = TA_Handler(
        symbol=ETH,
        screener="crypto",
        exchange="COINBASE",
        interval=Interval.INTERVAL_1_DAY
    )

    analysis = handler.get_analysis()

    blue_line = analysis.indicators["MACD.macd"] #BLUE LINE
    orange_line = analysis.indicators["MACD.signal"] #ORANGE LINE
    rsi = analysis.indicators["RSI"]
    ema_200 = analysis.indicators["EMA200"]
    ema_20 = analysis.indicators["EMA20"]
    ema_50 = analysis.indicators["EMA50"]
    price = analysis.indicators['close']
    daily_change = analysis.indicators['change']
    
    if blue_line < orange_line and blue_line <= 0 and orange_line <= 0 and math.isclose(blue_line, orange_line, abs_tol = 4.00) == True and price < ema_200 and rsi < 50:
        print("GOOD TIME TO DCA ETH")
        sms_api.send_buy_eth_sms()
    else: pass
    
    if blue_line < orange_line and blue_line <= 0 and orange_line <= 0 and math.isclose(blue_line, orange_line, abs_tol = 4.00) == True and price > ema_200:
        print("GOOD TIME TO ENTER TRADE")
        sms_api.send_buy_eth_sms()
    else: pass
    
    if blue_line > orange_line and blue_line > 170 and orange_line > 0 and math.isclose(blue_line, orange_line, abs_tol = 4.00) == True and price > ema_200:
        print("GOOD TIME TO TAKE PROFIT ETH")
        sms_api.send_sell_eth_sms()
    else: pass

    if math.isclose(ema_20, ema_50, abs_tol = 12.00) == True:
        print("GOLDEN CROSS OR BEAR CROSS ON ETH")
        sms_api.send_eth_ema_sms()
    else: pass

    if daily_change <= -17.0000:
        print("Decent dip to DCA ETH")
        sms_api.send_buy_eth_sms()
    else: pass
    
    if daily_change >= 17.0000:
        print("Decent spike to take profit ETH")
        sms_api.send_sell_eth_sms()
    else: pass


def buy_or_sell_link():

    handler = TA_Handler(
        symbol=LINK,
        screener="crypto",
        exchange="COINBASE",
        interval=Interval.INTERVAL_1_DAY
    )

    analysis = handler.get_analysis()

    blue_line = analysis.indicators["MACD.macd"] #BLUE LINE
    orange_line = analysis.indicators["MACD.signal"] #ORANGE LINE
    rsi = analysis.indicators["RSI"]
    ema_200 = analysis.indicators["EMA200"]
    ema_20 = analysis.indicators["EMA20"]
    ema_50 = analysis.indicators["EMA50"]
    price = analysis.indicators['close']
    daily_change = analysis.indicators['change']
    
    if blue_line < orange_line and blue_line <= 0 and orange_line <= 0 and math.isclose(blue_line, orange_line, abs_tol = 0.45) == True and price < ema_200 and rsi < 50:
        print("GOOD TIME TO DCA LINK")
        sms_api.send_buy_link_sms()
    else: pass
    
    if blue_line < orange_line and blue_line <= 0 and orange_line <= 0 and math.isclose(blue_line, orange_line, abs_tol = 0.25) == True and price > ema_200:
        print("GOOD TIME TO ENTER TRADE")
        sms_api.send_buy_link_sms()
    else: pass
    
    if blue_line < orange_line and blue_line <= 1.65 and orange_line > 0 and math.isclose(blue_line, orange_line, abs_tol = 0.15) == True and price > ema_200:
        print("GOOD TIME TO TO ENTER TRADE LINK")
        sms_api.send_buy_link_sms()
    else: pass

    if blue_line > orange_line and blue_line > 1.65 and orange_line > 0 and math.isclose(blue_line, orange_line, abs_tol = 0.15) == True and price > ema_200:
        print("GOOD TIME TO TAKE PROFIT LINK")
        sms_api.send_sell_link_sms()
    else: pass

    if math.isclose(ema_20, ema_50, abs_tol = 0.80) == True:
        print("GOLDEN CROSS OR BEAR CROSS ON LINK")
        sms_api.send_link_ema_sms()
    else: pass

    if daily_change <= -17.0000:
        print("Decent dip to DCA LINK")
        sms_api.send_buy_link_sms()
    else: pass
    
    if daily_change >= 17.0000:
        print("Decent spike to take profit LINK")
        sms_api.send_sell_link_sms()
    else: pass











#""" Fn's to get asset price data """

def eos_price():
    

    eos_price = TA_Handler(
        symbol=EOS,
        screener="crypto",
        exchange="COINBASE",
        interval=Interval.INTERVAL_1_MINUTE
    )


    analysis = eos_price.get_analysis()

    price = analysis.indicators['close']
    
    return price






def xrp_price():
    

    xrp_price = TA_Handler(
        symbol=XRP,
        screener="crypto",
        exchange="BITFINEX",
        interval=Interval.INTERVAL_1_MINUTE
    )


    analysis = xrp_price.get_analysis()

    price = analysis.indicators['close']
    #print(price)
    return price









def bch_price():
    

    bch_price = TA_Handler(
        symbol=BCH,
        screener="crypto",
        exchange="COINBASE",
        interval=Interval.INTERVAL_1_MINUTE
    )


    analysis = bch_price.get_analysis()

    price = analysis.indicators['close']

    return price







def dash_price():
    

    dash_price = TA_Handler(
        symbol=DASH,
        screener="crypto",
        exchange="COINBASE",
        interval=Interval.INTERVAL_1_MINUTE
    )


    analysis = dash_price.get_analysis()

    price = analysis.indicators['close']

    return price







def xlm_price():
    

    dash_price = TA_Handler(
        symbol=XLM,
        screener="crypto",
        exchange="COINBASE",
        interval=Interval.INTERVAL_1_MINUTE
    )


    analysis = dash_price.get_analysis()

    price = analysis.indicators['close']

    return price







def btc_price():
    

    btc_price = TA_Handler(
        symbol=BTC,
        screener="crypto",
        exchange="COINBASE",
        interval=Interval.INTERVAL_1_MINUTE
    )


    analysis = btc_price.get_analysis()

    price = analysis.indicators['close']
    
    return price







def link_price():
    

    link_price = TA_Handler(
        symbol=LINK,
        screener="crypto",
        exchange="COINBASE",
        interval=Interval.INTERVAL_1_MINUTE
    )


    analysis = link_price.get_analysis()

    price = analysis.indicators['close']
    
    return price
