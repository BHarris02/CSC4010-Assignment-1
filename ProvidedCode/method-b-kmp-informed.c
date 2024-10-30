/**
 * Method B
 * 
 * Load the source file into a single char array (one line)
 * Load the pattern lines (each of fixed length SEARCH_LINE_SIZE)
 * 
 * Search the source line looking for patterns, returning the number 
 * of instances of the pattern found (0 if not found)
 * 
 * For each pattern output a line to stdout of the format:
 * **,pattern,count\n
 * 
 * 
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "search.h" // include the search library

// Function to compute the LPS array for KMP
void computeLPSArray(char* pat, int m, int* lps) {
    int len = 0;
    lps[0] = 0; // LPS[0] is always 0
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

// Function to use KMP's LPS for candidate positions and then `Search` for verification
int KMPInformedSearchCount(char* pat, char* txt) {
    int m = strlen(pat);
    int n = strlen(txt);
    int match_count = 0;

    // Calculate the LPS array for the pattern
    int* lps = (int*)malloc(m * sizeof(int));
    computeLPSArray(pat, m, lps);

    // Use Search iteratively to confirm each match and move to the next position after each match
    int start_pos = 0;
    while (start_pos <= n - m) {
        // Search for the first occurrence of the pattern from the current start position
        int match_pos = Search(txt + start_pos, n - start_pos, pat, m, SEARCH_MODE_FIRST);

        if (match_pos == -1) {
            break;  // No more matches in this segment
        } else {
            // A match is found; increment the match count
            match_count++;

            // Update start position to move past the current match
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
