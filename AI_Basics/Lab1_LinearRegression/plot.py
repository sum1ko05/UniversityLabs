import matplotlib.pyplot as plt
import matplotlib.patches as patches
from extracted_table import Table, LineFunction
import regression

# Reading data from table
table = Table("student_scores.csv")
stats = table.get_stats()

# Calculating linear approximation
func = regression.approximate_function(table)

# Init plot
fig, ax = plt.subplots()

ax.set_xlabel(table.title[0])
ax.set_ylabel(table.title[1])

# Make shaded squared at bottom layer
stretch = (stats[table.title[0]][0])/(stats[table.title[1]][0])
for i in range(len(table.points)):
    square = patches.Patch()
    error = abs(func.y[i] - table.y[i])
    
    if func.y[i] < table.y[i]:
        square = patches.Rectangle(xy=(func.x[i]-error*stretch, func.y[i]),
                                   width=error*stretch, height=error,
                                   linewidth=1, edgecolor='g', facecolor='y')
    else:
        square = patches.Rectangle(xy=(func.x[i], func.y[i]-error),
                                   width=error*stretch, height=error,
                                   linewidth=1, edgecolor='g', facecolor='y')
    
    ax.add_patch(square)

# Displaying stats
rect = patches.Rectangle(xy=(stats[table.title[0]][1], stats[table.title[1]][1]),
                         width=stats[table.title[0]][0] - stats[table.title[0]][1],
                         height=stats[table.title[1]][0] - stats[table.title[1]][1],
                         linewidth=1, edgecolor='r', facecolor='none')
mid_x = patches.Rectangle(xy=(stats[table.title[0]][2], stats[table.title[1]][1]),
                          width=0, height=stats[table.title[1]][0] - stats[table.title[1]][1],
                          linewidth=1, edgecolor='r', facecolor='none')
mid_y = patches.Rectangle(xy=(stats[table.title[0]][1], stats[table.title[1]][2]),
                          width=stats[table.title[0]][0] - stats[table.title[0]][1], height=0,
                          linewidth=1, edgecolor='r', facecolor='none')
ax.add_patch(rect)
ax.add_patch(mid_x)
ax.add_patch(mid_y)

# Displaying points separately
ax.scatter(table.x, table.y)

# Displaying calculated function
ax.plot(func.x, func.y, color='g', linewidth=2)

# Show
plt.show()
