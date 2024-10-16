import math

#author: ukerma

# Euclidean distance function
def euclideanDistance(point1, point2):
    # Returns the Euclidean distance between two points
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Definition of points
points = [(1, 2), (4, 6), (5, 9), (8, 2)]

# List to store distances
distances = []

# Calculate the distance between each pair of points
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Find the minimum distance
min_distance = min(distances)

# Print the results
print("All distances:", distances)
print("Minimum distance:", min_distance)
