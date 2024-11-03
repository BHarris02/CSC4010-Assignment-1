import matplotlib.pyplot as plt

# Pattern 1
voluntary_switches_a_ac_informed_pattern1 = [34,122,30163,31393,32213]
involuntary_switches_a_ac_informed_pattern1 = [153,1208,60,156,476]

voluntary_switches_a_ac_full_pattern1 = [98,849,325,33171,50340]
involuntary_switches_a_ac_full_pattern1 = [198,213,98,7,25]

voluntary_switches_b_ac_informed_pattern1 = [6,9,14,22,160]
involuntary_switches_b_ac_informed_pattern1 = [29,20,8,20,12]

voluntary_switches_b_ac_full_pattern1 = [7,12,19,37,64]
involuntary_switches_b_ac_full_pattern1 = [83,63,13,9,13]

# Pattern 2
voluntary_switches_a_ac_informed_pattern2 = [14,173,293,759,6092]
involuntary_switches_a_ac_informed_pattern2 = [73,233,47,122,61]

voluntary_switches_a_ac_full_pattern2 = [52,749,194,2153,15675]
involuntary_switches_a_ac_full_pattern2 = [90,135,143,11,14]

voluntary_switches_b_ac_informed_pattern2 = [22,9,18,26,48]
involuntary_switches_b_ac_informed_pattern2 = [23,21,29,16,9]

voluntary_switches_b_ac_full_pattern2 = [6,10,19,33,67]
involuntary_switches_b_ac_full_pattern2 = [25,45,7,12,44]

# X-axis labels for thread counts
thread_counts = [1, 2, 4, 8, 16]

# Method A, Pattern 1
fig, ax = plt.subplots(figsize=(10, 6))
ax.stackplot(thread_counts, 
             voluntary_switches_a_ac_informed_pattern1, involuntary_switches_a_ac_informed_pattern1,
             voluntary_switches_a_ac_full_pattern1, involuntary_switches_a_ac_full_pattern1,
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
             voluntary_switches_a_ac_informed_pattern2, involuntary_switches_a_ac_informed_pattern2,
             voluntary_switches_a_ac_full_pattern2, involuntary_switches_a_ac_full_pattern2,
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
             voluntary_switches_b_ac_informed_pattern1, involuntary_switches_b_ac_informed_pattern1,
             voluntary_switches_b_ac_full_pattern1, involuntary_switches_b_ac_full_pattern1,
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
             voluntary_switches_b_ac_informed_pattern2, involuntary_switches_b_ac_informed_pattern2,
             voluntary_switches_b_ac_full_pattern2, involuntary_switches_b_ac_full_pattern2,
             labels=['B Informed Voluntary', 'B Informed Involuntary', 'B Full Voluntary', 'B Full Involuntary'],
             alpha=0.6)
ax.set_title("Context Switches - Method B, Pattern 2")
ax.set_xlabel("Thread Count")
ax.set_ylabel("Context Switches")
ax.legend(loc='upper left')
plt.savefig("Context Switches - Method B, Pattern 2.png")
plt.show()