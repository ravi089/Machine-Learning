import random
import optimization

# search for best solution by creating random
# solutions and checking their cost.
def randomsearch(domain, costf):
    best = 999999999
    bestsol = None
    # random number of iterations.
    for i in range(1000):
        # create a random solution.
        sol = [random.randint(domain[i][0],domain[i][1])
                 for i in range(len(domain))]
        # calculate the cost.
        cost = costf(sol)
        if best > cost:
            best = cost
            bestsol = sol
    return sol

# for each person there are 9 outbound and inbound flights.
domain = [(0,8)]*(len(optimization.dataset)*2)
sol = randomsearch(domain, optimization.schedulecost)
print (optimization.schedulecost(sol))

