from twilio.rest import Client
from nsetools import Nse
import time

account_sid = 'AC67f2e595460b7b816d0ae8c062c63402'
auth_token = '85f566723e340c606635de03d2617f9f'
client = Client(account_sid, auth_token)
nse = Nse()


# a = nse.get_index_quote("nifty bank")
# top_gainers = nse.get_top_gainers()
# #print(a)
# print(top_gainers)
def send_msg():
    q = nse.get_quote('HINDALCO')
    result = time.localtime()
    ans = {}
    for i in q:
        # if i in ['symbol', 'companyName', 'previousClose', 'open', 'dayHigh', 'dayLow', 'closePrice', 'averagePrice',
        # 'change', 'pChange', 'quantityTraded', 'high52', 'low52', 'faceValue', 'lastPrice']:
        # print(i.capitalize(), ':', q[key])
        if i == 'lastPrice':
            ans[i.capitalize()] = q[i]
    res = ans['Lastprice']
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body="✨🤍✨----------|(GAIL)|----------✨🤍✨" + "\n" + "                                  :->  " + str(res) + "  <-:                                  " + "\n" + "✨🤍✨--------Thank  You--------✨🤍✨",
        # body="\n".join("{!r}  :  {!r},".format(k, v) for k, v in ans.items())+"\n"+"All The Best...Have a Great Day.",
        to='whatsapp:+919325145178'
    )
    print(message.sid)


def checktimes():
    if (time.localtime().tm_hour >= 4) and (time.localtime().tm_hour <= 10):
        send_msg()
    else:
        print("Sorry, Not in Time...!!!")
        print(time.localtime().tm_hour)
# from twilio.rest import Client
# account_sid = 'AC85c69d7efd2ab265bce5f40bc34dc980'
# auth_token = '1802e3ab8a9715cb8db89a8827738f67'
# client = Client(account_sid, auth_token)

# message = client.messages.create(
#    from_='whatsapp:+14155238886',
#    body='Your Twilio code is 1238432',
#    to='whatsapp:+919325145178'
# )
# print(message.sid)

