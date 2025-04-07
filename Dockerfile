FROM python:3.8-slim-buster

# Install AWS CLI
RUN apt update -y && apt install -y awscli

# Set working directory
WORKDIR /app

# Copy requirements first to leverage Docker caching
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install --upgrade accelerate && \
    pip uninstall -y transformers accelerate && \
    pip install transformers accelerate

# Copy remaining code
COPY . .

# Command to run your app
CMD ["python3", "app.py"]
