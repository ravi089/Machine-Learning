# Recommendation System.
from math import sqrt

movies={}
preferences={}

# parse data from file into dictionary.
def readfiles():
    # movies['movieid'--'moviename']
    with open('movies.txt',encoding='latin-1') as file:
        lines=[line for line in file]
        for line in lines[1:]:
            data=line.strip().split(',')
            movies[data[0]]=data[1]
    # users['userid'--'movieid'--'rating']
    with open('ratings.txt',encoding='latin-1') as obj:
        lines=[line for line in obj]
        for line in lines[1:]:
            data=line.strip().split(',')
            userid=data[0]
            movieid=data[1]
            rating=float(data[2])
            preferences.setdefault(userid,{})
            preferences[userid][movieid]=rating

# calculating similarity using pearson coefficient.
def similarity(preferences, person1, person2):
    # get the list of all shared items.
    shared_items = {}
    for item in preferences[person1]:
        if item in preferences[person2]:
            shared_items[item] = 1
    # if there are no shared items, then return 0.
    num_items = len(shared_items)
    if num_items == 0:
        return 0
    # summation.
    sum1 = sum([preferences[person1][item] for item in shared_items])
    sum2 = sum([preferences[person2][item] for item in shared_items])
    # squares summation.
    ssum1 = sum([pow(preferences[person1][item],2) for item in shared_items])
    ssum2 = sum([pow(preferences[person2][item],2) for item in shared_items])
    # product summation.
    psum = sum([preferences[person1][item]*preferences[person2][item] for item in shared_items])
    # pearson corelation coeff.
    num = psum - (sum1 * sum2/num_items)
    den = sqrt((ssum1 - pow(sum1,2)/num_items)*(ssum2 - pow(sum2,2)/num_items))
    if den == 0:
        return 0
    r = num/den
    return r
    
# get recommendations for a person by using a weighted average
# of every other user's rankings.
def recommendations(preferences, person):
    totalscores = {}
    similaritysum = {}
    # for every other person in the set.
    for other in preferences:
        if other == person:
            continue
        # get similarity between these two.
        simscore = similarity(preferences, person, other)
        if simscore <= 0:
            continue
        # for all items rated by this person which were not
        # rated by me calculate the weighted average.
        for item in preferences[other]:
            if item not in preferences[person] or preferences[person][item] == 0:
                totalscores.setdefault(item, 0)
                totalscores[item] += preferences[other][item] * simscore
                similaritysum.setdefault(item, 0)
                similaritysum[item] += simscore
    # create a normalized list.
    ratings = [(totalscore/similaritysum[item], movies[item]) for (item,totalscore) in totalscores.items()]
    ratings.sort()
    ratings.reverse()
    return ratings[0:10]

if __name__ == '__main__':
    readfiles()
    topmovies = recommendations(preferences,'1')
    for movie in topmovies:
        print (movie)
