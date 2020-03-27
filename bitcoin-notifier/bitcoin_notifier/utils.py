# importing required packages for running this file
import json
import requests
import time
from datetime import datetime
from requests import Session

# IFTTT web hook url
web_hook_url = 'https://maker.ifttt.com/trigger/{}/with/key/m2syzMN9J62HA9Id46Z63e3wvUkpdHj-nDulcfmEpuy'


# this function fetches the bitcoin price from the CoinMarketCap API, fetches the price in USD and returns it as a
# float value
def get_latest_bitcoin_price():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '14d8fff4-16d8-4b5e-84d6-0bc99ea1b45d',
    }
    # a session object is created and the header is updated with the values defined above
    session = Session()
    session.headers.update(headers)
    # trying to get the response from the session object and loading the text from the json file to data
    try:
        response = session.get(url)
        data = json.loads(response.text)
    except:
        print("Error Occurred!!!")
    print("Latest BTC Price : ", float('{0:.2f}'.format(data['data'][0]['quote']['USD']['price'])))
    return float('{0:.2f}'.format(data['data'][0]['quote']['USD']['price']))


# function to change the web hook url according to the event that needs to be triggered and pass it in the post function
def post_web_hook(event, value):
    data = {'value1': value}
    event_url = web_hook_url.format(event)
    requests.post(event_url, json=data)
    print("Triggering event : ", event_url)


# function to format the data fetched from the API in correct datetime and price format and making a string obj by
# concatenating both and then finally append to a list and return the joined elements of the list
def format_bitcoin_history(bitcoin_history):
    rows = []
    for bitcoin_price in bitcoin_history:
        date = bitcoin_price['date'].strftime('%d.%m.%Y %H:%M')
        price = bitcoin_price['price']
        row = '{}: $<b>{}</b>'.format(date, price)
        rows.append(row)
    return '<br>'.join(rows)


# main runner function which is called from the utils.main(), it runs for the time interval and threshold passed as
# arguments
def run(BITCOIN_PRICE_THRESHOLD, interval):
    bitcoin_history = []
    threshold = float(BITCOIN_PRICE_THRESHOLD[0])
    time_interval = float(interval[0])
    while True:
        price = get_latest_bitcoin_price()
        date = datetime.now()
        bitcoin_history.append({'date': date, 'price': price})

        if price < threshold:
            post_web_hook('bitcoin_price_emergency', price)

        if len(bitcoin_history) == 5:
            post_web_hook('bitcoin_price_update', format_bitcoin_history(bitcoin_history))
            bitcoin_history = []

        time.sleep(time_interval * 60)
