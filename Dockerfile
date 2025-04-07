FROM python:3.8-slim-buster

# Install required build tools and awscli
RUN apt update -y && apt install -y \
    gcc \
    g++ \
    make \
    awscli \
    libz-dev

# Set working directory
WORKDIR /app

# Copy source code
COPY . /app

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Reinstall transformers and accelerate (if needed)
RUN pip install --upgrade accelerate
RUN pip uninstall -y transformers accelerate && pip install transformers accelerate

# Run the app
CMD ["python3", "app.py"]
