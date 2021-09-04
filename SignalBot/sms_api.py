import asyncio
import re
from email.message import EmailMessage
from typing import Tuple, Union
import sms_auth
import aiosmtplib
from cooldown import cooldown

HOST = "smtp.gmail.com"
# https://kb.sandisk.com/app/answers/detail/a_id/17056/~/list-of-mobile-carrier-gateway-addresses
# https://www.gmass.co/blog/send-text-from-gmail/



# pylint: disable=too-many-arguments
async def send_txt(
    num: Union[str, int], carrier: str, email: str, pword: str, msg: str, subj: str
) -> Tuple[dict, str]:
    to_email = sms_auth.CARRIER_MAP[carrier]

    # build message
    message = EmailMessage()
    message["From"] = "Price Alert Server01"
    message["To"] = f"{num}@{to_email}"
    message["Subject"] = subj
    message.set_content(msg)
    message.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">This is HTML to overwite this bad API!</h1> 
    </body>
</html>
""", subtype='html')

    # send
    send_kws = dict(username=email, password=pword, hostname=HOST, port=587, start_tls=True)
    res = await aiosmtplib.send(message, **send_kws)  # type: ignore
    msg = "failed" if not re.search(r"\sOK\s", res[1]) else "Message successfully sent \n"
    print(msg)
    return res






''' ALERT SMS's '''

@cooldown(seconds=2700)
def send_eos_sms():

    _msg = "                                 EOS NEAR TARGET"
    _subj = "EOS NEAR TARGET!"
    send = send_txt(sms_auth.NUMBER, sms_auth.CARRIER, sms_auth.EMAIL, sms_auth.PASS, _msg, _subj)
    asyncio.run(send)
    

@cooldown(seconds=2700)
def send_xrp_sms():

    _msg = "                                 XRP NEAR TARGET"
    _subj = "XRP NEAR TARGET"
    send = send_txt(sms_auth.NUMBER, sms_auth.CARRIER, sms_auth.EMAIL, sms_auth.PASS, _msg, _subj)
    asyncio.run(send)


@cooldown(seconds=2700)
def send_bch_sms():

    _msg = "                                 BCH NEAR TARGET"
    _subj = "BCH NEAR TARGET"
    send = send_txt(sms_auth.NUMBER, sms_auth.CARRIER, sms_auth.EMAIL, sms_auth.PASS, _msg, _subj)
    asyncio.run(send)


@cooldown(seconds=2700)
def send_dash_sms():

    _msg = "                                 DASH NEAR TARGET"
    _subj = "DASH NEAR TARGET"
    send = send_txt(sms_auth.NUMBER, sms_auth.CARRIER, sms_auth.EMAIL, sms_auth.PASS, _msg, _subj)
    asyncio.run(send)


@cooldown(seconds=2700)
def send_eos_ema_sms():

    _msg = "                                 EOS daily 20/50 cross"
    _subj = "EOS bullish or bearish 20/50 EMA cross"
    send = send_txt(sms_auth.NUMBER, sms_auth.CARRIER, sms_auth.EMAIL, sms_auth.PASS, _msg, _subj)
    asyncio.run(send)
    

@cooldown(seconds=2700)
def send_xrp_ema_sms():

    _msg = "                                 XRP daily 20/50 cross"
    _subj = "XRP bullish or bearish 20/50 EMA cross"
    send = send_txt(sms_auth.NUMBER, sms_auth.CARRIER, sms_auth.EMAIL, sms_auth.PASS, _msg, _subj)
    asyncio.run(send)
    

@cooldown(seconds=2700)
def send_bch_ema_sms():

    _msg = "                                 BCH daily 20/50 cross"
    _subj = "BCH bullish or bearish 20/50 EMA cross"
    send = send_txt(sms_auth.NUMBER, sms_auth.CARRIER, sms_auth.EMAIL, sms_auth.PASS, _msg, _subj)
    asyncio.run(send)
    

@cooldown(seconds=2700)
def send_dash_ema_sms():

    _msg = "                                 DASH daily 20/50 cross"
    _subj = "DASH bullish or bearish 20/50 EMA cross"
    send = send_txt(sms_auth.NUMBER, sms_auth.CARRIER, sms_auth.EMAIL, sms_auth.PASS, _msg, _subj)
    asyncio.run(send)
    

@cooldown(seconds=2700)
def send_xlm_ema_sms():

    _msg = "                                 XLM daily 20/50 cross"
    _subj = "XLM bullish or bearish 20/50 EMA cross"
    send = send_txt(sms_auth.NUMBER, sms_auth.CARRIER, sms_auth.EMAIL, sms_auth.PASS, _msg, _subj)
    asyncio.run(send)
    

@cooldown(seconds=2700)
def send_btc_ema_sms():

    _msg = "                                 BTC daily 20/50 cross"
    _subj = "BTC bullish or bearish 20/50 EMA cross"
    send = send_txt(sms_auth.NUMBER, sms_auth.CARRIER, sms_auth.EMAIL, sms_auth.PASS, _msg, _subj)
    asyncio.run(send)
    

@cooldown(seconds=2700)
def send_eth_ema_sms():

    _msg = "                                 ETH daily 20/50 cross"
    _subj = "ETH bullish or bearish 20/50 EMA cross"
    send = send_txt(sms_auth.NUMBER, sms_auth.CARRIER, sms_auth.EMAIL, sms_auth.PASS, _msg, _subj)
    asyncio.run(send)
    

@cooldown(seconds=2700)
def send_link_ema_sms():

    _msg = "                                 LINK daily 20/50 cross"
    _subj = "LINK bullish or bearish 20/50 EMA cross"
    send = send_txt(sms_auth.NUMBER, sms_auth.CARRIER, sms_auth.EMAIL, sms_auth.PASS, _msg, _subj)
    asyncio.run(send)
    










''' BUY SMS's '''

@cooldown(seconds=2700)
def send_buy_eos_sms():

    _msg = "Good time to DCA into EOS"
    _subj = "DCA EOS"
    send = send_txt(sms_auth.NUMBER, sms_auth.CARRIER, sms_auth.EMAIL, sms_auth.PASS, _msg, _subj)
    asyncio.run(send)


@cooldown(seconds=2700)
def send_buy_xrp_sms():

    _msg = "Good time to DCA into XRP"
    _subj = "DCA XRP"
    send = send_txt(sms_auth.NUMBER, sms_auth.CARRIER, sms_auth.EMAIL, sms_auth.PASS, _msg, _subj)
    asyncio.run(send)


@cooldown(seconds=2700)
def send_buy_bch_sms():

    _msg = "Good time to DCA into BCH"
    _subj = "DCA BCH"
    send = send_txt(sms_auth.NUMBER, sms_auth.CARRIER, sms_auth.EMAIL, sms_auth.PASS, _msg, _subj)
    asyncio.run(send)


@cooldown(seconds=2700)
def send_buy_dash_sms():

    _msg = "Good time to DCA into DASH"
    _subj = "DCA DASH"
    send = send_txt(sms_auth.NUMBER, sms_auth.CARRIER, sms_auth.EMAIL, sms_auth.PASS, _msg, _subj)
    asyncio.run(send)


@cooldown(seconds=2700)
def send_buy_xlm_sms():

    _msg = "Good time to DCA into XLM"
    _subj = "DCA XLM"
    send = send_txt(sms_auth.NUMBER, sms_auth.CARRIER, sms_auth.EMAIL, sms_auth.PASS, _msg, _subj)
    asyncio.run(send)


@cooldown(seconds=2700)
def send_buy_btc_sms():

    _msg = "Good time to DCA into BTC"
    _subj = "DCA BTC"
    send = send_txt(sms_auth.NUMBER, sms_auth.CARRIER, sms_auth.EMAIL, sms_auth.PASS, _msg, _subj)
    asyncio.run(send)


@cooldown(seconds=2700)
def send_buy_eth_sms():

    _msg = "Good time to DCA into ETH"
    _subj = "DCA ETH"
    send = send_txt(sms_auth.NUMBER, sms_auth.CARRIER, sms_auth.EMAIL, sms_auth.PASS, _msg, _subj)
    asyncio.run(send)


@cooldown(seconds=2700)
def send_buy_link_sms():

    _msg = "Good time to DCA into LINK"
    _subj = "DCA LINK"
    send = send_txt(sms_auth.NUMBER, sms_auth.CARRIER, sms_auth.EMAIL, sms_auth.PASS, _msg, _subj)
    asyncio.run(send)
    










''' SELL SMS's '''

@cooldown(seconds=2700)
def send_sell_eos_sms():

    _msg = "Good time to convert EOS into stablecoin"
    _subj = "STABLE COIN EOS"
    send = send_txt(sms_auth.NUMBER, sms_auth.CARRIER, sms_auth.EMAIL, sms_auth.PASS, _msg, _subj)
    asyncio.run(send)


@cooldown(seconds=2700)
def send_sell_xrp_sms():

    _msg = "Good time to convert XRP into stablecoin"
    _subj = "STABLE COIN XRP"
    send = send_txt(sms_auth.NUMBER, sms_auth.CARRIER, sms_auth.EMAIL, sms_auth.PASS, _msg, _subj)
    asyncio.run(send)


@cooldown(seconds=2700)
def send_sell_bch_sms():

    _msg = "Good time to convert BCH into stablecoin"
    _subj = "STABLE COIN BCH"
    send = send_txt(sms_auth.NUMBER, sms_auth.CARRIER, sms_auth.EMAIL, sms_auth.PASS, _msg, _subj)
    asyncio.run(send)


@cooldown(seconds=2700)
def send_sell_dash_sms():

    _msg = "Good time to convert DASH into stablecoin"
    _subj = "STABLE COIN DASH"
    send = send_txt(sms_auth.NUMBER, sms_auth.CARRIER, sms_auth.EMAIL, sms_auth.PASS, _msg, _subj)
    asyncio.run(send)


@cooldown(seconds=2700)
def send_sell_xlm_sms():

    _msg = "Good time to convert XLM into stablecoin"
    _subj = "STABLE COIN XLM"
    send = send_txt(sms_auth.NUMBER, sms_auth.CARRIER, sms_auth.EMAIL, sms_auth.PASS, _msg, _subj)
    asyncio.run(send)


@cooldown(seconds=2700)
def send_sell_btc_sms():

    _msg = "Good time to convert BTC into stablecoin"
    _subj = "STABLE COIN BTC"
    send = send_txt(sms_auth.NUMBER, sms_auth.CARRIER, sms_auth.EMAIL, sms_auth.PASS, _msg, _subj)
    asyncio.run(send)


@cooldown(seconds=2700)
def send_sell_eth_sms():

    _msg = "Good time to convert ETH into stablecoin"
    _subj = "STABLE COIN ETH"
    send = send_txt(sms_auth.NUMBER, sms_auth.CARRIER, sms_auth.EMAIL, sms_auth.PASS, _msg, _subj)
    asyncio.run(send)


@cooldown(seconds=2700)
def send_sell_link_sms():

    _msg = "Good time to convert LINK into stablecoin"
    _subj = "STABLE COIN LINK"
    send = send_txt(sms_auth.NUMBER, sms_auth.CARRIER, sms_auth.EMAIL, sms_auth.PASS, _msg, _subj)
    asyncio.run(send)
