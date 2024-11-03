import matplotlib.pyplot as plt
import numpy as np

# Data lists for CPU usage across different thread counts for Pattern 1 and Pattern 2
threads = [1, 2, 4, 8, 16]  

# Pattern 1
cpu_usage_method_a_ac_informed_pattern1 = [99,135,158,189,227]  
cpu_usage_method_a_ac_full_pattern1 = [97,132,224,60,63]      # Method A AC-Full for Pattern 1
cpu_usage_method_b_ac_informed_pattern1 = [99,99,99,101,101]  
cpu_usage_method_b_ac_full_pattern1 = [98,98,100,102,104]      # Method B AC-Full for Pattern 1

# Pattern 2
cpu_usage_method_a_ac_informed_pattern2 = [99,180,354,519,856]  
cpu_usage_method_a_ac_full_pattern2 = [98,150,232,395,454]      # Method A AC-Full for Pattern 2
cpu_usage_method_b_ac_informed_pattern2 = [98,99,99,99,102]  
cpu_usage_method_b_ac_full_pattern2 = [99,98,100,102,104]      # Method B AC-Full for Pattern 2

# Set up the width for each bar in the chart
bar_width = 0.2
bar_positions = np.arange(len(threads))

# Plotting CPU Usage for Pattern 1
fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(bar_positions - bar_width*1.5, cpu_usage_method_a_ac_informed_pattern1, bar_width, label='Method A AC-Informed (Pattern 1)')
ax.bar(bar_positions - bar_width*0.5, cpu_usage_method_a_ac_full_pattern1, bar_width, label='Method A AC-Full (Pattern 1)')
ax.bar(bar_positions + bar_width*0.5, cpu_usage_method_b_ac_informed_pattern1, bar_width, label='Method B AC-Informed (Pattern 1)')
ax.bar(bar_positions + bar_width*1.5, cpu_usage_method_b_ac_full_pattern1, bar_width, label='Method B AC-Full (Pattern 1)')
ax.set_xlabel('Thread Count')
ax.set_ylabel('CPU Usage (%)')
ax.set_title('CPU Usage for Aho-Corasick Implementations (1GB Dataset + Pattern 1)')
ax.set_xticks(bar_positions)
ax.set_xticklabels(threads)
ax.legend()
plt.tight_layout()
plt.savefig("CPU AC pattern1.png")
plt.show()

# Plotting CPU Usage for Pattern 2
fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(bar_positions - bar_width*1.5, cpu_usage_method_a_ac_informed_pattern2, bar_width, label='Method A AC-Informed (Pattern 2)')
ax.bar(bar_positions - bar_width*0.5, cpu_usage_method_a_ac_full_pattern2, bar_width, label='Method A AC-Full (Pattern 2)')
ax.bar(bar_positions + bar_width*0.5, cpu_usage_method_b_ac_informed_pattern2, bar_width, label='Method B AC-Informed (Pattern 2)')
ax.bar(bar_positions + bar_width*1.5, cpu_usage_method_b_ac_full_pattern2, bar_width, label='Method B AC-Full (Pattern 2)')
ax.set_xlabel('Thread Count')
ax.set_ylabel('CPU Usage (%)')
ax.set_title('CPU Usage for Aho-Corasick Implementations (1GB Dataset + Pattern 2)')
ax.set_xticks(bar_positions)
ax.set_xticklabels(threads)
ax.legend()
plt.tight_layout()
plt.savefig("CPU AC pattern2.png")
plt.show()
