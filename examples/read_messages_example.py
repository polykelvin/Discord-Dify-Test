import requests
import json

# Replace with your actual plugin endpoint
PLUGIN_URL = "http://localhost:5000"

def read_discord_messages(bot_token, channel_id, limit=10):
    """
    Read messages from a Discord channel using the Discord Tools Plugin
    
    Args:
        bot_token (str): Discord bot token
        channel_id (str): Discord channel ID
        limit (int, optional): Maximum number of messages to retrieve
    
    Returns:
        dict: Response from the plugin containing messages
    """
    payload = {
        "bot_token": bot_token,
        "channel_id": channel_id,
        "limit": limit
    }
    
    response = requests.post(
        f"{PLUGIN_URL}/api/read-messages",
        json=payload
    )
    
    return response.json()

if __name__ == "__main__":
    # Replace with your actual Discord bot token and channel ID
    bot_token = "YOUR_DISCORD_BOT_TOKEN"
    channel_id = "YOUR_DISCORD_CHANNEL_ID"
    
    # Get the last 5 messages
    result = read_discord_messages(bot_token, channel_id, 5)
    
    if result.get("success"):
        print(f"Retrieved {len(result['messages'])} messages:")
        for msg in result["messages"]:
            print(f"[{msg['timestamp']}] {msg['author']['username']}: {msg['content']}")
    else:
        print(f"Error: {result.get('message')}")