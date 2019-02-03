# CountByCars

This was a challenge presented to me while on a run once:

> If you pass 600 cars in a day, to what number would you be able to count using only numbers that appear in each car's number plate?

For example, if you pass the following cars:  
`CA 312-456`, `CA 798-301`, `CA 456-321`, `CA 909-303`  
you could count up to 3 using a `1` from the first licence, a `2` from the third and a `3` from the fourth. When the second car passed, you were looking for a `2` but the number plate did not have one so you couldn't use it.

For now I am assuming you can only get one number from each number plate.

## Approach

This uses the Monte Carlo method to estimate the result over a number of simulations. The output is the mean of the total counts achieved.

## Running the script

Simply use `python -m CountByCars.py` from the command line.

You can pass in the folliwing arguments to get extra info in the output:  
`--min-max`: Display the lowest and highest count  
`--list-all`: List the count achieved in each simulation
