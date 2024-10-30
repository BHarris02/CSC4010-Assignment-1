# Function to read lines from a file and return them as a set
def read_lines(filename):
    with open(filename, 'r') as file:
        return set(file.readlines())

# Function to find lines in file2 that are not in file1
def find_unique_lines(file1, file2):
    lines1 = read_lines(file1)
    lines2 = read_lines(file2)
    
    # Lines in file2 that are not in file1
    unique_lines = lines2 - lines1
    
    return unique_lines

# Paths to your files
file1 = 'method-a-seq.txt'
file2 = 'method-a-par.txt'

# Get the unique lines
unique_lines = find_unique_lines(file1, file2)

# Output the unique lines
print("Unique lines in the larger file (file2):")
for line in unique_lines:
    print(line.strip())
