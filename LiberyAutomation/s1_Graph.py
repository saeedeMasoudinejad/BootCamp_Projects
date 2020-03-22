#mark_nodes = list()
class Graph:
    def __init__(self):
        self.adjList = {}
    def __addSinglevertex(self , node):
        if node not in self.adjList.keys():
            self.adjList[node] = []


    def addVertices(self, nodes):
        if type(nodes) == list:
            for node in nodes:
                self.__addSinglevertex(node)

        elif type(nodes) == str:
            self.__addSinglevertex(nodes)

    def addEdg(self, node1, node2):
        if node1 in self.adjList.keys() and node2 in self.adjList.keys() :
            if node1 in self.adjList[node2]:
                return
            else:
                self.adjList[node1].append(node2)
                self.adjList[node2].append(node1)

    def addWeightEdge(self, node1, node2, weigth):
        if node1 in self.adjList and node2 in self.adjList:
            self.adjList[node1].append((node2, weigth))
            self.adjList[node2].append((node1, weigth))

    def remnode(self, node):
        if node not in self.adjList.keys():
            return
        else:
            for i in self.adjList.values():
                    if node in i:
                        i.remove(node)
        del self.adjList[node]

    def remnode_weigth(self, node):
        for i in self.adjList[node]:
            self.adjList[i[0]].remove((node,i[1]))
        del self.adjList[node]

    def remedge(self, node1, node2):
        if node1 not in self.adjList and node2 not in self.adjList:
            return
        elif node2 in self.adjList[node1] and node1 in self.adjList[node2]:
            self.adjList[node1].remove(node2)
            self.adjList[node2].remove(node1)

    def isConnerct(self):
        nodes = list(self.adjList.keys())
        mark_nodes = []
        visit_node = self.DFS(nodes[0], mark_nodes)
        if len(visit_node) == len(nodes):
            print("This graph is connectet")
        else:
            print("This graph is not connectet")

    def shortestPath(self, node1, node2):
        queue = []
        visited = []
        predesor = {}
        shortestpaht = []
        path = self.BFS(node1, queue, visited, predesor)
        print(path)
        shortestpaht.append(node2)
        while path[node2] != node1:
            shortestpaht.append(path[node2])
            node2 = path[node2]
        shortestpaht.append(node1)
        shortestpaht.reverse()
        print(shortestpaht)

    def PrintGraph(self):
        print(self.adjList)

    def DFS(self, node, mark_nodes):
        if len(self.adjList[node]) == 0:
            mark_nodes.append(self.adjList[node])
            pass
        else:
            mark_nodes.append(node)
            condidate_nodes = self.adjList[node]
            for i in condidate_nodes:
                if i not in mark_nodes:
                    self.DFS(i, mark_nodes)
        return mark_nodes

    def BFS(self, node, queue, visit_node, prede_dic):
        if len(queue) == 0:
            queue.append(node)
        if len(prede_dic) == 0:
            prede_dic[node] = -1
        for j in self.adjList[node]:
            if j not in visit_node and j not in queue and j not in prede_dic:
                queue.append(j)
                prede_dic[j] = node
        visit_node.append(queue.pop(0))
        if len(queue) == 0:
            pass
        else:
            if queue[0] not in visit_node:
                self.BFS(queue[0], queue, visit_node, prede_dic)
            else:
                queue.pop(0)
        return prede_dic











# G1 = Graph()
# G1.addVertices([0,1,2,3,4,5,6,7])
# G1.addEdg(1,0)
# G1.addEdg(0,2)
# G1.addEdg(1,3)
# G1.addEdg(1,4)
# G1.addEdg(2,7)
# G1.addEdg(3,5)
# G1.addEdg(3,6)
# G1.addEdg(4,6)
# G1.addEdg(4,7)
# G1.addEdg(2,7)
# #G1.remedge(0,1)
# G1.PrintGraph()
#
# G1.isConnerct()
# a = list()
# v = list()
# G1.shortestPath(7,1)

g2 = Graph()
g2.addVertices([1,2,3,4])
g2.addWeightEdge(1,2,15)
g2.addWeightEdge(1,3,10)
g2.addWeightEdge(3,2,14)
g2.PrintGraph()
g2.remnode_weigth(2)
g2.PrintGraph()