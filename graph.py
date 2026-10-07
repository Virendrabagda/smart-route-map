
import heapq
from database import connection
class graph:

    def __init__(self,V):
        self.V = V
        self.graph = [[]for _ in range(V)]
    def addedge(self,u,v,distance):
        self.graph[u].append((v, distance))
        self.graph[v].append((u, distance))
    def printgraph(self):
        for i in range(self.V):
            print(i,"->",end=" ")
            for v, distance in self.graph[i]:
                print((v, distance),end=" ")
            print()

    def dijkstra(self , src):
        distance = [float('inf')]*self.V
        distance[src]=0
        parent = [-1] * self.V
        pq = [(0,src)]
        while pq:
            current_distance, node = heapq.heappop(pq) 
            for v, wt in self.graph[node]: 
                newDist = current_distance + wt 
                if newDist < distance[v]: 
                    distance[v] = newDist 
                    parent[v] = node;
                    heapq.heappush(pq, (newDist, v)) 
        return distance,parent

cursor = connection.cursor()

cursor.execute("SELECT id, name FROM cities")

cities_data = cursor.fetchall()
cursor.close()    
city_index = {}

cities = {} 
for city_id, city_name in cities_data: 
    cities[city_id - 1] = city_name

for city_id, city_name in cities_data:
    city_index[city_name.lower()] = city_id - 1

cursor = connection.cursor()

cursor.execute("SELECT source_id, destination_id, distance FROM routes")

routes = cursor.fetchall()
cursor.close()


g = graph(6)
for source, destination, distance in routes:
    g.addedge(source - 1, destination - 1, distance)


# g.printgraph()
# print("Available Cities:")

# for city_id, city_name in cities_data:
#     print(city_name)
# source_city = input("Aap abhi kahan ho? ").strip().lower()
# destination_city = input("Aapko kahan jana hai? ").strip().lower()

# source = city_index[source_city]
# destination = city_index[destination_city]

# distance, parent = g.dijkstra(source)

# # print("Distance:", distance)
# # print("Parent:", parent)

# path = []
# node = destination

# while node != -1:
#     path.append(node)
#     node = parent[node]

# path.reverse()

# print("Shortest Route:")

# for i in range(len(path)):
#     print(cities[path[i]], end="")

#     if i < len(path) - 1:
#         print(" → ", end="")

# print()

# print("Distance:", distance[destination], "km")