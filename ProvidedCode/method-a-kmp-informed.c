/**
 * Method A
 * 
 * Load and split the source file into a set of char arrays each of SOURCE_LINE_SIZE long
 * Load the pattern lines (each of fixed length SEARCH_LINE_SIZE)
 * 
 * Search the source lines looking for pattern, returning the first occurance of the pattern index
 * or -1 if not found
 * 
 * If the pattern is found in a line output to stdout:
 * **,PATTERN,line_number,index\n
 * 
 * 
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "search.h" // include the search library

int main(int ac, char** av) {
    if (ac < 3) {
        FatalError("Usage: command sourcefile.txt patternfile.txt");
    }

    char* sourcefile = av[1];
    char* patternfile = av[2];

    // Load the source data into chunks of SOURCE_LINE_SIZE
    struct FileData fd;
    readSourceFile(sourcefile, &fd, FILE_LOAD_SPLIT_ONELINE, SOURCE_LINE_SIZE);

    // Load the pattern file of fixed length lines
    struct FileData pat;
    readSourceFile(patternfile, &pat, FILE_LOAD_LINES, SEARCH_LINE_SIZE);

    //#pragma omp parallel for schedule(dynamic)
    for (long p = 0; p < pat.lines; ++p) {
        long pat_len = strlen(pat.data[p]);

        // Loop through each line of the source
        for (long l = 0; l < fd.lines; ++l) {
            int match_start = 0; // Position from which to search in each line

            while (match_start < fd.linesize) {
                // Call the provided Search function to find the first occurrence
                long s = Search(fd.data[l] + match_start, fd.linesize - match_start, pat.data[p], pat_len, SEARCH_MODE_FIRST);

                // If a match is found
                if (s != -1) {
                    #pragma omp critical
                    printf("**,%s,%ld,%ld\n", pat.data[p], l, match_start + s);

                    // Move match_start by the length of the pattern to avoid overlapping matches
                    match_start += s + pat_len;
                } else {
                    break;  // No further matches in this line
                }
            }
        }
    }
    return 0;
}

