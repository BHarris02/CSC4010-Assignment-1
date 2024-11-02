import matplotlib.pyplot as plt

# Sample data for wall clock time (replace these with your actual data)
threads = [1, 2, 4, 8, 16]
wall_clock_time_a_inf_p1 = [0.13, 0.09, 0, 0.1, 0.03]
wall_clock_time_a_full_p1 = [0.03, 0.02, 0.15, 0.14, 0.13]
wall_clock_time_b_inf_p1 = [0.07, 0.07, 0.01, 0.09, 0.04]
wall_clock_time_b_full_p1 = [0, 0.01, 0.04, 0.1, 0.07]

wall_clock_time_a_inf_p2 = [0.04, 0.06, 0, 0.12, 0.03]
wall_clock_time_a_full_p2 = [0.02, 0.01, 0.08, 0.14, 0.12]
wall_clock_time_b_inf_p2 = [0.03, 0.05, 0.01, 0.07, 0.03]
wall_clock_time_b_full_p2 = [0, 0.01, 0.06, 0.06, 0.06]

# Define the thread counts you want to include in the graph
threads = [1, 2, 4, 8, 16]

# Plot for Wall Clock Time (Pattern 1)
plt.figure(figsize=(10, 6))
plt.plot(threads, wall_clock_time_a_inf_p1, marker='o', label="Method A AC-Informed")
plt.plot(threads, wall_clock_time_a_full_p1, marker='o', label="Method A AC-Full")
plt.plot(threads, wall_clock_time_b_inf_p1, marker='o', label="Method B AC-Informed")
plt.plot(threads, wall_clock_time_b_full_p1, marker='o', label="Method B AC-Full")
plt.xlabel("Number of Threads")
plt.ylabel("Wall Clock Time (s)")
plt.xticks(threads)
plt.title("Wall Clock Time for 1MB Dataset + Pattern 1")
plt.legend()
plt.grid(True)
plt.savefig("wall_clock_time_1mb_pattern1.png")
plt.show()

# Plot for Wall Clock Time (Pattern 2)
plt.figure(figsize=(10, 6))
plt.plot(threads, wall_clock_time_a_inf_p2, marker='o', label="Method A AC-Informed")
plt.plot(threads, wall_clock_time_a_full_p2, marker='o', label="Method A AC-Full")
plt.plot(threads, wall_clock_time_b_inf_p2, marker='o', label="Method B AC-Informed")
plt.plot(threads, wall_clock_time_b_full_p2, marker='o', label="Method B AC-Full")
plt.xlabel("Number of Threads")
plt.ylabel("Wall Clock Time (s)")
plt.xticks(threads)
plt.title("Wall Clock Time for 1MB Dataset + Pattern 2")
plt.legend()
plt.grid(True)
plt.savefig("wall_clock_time_1mb_pattern2.png")
plt.show()


