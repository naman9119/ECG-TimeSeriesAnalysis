import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data
data = pd.read_csv('100.csv')

m = data.shape[0]
n = data.shape[1]
print('Number of rows: ', m)
print('Number of columns: ', n)

# Plot the data
columns = data.columns
print(columns)

mean1 = np.mean(data[columns[1]])
mean2 = np.mean(data[columns[2]])

var1 = np.var(data[columns[1]])
var2 = np.var(data[columns[2]])

std1 = np.std(data[columns[1]])
std2 = np.std(data[columns[2]])

print('Mean: ', mean1)
print('Variance: ', var1)
print('Standard deviation: ', std1)

print('Mean: ', mean2)
print('Variance: ', var2)
print('Standard deviation: ', std2)

for i in range(1, n):
    plt.plot(data[columns[0]], data[columns[i]], label=columns[i])
plt.legend()

# plt.figure()
plt.plot(data[columns[0]], data[columns[1]], label=columns[1])
plt.axhline(y=mean1, color='r', linestyle='-', label='Mean')
plt.legend()

# plt.figure()
plt.plot(data[columns[0]], data[columns[2]], label=columns[2])
plt.axhline(y=mean2, color='r', linestyle='-', label='Mean')
plt.legend()

subset_data = data[columns[1]].loc[0:1000]
plt.figure()
plt.plot(subset_data, label=columns[1])
plt.show()