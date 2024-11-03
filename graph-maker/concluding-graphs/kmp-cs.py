import matplotlib.pyplot as plt

# Pattern 1
voluntary_switches_a_kmp_informed_pattern1 = [26541,155,27790,26337,27760]
involuntary_switches_a_kmp_informed_pattern1 = [88,45,36,38,35]

voluntary_switches_a_kmp_full_pattern1 = [135,33,33,41592,209545]
involuntary_switches_a_kmp_full_pattern1 = [109,151,413,750,130]

voluntary_switches_b_kmp_informed_pattern1 = [26,9,21,30,50]
involuntary_switches_b_kmp_informed_pattern1 = [74,51,266,454,1831]

voluntary_switches_b_kmp_full_pattern1 = [8,29,12,49,52]
involuntary_switches_b_kmp_full_pattern1 = [81,84,1714,980,436]

# Pattern 2
voluntary_switches_a_kmp_informed_pattern2 = [126,130,123,121,15]
involuntary_switches_a_kmp_informed_pattern2 = [73,34,28,37,28]

voluntary_switches_a_kmp_full_pattern2 = [12,108,14,19635,2803]
involuntary_switches_a_kmp_full_pattern2 = [79,117,1238,260,62]

voluntary_switches_b_kmp_informed_pattern2 = [6,9,12,23,290]
involuntary_switches_b_kmp_informed_pattern2 = [38,32,170,347,72]

voluntary_switches_b_kmp_full_pattern2 = [6,7,12,130,36]
involuntary_switches_b_kmp_full_pattern2 = [59,61,1050,953,63]

# X-axis labels for thread counts
thread_counts = [1, 2, 4, 8, 16]

# Method A, Pattern 1
fig, ax = plt.subplots(figsize=(10, 6))
ax.stackplot(thread_counts, 
             voluntary_switches_a_kmp_informed_pattern1, involuntary_switches_a_kmp_informed_pattern1,
             voluntary_switches_a_kmp_full_pattern1, involuntary_switches_a_kmp_full_pattern1,
             labels=['A Informed Voluntary', 'A Informed Involuntary', 'A Full Voluntary', 'A Full Involuntary'],
             alpha=0.6)
ax.set_title("Context Switches - Method A, Pattern 1")
ax.set_xlabel("Thread Count")
ax.set_ylabel("Context Switches")
ax.legend(loc='upper left')
plt.savefig("Context Switches - Method A, Pattern 1.png")
plt.show()

# Method A, Pattern 2
fig, ax = plt.subplots(figsize=(10, 6))
ax.stackplot(thread_counts, 
             voluntary_switches_a_kmp_informed_pattern2, involuntary_switches_a_kmp_informed_pattern2,
             voluntary_switches_a_kmp_full_pattern2, involuntary_switches_a_kmp_full_pattern2,
             labels=['A Informed Voluntary', 'A Informed Involuntary', 'A Full Voluntary', 'A Full Involuntary'],
             alpha=0.6)
ax.set_title("Context Switches - Method A, Pattern 2")
ax.set_xlabel("Thread Count")
ax.set_ylabel("Context Switches")
ax.legend(loc='upper left')
plt.savefig("Context Switches - Method A, Pattern 2.png")
plt.show()

# Method B, Pattern 1
fig, ax = plt.subplots(figsize=(10, 6))
ax.stackplot(thread_counts, 
             voluntary_switches_b_kmp_informed_pattern1, involuntary_switches_b_kmp_informed_pattern1,
             voluntary_switches_b_kmp_full_pattern1, involuntary_switches_b_kmp_full_pattern1,
             labels=['B Informed Voluntary', 'B Informed Involuntary', 'B Full Voluntary', 'B Full Involuntary'],
             alpha=0.6)
ax.set_title("Context Switches - Method B, Pattern 1")
ax.set_xlabel("Thread Count")
ax.set_ylabel("Context Switches")
ax.legend(loc='upper left')
plt.savefig("Context Switches - Method B, Pattern 1.png")
plt.show()

# Method B, Pattern 2
fig, ax = plt.subplots(figsize=(10, 6))
ax.stackplot(thread_counts, 
             voluntary_switches_b_kmp_informed_pattern2, involuntary_switches_b_kmp_informed_pattern2,
             voluntary_switches_b_kmp_full_pattern2, involuntary_switches_b_kmp_full_pattern2,
             labels=['B Informed Voluntary', 'B Informed Involuntary', 'B Full Voluntary', 'B Full Involuntary'],
             alpha=0.6)
ax.set_title("Context Switches - Method B, Pattern 2")
ax.set_xlabel("Thread Count")
ax.set_ylabel("Context Switches")
ax.legend(loc='upper left')
plt.savefig("Context Switches - Method B, Pattern 2.png")
plt.show()