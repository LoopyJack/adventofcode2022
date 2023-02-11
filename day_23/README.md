
# Part 1

Started by first making a 2D array and looping over the x,y coordinates individually, but since elves could move into negative territory it was inefficient to translate the whole terrain map to accomodate for the new size.  So I switched to a nested dictionary with the x,y values as keys which allowed for the insertion of negative coordinates.  While writing that I realized I was making the problem more complicated than it needed to be and just made the the x, y coordinate for each elf a tuple, got rid of the terrain map, in favor of a set (valueless dict).  Checking the coordinate tuples surrounding each elf is as easy at that point. 

# Part 2

Not much to add for this one.  Just iterate until there were no proposals made.