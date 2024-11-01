import matplotlib.pyplot as plt

# Data for the plots
data_sizes = ['1MB', '100MB', '1GB']
method_a_times = [0.03, 3.28, 26.29]
method_b_times = [0.03, 3.31, 26.68]
cpu_usage_a = [91, 99, 99]
cpu_usage_b = [90, 98, 99]

# Plot 1: Wall Clock Time vs Data Size
plt.figure(figsize=(10, 6))
plt.plot(data_sizes, method_a_times, marker='o', label='Method A')
plt.plot(data_sizes, method_b_times, marker='o', label='Method B')
plt.title('Wall Clock Time vs Data Size')
plt.xlabel('Data Size')
plt.ylabel('Wall Clock Time (s)')
plt.legend()
plt.grid(True)
plt.savefig("WCT vs DS.png")

# Plot 2: CPU Usage % vs Data Size
plt.figure(figsize=(10, 6))
plt.bar([x + ' A' for x in data_sizes], cpu_usage_a, label='Method A', width=0.4, align='center')
plt.bar([x + ' B' for x in data_sizes], cpu_usage_b, label='Method B', width=0.4, align='edge')
plt.title('CPU Usage % vs Data Size')
plt.xlabel('Data Size')
plt.ylabel('CPU Usage (%)')
plt.legend()
plt.grid(True)
plt.savefig("CPU vs DS.png")
