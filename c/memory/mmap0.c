// Requests memory from kernel:
// I need more memory in my address space to be usable (a bigger data section)

// But rather than allowing you to bump up/down the program break, mmap gives
// you more options

#include <sys/mman.h>
#include <stdint.h>
#include <stddef.h>
#include <stdio.h>

#define PAGESIZE (4 * 1024)

int main(void)
{
    // void *
    // mmap(void *addr, size_t len, int prot, int flags, int fd, off_t offset);

    // addr: NULL => a hint to the operating system: I need memory, just put it
    // anywhere.
    // If you specify an address it tries to satisfy that request.
    // (void*)0xFEEDBEEF => 0xfeedb000
    // But blocks of memory are going to be aligned to the beginning of a page.

    // len: size of the block of memory to allocate. one can request sizes that
    // are not multiple of page size, but it doesn't make any sense because
    // you're gonna get a multiple of page size one way or the other

    // prot (protection): read-only or write-only or both.

    // flags: tells the kernel how we want the memory to be managed/shared; do
    // we want it to be shared at all or do we want it to be private to
    // particular process.

    // fd (file descriptor)
    // offset
    // These two are used for memory-mapped files

#define ADDR (void*)0xFEEDBEEF
    uint8_t* first = mmap(ADDR, 4*PAGESIZE, PROT_READ | PROT_WRITE,
                          MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);

    uint8_t* second = mmap(NULL, PAGESIZE, PROT_READ | PROT_WRITE,
                           MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);

    printf("First: %p\n", first);
    printf("Second: %p\n", second);

    return 0;
}
