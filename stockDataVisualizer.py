import requests
import pygal
import webbrowser
import platform

def intradaily(symbol):
    return 'https://alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + symbol + '&interval=5min&apikey=K7HLGROEFZW2C06M'

def daily(symbol):
    return 'https://alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + symbol + '&outputsize=full&apikey=K7HLGROEFZW2C06M'

def weekly(symbol):
    return 'https://alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=' + symbol + '&outputsize=full&apikey=K7HLGROEFZW2C06M'

def monthly(symbol):
    return 'https://alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=' + symbol + '&outputsize=full&apikey=K7HLGROEFZW2C06M'

url = daily('GOOGL') #THIS WILL NEED TO CHANGE TO THE USER INPUTTED STOCK VALUE
r = requests.get(url)
data = r.json()
dataInRange = []
dataSorted = []

for x in data["Time Series (Daily)"]:
    year, month, day = x.split('-')    
    if int(year) == 2024 and int(month) == 2 and int(day) >= 1 and int(day) <= 24:
        open = data["Time Series (Daily)"][x]['1. open']
        high = data["Time Series (Daily)"][x]['2. high']
        low = data["Time Series (Daily)"][x]['3. low']
        close = data["Time Series (Daily)"][x]['4. close']
        dataInRange.append([x, open, high, low, close])

dataLength = len(dataInRange)
for x in range(dataLength):
    dataSorted.append(dataInRange[dataLength - x - 1])

dates = []
open = []
high = []
low = []
close = []

for x in dataSorted:
    dates.append(x[0])
    open.append(float(x[1]))
    high.append(float(x[2]))
    low.append(float(x[3]))
    close.append(float(x[4]))

line_chart = pygal.Line()
line_chart.title = 'Stock Data for IBM: 2024-02-01 to 2024-02-24'
line_chart.x_labels = map(str, dates)
line_chart.add('Open', open)
line_chart.add('High', high)
line_chart.add('Low', low)
line_chart.add('Close', close)
line_chart.render_to_file('chart.svg')

if platform.system() == "Windows":
    browser = webbrowser.get('windows-default')
    browser.open('chart.svg')
elif platform.system() == "macOS":
    browser = webbrowser.get('macosx')
    browser.open('chart.svg')
else:
    browser = webbrowser.get('firefox')
    browser.open('chart.svg')