import matplotlib.pyplot as plt

# Thread counts
threads = [1, 2, 4, 8, 16]
speedup_a_ac_informed_pattern1 = [0.001, 0.001, 0.002, 0.002, 0.002]  
speedup_a_ac_full_pattern1 = [0.004, 0.006, 0.011, 0.003, 0.003] 
speedup_a_ac_informed_pattern2 = [0.001, 0.002, 0.005, 0.008, 0.013]  
speedup_a_ac_full_pattern2 = [0.004, 0.006, 0.011, 0.018, 0.020]       

speedup_b_ac_informed_pattern1 = [0.004, 0.004, 0.004, 0.005, 0.004]  
speedup_b_ac_full_pattern1 = [0.004, 0.004, 0.004, 0.004, 0.004]   
speedup_b_ac_informed_pattern2 = [0.004, 0.004, 0.004, 0.005, 0.004]  
speedup_b_ac_full_pattern2 = [0.004, 0.004, 0.004, 0.004, 0.004]      

# Plot for Method A
plt.figure(figsize=(10, 6))
plt.plot(threads, speedup_a_ac_informed_pattern1, marker='o', label="Method A ac-Informed Pattern 1")
plt.plot(threads, speedup_a_ac_full_pattern1, marker='o', label="Method A ac-Full Pattern 1")
plt.plot(threads, speedup_a_ac_informed_pattern2, marker='o', label="Method A ac-Informed Pattern 2")
plt.plot(threads, speedup_a_ac_full_pattern2, marker='o', label="Method A ac-Full Pattern 2")
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
plt.plot(threads, speedup_b_ac_informed_pattern1, marker='o', label="Method B ac-Informed Pattern 1")
plt.plot(threads, speedup_b_ac_full_pattern1, marker='o', label="Method B ac-Full Pattern 1")
plt.plot(threads, speedup_b_ac_informed_pattern2, marker='o', label="Method B ac-Informed Pattern 2")
plt.plot(threads, speedup_b_ac_full_pattern2, marker='o', label="Method B ac-Full Pattern 2")
plt.xlabel("Number of Threads")
plt.ylabel("Speedup")
plt.xticks(threads)
plt.title("Speedup for Method B on 1GB Dataset")
plt.legend()
plt.grid(True)
plt.savefig("speedup_method_b_1gb.png")
plt.show()