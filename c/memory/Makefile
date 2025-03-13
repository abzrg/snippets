CC = gcc
CFLAGS = -Wall -Wextra -std=c17 -pedantic -g

BUILDDIR = build
SRCS = $(wildcard *.c)
TARGETS = $(patsubst %.c,$(BUILDDIR)/%,$(SRCS))

all: $(BUILDDIR) $(TARGETS)

$(BUILDDIR)/%: %.c
	$(CC) $(CFLAGS) $< -o $@

$(BUILDDIR):
	@mkdir -pv $@

clean:
	@$(RM) -vf $(TARGETS)
