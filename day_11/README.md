
# Part 1

No real tricks to this part.  Just making sure to do the operations in the right order was the hardest aspect.

# Part 2

Same problem, just with different inputs.  The number of iterations caused the value of the counts to explode and doing any kind of math on values that big wasn't feasible.  I was stumped here and had to peak at other solutions online.   Multiplying all the divisors together and then getting the modulus of the value with that number was the way to keep the values from spiraling out of control.  This worked for a worry level of 1, but going back and trying to rerun the code on the part 1, gave a wrong answer.  Turns out the product of all the divisors had to be multiplied by the worry level as well.  This was a guess but it worked, but I don't know if it'll give the correct answer for any input.  