import sys
import re
import itertools

# Initial file reading
layers = 0
total_edges = 0
widths = []
in_layers = []
edges = []
matrix = []

# Organized dictionaries
edge_dict = {}
layer_edges = {}
layer_dict = {}

# Stored indexes for easy access
indexes1 = []
indexes2 = []

# Keep track of optimization for pruning
optimization = 0


# Process each line and put the data into appropriate variable as integers for faster processing
def process_line(line):
    if "layers" in line:
        # Get the number of layers
        layer = re.findall('\d+', line)
        global layers
        layers = int(layer[0])
    elif "width" in line:
        # Get width of each row
        width = re.findall('\d+', line)
        widths.append(list(map(int, width)))
    elif "in_layer" in line:
        layer = re.findall('\d+', line)
        in_layers.append(list(map(int, layer)))
    else:
        global total_edges
        total_edges = total_edges + 1
        edge = re.findall('\d+', line)
        edges.append(list(map(int, edge)))
    return;


# Organize the data for easy use
def process_data():

    # Sort the edges into a dictionary
    edges.sort(key = lambda i: i[0])
    for x in edges:
        edge_dict.setdefault(x[0], []).append(x)

    # TODO Organize the edges by layer


    # Sort the nodes per layer into a dictionary
    for y in in_layers:
        layer_dict.setdefault(y[0], []).append(y[1])

    return;


# Evaluate each permutation to see for a proper match
def evaluate2(perm1, perm2):
    global optimization
    for x in perm1:
        for y in perm2:

            # TODO Check each edge to see for crossing
            layer_len = len(x)



            return;


# Generates the permutations per layer
def permute():
    # Reformat the data for easier use
    process_data()
    # Permute each layer
    for i in range(layers):
        if i == 0 | i == 1:
            layer_permutations1 = list(itertools.permutations(layer_dict.get(i)))
            layer_permutations2 = list(itertools.permutations(layer_dict.get(i + 1)))
            evaluate2(layer_permutations1, layer_permutations2)
        else:
            layer_permutations = list(itertools.permutations(layer_dict.get(i)))

            # TODO evaluate successive layers

    return;


if __name__ == "__main__":
    # Take the file in as input
    inputFile = './input/input_01.txt'
    #inputFile = sys.argv[1]

    # Open the file for reading
    with open(inputFile, 'r') as fileObj:
        # Loop through and read the file line by line processing layers, widths, and edges
        while True:
            line = fileObj.readline()
            if not line:
                break
            # Process the input
            process_line(line)
    # Close the file
    fileObj.closed
    permute()