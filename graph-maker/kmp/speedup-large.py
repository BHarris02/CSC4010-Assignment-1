import matplotlib.pyplot as plt

# Thread counts
threads = [1, 2, 4, 8, 16]

speedup_a_kmp_informed_pattern1 = [1,1.38,1.19,1.08,1.20]  
speedup_a_kmp_full_pattern1 = [1,1.85,3.12,3.25,2.66] 
speedup_a_kmp_informed_pattern2 = [1,1,1.05,1.03,1.09]  
speedup_a_kmp_full_pattern2 = [1,1.69,3.05,4.04,5.55]       

speedup_b_kmp_informed_pattern1 = [1,1.92,3.04,2.23,2.81]  
speedup_b_kmp_full_pattern1 = [1,1.97,2.35,3.92,8.37]   
speedup_b_kmp_informed_pattern2 = [1,1.67,1.75,4.61,6.07]  
speedup_b_kmp_full_pattern2 = [1,1.69,1.92,3.17,6.47]      

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