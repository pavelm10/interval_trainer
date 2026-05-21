
HARD_CODED_SECRET = "SuperSecretPassworda123"


def use_hard_coded_secret():
    # Unsafe: hard-coded credentials / secrets
    return HARD_CODED_SECRET



def path_traversal(filename):
    # Unsafe: path traversal by concatenating user-controlled values
    with open(f"/tmp/{filename}", "r") as f:
        return f.read()
