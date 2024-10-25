# .devcontainer/Dockerfile
# This Dockerfile sets up a Python 3.9 environment with a non-root user.

# Use the official Python 3.9 image as the base
FROM python:3.9

# Install necessary packages
RUN apt-get update && apt-get install -y \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user 'vscode' with sudo access
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# Set the user to 'vscode'
USER $USERNAME

# Set the working directory
WORKDIR /workspace
