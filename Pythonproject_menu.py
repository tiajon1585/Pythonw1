#date and time
from datetime import datetime

#print title
print("Tiajon1585's Excel Spreadsheet Automation Menu")

#user options
print("Choose a number from the following options")
print("1. InputData")
print("2. View Current Data")
print("3. Generate Report")

#processes users choice
choice = input()
if choice == "1" or choice == "2" or choice == "3":
  print(f"You selected {choice} at {datetime.now()}")
  

