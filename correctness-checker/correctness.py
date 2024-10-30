def are_files_identical(file1, file2):
    # Read and store each line in a set to ignore order and duplicates
    with open(file1, 'r') as f1:
        lines1 = set(line.strip() for line in f1 if line.strip())

    with open(file2, 'r') as f2:
        lines2 = set(line.strip() for line in f2 if line.strip())

    # Compare the sets to determine if the files are identical
    return lines1 == lines2

# Example usage:
file1 = 'method-a-seq.txt'
file2 = 'method-a-par.txt'

if are_files_identical(file1, file2):
    print("The files have the same content.\n")
else:
    print("The files do not have the same content.\n")

