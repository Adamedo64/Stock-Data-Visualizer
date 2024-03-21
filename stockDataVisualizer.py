import datetime;


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
        try:
            end_date_str = input("\nEnter the end date (YYYY-MM-DD): ")
            end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d").date()
            if end_date > start_date:
                break
            else:
                print("The end date must be after the start date.")
        except ValueError:
            print("Please enter the date in the proper format (YYYY-MM-DD).")
    #Ask the user if they would like more stock data
    #Check to make sure value is a y or n
    while True:
        Continue_Stock = input("Would you like to view more stock data? Press 'y' to continue or Press 'n' to exit: ")
        if Continue_Stock.lower() == 'y':
            pass
        elif Continue_Stock.lower() == 'n':
            print("Exiting the program.")
            break
        else:
            print("Invalid input. Please enter 'y' to continue or 'n' to exit.")
   
main()



