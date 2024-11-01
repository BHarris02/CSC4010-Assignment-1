import matplotlib.pyplot as plt

# Thread counts
threads = [1, 2, 4, 8, 16]

speedup_a_kmp_informed_pattern1 = [0.94, 1, 1.1, 1.28, 0.74]  
speedup_a_kmp_full_pattern1 = [0.65, 0.67, 2.14, 3.25, 4.15] 
speedup_a_kmp_informed_pattern2 = [0.91, 1, 1.03, 1.03, 0.96]  
speedup_a_kmp_full_pattern2 = [0.65, 0.88, 1.56, 3.67, 3.13]       

speedup_b_kmp_informed_pattern1 = [0.96, 1.98, 3.38, 3.09, 5.17]  
speedup_b_kmp_full_pattern1 = [0.69, 0.98, 2.11, 3.56, 6.02]   
speedup_b_kmp_informed_pattern2 = [0.9, 1.8, 3.28, 4.03, 4.79]  
speedup_b_kmp_full_pattern2 = [0.68, 1.14, 1.75, 3.59, 3.33]      

# Plot for Method A
plt.figure(figsize=(10, 6))
plt.plot(threads, speedup_a_kmp_informed_pattern1, marker='o', label="Method A KMP-Informed Pattern 1")
plt.plot(threads, speedup_a_kmp_full_pattern1, marker='o', label="Method A KMP-Full Pattern 1")
plt.plot(threads, speedup_a_kmp_informed_pattern2, marker='o', label="Method A KMP-Informed Pattern 2")
plt.plot(threads, speedup_a_kmp_full_pattern2, marker='o', label="Method A KMP-Full Pattern 2")
plt.xlabel("Number of Threads")
plt.ylabel("Speedup")
plt.xticks(threads)
plt.title("Speedup for Method A on 100MB Dataset")
plt.legend()
plt.grid(True)
plt.savefig("speedup_method_a_100mb.png")
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
plt.title("Speedup for Method B on 100MB Dataset")
plt.legend()
plt.grid(True)
plt.savefig("speedup_method_b_100mb.png")
plt.show()