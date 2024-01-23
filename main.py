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

def move(ind , org_K_group, target_K_group):
    item = org_K_group.pop(ind)
    target_K_group.append(item)
    return

def move_to_closest(vector, K_centroids, newgroups):
    distances = [euclidean_distance(vector, K_centroids[i]) for i in range(len(K_centroids))]
    x = min(distances)
    if x < 0.001:
        return False

print(parse_data(open("C:/Users/Roy Dahan/Desktop/לימודים/פרויקטו/tests/input_1.txt",mode="r"),3 , 5))
