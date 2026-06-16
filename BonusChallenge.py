def search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
        
    # Start at top-right corner
    row = 0
    col = len(matrix[0]) - 1
    
    while row < len(matrix) and col >= 0:
        current = matrix[row][col]
        
        if current == target:
            return True
        elif target > current:
            row += 1  # Move down to access larger numbers
        else:
            col -= 1  # Move left to access smaller numbers
            
    return False

# Testing
matrix = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]
target = 5
print(f"Is target {target} in matrix?: {search_matrix(matrix, target)}")