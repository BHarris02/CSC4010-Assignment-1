import matplotlib.pyplot as plt

# Thread counts
threads = [1, 2, 4, 8, 16]

speedup_a_ac_informed_pattern1 = [100, 166.6666667, 300, 277.7777778, 441.1764706] 
speedup_a_ac_full_pattern1 = [100, 221.7105263, 330.3921569, 432.0512821, 571.1864407] 
speedup_a_ac_informed_pattern2 = [100, 178.7234043, 365.2173913, 280, 494.1176471] 
speedup_a_ac_full_pattern2 = [100, 164.9122807, 206.5934066, 324.137931, 318.6440678]       

speedup_b_ac_informed_pattern1 = [100, 100, 111.3924051, 87.12871287, 115.7894737] 
speedup_b_ac_full_pattern1 = [100, 86.48648649, 71.11111111, 74.41860465, 88.88888889]  
speedup_b_ac_informed_pattern2 = [100, 97.89473684, 112.0481928, 94.89795918, 114.8148148] 
speedup_b_ac_full_pattern2 = [100, 79.76190476, 74.44444444, 75.28089888, 87.01298701]      

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