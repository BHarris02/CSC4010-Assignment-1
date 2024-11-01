import matplotlib.pyplot as plt

# Thread counts
threads = [1, 2, 4, 8, 16]

# Replace these lists with actual calculated Speedup values for Method A and Method B
# Speedup values for Method A with KMP-Informed and KMP-Full on the 1MB dataset
speedup_a_kmp_informed = [1, 1, 1, 1, 0.75]  
speedup_a_kmp_full = [0.6, 0.5, 1, 0.75, 0.375]  
speedup_a_kmp_informed_pattern2 = [1,1,1,1,1]  
speedup_a_kmp_full_pattern2 = [0.22,0.33,0.25,0.67,0.4]      

# Speedup values for Method B with KMP-Informed and KMP-Full on the 1MB dataset
speedup_b_kmp_informed = [1, 3, 3, 1.5, 0.3]  
speedup_b_kmp_full = [0.375, 0.5, 0.6, 0.75, 0.5]   
speedup_b_kmp_informed_pattern2 = [1,2,2,0.5,0.28]  
speedup_b_kmp_full_pattern2 = [0.33,0.5,1,0.67,0.5]    

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
