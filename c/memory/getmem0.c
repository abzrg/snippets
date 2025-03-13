// at low memory it calls brk

#include <stdio.h>
#include <stdlib.h>

#define MEMORY_BLOCK_SIZE 50000

int main(void)
{
    for (int i = 0; i < 5; i++) {
        char *ptr = malloc(MEMORY_BLOCK_SIZE);
        printf("Got memory! (address=%p)\n", (void*)ptr);
    }

    return 0;
}
