import math
import random

def Kmeans(K , N , d, iter , raw_data):
    assert K > 1 and K < N and K.isdigit() , "Invalid number of clusters!"
    assert N > 1 and N.isdigit() , "Invalid number of points!"
    assert d.isdigit() , "Invalid dimension number of point!"
    assert iter > 1 and iter < 1000 and iter.isdigit() , "Invalid maximum iteration"

    data = parse_data(raw_data , d , N)
    K_groups , K_centers = init_classification(K , data , d)


    pass

def Kmeans(K , N , d ,raw_data):
    return Kmeans(K, N ,d, "200" , raw_data)

def euclidean_distance(vector1 , vector2):
    square_sum = 0
    for i in range(len(vector1)):
        square_sum += math.pow(vector1[i] - vector2[i],2)
    return math.sqrt(square_sum)


def init_classification(K , data , d):
    pass

def init_classification(K,data,d):
    K_Group=[[] for i in range(K)]
    K_centroid = []
    cnt=0
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
    raw_data_lines = [line.rstrip() for line in raw_data]
    data = []
    for line in raw_data_lines:
        print(line)
        data.append([float(x) for x in line.split(",")])
    return data

def move_to_closest(vector, K_centroids, newgroups , current_group):
    distances = [euclidean_distance(vector, K_centroids[i]) for i in range(len(K_centroids))]
    min_dist = min(distances)
    min_index = distances.index(min_dist)
    if euclidean_distance(K_centroids[min_dist],K_centroids[current_group]) < 0.001 or min_index == current_group:
        newgroups[current_group].append(vector)
        return False
    else:
        newgroups[min_index].append(vector)
        return True

