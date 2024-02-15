# Jordan Scott, David Smical,  & Eli Streitmatter
# AST part 1 CST-301 
import javalang
import json

# Function to convert node to a serializable format
def node_to_dict(node):
    if isinstance(node, javalang.tree.Node):
        # Initialize with node type
        node_dict = {"type": node.__class__.__name__}
        # Iterate through the node attributes
        for attribute in node.__dict__:
            value = getattr(node, attribute)
            if isinstance(value, javalang.tree.Node) or isinstance(value, list):
                node_dict[attribute] = node_to_dict(value)
            elif isinstance(value, set):
                # Convert sets to lists to make them serializable
                node_dict[attribute] = list(node_to_dict(v) for v in value)
            else:
                node_dict[attribute] = value
    elif isinstance(node, list):
        return [node_to_dict(elem) for elem in node]
    else:
        return node
    return node_dict

# Path to the Java file to parse
java_file_path = "/Users/bignola/eclipse-workspace/Exercise2/src/app/Exercise2.java"

# Read the Java code from the file
with open(java_file_path, "r") as file:
    java_code = file.read()

# Parse the Java code to obtain the AST
tree = javalang.parse.parse(java_code)

# Convert the AST to a dictionary
ast_dict = node_to_dict(tree)

# Serialize the dictionary to JSON and write it to a file
json_file_path = "/Users/bignola/Desktop/output_ast.json"  # Adjust this path to your needs
with open(json_file_path, "w") as json_file:
    json.dump(ast_dict, json_file, indent=4)

print(f"AST has been exported to JSON at {json_file_path}")
