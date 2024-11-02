import matplotlib.pyplot as plt

# Thread counts
threads = [1, 2, 4, 8, 16]
speedup_a_ac_informed_pattern1 = [100, 131.9309123, 173.2984293, 205.306685, 241.9983753]  
speedup_a_ac_full_pattern1 = [100, 125.3846154, 240.5904059, 57.54633716, 57.90408526] 
speedup_a_ac_informed_pattern2 = [100, 171.8944099, 406.2385321, 578.0678851, 962.6086957]  
speedup_a_ac_full_pattern2 = [100, 139.2712551, 245.7142857, 414.4578313, 455.6291391]       

speedup_b_ac_informed_pattern1 = [100, 101.4844804, 114.9847095, 115.6923077, 110.102489] 
speedup_b_ac_full_pattern1 = [100, 101.1889036, 108.6524823, 114.6706587, 114.4992526]  
speedup_b_ac_informed_pattern2 = [100, 101.9011407, 115.8501441, 132.4546952, 112.605042]  
speedup_b_ac_full_pattern2 = [100, 101.1320755, 107.3431242, 114.0425532, 113.0801688]     

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