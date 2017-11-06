# Group of friends from all over the country are planning a trip
# together in New york. They will all arrive on the same day and
# leave on the same day and they would like to share transportation
# to and from the airport so as to minimize the cost for the trip.
import time
import random
import math
from datetime import datetime
from datetime import timedelta

# person <--> origin
dataset = [('Arnold', 'BOS'),
           ('Genie', 'DAL'),
           ('Elvin', 'CAK'),
           ('Phoenix', 'MIA'),
           ('Tesla', 'ORD'),
           ('John', 'OMA')]

# final destination.
destination = 'LGA'

flights = {}
# parse file for flight details.
file = open('schedule.txt', 'r')
lines = [line for line in file]
for line in lines:
    origin,dest,depart,arrive,price = line.strip().split(',')
    flights.setdefault((origin, dest), [])
    flights[(origin,dest)].append((depart,arrive,int(price)))

# get time in minutes in a day.
def getminutes(t):
    x = time.strptime(t,'%H:%M')
    return x[3]*60 + x[4]

# get difference between two times in minutes.
def getdifference(t1,t2):
    tdiff = datetime.strptime(t2,'%H:%M') - datetime.strptime(t1,'%H:%M')
    if tdiff.days < 0:
        tdiff = timedelta(days = 0, seconds = tdiff.seconds,
                          microseconds = tdiff.microseconds)
    return ((tdiff.seconds)/60)

# solution is in a form [1,4,3,2,7,3,6,3,2,4,5,3] i.e
# Arnold has taken 2nd flight in a day for way to New york.
# and took 5th flight return journey home.
def printschedule(sol):
    for idx in range(int(len(sol)/2)):
        name = dataset[idx][0]
        origin = dataset[idx][1]
        out = flights[(origin,destination)][sol[idx]]
        ret = flights[(destination,origin)][sol[idx+1]]
        print ('%10s%10s %5s-%5s $%3s %5s-%5s $%3s' % (name,origin,
                                                      out[0],out[1],out[2],
                                                      ret[0],ret[1],ret[2]))

# cost function for evaluating the cost of schedule.
# parameters chosen are :-
# 1) total cost of flight tickets.
# 2) total time spent on flights.
# 3) total wait time at airport for every person.
# 4) whether to rent a car for an extra day.
def schedulecost(sol):
    totalprice = 0
    totaltime = 0
    latestarrival = 0
    earliestdep = 24*60

    for idx in range(int(len(sol)/2)):
        # get inbound and outbound flights.
        origin = dataset[idx][1]
        outbound = flights[(origin,destination)][sol[idx]]
        returnf = flights[(destination,origin)][sol[idx+1]]

        # calculate total amount spent on flight tickets.
        totalprice += outbound[2]
        totalprice += returnf[2]

        # calculate total time spent on flights during journey.
        totaltime += getdifference(outbound[0], outbound[1])
        totaltime += getdifference(returnf[0], returnf[1])
        
        # get lastest arrival and earliest departure.
        if latestarrival < getminutes(outbound[1]):
            latestarrival = getminutes(outbound[1])
        if earliestdep > getminutes(returnf[0]):
            earliestdep = getminutes(returnf[0])
    # calculate total time spent waiting for flights.
    totalwait = 0
    for idx in range(int(len(sol)/2)):
        origin = dataset[idx][1]
        outbound = flights[(origin,destination)][sol[idx]]
        returnf = flights[(destination,origin)][sol[idx+1]]
        totalwait += latestarrival - getminutes(outbound[1])
        totalwait += getminutes(returnf[0]) - earliestdep

    # if car needs to be rented for an extra day.
    if latestarrival > earliestdep:
        totalprice += 50
        
    return totalprice + totalwait + totaltime
