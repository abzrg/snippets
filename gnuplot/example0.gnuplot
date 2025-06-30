# source: git@github.com:solids4foam/fluid-benchmarks
#
# This Gnuplot script is used to generate a PDF plot that visualizes the order
# of accuracy of a numerical method with respect to mesh spacing, on a
# logarithmic x-axis.
# -----------------------------------------------------------------------------

# Example Data:
#
#  col index:   1     2          3         4
#               ^     ^          ^         ^
#             # Mesh  L1         L2        LInf
#               1     0.251286   0.499005  0.750095
#               2     1.1262     1.08913   0.897196
#               3     0.377011   0.453564  0.53104
#               4     0.0321025  0.062208  0.180142
#
# -----------------------------------------------------------------------------

# Uses the pdfcairo terminal with dashed lines and enhanced text formatting for
# high-quality vector output.
set term pdfcairo dashed enhanced

# Assumes that the data file is space-separated.
set datafile separator " "

# Check whether the first argument was passed or not
# ARGC: argument count
# ARG1: first argument
if (ARGC < 1) { # this `{` *must* be in the same line as `if`
    print "Error: No input configuration name provided."
    print "usage: ", ARG0, " <configName>"
    exit
} else {
    configName = ARG1
}

# Sets the name of the output PDF file.
# `.` concatenate string values
set output configName.".velocity_orderOfAccuracy.pdf"

# Enables a grid in the background of the plot.
set grid

# Limit the X- and Y-axis
set xrange [10:200]
set yrange [0:3]

# Sets specific tick marks on the X-axis and uses default Y-axis ticks.
set xtics
set xtics add (25, 50, 100, 200)
set ytics

# Applies a logarithmic scale to the X-axis, which is appropriate for mesh
# refinements (spacing often halves geometrically).
# The Y-axis remains linear
set logscale x

# Sets axis labels and places the legend at the bottom-left.
set xlabel "Average cell spacing (in mm)"
set ylabel "Order of accuracy"
set key bottom left;

# Average mesh spacing of mesh1
# Initial (coarsest) average mesh spacing in millimeters.
dx=0.2

datafile = configName.".orderOfAccuracy.txt"
# Assume the mesh spacing is being halved for each succesive mesh
# Each row in the data corresponds to a finer mesh, where the spacing is halved
# each time.
plot \
    datafile using (1e3*dx/(2**($0))):2 skip 1 w lp pt 5 lc "green" t "L_1", \
    datafile using (1e3*dx/(2**($0))):3 skip 1 w lp pt 5 lc "red" t "L_2", \
    datafile using (1e3*dx/(2**($0))):4 skip 1 w lp pt 4 lc "blue" t "L_∞"

# 1e3: converts from 'm' to 'mm'.
# $0: row index or the line number (starting from 0).
#     - skip 1: skips the first line (usually a header).
#       Because of skip 1, the first data line (1 0.251286 ...) corresponds to
#       $0 = 0, second line is $0 = 1, etc.
# w lp: with lines and points.
# pt: the point type (5 or 4).
# lc: line color.
# t: gives the legend title.
# x:y (x=(1e3*dx...), y=2 (second column))
#
# -----------------------------------------------------------------------------

# | Mesh Index  | Line # (`$0`) | X (Spacing, mm) | Y (L₁ Error) |
# | ----------  | ------------- | --------------- | ------------ |
# | 1 (5 5 1)   | 0             | 200             | 0.251286     |
# | 2 (10 10 1) | 1             | 100             | 1.1262       |
# | 3 (20 20 1) | 2             | 50              | 0.377011     |
# | 4 (40 40 1) | 3             | 25              | 0.0321025    |


# The script go through *all lines* in the data file (except the header) and
# processes them *row by row*.
#
# 1. *Skips the first line* due to `skip 1` (header line).
# 2. Reads the *next lines*, one at a time.
# 3. For each line (say, line number `i`):
#    * `$0 = i` (starting from 0)
#    * Reads column 2 (`$2`) → Y-value
#    * Computes `(1e3 * dx / 2**($0))` → X-value
# 4. Adds the (X, Y) point to the plot.
# 5. Repeats for *all remaining lines* in the file.
#
# So if your file has 4 data lines (after the header), Gnuplot will compute and
# plot 4 points.
