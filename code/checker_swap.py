import sys

def swap_positions(cube_state):
    # Define the swap mapping
    swap_map = {
        'U': 'D', 'D': 'U',
        'F': 'B', 'B': 'F',
        'L': 'R', 'R': 'L'
    }
    
    # Function to swap each face of the cube state if it's two letters long
    def swap_face(face):
        if len(face) == 2:
            return ''.join(swap_map.get(char, char) for char in face)
        return face  # Leave three-letter words unchanged
    
    # Split the cube state into individual positions
    positions = cube_state.split()
    
    # Apply the swap to each position
    swapped_positions = [swap_face(pos) for pos in positions]
    
    return ' '.join(swapped_positions)

def main():
    # Check if a filename was provided
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
        return
    
    # Read the file specified in argv[1]
    filename = sys.argv[1]
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Remove any leading/trailing whitespace and perform the swap
                swapped_line = swap_positions(line.strip())
                print(swapped_line)
    except FileNotFoundError:
        print(f"File not found: {filename}")

if __name__ == "__main__":
    main()

