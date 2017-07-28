# Artificial Intelligence Nanodegree
## Diagonal Sudoku Solver

I will try to explain the high level intuition behind the AI sudoku solver.  

Basically, the sudoku puzzle combines **constraint propagation** technique with **depth first search**.

**Contraint Propagation** is the process of reducing the search space of a problem by applying various strategies or heuristics.  In the context of sudoku, the goal is to solve the puzzle by filling out all rows, columns, and boxes with unique 1-9 values.  Taking into account this goal, constraint propagation involves applying various strategies in an attempt to narrow down the possible values for each of the squares.  Different strategies can be applied iteratively to narrow down the search space.  Sometimes, one strategy runs into a brick wall, and switching to a different strategy can make further progress.

**Depth First Search** is useful when constraint propagation fails to solve the puzzle.  After running many iterations of constraint propagation, sometimes the puzzle is still left with many possibilities and no definite solution.  In this case, using search is a good strategy.  Search allows you to branch off and try different possibilities until a solution is found.

Combining these two techniques, any sudoku puzzle can be solved.


# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: The naked twins problem is solved by identifying peer groups which have "naked twin" values.  In other words, two boxes that have the same pair of two digit values.  When a "naked twin" is identified in a peer group, then the digits can be removed from all other boxes in the peer group

The "naked twins" technique can be used as a one possible heuristic in constraint propagation for narrowing down the search space of the sudoku problem.


# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: To solve the diagonal sudoku problem, you can just add diagonals as peer groups in the peer list.  This is because the game of sudoku is solved by satisfying conditions (unique 1-9) within each peer group.   Furthermore, all the constraint propogation strategies that we have implemented so far (only choice, naked twins, eliminate) use these peer groups to reduce the search space.  

This is a great article by Peter Norvig which explains the approach in more detail:
http://norvig.com/sudoku.html
