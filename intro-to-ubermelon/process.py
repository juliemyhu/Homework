log_file = open("um-server-01.txt")  # 


def sales_reports(log_file):   # Function that takes a file of different dates and prints sales reports
    for line in log_file:      
        line = line.rstrip()  #function
        day = line[0:3]       # the day is the first 4 numbers of the line
        if day == "Mon":    # only prints Tues files 
            print(line) 


sales_reports(log_file)
