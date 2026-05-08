

def path_traversal(filename):
    # Unsafe: path traversal by concatenating user-controlled values
    with open(f"/tmp/{filename}", "r") as f:
        return f.read()

