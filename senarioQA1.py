def min_distance_to_spots(total_spots, gates):
    spots = [0] * (total_spots + 1)  
    
    total_distance = 0
    
    for gate in gates:
        pos, fishermen = gate
        distances = []
        
        for i in range(1, total_spots + 1):
            if spots[i] == 0:
                distance = abs(pos - i)
                distances.append((distance, i))
        
        distances.sort()
        
        for j in range(fishermen):
            distance, spot = distances[j]
            spots[spot] = 1
            total_distance += distance
    
    return total_distance


# Example Usage:
gates = [(4, 5), (6, 2), (10, 2)]
total_spots = 10
result = min_distance_to_spots(total_spots, gates)
print(f"Total minimum distance: {result} m")
