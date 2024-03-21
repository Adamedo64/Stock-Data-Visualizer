import requests;
import pygal;
import webbrowser;
import datetime;
import platform;

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
    if int(year) == 2020 and int(month) == 8 and int(day) >= 1 and int(day) <= 31: #this will need to be updated to pass the user entered values
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
dates = ['2020-08-03', '2020-08-04', '2020-08-05', '2020-08-06', '2020-08-07', '2020-08-10', '2020-08-11', '2020-08-12', '2020-08-13', '2020-08-14', '2020-08-17', '2020-08-18', '2020-08-19', '2020-08-20', '2020-08-21', '2020-08-24', '2020-08-25', '2020-08-26', '2020-08-27', '2020-08-28', '2020-08-31']
open = [1491.0, 1486.71, 1476.82, 1476.15, 1509.04, 1490.8, 1494.0, 1487.1245, 1508.21, 1513.61, 1515.97, 1526.12, 1552.49, 1539.97, 1571.8, 1592.47, 1580.1, 1606.3, 1646.61, 1629.47, 1643.57]
high = [1497.73, 1493.11, 1490.0, 1506.27, 1520.09, 1507.15, 1510.44, 1511.67, 1536.9744, 1519.785, 1523.78, 1557.37, 1568.86, 1580.17, 1591.88, 1608.78, 1608.88, 1652.79, 1647.99, 1641.35, 1644.5]
low = [1471.72, 1464.03, 1471.215, 1471.9, 1486.27, 1477.4901, 1478.19, 1485.0, 1508.21, 1499.0, 1505.0, 1521.665, 1540.0, 1534.46, 1562.31, 1575.04, 1577.88, 1600.9754, 1618.8137, 1625.605, 1625.33]
close = [1482.76, 1473.3, 1479.09, 1504.95, 1498.37, 1496.82, 1480.54, 1507.24, 1516.65, 1504.63, 1516.24, 1555.78, 1544.61, 1576.25, 1575.57, 1585.15, 1605.85, 1644.13, 1628.52, 1639.43, 1629.53]

#assigning values to the lists
for x in dataSorted:
    dates.append(x[0])
    open.append(float(x[1]))
    high.append(float(x[2]))
    low.append(float(x[3]))
    close.append(float(x[4]))

print(dates)
print(open)
print(high)
print(low)
print(close)

#making the graph
line_chart = pygal.Line()
line_chart.title = 'Stock Data for IBM: 2024-02-01 to 2024-02-24' #graph title
line_chart.x_labels = map(str, dates) #x axis
line_chart.add('Open', open) #open line
line_chart.add('High', high) #high line
line_chart.add('Low', low) #low line
line_chart.add('Close', close) #close line
line_chart.render_to_file('chart.svg') #rendering chart to file

import platform

if platform.system() == "Windows": #if user is using Windows it will choose this
    browser = webbrowser.get('windows-default') #default windows browser
    browser.open('chart.svg') #opening file in browser
elif platform.system() == "macOS": #if user is using macOS it will choose this
    browser = webbrowser.get('macosx') #default macOS browser
    browser.open('chart.svg')
else: #couldnt find one for a default linux, but i assume most linux users use firefox lol
    browser = webbrowser.get('firefox') #firefox lol
    browser.open('chart.svg')

def main():
    #Title Screen
    print("---------------------")
    print("Stock Data Visualizer")
    print("---------------------\n")
    #Ask the user to enter the stock symbol
    #Make sure the user actually enters an input
    while True:
        Stock_Symbol = input("Enter The Stock Symbol You Are Looking For (ex: GOOGL): ")
        if Stock_Symbol.strip():  # Check if the input is not empty after removing leading and trailing whitespaces
            break
        else:
            print("Please enter a valid stock symbol.")
    #Chart Type Screen
    print("\n-----------")
    print("Chart Types")
    print("-----------")
    print("1. Bar")
    print("2. Line\n")
    #Ask the User to enter the chart type
    #Make sure the user enters a 1 or 2
    while True:
        try:
            Chart_Type = int(input("Enter The Chart Type (1 or 2): "))
            if Chart_Type in [1, 2]:
                break
            else:
                print("Please enter either 1 or 2.")
        except ValueError:
            print("Please enter a valid number (1 or 2).")
    #Time Series Screen
    print("\n--------------------------------------------------------")
    print("Select the Time Series of the Chart you want to Generate")
    print("--------------------------------------------------------")
    print("1. Intraday")
    print("2. Daily")
    print("3. Weekly")
    print("4. Monthly\n")
    #Ask the user to enter time series
    #Check to make sure user enters a 1, 2, 3, or 4
    while True:
        try:
            Series_Type = int(input("Enter Time Series Option(1, 2, 3, or 4): "))
            if Series_Type in [1, 2, 3, 4]:
                break
            else:
                print("Please enter either 1, 2, 3, or 4.")
        except ValueError:
            print("Please enter a valid number (1, 2, 3, or 4).")
    #Ask the user to enter start date
    #Check to make sure the date is entered in the proper format
    while True:
        try:
            start_date_str = input("\nEnter the start date (YYYY-MM-DD): ")
            start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Please enter the date in the proper format (YYYY-MM-DD).")
    #Ask the user to enter end date
    #Check to make sure user enters a valid format end date
    while True:
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")

    try:
        start_y, start_m, start_d = start_date.split('-')
        end_y, end_m, end_d = end_date.split('-')

        if (start_y, start_m, start_d) > (end_y, end_m, end_d):
            print("Start date cannot be later than end date. Please try again.")
        else:
            break
    except ValueError:
        print("Invalid date format. Please enter date in YYYY-MM-DD format.")

print("Start date:", start_date)
print("End date:", end_date)
        else:
            print("Invalid input. Please enter 'y' to continue or 'n' to exit.")
   
main()


