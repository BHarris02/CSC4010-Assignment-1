import matplotlib.pyplot as plt

# Thread counts
threads = [1, 2, 4, 8, 16]

speedup_a_kmp_informed_pattern1 = [1,1.06,1.16,1.35,0.79]  
speedup_a_kmp_full_pattern1 = [1,2.07,3.52,3.22,5.39] 
speedup_a_kmp_informed_pattern2 = [1,1.11,1.14,1.13,1.06]  
speedup_a_kmp_full_pattern2 = [1,1.98,3.63,4.46,5.29]       

speedup_b_kmp_informed_pattern1 = [1,1.03,3.28,4.97,6.35]  
speedup_b_kmp_full_pattern1 = [1,1.42,3.03,5.12,8.65]   
speedup_b_kmp_informed_pattern2 = [1,1.36,2.4,5.66,4.83]  
speedup_b_kmp_full_pattern2 = [1,1.68,2.59,5.30,4.91]      

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