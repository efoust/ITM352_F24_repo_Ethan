#read from the survey_1000.csv file and calculate 
#the average, max, min values for the REAL INC Field 
# if values are greater than 0
#report the number of non-zero values. 

import csv
import os
filepath = "/Users/user/Downloads/survey_1000.csv"
lin_number = 0
total_RealInc = 0
num_values = 0
max_RealInc = 0
min_RealInc = 99999999999999   #very large number to initialize min income

if os.path.exists(filepath) and os.access(filepath, os.R_OK):
    fileSize = os.path.getsize(filepath)
    filePerms = os.stat(filepath).st_mode
    print(f"File: {filepath}")
    print(f"Size: {fileSize}")
    print(f"permissions: {oct(filePerms)}")
    

with open(filepath, "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ",")

    for line in csv_reader:
        if (lin_number > 0):
            RealInc = float(line[5456])
            if (RealInc > 0):
                num_values += 1
                total_RealInc += RealInc
                if (RealInc > max_RealInc):
                    max_RealInc = RealInc
                if(RealInc < min_RealInc):
                    min_RealInc = RealInc
        lin_number += 1

print(f"The number of non 0 values is {num_values}")
print(f"Average RealInc: ${round(total_RealInc / num_values, 2)}")
print(f"Min RealInc: ${min_RealInc:.2f} Max RealInc: ${round(max_RealInc, 2)}")

