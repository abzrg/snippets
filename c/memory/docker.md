https://jvns.ca/blog/2020/04/29/why-strace-doesnt-work-in-docker/

docker run -it --rm --cap-add=SYS_PTRACE -v ./:/workspace cdev
