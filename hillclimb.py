import optimization
import random

# hill climbing method for optimization.
def hillclimb(domain, costf):
    # create a random solution.
    sol = [random.randint(domain[i][0],domain[i][1])
               for i in range(len(domain))]
    while True:
        # create list of neighboring solutions.
        neighbors = []
        for i in range(len(domain)):
            # choose next flight for this person.
            if sol[i] > domain[i][0]:
                neighbors.append(sol[0:i]+[sol[i]+1]+sol[i+1:])
            # choose previous flight for this person.
            if sol[i] < domain[i][1]:
                neighbors.append(sol[0:i]+[sol[i]-1]+sol[i+1:])
        current = costf(sol)
        best = current
        # find best solution among neighbors.
        for i in range(len(neighbors)):
            cost = costf(neighbors[i])
            if best > cost:
                best = cost
                sol = neighbors[i]
        # if there's no improvement, finish it.
        if best == current:
            break
    return sol

domain = [(0,8)]*(len(optimization.dataset)*2)
sol = hillclimb(domain, optimization.schedulecost)
print (optimization.schedulecost(sol))
            

