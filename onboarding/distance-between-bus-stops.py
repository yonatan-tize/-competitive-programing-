class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start
        
        a = sum(distance[start:destination])
        return min(a, sum(distance)-a )
        

