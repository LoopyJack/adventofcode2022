
Parts 1 and 2 are the same problem with different parameters.

# Python Solution

I wrote two different solutions.  The first is more "pythonic" making use of the built in set() and range() functions and list slicing.  Very concise, but just blindly iterates until it finds the solution. The second solution is a copy of the Go solution. It still uses a set() to check for duplicates but cuts out the range generator and list slicing. It now jumps the check window ahead of the first occurence of the duplicate character.  So often I read that looping in python is slow and to use the built-in functions; but in this case just using plain old loops but skipping known-to-be wrong answers is more than twice as fast. 

# Go Solution

Had originally copied the first Python solution, but not having list/dict/set comprehension in Go forced me to actually write the loop out, which allowed for checking and skipping any more iterations needed to be done.  The original python solution ran in a couple milliseconds so I wasn't too concerned with the efficiency of the solution.  The big efficiency gain was jumping the duplicate check window forward past the first occurence of the duplicate character.  Don't do unnecessary calculations.  The Go solution is quite a bit faster than the second python one for this problem.  