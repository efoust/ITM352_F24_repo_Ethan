count = 0
while count <= 10:
    if count >= 8: 
        count += 1
        print("done")
        break
    elif count == 5: 
        count+=1
        continue
    else:
        print(count)
        count += 1
