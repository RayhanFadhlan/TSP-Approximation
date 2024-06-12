import heapq

class MstTsp:
    def __init__(self,adj_matrix):
        self.visited = [False] * len(adj_matrix)
        self.path = []
        self.adj_matrix = adj_matrix


    def prim_mst(self,adj_matrix):
        mst = []
        visited = set()
        edges = []
        
        # add start edge
        for to, wt in enumerate(adj_matrix[0]):
            if wt > 0:
                heapq.heappush(edges, (wt, 0, to))
        
        
        while edges:
            wt, frm, to = heapq.heappop(edges)
            if to in visited:
                continue
            visited.add(to)
            mst.append((frm, to, wt))
            for to_next, wt_next in enumerate(adj_matrix[to]):
                if wt_next > 0 and to_next not in visited:
                    heapq.heappush(edges, (wt_next, to, to_next))

        # print(mst)
        # print(self.path)
        return mst


    def dfs(self, city,visited, mst):
        if(visited[city]):
            return
        visited[city] = True
        self.path.append(city)
        for edge in mst:
            if edge[0] == city:
                self.dfs(edge[1],visited, mst)
            elif edge[1] == city:
                self.dfs(edge[0],visited, mst)



    def calculate_tsp_cost(self,path, adj_matrix):
        cost = 0
        for i in range(len(path) - 1):
            cost += adj_matrix[path[i]][path[i + 1]]
        return cost

    def calculate_tsp(self,adj_matrix):
        self.path.clear()
        self.visited = [False] * len(adj_matrix)
        mst = self.prim_mst(adj_matrix)
        self.dfs(0,self.visited,mst)
        self.path.append(0)
        return self.path



    # Below is the 2 opt optimization for approximation tsp
    def alter_tour(self, tour, tour_length):
        n = len(tour)
        for i in range(2, n):
            for j in range(i + 1, n):
                altered_tour = self.swap_2opt(tour, i, j)
                altered_tour_length = self.calculate_tsp_cost(altered_tour, self.adj_matrix)

                if altered_tour_length < tour_length:
                    return self.alter_tour(altered_tour, altered_tour_length)
        return tour

    def swap_2opt(self, tour, i, j):
        new_tour = tour[:i]
        new_tour.extend(reversed(tour[i:j]))
        new_tour.extend(tour[j:])
        return new_tour

# Example usage
# adj_matrix = [
#     [0, 2, 0, 6, 0],
#     [2, 0, 3, 8, 5],
#     [0, 3, 0, 0, 7],
#     [6, 8, 0, 0, 9],
#     [0, 5, 7, 9, 0]
# ]

# adj_matrix2 = [
#     [0,9,75,float('inf'),float('inf')],
#     [9,0,95,19,42],
#     [75,95,0,51,float('inf')],
#     [float('inf'),19,51,0,31],
#     [float('inf'),42,float('inf'),31,0]
# ]

# adj_matrix3 = [
#     [0,2,3,float('inf'),4],
#     [2,0,2,3,float('inf')],
#     [3,2,0,2,2],
#     [float('inf'),3,2,0,3],
#     [4,float('inf'),2,3,0]
# ]


