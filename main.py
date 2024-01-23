import math
import random


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

def init_classification(K,data,d):
    K_Group=[[] for i in range(K)]
    K_centroid = []
    cnt=0;
    for vector in data:
        K_Group[cnt%K].append(vector)
        cnt+=1
    for group in K_Group:
        K_centroid.append(groupmean(group,d))
    return K_Group,K_centroid

def groupmean(group,d):
    mean=[]
    for i in range(d):
        sum=0
        for vector in group:
            sum+=vector[i]
        mean[i] = sum/len(group)
    return mean


def parse_data(raw_data , d , N):
    pass

