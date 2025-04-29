import heapq

def min_total_connection_cost(cables):
    # Turn the list into a heap
    heapq.heapify(cables)

    total_cost = 0

    while len(cables) > 1:
        # Pop two smallest cables
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        # Combine them
        cost = first + second
        total_cost += cost

        # Push the new combined cable back into the heap
        heapq.heappush(cables, cost)

    return total_cost

# Example
cables = [14, 13, 12, 16, 22, 11, 20, 17]
print(f"Minimum total cost to connect cables: {min_total_connection_cost(cables)}")