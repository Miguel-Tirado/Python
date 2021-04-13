import matplotlib.pyplot as plt 

# x and y values stored inside list
x_values = range(1,1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
#Note that c has y_values to know which values to set the colormap too
ax.scatter(x_values,y_values,c=y_values, cmap=plt.cm.Blues, s=10)

# set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Sqaure of Value", fontsize=14)

# set size of tick labels
ax.tick_params(axis='both', which='major',labelsize=14)
ax.axis([0,1100, 0, 1100000])
# save the output to a file
plt.savefig('sqaures_plot.png', bbox_inches='tight')
#plt.show()