from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 拓扑排序：将入度为零的节点先都加入队列中,然后遍历队列取出的同时将当前节点指向的另一个节点的入度减一，如果另一个节点此时的入度也为零那么就加入队列，需要用到邻接表来查询当前节点所连向的后续节点。
        # O(M+N) Z(M+N)
        ind = [0]*(numCourses)
        adj = [[] for _ in range(numCourses)]
        queue = deque()
        for cur, pre in prerequisites:
            ind[cur] += 1
            adj[pre].append(cur)
        for i in range(numCourses):
            if not ind[i]:
                queue.append(i)
        # BFS
        while queue:
            pre = queue.popleft()
            numCourses -= 1
            for cur in adj[pre]:
                ind[cur] -= 1
                if not ind[cur]:
                    queue.append(cur)
        
        return not numCourses
        