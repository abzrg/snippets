#include <stdio.h>
#include <unistd.h>

int main(void)
{
    // sbrk: returns the address to the previous break (heap clif!)
    // sbrk(0): tell where the break is.
    void *first = sbrk(0);
    // Move program break 4kb up; Modern virtual memory systems use paging and
    // page size is 4kb and it will round up to the next 4kb page
    void *second = sbrk(4 * 1024);
    void *third = sbrk(0);

    printf("First: %p\n", first);
    printf("Second: %p\n", second);
    printf("Third: %p\n", third);

    int *ptr = (int*)(third + 1);
    *ptr = 0xDEAD; // SEGFAULT

    return 0;
}
