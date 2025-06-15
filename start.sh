docker build -t baguette .
docker run -d --restart unless-stopped -e DISCORD_TOKEN=YOUR_DISCORD_TOKEN baguette