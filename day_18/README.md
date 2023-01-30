
# Part 1

Started off modeling the total space, but realized the just the cubes needed to be compared. Neighbors are easy to find. Since diagonals don't matter, adjacent cubes will only have a max difference of 1 summed across all 3 axes.  Cubes have 6 sides, subtract for each contact a cube has, and finally some the exposed sides.  Got this one fairly easily.

# Part 2

Use a breadth first search starting from an empty cube space that is known to be outside object space. Count the number of surfaces contacted.  Have to add empty space around the object so the that BFS can explore all surfaces.