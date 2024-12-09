import sys

def inverse_moves(moves):
    # Dictionary to map a move to its inverse
    inverse = {
        'F1': 'F3', 'F2': 'F2', 'F3': 'F1',
        'L1': 'L3', 'L2': 'L2', 'L3': 'L1',
        'R1': 'R3', 'R2': 'R2', 'R3': 'R1',
        'B1': 'B3', 'B2': 'B2', 'B3': 'B1',
        'U1': 'U3', 'U2': 'U2', 'U3': 'U1',
        'D1': 'D3', 'D2': 'D2', 'D3': 'D1'
    }

    # Split the input moves into a list
    moves_list = moves.split()

    # Reverse the list and apply the inverse to each move
    inverse_list = [inverse[move] for move in reversed(moves_list)]

    # Join the inverse moves into a string
    return ' '.join(inverse_list)

def process_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Process each line to get the inverse moves
    for line in lines:
        line = line.strip()
        if line:  # Ensure the line is not empty
            inversed_line = inverse_moves(line)
            print(inversed_line)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py input_file")
    else:
        input_file = sys.argv[1]
        process_file(input_file)

