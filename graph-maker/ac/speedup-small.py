import matplotlib.pyplot as plt

# Thread counts
threads = [1, 2, 4, 8, 16]
# Replace these lists with actual calculated Speedup values for Method A and Method B
# Speedup values for Method A with ac-Informed and ac-Full on the 1MB dataset
speedup_a_ac_informed = [0.23, 0.33, 30, 0.3, 1]  
speedup_a_ac_full = [1, 1.5, 0.2, 0.21, 0.23]  
speedup_a_ac_informed_pattern2 = [0.75, 0.5, 30, 0.25, 1]  
speedup_a_ac_full_pattern2 = [1.5, 3, 0.37, 0.21, 0.25]      

# Speedup values for Method B with ac-Informed and ac-Full on the 1MB dataset
speedup_b_ac_informed = [0.43, 0.43, 3, 0.33, 0.75]  
speedup_b_ac_full = [30, 3, 0.75, 0.3, 0.43]   
speedup_b_ac_informed_pattern2 = [1, 0.6, 3, 0.43, 1]  
speedup_b_ac_full_pattern2 = [30, 3, 0.5, 0.5, 0.5]    

# Plot for Method A
plt.figure(figsize=(10, 6))
plt.plot(threads, speedup_a_ac_informed, marker='o', label="Method A ac-Informed Pattern 1")
plt.plot(threads, speedup_a_ac_full, marker='o', label="Method A ac-Full Pattern 1")
plt.plot(threads, speedup_a_ac_informed_pattern2, marker='o', label="Method A ac-Informed Pattern 2")
plt.plot(threads, speedup_a_ac_full_pattern2, marker='o', label="Method A ac-Full Pattern 2")
plt.xlabel("Number of Threads")
plt.ylabel("Speedup")
plt.xticks(threads)
plt.title("Speedup for Method A on 1MB Dataset")
plt.legend()
plt.grid(True)
plt.savefig("speedup_method_a_1mb.png")
plt.show()

# Plot for Method B
plt.figure(figsize=(10, 6))
plt.plot(threads, speedup_b_ac_informed, marker='o', label="Method B ac-Informed Pattern 1")
plt.plot(threads, speedup_b_ac_full, marker='o', label="Method B ac-Full Pattern 1")
plt.plot(threads, speedup_b_ac_informed_pattern2, marker='o', label="Method B ac-Informed Pattern 2")
plt.plot(threads, speedup_b_ac_full_pattern2, marker='o', label="Method B ac-Full Pattern 2")
plt.xlabel("Number of Threads")
plt.ylabel("Speedup")
plt.xticks(threads)
plt.title("Speedup for Method B on 1MB Dataset")
plt.legend()
plt.grid(True)
plt.savefig("speedup_method_b_1mb.png")
plt.show()
