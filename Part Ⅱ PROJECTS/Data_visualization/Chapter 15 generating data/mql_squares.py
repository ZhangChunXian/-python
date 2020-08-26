# P346 
import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
#%%
fix, ax = plt.subplots()
# 1
ax.plot(squares, lineWidth=3)

# Set chart title and label axes
# 2
ax.set_title("Square Numbers", fontsize=24)
# 3
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
# 4
ax.tick_params(axis='both', labelsize=14)

plt.show()
# %%
