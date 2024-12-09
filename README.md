# cube-scrambling
We implement the simulation of the scrambling and solving of many Rubik's cubes to provide the first lower bound on the [cube scrambling problem](https://theconversation.com/how-hard-is-it-to-scramble-rubiks-cube-129916).

## Source Code
Source code is located in GitHub at the link: [https://github.com/hillaryyang/cube-scrambling](https://github.com/hillaryyang/cube-scrambling)

## Repository Structure
* `code/`: code that compiles data 
* `data/`: sample of intermediary raw data
* `data_processing/`: calculates probability distributions and TVD

## Background
A good description of the problem can be found here: [https://theconversation.com/how-hard-is-it-to-scramble-rubiks-cube-129916](https://theconversation.com/how-hard-is-it-to-scramble-rubiks-cube-129916). We use the [half turn metric](https://www.speedsolving.com/wiki/index.php?title=Metric) in Rubik's cube solving. General notation information can be found [here](https://ruwix.com/the-rubiks-cube/notation/). 

## Installation
1. Clone the repository:
```
git clone https://github.com/hillaryyang/cube-scrambling.git
cd cube-scrambling
```

2. Create and activate venv:
```
python -m venv ~/env
source ~/env/bin/activate  
```

3. Install dependencies:
```
pip install -r requirements.txt
```

## Usage
1. For our scrambles, we use a file of 53 million randomly generated scrambles, named `scrambles.txt`:
* (1) For each number n between 1 and 52, we have 1 million sequences of moves of length n 
* (2) The last million cubes are of random length and are used to generate the baseline probability distribution.

2. To solve these cubes optimally, we use Tomas Rokicki's Two-Phase solver, [nxopt](https://github.com/rokicki/cube20src) to generate `solved_len.txt`, a file with 53 million lines, each containing a single integer: the number of moves taken to optimally solve the corresponding scramble in `scrambles.txt`.

3. Run `python3 code/compile_data.py` to generate a file `solved_len_data.txt`. This file contains three columns:
* `scramble`: the scramble/sequence of moves itself
* `length`: the length of the scramble in the half turn metric, an integer between 1 and 52
* `distance`: the optimal solution length, an integer between 0 and 20

**Important** The last million cubes are scrambles of random length, which are used for generating the "baseline" probability distribution. They -1 in the length field.

4. Run `python3 code/gen_distrib.py` which converts `solved_len_data.txt` into probability distributions for each length (-1 for the baseline, and between 1 and 53). These distributions can be found [here](https://github.com/hillaryyang/cube-scrambling/blob/main/data/df_dis.csv).

For each scramble length (1 to 53), calculate the TVD (sum of 0.5 * absolute difference). Optionally, generate a graph that plots scramble length against TVD.