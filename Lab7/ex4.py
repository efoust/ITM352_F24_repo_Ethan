


def fare_Calculation(fares):
    
    for x in fares:
        if (x > 12):
             print(f"This fare {x} is high!")
        else: 
            print(f"This fare {x} is low")
        

fares_data = [8.60, 5.75, 13.25, 21.21] 

fare_Calculation(fares_data)