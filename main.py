import math
import sys


def Kmeans(K, N, d, iter, raw_data):
    assert int(K) > 1 and int(K) < int(N) and K.isdigit(), "Invalid number of clusters!"
    assert int(N) > 1 and N.isdigit(), "Invalid number of points!"
    assert d.isdigit(), "Invalid dimension number of point!"
    assert int(iter) > 1 and int(iter) < 1000 and iter.isdigit(), "Invalid maximum iteration"
    K, N, d, iter = int(K), int(N), int(d), int(iter)
    data = parse_data(raw_data, d, N)
    K_groups, K_centers = init_classification(K, data, d)

    for cnt in range(iter):
        move_flag = False
        newgroups = [[] in range(K)]
        for i in range(K):
            for vector in K_groups[i]:
                move_flag = move_flag or move_to_closest(vector, K_centers, newgroups, i)
        if (not move_flag):
            break
        K_groups = newgroups
    return K_groups


def euclidean_distance(vector1, vector2):
    square_sum = 0
    for i in range(len(vector1)):
        square_sum += math.pow(vector1[i] - vector2[i], 2)
    return math.sqrt(square_sum)


def init_classification(K, data, d):
    pass


def init_classification(K, data, d):
    K_Group = [[] for i in range(K)]
    K_centroid = []
    cnt = 0
    for vector in data:
        K_Group[cnt % K].append(vector)
        cnt += 1
    for group in K_Group:
        K_centroid.append(groupmean(group, d))
    return K_Group, K_centroid


def groupmean(group, d):
    mean = []
    for i in range(d):
        sum = 0
        for vector in group:
            sum += vector[i]
        mean[i] = sum / len(group)
    return mean


def parse_data(raw_data, d, N):
    raw_data_lines = [line.rstrip() for line in raw_data]
    data = []
    for line in raw_data_lines:
        print(line)
        data.append([float(x) for x in line.split(",")])
    return data


def move(ind, org_K_group, target_K_group):
    item = org_K_group.pop(ind)
    target_K_group.append(item)
    return


def move_to_closest(vector, K_centroids, newgroups, current_group):
    distances = [euclidean_distance(vector, K_centroids[i]) for i in range(len(K_centroids))]
    min_dist = min(distances)
    min_index = distances.index(min_dist)
    if euclidean_distance(K_centroids[min_dist], K_centroids[current_group]) < 0.001 or min_index == current_group:
        newgroups[current_group].append(vector)
        return False
    else:
        newgroups[min_index].append(vector)
        return True


def main():
    args = sys.argv[1:]
    if len(args) == 5:
        print(Kmeans(args[0], args[1], args[2], args[3], args[4]))
    else:
        print(Kmeans(args[0], args[1], args[2], args[3]))
