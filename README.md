# Discord Tools Plugin for Dify

This plugin allows Dify users to interact with Discord by sending messages to Discord channels and reading messages from Discord channels.

## Features

- **Send Discord Message**: Send messages to Discord channels using webhook URLs
- **Read Discord Messages**: Read messages from Discord channels using a bot token and channel ID

## Setup

### Prerequisites

- Python 3.9 or higher
- Discord webhook URL (for sending messages)
- Discord bot token with appropriate permissions (for reading messages)
- Discord channel ID (for reading messages)

### Installation

1. Clone this repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the server:
   ```
   python server.py
   ```

## Usage

### In Dify

1. Add this plugin to your Dify instance
2. Configure the plugin with your Discord credentials
3. Use the tools in your Dify applications

### Send Discord Message

This tool allows you to send messages to a Discord channel using a webhook URL.

Parameters:
- `webhook_url` (required): Discord webhook URL for the channel
- `message` (required): Message content to send to Discord
- `title` (optional): Title for the message embed
- `color` (optional): Hex color code for the embed (without #)

### Read Discord Messages

This tool allows you to read messages from a Discord channel using a bot token and channel ID.

Parameters:
- `bot_token` (required): Discord bot token with permissions to read messages
- `channel_id` (required): Discord channel ID to read messages from
- `limit` (optional): Maximum number of messages to retrieve (default: 10)

## Discord Bot Setup

To use the "Read Discord Messages" feature, you need to create a Discord bot:

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application
3. Navigate to the "Bot" tab and create a bot
4. Enable the "Message Content Intent" under Privileged Gateway Intents
5. Copy the bot token for use with this plugin
6. Invite the bot to your server using the OAuth2 URL generator with the "bot" scope and "Read Messages" permission

## Docker Support

You can also run this plugin using Docker:

```
docker build -t discord-tools-plugin .
docker run -p 5000:5000 discord-tools-plugin
```