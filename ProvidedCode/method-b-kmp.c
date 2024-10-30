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

// Function to compute the LPS array for KMP preprocessing
void computeLPSArray(char* pat, int M, int* lps) {
    int len = 0;
    lps[0] = 0;
    int i = 1;
    while (i < M) {
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

// KMP search function that counts occurrences of the pattern in the text
int KMPSearchCount(char* pat, char* txt) {
    int m = strlen(pat);
    int n = strlen(txt);
    int count = 0;

    // Preprocess the pattern to get the LPS array
    int* lps = (int*)malloc(sizeof(int) * m);
    computeLPSArray(pat, m, lps);

    int i = 0, j = 0; // i -> txt[], j -> pat[]
    while (i < n) {
        if (pat[j] == txt[i]) {
            j++;
            i++;
        }

        if (j == m) { // Found a match
            count++;
            j = lps[j - 1];
        } 
        else if (i < n && pat[j] != txt[i]) { // Mismatch after j matches
            if (j != 0)
                j = lps[j - 1];
            else
                i = i + 1;
        }
    }
    free(lps);
    return count;
}

int main(int ac, char** av) {
    if (ac < 2) {
        FatalError("Usage: command sourcefile.txt patternfile.txt");
    }

    char* sourcefile = av[1];
    char* patternfile = av[2];

    // Load the source data as a single chunk
    struct FileData fd;
    readSourceFile(sourcefile, &fd, FILE_LOAD_ONELINE, 1);

    // Load the pattern file of fixed length lines
    struct FileData pat;
    readSourceFile(patternfile, &pat, FILE_LOAD_LINES, SEARCH_LINE_SIZE);

    printf("Read %ld lines for %ld characters in source, %ld lines for %ld chars in pattern\n", fd.lines, fd.length, pat.lines, pat.length);

    long patterncount[pat.lines];
    for (long i = 0; i < pat.lines; ++i) {
        patterncount[i] = 0;
    }

    // Parallelize the pattern counting
    #pragma omp parallel for schedule(dynamic)
    for (long p = 0; p < pat.lines; ++p) {
        patterncount[p] = KMPSearchCount(pat.data[p], fd.data[0]);
    }

    // Output the results
    for (long p = 0; p < pat.lines; ++p) {
        #pragma omp critical
        printf("**,%s,%ld\n", pat.data[p], patterncount[p]);
    }

    return 0;
}
