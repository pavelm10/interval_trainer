"""Intentionally vulnerable sample code for security detection testing.

This file is for testing only. Do not use these patterns in production.
"""
import os
import subprocess


HARD_CODED_SECRET = "SuperSecretPassword123"


def use_hard_coded_secret():
    # Unsafe: hard-coded credentials / secrets
    return HARD_CODED_SECRET


def command_injection(user_command):
    # Unsafe: shell injection via untrusted input
    os.system(f"echo Running: {user_command}")


def subprocess_injection(user_command):
    # Unsafe: using shell=True with untrusted input
    subprocess.run(user_command, shell=True)


def path_traversal(filename):
    # Unsafe: path traversal by concatenating user-controlled values
    with open(f"/tmp/{filename}", "r") as f:
        return f.read()
