"""
library/itertools

Faster and more memory-efficient ways of iterating

> The module standardizes a core set of fast, memory efficient tools that are
> useful by themselves or in combination. Together, they form an 'iterator
> algebra' making it possible to construct specialized tools succinctly and
> efficiently in pure Python.

- accumulate()
- combinations()
- combinations_with_replacement()
- count()
- cycle()
- chain()
- compress()
- dropwhile()
- filterfalse()
- groupby()
- islice()
- permutations()
- product()
- repeat()
- starmap()
- takewhile()
- tee()
- zip_longest()

Documentations:
    - https://docs.python.org/3/library/itertools.html

References:
    - https://softwaretechnologymq.github.io/python_cheat_sheet.html#itertools-module

"""

# This module exports a set of functions corresponding to the intrinsic
# operators of Python. For example, operator.add(x, y) is equivalent to the
# expression x+y.
import operator
import itertools

from src.helper import p, set_debug

set_debug(True)


# -----------------------------------------------------------------------------
# accumulate()
# Makes an iterator that returns the results of a function.
#
#     itertools.accumulate(iterable[, func])
#

# Sum at every iteration
data = [5, 2, 6, 4, 5, 9, 1]
result = itertools.accumulate(data)  # operator.add by defult
acc_adds = [add for add in result]

# Default: operator.add
# 5 --+2--> 7 --+6--> 13 --+4--> 17 --+5--> 22 --+9--> 31 --+1--> 32

# Multiply at each iteration
data = [1, 2, 3, 4, 5]
result = itertools.accumulate(data, operator.mul)
acc_mults = [mult for mult in result]

# operator.mul(1, 2) <==> 1 * 2
# 1 --*2--> 2 --*3--> 6 --*4--> 24 --*5--> 120


# -----------------------------------------------------------------------------
# combinations()
# Takes an iterable and a integer. This will create all the unique combination
# that have r members.
#
#     itertools.combinations(iterable, r)
#

shapes = ["circle", "triangle", "square"]

result = itertools.combinations(shapes, 2)
combos = [combo for combo in result]
# [('circle', 'triangle') ('circle', 'square') ('triangle', 'square')]

result = itertools.combinations(shapes, 3)
combos = [combo for combo in result]
# [('circle', 'triangle', 'square')]

# -----------------------------------------------------------------------------
# combinations_with_replacement()
# Just like combinations(), but allows individual elements to be repeated more
# than once.
#
#     itertools.combinations(iterable, r)
#

shapes = ["circle", "triangle", "square"]
result = itertools.combinations_with_replacement(shapes, 2)
combos = [combo for combo in result]

# [('circle', 'circle'), ('circle', 'triangle'), ('circle', 'square'),
#  ('triangle', 'triangle'), ('triangle', 'square'), ('square', 'square')]

# -----------------------------------------------------------------------------
# count()
# Makes an iterator that returns evenly spaced values starting with number
# start.
#
#     itertools.count(start=0, step=1)
#

bounded_numbers = []
for i in itertools.count(10, 3):
    if i > 20:
        break
    bounded_numbers.append(i)

# [10, 13, 16, 19]

# -----------------------------------------------------------------------------
# cycle()
# This function cycles through an iterator endlessly.
#
#     itertools.cycle(iterable)
#

# --- example 1
# Print items with alternating colors until the list of items is exhausted

# Create an infinite cycle of these colors
colors = ["red", "green", "blue"]
color_cycle = itertools.cycle(colors)
items = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
for item in items:
    color = next(color_cycle)
    p(f"{color}: {item}")

# red: apple
# green: banana
# blue: cherry
# red: date
# green: elderberry
# blue: fig
# red: grape

# --- example 2
# Dealing M cards to N players (palyers create a cycle that consume cards)

# Define a deck of cards
deck = [
    "Ace of Spades",
    "2 of Hearts",
    "3 of Diamonds",
    "4 of Clubs",
    "5 of Hearts",
    "6 of Diamonds",
    "7 of Clubs",
    "8 of Hearts",
    "9 of Spades",
    "10 of Diamonds",
]

players = ["Player 1", "Player 2", "Player 3", "Player 4"]
# Create a dictionary to hold each player's cards
hands = {player: [] for player in players}
# Cycle through players and deal each card to the next player in line
player_cycle = itertools.cycle(players)
for card in deck:
    current_player = next(player_cycle)
    hands[current_player].append(card)
for player, hand in hands.items():
    p(f"{player}'s hand: {hand}")

# Player 1's hand: ['Ace of Spades', '5 of Hearts', '9 of Spades']
# Player 2's hand: ['2 of Hearts', '6 of Diamonds', '10 of Diamonds']
# Player 3's hand: ['3 of Diamonds', '7 of Clubs']
# Player 4's hand: ['4 of Clubs', '8 of Hearts']

# -----------------------------------------------------------------------------
# chain()
# Take a series of iterables and return them as one long iterable.
# "consumable concatanator?"
#
#     itertools.chain(*iterables)
#

colors = ["red", "orange", "yellow", "green", "blue"]
shapes = ["circle", "triangle", "square", "pentagon"]
result = itertools.chain(colors, shapes)
concatenated = [item for item in result]

# ['red', 'orange', 'yellow', 'green', 'blue', 'circle', 'triangle', 'square', 'pentagon']


# -----------------------------------------------------------------------------
# compress()
# Filters one iterable with another.
#
#     itertools.compress(data, selectors)
#

shapes = ["circle", "triangle", "square", "pentagon"]
selections = [True, False, True, False]
result = itertools.compress(shapes, selections)
selected_shapes = [selected for selected in result]

# ['circle', 'square']
