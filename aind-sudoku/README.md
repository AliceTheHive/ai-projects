# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: The naked twins problem is solved by identifying peer groups which have "naked twin" values.  In other words, two boxes that have the same pair of two digit values.  When a "naked twin" is identified in a peer group, then the digits can be removed from all other boxes in the peer group

The "naked twins" technique can be used as a one possible heuristic in constraint propagation for narrowing down the search space of the sudoku problem.


# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: To solve the diagonal sudoku problem, you can just add diagonals as peer groups in the peer list.  This is because the game of sudoku is solved by satisfying conditions (unique 1-9) within each peer group.   Furthermore, all the constraint propogation strategies that we have implemented so far (only choice, naked twins, eliminate) use these peer groups to reduce the search space.  

This is a great article by Peter Norvig which explains the approach in more detail:
http://norvig.com/sudoku.html
