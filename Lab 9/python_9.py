# -*- coding: utf-8 -*-
"""Python-9.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1deUPtGX1dB4fq8BAjg5d-RZcyDe7k_vf
"""

import matplotlib.pyplot as plt

# Example data (time values in seconds)
items = [5, 10, 15, 20]
time_backtracking = [0.005, 0.015, 0.025, 0.045]
time_branch_bound = [0.002, 0.005, 0.010, 0.020]
time_dynamic = [0.001, 0.003, 0.008, 0.015]

# Plotting
plt.plot(items, time_backtracking, label='Backtracking', marker='o')
plt.plot(items, time_branch_bound, label='Branch & Bound', marker='o')
plt.plot(items, time_dynamic, label='Dynamic Programming', marker='o')

# Labels and title
plt.xlabel('Number of Items')
plt.ylabel('Execution Time (seconds)')
plt.title('Performance Comparison of 0/1 Knapsack Approaches')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()