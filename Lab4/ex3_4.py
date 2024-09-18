#3.4 edit list
respones = [5,7,3,8]

respones.append(0)
#respones.insert(2,6)
respones = respones[0:6] + [6] + respones[2:]
respones.sort()
respones.remove(0)
print(respones)
