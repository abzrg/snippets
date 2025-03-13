// With large memory allocation it calls mmap on linux and virtualAloc on
// windows

#include <stdio.h>
#include <stdlib.h>

#define MEMORY_BLOCK_SIZE 5000000

int main(void)
{
    for (int i = 0; i < 5; i++) {
        char *ptr = malloc(MEMORY_BLOCK_SIZE);
        printf("Got memory! (address=%p)\n", ptr);
    }

    return 0;
}
