#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <omp.h>
#include "search.h" // include the search library

#define ALPHABET_SIZE 256

// Trie node structure for Aho-Corasick
typedef struct TrieNode {
    struct TrieNode* children[ALPHABET_SIZE];
    struct TrieNode* failure;
    int* pattern_indices;
    int pattern_count;
} TrieNode;

// Create a new Trie node
TrieNode* createTrieNode() {
    TrieNode* node = (TrieNode*)malloc(sizeof(TrieNode));
    node->failure = NULL;
    node->pattern_count = 0;
    node->pattern_indices = NULL;
    for (int i = 0; i < ALPHABET_SIZE; i++) {
        node->children[i] = NULL;
    }
    return node;
}

// Insert a pattern into the Trie and record its index
void insertPattern(TrieNode* root, const char* pattern, int pattern_index) {
    TrieNode* node = root;
    for (int i = 0; pattern[i] != '\0'; i++) {
        int index = (unsigned char)pattern[i];
        if (!node->children[index]) {
            node->children[index] = createTrieNode();
        }
        node = node->children[index];
    }
    // Add the pattern index to the node where the pattern ends
    node->pattern_count++;
    node->pattern_indices = (int*)realloc(node->pattern_indices, node->pattern_count * sizeof(int));
    node->pattern_indices[node->pattern_count - 1] = pattern_index;
}

// Build failure links for the Trie
void buildFailureLinks(TrieNode* root) {
    TrieNode** queue = (TrieNode**)malloc(ALPHABET_SIZE * sizeof(TrieNode*));
    int front = 0, rear = 0;

    // Initialize failure links of root's children
    for (int i = 0; i < ALPHABET_SIZE; i++) {
        if (root->children[i]) {
            root->children[i]->failure = root;
            queue[rear++] = root->children[i];
        }
    }

    // BFS to set up failure links
    while (front < rear) {
        TrieNode* current = queue[front++];
        for (int i = 0; i < ALPHABET_SIZE; i++) {
            if (current->children[i]) {
                TrieNode* fail = current->failure;
                while (fail && !fail->children[i]) {
                    fail = fail->failure;
                }
                current->children[i]->failure = fail ? fail->children[i] : root;
                queue[rear++] = current->children[i];
            }
        }
    }
    free(queue);
}

// Function to search and count pattern occurrences in the text
void ahoCorasickSearch(TrieNode* root, char* text, int* pattern_count) {
    TrieNode* node = root;
    int text_length = strlen(text);

    for (int i = 0; i < text_length; i++) {
        int index = (unsigned char)text[i];

        // Follow failure links if no match for current character
        while (node != root && !node->children[index]) {
            node = node->failure;
        }
        if (node->children[index]) {
            node = node->children[index];
        }

        TrieNode* temp = node;
        while (temp != root) {
            if (temp->pattern_count > 0) {
                // Use a critical section to safely update pattern counts
                #pragma omp critical
                {
                    for (int j = 0; j < temp->pattern_count; j++) {
                        pattern_count[temp->pattern_indices[j]]++;
                    }
                }
            }
            temp = temp->failure;
        }
    }
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

    // Load the pattern file of fixed-length lines
    struct FileData pat;
    readSourceFile(patternfile, &pat, FILE_LOAD_LINES, SEARCH_LINE_SIZE);

    // Build Aho-Corasick Trie and failure links
    TrieNode* root = createTrieNode();
    // Parallelise inserting patterns
    #pragma omp parallel for
    for (long p = 0; p < pat.lines; ++p) {
        #pragma omp critical
        insertPattern(root, pat.data[p], p);
    }
    buildFailureLinks(root);

    // Array to store match counts for each pattern
    int* pattern_count = (int*)calloc(pat.lines, sizeof(int));
    if (!pattern_count) {
        FatalError("Memory allocation failed for pattern_count array.");
    }

    // Perform Aho-Corasick search on the entire text
    ahoCorasickSearch(root, fd.data[0], pattern_count);

    // Output the results
    for (long p = 0; p < pat.lines; ++p) {
        printf("**,%s,%d\n", pat.data[p], pattern_count[p]);
    }

    free(pattern_count);
    free(root);
    return 0;
}
