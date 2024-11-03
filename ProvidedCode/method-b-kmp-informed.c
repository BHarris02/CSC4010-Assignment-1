#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "search.h" 

// Function to compute LPS array for KMP
void computeLPSArray(char* pat, int m, int* lps) {
    int len = 0;
    lps[0] = 0;
    int i = 1;
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

// Function to use LPS for candidate positions then Search for verification
int KMPInformedSearchCount(char* pat, char* txt) {
    int m = strlen(pat);
    int n = strlen(txt);
    int match_count = 0;

    // Calculate LPS array
    int* lps = (int*)malloc(m * sizeof(int));
    computeLPSArray(pat, m, lps);

    int start_pos = 0;
    while (start_pos <= n - m) {
        // Search for first occurrence of pattern from current start position
        int match_pos = Search(txt + start_pos, n - start_pos, pat, m, SEARCH_MODE_FIRST);

        if (match_pos == -1) {
            break;  // No more matches in this segment
        } else {
            // Match found incrementmatch count
            match_count++;

            // Update start position
            start_pos += match_pos + 1;
        }
    }

    free(lps);
    return match_count;
}

int main(int ac, char** av) {
    if (ac < 3) {
        FatalError("Usage: command sourcefile.txt patternfile.txt");
    }

    char* sourcefile = av[1];
    char* patternfile = av[2];

    // Load the entire source data as a single line
    struct FileData fd;
    readSourceFile(sourcefile, &fd, FILE_LOAD_ONELINE, 1);

    // Load the pattern file of fixed length lines
    struct FileData pat;
    readSourceFile(patternfile, &pat, FILE_LOAD_LINES, SEARCH_LINE_SIZE);

    // Array to store match counts for each pattern
    int* patterncount = (int*)malloc(pat.lines * sizeof(int));
    #pragma omp parallel for
    for (long p = 0; p < pat.lines; ++p) {
        patterncount[p] = KMPInformedSearchCount(pat.data[p], fd.data[0]);
    }

    // Output the results
    for (long p = 0; p < pat.lines; ++p) {
        #pragma omp critical
        printf("**,%s,%d\n", pat.data[p], patterncount[p]);
    }

    free(patterncount);
    return 0;
}
