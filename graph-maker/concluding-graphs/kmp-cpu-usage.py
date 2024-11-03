import matplotlib.pyplot as plt
import numpy as np

# Data lists for CPU usage kmpross different thread counts for Pattern 1 and Pattern 2
threads = [1, 2, 4, 8, 16]  

# Pattern 1
cpu_usage_method_a_kmp_informed_pattern1 = [70,99,77,74,76,]  
cpu_usage_method_a_kmp_full_pattern1 = [99,195,315,269,301]      
cpu_usage_method_b_kmp_informed_pattern1 = [99,178,317,332,255]  
cpu_usage_method_b_kmp_full_pattern1 = [99,195,233,448,739]      

# Pattern 2
cpu_usage_method_a_kmp_informed_pattern2 = [99,99,99,99,99]  
cpu_usage_method_a_kmp_full_pattern2 = [99,169,177,562,553]      
cpu_usage_method_b_kmp_informed_pattern2 = [99,178,325,418,560]  
cpu_usage_method_b_kmp_full_pattern2 = [99,173,193,373,600]      

# Set up the width for ekmph bar in the chart
bar_width = 0.2
bar_positions = np.arange(len(threads))

# Plotting CPU Usage for Pattern 1
fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(bar_positions - bar_width*1.5, cpu_usage_method_a_kmp_informed_pattern1, bar_width, label='Method A KMP-Informed (Pattern 1)')
ax.bar(bar_positions - bar_width*0.5, cpu_usage_method_a_kmp_full_pattern1, bar_width, label='Method A kmp-Full (Pattern 1)')
ax.bar(bar_positions + bar_width*0.5, cpu_usage_method_b_kmp_informed_pattern1, bar_width, label='Method B KMP-Informed (Pattern 1)')
ax.bar(bar_positions + bar_width*1.5, cpu_usage_method_b_kmp_full_pattern1, bar_width, label='Method B kmp-Full (Pattern 1)')
ax.set_xlabel('Thread Count')
ax.set_ylabel('CPU Usage (%)')
ax.set_title('CPU Usage for KMP Implementations (1GB Dataset + Pattern 1)')
ax.set_xticks(bar_positions)
ax.set_xticklabels(threads)
ax.legend()
plt.tight_layout()
plt.savefig("CPU kmp pattern1.png")
plt.show()

# Plotting CPU Usage for Pattern 2
fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(bar_positions - bar_width*1.5, cpu_usage_method_a_kmp_informed_pattern2, bar_width, label='Method A KMP-Informed (Pattern 2)')
ax.bar(bar_positions - bar_width*0.5, cpu_usage_method_a_kmp_full_pattern2, bar_width, label='Method A kmp-Full (Pattern 2)')
ax.bar(bar_positions + bar_width*0.5, cpu_usage_method_b_kmp_informed_pattern2, bar_width, label='Method B KMP-Informed (Pattern 2)')
ax.bar(bar_positions + bar_width*1.5, cpu_usage_method_b_kmp_full_pattern2, bar_width, label='Method B kmp-Full (Pattern 2)')
ax.set_xlabel('Thread Count')
ax.set_ylabel('CPU Usage (%)')
ax.set_title('CPU Usage for KMP Implementations (1GB Dataset + Pattern 2)')
ax.set_xticks(bar_positions)
ax.set_xticklabels(threads)
ax.legend()
plt.tight_layout()
plt.savefig("CPU kmp pattern2.png")
plt.show()
