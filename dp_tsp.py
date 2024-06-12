
class DpTsp:
    def __init__(self, adj_matrix):
        self.dist = adj_matrix
        self.n = len(adj_matrix)
        self.memo = [[-1] * (1 << self.n) for _ in range(self.n)]
        self.parent = [[-1] * (1 << self.n) for _ in range(self.n)]
        self.final_cost = 0

# dist[i][j] represents shortest distance to go from i to j
# this matrix can be calculated for any given graph using
# all-pair shortest path algorithms

    def fun(self,i, mask):
        # base case: if mask only contains the first node and ith node
        if mask == (1 << i) | 1:
            return self.dist[0][i]

        # memoization
        if self.memo[i][mask] != -1:
            return self.memo[i][mask]

        res = 10**9  # result of this sub-problem
        for j in range(self.n):
            if (mask & (1 << j)) != 0 and j != i and j != 0:
                cost = self.fun(j, mask & (~(1 << i))) + self.dist[j][i]
                if cost < res:
                    res = cost
                    self.parent[i][mask] = j
        self.memo[i][mask] = res  # storing the minimum value
        return res
    def solve(self):
        ans = 10**9
        end_node = -1
        full_mask = (1 << self.n) - 1

        for i in range(1, self.n):
            cost = self.fun(i, full_mask) + self.dist[i][0]
            if cost < ans:
                ans = cost
                end_node = i

        path = self.get_path(end_node, full_mask)
        path.append(0)
        path = path[::-1]
        self.final_cost = ans
        path.append(0)  # adding the starting node to complete the cycle
        return path

    def get_path(self, i, mask):
        path = []
        while i != -1:
            path.append(i)
            next_i = self.parent[i][mask]  # get next node
            mask = mask & ~(1 << i)  # update mask after storing next node
            i = next_i  # move to next node

        return path
    
    def get_cost(self):
        return self.final_cost
    
