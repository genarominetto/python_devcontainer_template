# main.py
# This script prints "Hello, World!" and checks for the 'boto3' package.
# If 'boto3' is not installed, it raises an error with an instruction to install it.

try:
    import boto3
except ImportError:
    raise ImportError("The 'boto3' package is required. Please install it using 'pip install boto3'.")

print("Hello, World!")
