
# Part 1

The original solution works but was overly complicated.  Kept a list of all directories (which included their parents) and a dictionary of lists of files keyed by the directories in the list.  Looping through the commands, then files, then directories separately was just ineffecient.  After peeking online, I realized a stack of the current directory depth would give all the directory sizes that needed to be added to.  solution2 is the refined solution.

# Part 2

Did some algebra on the already calculated structures.