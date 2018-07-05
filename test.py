from solution import *
from utils import *

grid ='.581..7..1...7...63...8.1.44..8..6....1...2....5..1..85.9.1...27...5...1..3..786.'
values = grid2values(grid)
display(values)
values2 = reduce_puzzle(values)
display(values2)

values3 = solve(grid)
display(values3)

"""
print("Eliminate:")
values2 = eliminate(values)
display(values2)
print("Eliminate:")
values2 = eliminate(values)
display(values2)
print("Only Choice:")
values3 = only_choice(values2)
display(values3)
print("Naked Twins:")
values4 = naked_twins(values3)
display(values4)
"""
