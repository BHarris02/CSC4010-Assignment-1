import matplotlib.pyplot as plt

# Thread counts
threads = [1, 2, 4, 8, 16]

speedup_a_kmp_informed_pattern1 = [0.61, 0.84, 0.73, 0.66, 0.73]  
speedup_a_kmp_full_pattern1 = [0.6, 1.15, 1.81, 1.33, 1.67] 
speedup_a_kmp_informed_pattern2 = [0.87, 0.87, 0.91, 0.90, 0.95]  
speedup_a_kmp_full_pattern2 = [0.61, 1.03, 1.07, 2.83, 3.73]       

speedup_b_kmp_informed_pattern1 = [0.89, 1.66, 2.8, 2.91, 2.38]  
speedup_b_kmp_full_pattern1 = [0.62, 1.22, 1.46, 2.44, 5.21]   
speedup_b_kmp_informed_pattern2 = [0.88, 1.49, 2.69, 3.55, 4.88]  
speedup_b_kmp_full_pattern2 = [0.63, 1.07, 1.22, 2.01, 4.1]      

# Plot for Method A
plt.figure(figsize=(10, 6))
plt.plot(threads, speedup_a_kmp_informed_pattern1, marker='o', label="Method A KMP-Informed Pattern 1")
plt.plot(threads, speedup_a_kmp_full_pattern1, marker='o', label="Method A KMP-Full Pattern 1")
plt.plot(threads, speedup_a_kmp_informed_pattern2, marker='o', label="Method A KMP-Informed Pattern 2")
plt.plot(threads, speedup_a_kmp_full_pattern2, marker='o', label="Method A KMP-Full Pattern 2")
plt.xlabel("Number of Threads")
plt.ylabel("Speedup")
plt.xticks(threads)
plt.title("Speedup for Method A on 1GB Dataset")
plt.legend()
plt.grid(True)
plt.savefig("speedup_method_a_1gb.png")
plt.show()

# Plot for Method B
plt.figure(figsize=(10, 6))
plt.plot(threads, speedup_b_kmp_informed_pattern1, marker='o', label="Method B KMP-Informed Pattern 1")
plt.plot(threads, speedup_b_kmp_full_pattern1, marker='o', label="Method B KMP-Full Pattern 1")
plt.plot(threads, speedup_b_kmp_informed_pattern2, marker='o', label="Method B KMP-Informed Pattern 2")
plt.plot(threads, speedup_b_kmp_full_pattern2, marker='o', label="Method B KMP-Full Pattern 2")
plt.xlabel("Number of Threads")
plt.ylabel("Speedup")
plt.xticks(threads)
plt.title("Speedup for Method B on 1GB Dataset")
plt.legend()
plt.grid(True)
plt.savefig("speedup_method_b_1gb.png")
plt.show()