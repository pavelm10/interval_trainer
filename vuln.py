"""Intentionally vulnerable sample code for security detection testing.

This file is for testing only. Do not use these patterns in production.
"""
import os
import subprocess


def path_traversal(filename):
    # Unsafe: path traversal by concatenating user-controlled values
    with open(f"/tmp/{filename}", "r") as f:
        return f.read()
