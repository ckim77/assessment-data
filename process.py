log_file = open("um-server-01.txt") #the open code opens the txt file and reads the data into a variable called log_file


def sales_reports(log_file): # def is the boilerplate code needed to code a function in python, sales_reports is the function name and log_file is the parameter
    for line in log_file: # line can be any variable like i, x, or a and this code loops through each line in our txt data file that was saved to log_file
        line = line.rstrip() # rstrip is a method that removes white space, which is a very handy method to clean our data
        day = line[0:3] # the first three strings of the current line in the loop has been saved to a variable called day, which is the weekday
        if day == "Mon": # this is a conditional that is looking for the strings "Tue", and if that is the case it will do something on the next line
            print(line) # if the conditional above is met, we print the current line.  We should have output that is all "Tue" in the beginning


# sales_reports(log_file) # this code calls the function


## Extra Credit ##

def melons(log_file):
    for line in log_file:
        line = line.rstrip()
        if int(line[16:18]) > 10:
            print(line)
        

# melons(log_file)