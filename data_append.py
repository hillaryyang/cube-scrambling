# Define file paths
scramble_file = 'sf_append.txt'
num_file = 'num'
output_file = 'data.txt'

# Read scramble sequences
with open(scramble_file, 'r') as f_scramble:
    scrambles = f_scramble.readlines()

# Read data from master
with open(num_file, 'r') as f_num:
    numbers = f_num.readlines()

# Check if both files have the same number of lines
if len(scrambles) != len(numbers):
    print("Error: The number of lines in '53M.2' and 'master.num' do not match.")
    exit(1)

# Write the output to data.txt≈
with open(output_file, 'w') as f_output:
    for scramble, number in zip(scrambles, numbers):
        scramble = scramble.strip()
        number = number.strip()
        length = len(scramble.split())
        f_output.write(f"{scramble},{length},{number}\n")

print(f"Data written to {output_file}")
