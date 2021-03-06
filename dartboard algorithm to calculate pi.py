# 'compute' is the core calculation
def compute(s, n):
    import random

    inside = 0
    random.seed(s)

    # For the number of points requested
    for i in range(n):
        
        # Create a random point
        x = random.uniform(0.0, 1.0)
        y = random.uniform(0.0, 1.0)

        # Calculate the radius
        z = x*x + y*y

        # Check whether the radius is inside the circle
        if (z <= 1.0):
            inside = inside + 1    

    return(inside)


# main 
if __name__ == '__main__':
    import random, decimal

    # Input the number of trials to run and the size of each trial
    no_of_points = int( input('Number of random points to include in each trial = ') )
    no_of_trials = int( input('Number of trials to run = ') )

    print(('Doing %s trials of %s points each' % (no_of_trials, no_of_points)))
    total_inside = 0

    # Run the desired number of trials
    for i in range(no_of_trials):
        
        # Create a new random seed
        ran_seed = random.randint(0,65535)

        # Run the compute function with this seed
        inside = compute(ran_seed, no_of_points)

        # Add this number to the total of points found inside
        total_inside += inside

        # Report back every 1000 trials
        if (i % 1000 == 0): 
            print(('Executed trial %i using random seed %i with result %i' % (i, ran_seed, inside)))

    # Calculate the total number of points tried
    total_no_of_points = no_of_points * no_of_trials

    # Override standard precision to avoid rounding problems
    decimal.getcontext().prec = 100

    # Calculate the estimated value of Pi
    Pi = decimal.Decimal(4 * total_inside / total_no_of_points)
    print(('The value of Pi is estimated to be %s using %s points' % (+Pi, total_no_of_points) ))
