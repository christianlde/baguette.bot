# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Copy the bot script and the requirements.txt into the container
COPY bot.py /app
COPY requirements.txt /app

# Install the dependencies from the requirements.txt
RUN pip install -r requirements.txt

# Command to run the bot
CMD ["python", "bot.py"]
