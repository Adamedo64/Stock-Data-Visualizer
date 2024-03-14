


def main():
    #Title Screen
    print("---------------------")
    print("Stock Data Visualizer")
    print("---------------------\n")
    #Ask the user to enter the stock symbol
    Stock_Symbol = input("Enter The Stock Symbol You Are Looking For (ex: GOOGL): ")
    #Chart Type Screen
    print("\n-----------")
    print("Chart Types")
    print("-----------")
    print("1. Bar")
    print("2. Line\n")
    #Ask the User to enter the chart type
    Chart_Type = int(input("Enter The Chart type (1 or 2): "))
    #Time Series Screen
    print("\n--------------------------------------------------------")
    print("Select the Time Series of the Chart you want to Generate")
    print("--------------------------------------------------------")
    print("1. Intraday")
    print("2. Daily")
    print("3. Weekly")
    print("4. Monthly\n")
    #Ask the user to enter time series
    Series_Type = int(input("Enter Time Series Option(1, 2, 3, or 4): "))
    #Ask the user to enter start date
    Start_Date = input("\nEnter the start date (YYYY-MM-DD): ")
    #Ask the user to enter end date
    End_Date = input("\nEnter the end date (YYYY-MM-DD): ")
    #Ask the user if they would like more stock data
    Continue_Stock = input("Would you like to view more stock data? Press 'y' to continue: ")
    
main()


