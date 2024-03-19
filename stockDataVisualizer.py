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