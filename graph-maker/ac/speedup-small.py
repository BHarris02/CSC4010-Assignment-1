import matplotlib.pyplot as plt

# Thread counts
threads = [1, 2, 4, 8, 16]
# Replace these lists with actual calculated Speedup values for Method A and Method B
# Speedup values for Method A with ac-Informed and ac-Full on the 1MB dataset
speedup_a_ac_informed = [100, 144.4444444, 13000, 130, 433.3333333]  
speedup_a_ac_full = [100, 150, 20, 21.42857143, 23.07692308]  
speedup_a_ac_informed_pattern2 = [100, 66.66666667, 4000, 33.33333333, 133.3333333]  
speedup_a_ac_full_pattern2 = [100, 200, 25, 14.28571429, 16.66666667]     

# Speedup values for Method B with ac-Informed and ac-Full on the 1MB dataset
speedup_b_ac_informed = [100, 100, 700, 77.77777778, 175]  
speedup_b_ac_full = [100, 10, 2.5, 1, 1.428571429] 
speedup_b_ac_informed_pattern2 = [100, 60, 300, 42.85714286, 100] 
speedup_b_ac_full_pattern2 = [100, 10, 1.666666667, 1.666666667, 1.666666667]   

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
