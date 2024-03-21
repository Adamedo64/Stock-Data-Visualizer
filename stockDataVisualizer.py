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

#defining lists to store data once the dates are filtered and sorted
dataInRange = []
dataSorted = []

#moves all data entries that fall within the date range provided by user
for x in data["Time Series (Daily)"]: #i think this will need to be changed for each model, just the (Daily) part
    year, month, day = x.split('-')    
    if int(year) == 2024 and int(month) == 2 and int(day) >= 1 and int(day) <= 24: #this will need to be updated to pass the user entered values
        open = data["Time Series (Daily)"][x]['1. open']
        high = data["Time Series (Daily)"][x]['2. high']
        low = data["Time Series (Daily)"][x]['3. low']
        close = data["Time Series (Daily)"][x]['4. close']
        dataInRange.append([x, open, high, low, close])

#by default stock data is in reverse (most recent date first, earliest date last), this function goes through and puts all the stock data in chronological order
dataLength = len(dataInRange)
for x in range(dataLength):
    dataSorted.append(dataInRange[dataLength - x - 1])

#defining lists for the graph values to be stored in
dates = []
open = []
high = []
low = []
close = []

#assigning values to the lists
for x in dataSorted:
    dates.append(x[0])
    open.append(float(x[1]))
    high.append(float(x[2]))
    low.append(float(x[3]))
    close.append(float(x[4]))

#making the graph
line_chart = pygal.Line()
line_chart.title = 'Stock Data for IBM: 2024-02-01 to 2024-02-24' #graph title
line_chart.x_labels = map(str, dates) #x axis
line_chart.add('Open', open) #open line
line_chart.add('High', high) #high line
line_chart.add('Low', low) #low line
line_chart.add('Close', close) #close line
line_chart.render_to_file('chart.svg') #rendering chart to file

if platform.system() == "Windows": #if user is using Windows it will choose this
    browser = webbrowser.get('windows-default') #default windows browser
    browser.open('chart.svg') #opening file in browser
elif platform.system() == "macOS": #if user is using macOS it will choose this
    browser = webbrowser.get('macosx') #default macOS browser
    browser.open('chart.svg')
else: #couldnt find one for a default linux, but i assume most linux users use firefox lol
    browser = webbrowser.get('firefox') #firefox lol
    browser.open('chart.svg')