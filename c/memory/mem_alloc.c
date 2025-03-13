#include <stdio.h>
#include <stdlib.h>

// Static
int my_variable = 80;

int main()
{
    // Dynamic (standard: malloc, calloc, realloc)
    int *x = malloc(sizeof(*x));

    // Returns either a pointer to a block of memory or NULL
    int *arr = malloc(sizeof(*arr) * 100);
    if (arr == NULL) { return -1; }

    *x = 12;
    arr[90] = 0xFEEDBEEF;
    arr[101] = 0xDEAD;         // Out of bound! (May corrupt other memory -> UB)


    // Tell allocator we don't need the memory any more.
    free(arr);
    arr = NULL;          // Best practice (so that we can tell it's empty later)
    free(arr);           // is this problematic?

    double *darr;
    // sizeof each element, # of elements
    // Also sets the bytes in the block to zero.
    darr = calloc(sizeof(*darr), 100);

    // Resizes an allocated block array.
    // NOTE: The address returned could be different from the original pointer
    // to the block (i.e. there wasn't room for the new block, so it had to move
    // it, meaning it will copy the old content to the new location)
    darr = realloc(darr, sizeof(*darr) * 500);

    return 0;
}
