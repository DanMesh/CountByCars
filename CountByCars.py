# CountByCars
# Daniel Mesham
# 2 February 2019

import numpy as np
import random

TOTAL_CARS_PASSED = 600
MAX_DIGITS = 6
FRACTION_NON_LOCAL_CARS = 0.2
NON_LOCAL_DIGITS = 3
NUM_TRIALS = 1000

def generate_licence(passed_local_licences = []):
    """Generate a sequence of numbers as they would appear in a licence number"""
    random_frac = random.random()
    if random_frac <= FRACTION_NON_LOCAL_CARS:
        # Use a non-local licence
        licence = random.randint(10 ** (NON_LOCAL_DIGITS-1), 10 ** NON_LOCAL_DIGITS)
        return str(licence), False
    # Use a local licence
    licence = random.randint(1, 10 ** MAX_DIGITS)
    while licence in passed_local_licences:
        licence = random.randint(1, 10 ** MAX_DIGITS)
    return str(licence), True

if __name__ == '__main__':
    results = []
    local_fractions = []
    for t in range(0,NUM_TRIALS):
        licences_with_length = {}
        passed_local_licences = []
        counted_licences = []
        num_local_licences = 0
        count = 1
        for l in range(0, TOTAL_CARS_PASSED):
            licence, is_local = generate_licence()
            licences_with_length[len(licence)] = licences_with_length.get(len(licence), 0) + 1
            if is_local:
                num_local_licences += 1
                passed_local_licences.append(licence)
            if str(count) in licence:
                count += 1
                counted_licences.append(licence)
        results.append(count-1)
        local_fractions.append(num_local_licences/TOTAL_CARS_PASSED)

    print np.mean(results)
