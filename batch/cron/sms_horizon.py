import requests
import urllib
from ssl_request import ssl_request
import json


class SmsHorizon:
    def __init__(self, user, api_key, main_url):
        self.user = user
        self.api_key = api_key
        self.main_url = main_url

    def send_sms(self, message, mobile, senderid="MYTEXT", type="txt"):
        url = self.main_url
        #message = urllib.quote_plus(message)
        querystring = {"user": self.user, "apikey": self.api_key, "mobile": mobile, "senderid": senderid,
                       "message": message, "type": type}

        try:
            response = ssl_request("GET", url, params=querystring)
            print response.url
            return json.loads(response)
        except Exception, e:
            return None


def main():
    # Replace with your username
    user = "porovvasu"

    # Replace with your API KEY (We have sent API KEY on activation email, also available on panel)
    apikey = "bgeKApJ22wBgmuwNlKfr"

    # Replace with the destination mobile Number to which you want to send sms
    mobile = "7417250179"

    # Replace if you have your own Sender ID, else donot change
    senderid = "MYTEXT"

    # Replace with your Message content
    message = "Test sms API"

    # For Plain Text, use "txt"  for Unicode symbols or regional Languages like hindi/tamil/kannada use "uni"
    type="txt"

    mainUrl="http://smshorizon.co.in/api/sendsms.php?"

    sms_horizon = SmsHorizon(user=user, api_key=apikey, main_url=mainUrl)
    sms_horizon.send_sms(message=message, mobile=mobile)

if __name__ == '__main__':
    main()
