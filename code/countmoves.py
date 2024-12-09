import sys

def count_moves_in_file(filename):
    with open(filename, 'r') as file:
        for i, line in enumerate(file, start=1):
            # Remove leading/trailing whitespace and split the line by spaces to get individual moves
            moves_list = line.strip().split()
            # Count the moves in the current line
            num_moves = len(moves_list)
            print(f"Line {i}: {num_moves} moves")

if __name__ == "__main__":
    # Ensure a filename is provided
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    count_moves_in_file(filename)

