# Python program to print all paths from a source to destination.

from collections import defaultdict

#This class represents a directed graph
# using adjacency list representation
class Graph:

    def __init__(self,vertices):
        #No. of vertices
        self.V= vertices

        # default dictionary to store graph
        self.graph = defaultdict(list)

    def getGraph(self):
        print(self.graph)

    # function to add an edge to graph
    def addEdge(self, edge):
        self.graph[edge.getFromWhichCity()].append([edge.getToWhichCity(), edge.getCost(), edge.getTime()])
        self.graph[edge.getToWhichCity()].append([edge.getFromWhichCity(), edge.getCost(), edge.getTime()])

    '''A recursive function to print all paths from 'u' to 'd'.
    visited[] keeps track of vertices in current path.
    path[] stores actual vertices and path_index is current
    index in path[]'''
    def printAllPathsUtil(self, start, end, maxTime, visited, path, time, cost):

        # Mark the current node as visited and store in path
        visited[start]= True
        path.append(start)

        # If current vertex is same as destination, then print
        # current path[]
        if start == end:
            sumTime = 0
            for i in time:
                sumTime += i
            # del time[:]
            if sumTime < maxTime:
                sumCost = 0
                for i in cost:
                    sumCost += i
                # del cost[:]
                print path
                print ("time: " + repr(sumTime))
                print ("cost: " + repr(sumCost) +"\n")

            else:
                return

        else:
            # If current vertex is not destination
            #Recur for all the vertices adjacent to this vertex
            for neighbour in self.graph[start]:
                # print(visited)
                if visited[neighbour[0]]==False:
                    time.append(neighbour[2])
                    cost.append(neighbour[1])
                    self.printAllPathsUtil(neighbour[0], end, maxTime, visited, path, time, cost)   

        # Remove current time and cost values from lists
        if time:
            time.pop()
        if cost:
            cost.pop()
        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[start]= False


    # Prints all paths from 'start' to 'end'
    def printAllPaths(self, start, end, maxTime):

        # Mark all the vertices as not visited
        visited =[False]*(self.V)

        # Create an array to store paths
        path = []
        time = []
        cost = []

        # Call the recursive helper function to print all paths
        self.printAllPathsUtil(start, end, maxTime, visited, path, time, cost)

# object which represents one edge of the graph
class Edge:

    fromWhichCity = -1
    toWhichCity = -1
    cost = 0
    time = 0
    number = -1

    def __init__(self, fromWhichCity, toWhichCity, cost, time):
        self.cost = cost
        self.time = time
        self.fromWhichCity = fromWhichCity
        self.toWhichCity = toWhichCity

    def getCost(self):
        return self.cost

    def getTime(self):
        return self.time

    def getFromWhichCity(self):
        return self.fromWhichCity

    def getToWhichCity(self):
        return self.toWhichCity

# Creating eadges
edge0 = Edge(0, 1, 2, 0)
edge1 = Edge(0, 2, 2, 1)
edge2 = Edge(0, 3, 3, 2)
edge3 = Edge(1, 3, 3, 3)
edge4 = Edge(1, 2, 1, 4)

# Create a graph given in the above diagram
g = Graph(4)
g.addEdge(edge0)
g.addEdge(edge1)
g.addEdge(edge2)
g.addEdge(edge3)
g.addEdge(edge4)

start = 2 ; end = 3 ; maxTime = 16

g.printAllPaths(start, end, maxTime)
