import math


def Kmeans(K , N , d, iter , raw_data):
    assert K > 1 and K < N and K.isdigit() , "Invalid number of clusters!"
    assert N > 1 and N.isdigit() , "Invalid number of points!"
    assert d.isdigit() , "Invalid dimension number of point!"
    assert iter > 1 and iter < 1000 and iter.isdigit() , "Invalid maximum iteration"

    data = parse_data(raw_data , d , N)
    pass

def Kmeans(K , N , d ,raw_data):
    return Kmeans(K, N ,d, "200" , raw_data)

def euclidean_distance(vector1 , vector2, d):
    square_sum = 0
    for i in range(d):
        square_sum += math.pow(vector1[i] - vector2[i],2)
    return math.sqrt(square_sum)

def init_classification():
    pass

def parse_data(raw_data , d , N):
    pass

