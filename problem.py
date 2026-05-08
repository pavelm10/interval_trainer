
def path_traversal(filename):
    # Unsafe: path traversal by concatenating user-controlled values
    with open(f"/tmp/{filename}", "r") as f:
        return f.read()


def sql_injection_example(username, password):
    # Unsafe: string formatting into SQL queries
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    return query


HARD_CODED_SECRET = "SuperSecretPassword123"


def use_hard_coded_secret():
    # Unsafe: hard-coded credentials / secrets
    return HARD_CODED_SECRET