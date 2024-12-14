def count_xmas_in_file(file_path):
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file.readlines()]  # Read and strip lines

    word = "XMAS"
    word_len = len(word)
    total_count = 0

    # Convert the grid into a 2D character array
    grid = [list(line) for line in lines]
    rows = len(grid)
    cols = max(len(line) for line in grid)

    # Pad rows to ensure equal lengths
    grid = [line + [' '] * (cols - len(line)) for line in grid]

    # Directions for searching: (row_delta, col_delta)
    directions = [
        (0, 1),   # Right (horizontal)
        (0, -1),  # Left (reverse horizontal)
        (1, 0),   # Down (vertical)
        (-1, 0),  # Up (reverse vertical)
        (1, 1),   # Diagonal Down-Right
        (1, -1),  # Diagonal Down-Left
        (-1, 1),  # Diagonal Up-Right
        (-1, -1)  # Diagonal Up-Left
    ]

    def search_word(start_row, start_col, delta_row, delta_col):
        """Search for the word in the specified direction starting from a position."""
        count = 0
        for i in range(word_len):
            row, col = start_row + i * delta_row, start_col + i * delta_col
            if not (0 <= row < rows and 0 <= col < cols) or grid[row][col] != word[i]:
                return 0
        return 1

    # Iterate through all starting positions in the grid
    for row in range(rows):
        for col in range(cols):
            # Search in all 8 possible directions from the current position
            for delta_row, delta_col in directions:
                total_count += search_word(row, col, delta_row, delta_col)

    print("Total occurrences of 'XMAS':", total_count)
    return total_count

# File path
file_path = 'day4/input.txt'
count_xmas_in_file(file_path)