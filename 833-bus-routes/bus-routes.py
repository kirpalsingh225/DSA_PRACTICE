from collections import deque
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        adj = {}
        for i in range(len(routes)):
            for stop in routes[i]:
                if stop not in adj:
                    adj[stop] = []
                adj[stop].append(i)

        q = deque()
        visited_routes = set()
        visited_stops = set()
        visited_stops.add(source)

        for route in adj.get(source, []):
            if route not in visited_routes:
                visited_routes.add(route)
                q.append(route)

        bus = 1
        while q:
            size = len(q)

            for _ in range(size):
                route = q.popleft()

                for stop in routes[route]:
                    if stop == target:
                        return bus

                    if stop not in visited_stops:
                        visited_stops.add(stop)
                        for neighbor_route in adj[stop]:
                            if neighbor_route not in visited_routes:
                                visited_routes.add(neighbor_route)
                                q.append(neighbor_route)

            bus += 1

        return -1