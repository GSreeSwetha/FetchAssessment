#!/bin/bash

# Update package index
sudo apt update

# Install required dependencies
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common

# Add Docker GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Add Docker repository to APT sources
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Update package index again
sudo apt update

# Install Docker
sudo apt install -y docker-ce

# Start and enable Docker service
sudo systemctl start docker
sudo systemctl enable docker

# Add the user to the docker group
sudo usermod -aG docker ubuntu

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Install python3-pip
sudo apt install -y python3-pip

# Install awscli-local
pip3 install awscli-local

# Install psycopg2-binary
pip3 install psycopg2-binary

# Install docker Python package
pip3 install docker

# Print versions
echo "Docker version:"
docker --version
echo "Docker Compose version:"
docker-compose --version
echo "Python version:"
python3 --version
echo "pip version:"
pip3 --version
echo "awscli-local installed"
