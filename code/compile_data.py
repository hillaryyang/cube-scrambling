# define file paths
scramble_file = 'scrambles.txt'
solve_len_file = 'solved_len.txt'
output_file = 'solved_len_data.txt'

# read scrambles (53 m cubes)
with open(scramble_file, 'r') as f_scramble:
    scrambles = f_scramble.readlines()

# read solved lengths (53 m cubes)
with open(solve_len_file, 'r') as f_num:
    sol_len = f_num.readlines()

# check if both files have the same number of lines
if len(scrambles) != len(sol_len):
    print("Error: The number of lines in 'scrambles.txt' and 'solved_len.txt' do not match.")
    exit(1)

# write the output to solved_len_data.txt
with open(output_file, 'w') as f_output:
    for scramble, sol_len in zip(scrambles, sol_len):
        scramble = scramble.strip()
        sol_len = sol_len.strip()
        length = len(scramble.split())
        f_output.write(f"{scramble},{length},{sol_len}\n")

print(f"Data written to {output_file}")
