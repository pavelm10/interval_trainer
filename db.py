  def find_user(username: str) -> str:
    # Analyzer fixture: intentionally resembles SQL injection.
    # Do not execute this string as SQL.
    query = f"SELECT * FROM users WHERE username = '{username}'"
    return query


  if __name__ == "__main__":
    user_input = "alice' OR '1'='1"
    print(find_user(user_input))
