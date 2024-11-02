import matplotlib.pyplot as plt

# Sample data for 1GB dataset (replace these lists with actual values if different)
threads = [1, 2, 4, 8, 16]
method_a_ac_informed_pattern1 = [29.79, 22.58, 17.19, 14.51, 12.31]
method_a_ac_full_pattern1 = [6.52, 5.2, 2.71, 11.33, 11.26]
method_b_ac_informed_pattern1 = [7.52, 7.41, 6.54, 6.5, 6.83]
method_b_ac_full_pattern1 = [7.66, 7.57, 7.05, 6.68, 6.69]

method_a_ac_informed_pattern2 = [22.14, 12.88, 5.45, 3.83, 2.3]
method_a_ac_full_pattern2 = [6.88, 4.94, 2.8, 1.66, 1.51]
method_b_ac_informed_pattern2 = [8.04, 7.89, 6.94, 6.07, 7.14]
method_b_ac_full_pattern2 = [8.04, 7.95, 7.49, 7.05, 7.11]

# Plotting 1GB dataset + Pattern 1
plt.figure(figsize=(10, 6))
plt.plot(threads, method_a_ac_informed_pattern1, 'o-', label="Method A ac-Informed", color="blue")
plt.plot(threads, method_a_ac_full_pattern1, 'o-', label="Method A ac-Full", color="orange")
plt.plot(threads, method_b_ac_informed_pattern1, 'o-', label="Method B ac-Informed", color="green")
plt.plot(threads, method_b_ac_full_pattern1, 'o-', label="Method B ac-Full", color="red")
plt.xticks(threads)
plt.xlabel("Number of Threads")
plt.ylabel("Wall Clock Time (s)")
plt.title("Wall Clock Time for 1GB Dataset + Pattern 1")
plt.legend()
plt.grid(True)
plt.savefig("Wall_Clock_Time_1GB_Dataset_Pattern1.png")
plt.show()

# Plotting 1GB dataset + Pattern 2
plt.figure(figsize=(10, 6))
plt.plot(threads, method_a_ac_informed_pattern2, 'o-', label="Method A ac-Informed", color="blue")
plt.plot(threads, method_a_ac_full_pattern2, 'o-', label="Method A ac-Full", color="orange")
plt.plot(threads, method_b_ac_informed_pattern2, 'o-', label="Method B ac-Informed", color="green")
plt.plot(threads, method_b_ac_full_pattern2, 'o-', label="Method B ac-Full", color="red")
plt.xticks(threads)
plt.xlabel("Number of Threads")
plt.ylabel("Wall Clock Time (s)")
plt.title("Wall Clock Time for 1GB Dataset + Pattern 2")
plt.legend()
plt.grid(True)
plt.savefig("Wall_Clock_Time_1GB_Dataset_Pattern2.png")
plt.show()
