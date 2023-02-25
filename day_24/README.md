
# Part 1

Calculating the state of the blizzard locations was relatively straight forward.  Finding the shortest/quickest path wasn't.  Once I realized that the blizzard locations were just a function of time, I could include the minute along with the x,y coordinates of the location and use a breadth first search.  Rather than recalculate the blizzard map every step, I just cached the map in an array indexed by minutes, so any blizzard look ups that were already done before didn't have to be recalculated. I didn't measure the difference in time this saves, but I'm assuming its helpful.

# Part 2 

Not much else to do for this part.  Just swap the entrance/exit and continue adding to the states from part 1 as time progresses.