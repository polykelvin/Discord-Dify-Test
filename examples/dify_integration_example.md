# Using Discord Tools Plugin with Dify

This document provides examples of how to integrate the Discord Tools Plugin with Dify applications.

## Setup in Dify

1. Log in to your Dify account
2. Go to the "Plugins" section
3. Click "Add Plugin"
4. Enter the URL of your deployed Discord Tools Plugin
5. Follow the authentication process

## Example: Sending Discord Messages from Dify

### Prompt Template Example

```
You are a helpful assistant that can send messages to Discord.

User input: {{input}}

To send a message to Discord, use the send_discord_message tool.
```

### Tool Configuration

In your Dify application settings, enable the Discord Tools Plugin and configure the `send_discord_message` tool with the following parameters:

- `webhook_url`: Your Discord webhook URL
- `message`: Will be filled by the LLM based on user input
- `title`: Optional title for the message
- `color`: Optional color for the message (e.g., "5865F2" for Discord blue)

### Example Conversation

**User**: "Please send a summary of today's weather forecast to my Discord channel."

**Assistant**: "I'll send a weather forecast summary to your Discord channel. Let me do that for you."

*Assistant uses the send_discord_message tool with:*
- message: "Today's Weather Forecast Summary: Partly cloudy with a high of 72°F (22°C) and a low of 58°F (14°C). 20% chance of rain in the afternoon. Enjoy your day!"
- title: "Weather Forecast"

**Assistant**: "I've sent the weather forecast summary to your Discord channel. Is there anything else you'd like me to do?"

## Example: Reading Discord Messages in Dify

### Prompt Template Example

```
You are a helpful assistant that can read messages from Discord and summarize them.

User input: {{input}}

To read messages from Discord, use the read_discord_messages tool.
```

### Tool Configuration

In your Dify application settings, enable the Discord Tools Plugin and configure the `read_discord_messages` tool with the following parameters:

- `bot_token`: Your Discord bot token (stored securely)
- `channel_id`: The Discord channel ID to read from
- `limit`: Number of messages to retrieve (e.g., 10)

### Example Conversation

**User**: "Can you summarize the last 5 messages from my Discord channel?"

**Assistant**: "I'll retrieve and summarize the last 5 messages from your Discord channel."

*Assistant uses the read_discord_messages tool with limit=5*

**Assistant**: "Here's a summary of the last 5 messages from your Discord channel:

1. John discussed the upcoming team meeting scheduled for Friday at 3 PM.
2. Sarah shared a link to the new project documentation.
3. Mike asked about the deadline for the quarterly report.
4. Lisa confirmed that she completed the customer feedback analysis.
5. Alex shared a meme about programming bugs.

Is there anything specific from these messages you'd like me to elaborate on?"