import tradingview_data
import sms_api
import time
import requests
import urllib3
import aiosmtplib.errors
from bs4 import BeautifulSoup

class main:

    def __init__(self):
     self.eos_target = 87.00
     self.xrp_target = 9.55
     self.bch_target = 9000.00
     self.dash_target = 2800.00


    def get_target(self):
        return self.eos_target
        return self.xrp_target
        return self.bch_target
        return self.dash_target




#""" Evaluates if the desired target is still greater than the current price.
#If so, send sms alert to the configured number."""

    def __gt__(self):

        if self.eos_target > tradingview_data.eos_price():
            pass #print('EOS target is not close.')
        else:
            sms_api.send_eos_sms()
            print('EOS TARGET IS CLOSE!')
#----------------------------------------------------------#
        if self.xrp_target > tradingview_data.xrp_price():
            pass #print('XRP target is not close.')
        else:
            sms_api.send_xrp_sms()
            print('XRP TARGET IS CLOSE!')
#----------------------------------------------------------#
        if self.bch_target > tradingview_data.bch_price():
            pass #print('BCH target is not close.')
        else:
            sms_api.send_bch_sms()
            print('BCH TARGET IS CLOSE!')
#----------------------------------------------------------#
        if self.dash_target > tradingview_data.dash_price():
            pass #print('DASH target is not close.')
        else:
            sms_api.send_dash_sms()
            print('DASH TARGET IS CLOSE!')




#""" Evaluates the highest remaining percentage of profit left in a particular asset which is based on the predetermined target. """

    def percentEval(self):
        if self.eos_target and self.xrp_target and self.bch_target and self.dash_target != 0:

            eos_margin = (abs(self.eos_target - tradingview_data.eos_price()) / tradingview_data.eos_price()) * 100
            xrp_margin = (abs(self.xrp_target - tradingview_data.xrp_price()) / tradingview_data.xrp_price()) * 100
            bch_margin = (abs(self.bch_target - tradingview_data.bch_price()) / tradingview_data.bch_price()) * 100
            dash_margin = (abs(self.dash_target - tradingview_data.dash_price()) / tradingview_data.dash_price()) * 100


            if eos_margin > max(xrp_margin, bch_margin, dash_margin):
                    print(str("{0:.2f}".format(eos_margin)) + '% left on EOS')
            elif xrp_margin > max(eos_margin, bch_margin, dash_margin):
                    print(str("{0:.2f}".format(xrp_margin)) + '% left on XRP')
            elif bch_margin > max(eos_margin, xrp_margin, dash_margin):
                    print(str("{0:.2f}".format(bch_margin)) + '% left on BCH')
            elif dash_margin > max(eos_margin, xrp_margin, bch_margin):
                    print(str("{0:.2f}".format(dash_margin)) + '% left on DASH')


        else:
            return "By some anomaly you have lost 100% on one of your assets or wanted something to go to zero."




#""" Calls each of the buy_or_sell and 24 hour perecnt change functions created in tradingview_data """
    def bos(self):
        tradingview_data.buy_or_sell_eos()
        tradingview_data.buy_or_sell_xrp()
        tradingview_data.buy_or_sell_bch()
        tradingview_data.buy_or_sell_dash()
        tradingview_data.buy_or_sell_xlm()
        tradingview_data.buy_or_sell_btc()
        tradingview_data.buy_or_sell_eth()
        tradingview_data.buy_or_sell_link()



#""" Checks for when the fear/greed index is in extreme states of fear or greed """
    def fgi(self):

        url = 'https://alternative.me/crypto/fear-and-greed-index/'

        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')

        now = ''
        
        for body in soup.find_all('body'):
            for main in body.find_all('main'):
                for div in main.find_all('div', {'class': 'status'})[0]:
                    now = div.text
                    
        print('Fear/Greed Index: ' + now)            
        if now == 'Extreme Fear':
            print('Exteme Fear on fear/greed index!')
            sms_api.send_buy_fgi_sms()

        elif now == 'Extreme Greed':
            print('Exteme Greed on fear/greed index!')
            sms_api.send_sell_fgi_sms()
















if __name__ == "__main__":

    r = main()
    starttime = time.time()

    while(True):
        try:
            r.bos()
            r.__gt__()
            r.percentEval()
            r.fgi()
        except(requests.exceptions.RequestException, urllib3.exceptions.ReadTimeoutError) as error:
            print('Connection dropped. . . \n')
            print('Attempting to reconnect in 27 seconds. . . \n')
        except aiosmtplib.SMTPAuthenticationError as error:
            print('\nInvaid credentials for Gmail Account. \n- See sms_api_auth.py to configure credentials.\n- Make sure that "less secure app access" is turned ON in your Gmail account settings')
        time.sleep(27.0 - ((time.time() - starttime) % 27.0))
