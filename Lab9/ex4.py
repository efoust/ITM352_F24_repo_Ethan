#read from the survey_1000.csv file and calculate 
#the average, max, min values for the REAL INC Field 
# if values are greater than 0
#report the number of non-zero values. 

import csv

lin_number = 0
total_trip_miles = 0
num_trip_miles = 0
max_trip_miles = 0
total_trip_fare = 0
trip_fares = 0
num_fares = 0

with open("/Users/user/Downloads/taxi_1000.csv", "r") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter = ",")
        for line in csv_reader:
            if( lin_number > 0):
                fare_test = float(line[10])
                if(fare_test > 10 ): 
                 trip_fares = float(line[10])
                 total_trip_fare = total_trip_fare + trip_fares
                 num_fares += 1
                 trip_miles = float(line[5])
                 total_trip_miles += trip_miles
                 num_trip_miles += 1
                 

            
                 if(trip_miles > max_trip_miles):
                    max_trip_miles = trip_miles
            lin_number +=1 
        
        if num_fares > 0:
            avg_fares = total_trip_fare / num_fares
            print(f" Total Fares: ${round(total_trip_fare,2)}")
            print(f" Average Cost: ${round(avg_fares,2)} ")
            print(f" The longest trip was: {max_trip_miles} miles")
        else:
            print(f" Total Fares: ${round(total_trip_fare,2)} ")
