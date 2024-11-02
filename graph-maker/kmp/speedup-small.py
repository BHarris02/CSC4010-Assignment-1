import matplotlib.pyplot as plt

# Thread counts
threads = [1, 2, 4, 8, 16]

# Replace these lists with actual calculated Speedup values for Method A and Method B
# Speedup values for Method A with KMP-Informed and KMP-Full on the 1MB dataset
speedup_a_kmp_informed = [1, 1, 1, 1, 0.75]  
speedup_a_kmp_full = [1, 3, 3, 1.5, 0.33]  
speedup_a_kmp_informed_pattern2 = [1,1,1,1,1]  
speedup_a_kmp_full_pattern2 = [1,2,2,0.5,0.29]      

# Speedup values for Method B with KMP-Informed and KMP-Full on the 1MB dataset
speedup_b_kmp_informed = [1, 0.83, 1.67, 1.25, 0.63]  
speedup_b_kmp_full = [1,1.33,1.6,2.0,1.33]   
speedup_b_kmp_informed_pattern2 = [1, 1.5, 1.13, 3, 1.8]  
speedup_b_kmp_full_pattern2 = [1,1.5,3,2,1.5]    

# Plot for Method A
plt.figure(figsize=(10, 6))
plt.plot(threads, speedup_a_kmp_informed, marker='o', label="Method A KMP-Informed Pattern 1")
plt.plot(threads, speedup_a_kmp_full, marker='o', label="Method A KMP-Full Pattern 1")
plt.plot(threads, speedup_a_kmp_informed_pattern2, marker='o', label="Method A KMP-Informed Pattern 2")
plt.plot(threads, speedup_a_kmp_full_pattern2, marker='o', label="Method A KMP-Full Pattern 2")
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
plt.plot(threads, speedup_b_kmp_informed, marker='o', label="Method B KMP-Informed Pattern 1")
plt.plot(threads, speedup_b_kmp_full, marker='o', label="Method B KMP-Full Pattern 1")
plt.plot(threads, speedup_b_kmp_informed_pattern2, marker='o', label="Method B KMP-Informed Pattern 2")
plt.plot(threads, speedup_b_kmp_full_pattern2, marker='o', label="Method B KMP-Full Pattern 2")
plt.xlabel("Number of Threads")
plt.ylabel("Speedup")
plt.xticks(threads)
plt.title("Speedup for Method B on 1MB Dataset")
plt.legend()
plt.grid(True)
plt.savefig("speedup_method_b_1mb.png")
plt.show()
