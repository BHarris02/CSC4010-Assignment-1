#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "search.h" // include the search library

// Function to compute the LPS array for KMP
void computeLPSArray(char* pat, int m, int* lps) {
    int len = 0; // length of the previous longest prefix suffix
    lps[0] = 0;  // lps[0] is always 0
    int i = 1;

    // Build the LPS array
    while (i < m) {
        if (pat[i] == pat[len]) {
            len++;
            lps[i] = len;
            i++;
        } else {
            if (len != 0) {
                len = lps[len - 1];
            } else {
                lps[i] = 0;
                i++;
            }
        }
    }
}

// Function to perform KMP search for the first match of `pat` within `txt`
int KMPSearchFirstMatch(char* pat, char* txt) {
    int m = strlen(pat);
    int n = strlen(txt);

    // Create the LPS array for the pattern
    int* lps = (int*)malloc(m * sizeof(int));
    computeLPSArray(pat, m, lps);

    int i = 0; // index for txt
    int j = 0; // index for pat

    while (i < n) {
        if (pat[j] == txt[i]) {
            j++;
            i++;
        }

        // If full match found, return start index
        if (j == m) {
            free(lps);
            return i - j;
        }

        // Mismatch after j matches
        else if (i < n && pat[j] != txt[i]) {
            if (j != 0) {
                j = lps[j - 1];
            } else {
                i++;
            }
        }
    }

    free(lps);
    return -1; // No match found
}

int main(int ac, char** av) {
    if (ac < 3) {
        FatalError("Usage: command sourcefile.txt patternfile.txt");
    }

    char* sourcefile = av[1];
    char* patternfile = av[2];

    // Load the source data into chunks of SOURCE_LINE_SIZE
    struct FileData fd;
    readSourceFile(sourcefile, &fd, FILE_LOAD_SPLIT_ONELINE, SOURCE_LINE_SIZE);

    // Load the pattern file of fixed-length lines
    struct FileData pat;
    readSourceFile(patternfile, &pat, FILE_LOAD_LINES, SEARCH_LINE_SIZE);

    int total_matches = 0;

    // Loop through each pattern and each line to search for occurrences
    #pragma omp parallel for schedule(dynamic)
    for (long p = 0; p < pat.lines; ++p) {
        for (long l = 0; l < fd.lines; ++l) {
            int match_index = KMPSearchFirstMatch(pat.data[p], fd.data[l]);
            if (match_index != -1) {
                #pragma omp critical
                {
                    printf("**,%s,%ld,%d\n", pat.data[p], l, match_index);
                }
                
                total_matches++;
            }
        }
    }

    printf("\nGrand total of matches: %d\n", total_matches);
    return 0;
}
