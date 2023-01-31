
# Part 1

Fairly straight forward problem.  Just a simple monkey class where calling `shout` returns the number or gets the numbers from the monkies that have them.  Relies on a global dictionary `monkies`

# Part 2

Took a brute force approach.  It must be possible to back out the number needed, but brute forcing worked with just a few seconds of work.  This is made a lot easier since a monkey that does a comparison return not just the comparison, but how much the two numbers differ by.  It's a little extra functionality than specified but nothing more than calling `shout` on the two contributing monkies in the first place so I don't consider it a big deal.  The brute force just ping pongs around the sign of the difference halving the delta in on each flip to zero in.