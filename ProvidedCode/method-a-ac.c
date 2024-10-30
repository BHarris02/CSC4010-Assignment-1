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
    int* pattern_indices;  // Tracks which patterns end at this node
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

// Function to search and find the first occurrence each pattern in a line
void ahoCorasickSearch(TrieNode* root, char* line, long line_number, struct FileData* patterns) {
    TrieNode* node = root;
    int text_length = strlen(line);
    int found_first_match = 0;

    for (int i = 0; i < text_length && !found_first_match; i++) {
        int index = (unsigned char)line[i];

        // Follow failure links if no match for current character
        while (node != root && !node->children[index]) {
            node = node->failure;
        }
        if (node->children[index]) {
            node = node->children[index];
        }

        // If we reach end node print first match
        TrieNode* temp = node;
        while (temp != root && !found_first_match) {
            if (temp->pattern_count > 0) {
                for (int j = 0; j < temp->pattern_count; j++) {
                    int pattern_index = temp->pattern_indices[j];
                    printf("**,%s,%ld,%d\n", patterns->data[pattern_index], line_number, i - strlen(patterns->data[pattern_index]) + 1);
                    found_first_match = 1;
                    break;
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

    // Load the source data into chunks of SOURCE_LINE_SIZE
    struct FileData fd;
    readSourceFile(sourcefile, &fd, FILE_LOAD_SPLIT_ONELINE, SOURCE_LINE_SIZE);

    // Load the pattern file of fixed-length lines
    struct FileData pat;
    readSourceFile(patternfile, &pat, FILE_LOAD_LINES, SEARCH_LINE_SIZE);

    // Build Aho-Corasick Trie
    TrieNode* root = createTrieNode();
    #pragma omp parallel for
    //Insert patterns in parallel
    for (long p = 0; p < pat.lines; ++p) {
        #pragma omp critical
        insertPattern(root, pat.data[p], p);
    }
    buildFailureLinks(root);

    // Perform Aho-Corasick search in parallel
    #pragma omp parallel for
    for (long l = 0; l < fd.lines; ++l) {
        ahoCorasickSearch(root, fd.data[l], l, &pat);
    }
    free(root);

    return 0;
}
