# import packages
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt

number_of_iterations = 50
# loading the csv file
data = pd.read_csv('Book1.csv')

# perform one sample t-test
def get_probability(avg):
    t_statistic, p_value = stats.ttest_1samp(a=data, popmean=avg)
    return p_value[0]

# get all p values
p_values=[]
avg = 0
for i in range(number_of_iterations):
    avg+=2
    p_val = get_probability(avg)
    p_values.append(p_val)


# plot data
print(p_values)
x_vals = [i for i in range(number_of_iterations)]
plt.scatter(x_vals, p_values)
plt.title('Distribution of p-values')
plt.xlabel('Avergae tested')
plt.ylabel('P-value')
plt.show()
