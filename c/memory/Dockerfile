FROM ubuntu:latest

ENV LANG=C.UTF-8
ENV TERM=xterm-256color
ENV DEBIAN_FRONTEND=noninteractive

# Disable unminization
RUN sed -i '/path-exclude/s:^:#:' /etc/dpkg/dpkg.cfg.d/excludes

# 1. update
# 2. install:
#    - build essentials, debugger and static analyzer
#    - dev tools
#    - network tools
#    - man pages
# 3. Remove some unneeded package manager cache
# 4. Let the 'man' do it's job
# 5. Update man pages index
RUN :                                                                           \
    && apt-get update                                                           \
    && apt-get install -y build-essential binutils strace ltrace                \
       vim tmux git curl wget gdb valgrind                                      \
       telnet iputils-ping netcat-openbsd libssl-dev openssl                    \
       man-db manpages manpages-dev manpages-posix manpages-posix-dev glibc-doc \
    && rm -rf /var/lib/apt/lists/*                                              \
    && mv /usr/bin/man.REAL /usr/bin/man                                        \
    && mandb -c

WORKDIR /workspace

CMD [ "bash" ]
