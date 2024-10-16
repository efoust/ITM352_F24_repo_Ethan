import numpy as np

incomes = [
    (10,14629), (20,25600), (30,37002), (40, 50000), (50, 63179), (60, 79542), (70, 100162), (80, 130000), (90, 184292)
]
np_incomes = np.array(incomes)

#report the dimensions of the array and the number of elements in it
print("The dimensions of the household income array: ", np_incomes.ndim)
print("The number of elements in the income array:", np_incomes.size)
for i in range(len(np_incomes)):
    print(np_incomes[i][0], np_incomes[i][1])

