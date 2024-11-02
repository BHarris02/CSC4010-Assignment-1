import matplotlib.pyplot as plt

# Thread counts
threads = [1, 2, 4, 8, 16]

speedup_a_ac_informed_pattern1 = [0.04, 0.07, 0.12, 0.11, 0.18]  
speedup_a_ac_full_pattern1 = [0.01, 0.02, 0.03, 0.04, 0.05] 
speedup_a_ac_informed_pattern2 = [0.04, 0.06, 0.13, 0.1, 0.18]  
speedup_a_ac_full_pattern2 = [0.02, 0.03, 0.03, 0.05, 0.05]       

speedup_b_ac_informed_pattern1 = [0.03, 0.03, 0.04, 0.03, 0.04]  
speedup_b_ac_full_pattern1 = [0.05, 0.04, 0.03, 0.03, 0.04]   
speedup_b_ac_informed_pattern2 = [0.03, 0.03, 0.04, 0.03, 0.04]  
speedup_b_ac_full_pattern2 = [0.04, 0.03, 0.03, 0.03, 0.04]      

# Plot for Method A
plt.figure(figsize=(10, 6))
plt.plot(threads, speedup_a_ac_informed_pattern1, marker='o', label="Method A ac-Informed Pattern 1")
plt.plot(threads, speedup_a_ac_full_pattern1, marker='o', label="Method A ac-Full Pattern 1")
plt.plot(threads, speedup_a_ac_informed_pattern2, marker='o', label="Method A ac-Informed Pattern 2")
plt.plot(threads, speedup_a_ac_full_pattern2, marker='o', label="Method A ac-Full Pattern 2")
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
plt.plot(threads, speedup_b_ac_informed_pattern1, marker='o', label="Method B ac-Informed Pattern 1")
plt.plot(threads, speedup_b_ac_full_pattern1, marker='o', label="Method B ac-Full Pattern 1")
plt.plot(threads, speedup_b_ac_informed_pattern2, marker='o', label="Method B ac-Informed Pattern 2")
plt.plot(threads, speedup_b_ac_full_pattern2, marker='o', label="Method B ac-Full Pattern 2")
plt.xlabel("Number of Threads")
plt.ylabel("Speedup")
plt.xticks(threads)
plt.title("Speedup for Method B on 100MB Dataset")
plt.legend()
plt.grid(True)
plt.savefig("speedup_method_b_100mb.png")
plt.show()