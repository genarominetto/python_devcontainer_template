# Use an official Python image as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /workspace

# Install any additional dependencies
RUN pip install --upgrade pip

# Set up a non-root user (optional but recommended for security)
RUN useradd -m vscode &&     chown -R vscode /workspace

# Switch to the new user
USER vscode

# Set environment variables for the container
ENV PYTHONUNBUFFERED=1
