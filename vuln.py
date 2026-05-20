"""Intentionally vulnerable sample code for security detection testing.

This file is for testing only. Do not use these patterns in production.
"""
import os
import subprocess


def eval_user_input(user_input):
    # Unsafe: directly evaluating untrusted input
    return eval(user_input)


def command_injection(user_command):
    # Unsafe: shell injection via untrusted input
    os.system(f"echo Running: {user_command}")