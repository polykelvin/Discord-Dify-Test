import requests
import json

# Replace with your actual plugin endpoint
PLUGIN_URL = "http://localhost:5000"

def send_discord_message(webhook_url, message, title=None, color=None):
    """
    Send a message to Discord using the Discord Tools Plugin
    
    Args:
        webhook_url (str): Discord webhook URL
        message (str): Message content to send
        title (str, optional): Title for the message embed
        color (str, optional): Hex color code for the embed (without #)
    
    Returns:
        dict: Response from the plugin
    """
    payload = {
        "webhook_url": webhook_url,
        "message": message
    }
    
    if title:
        payload["title"] = title
    
    if color:
        payload["color"] = color
    
    response = requests.post(
        f"{PLUGIN_URL}/api/send-message",
        json=payload
    )
    
    return response.json()

if __name__ == "__main__":
    # Replace with your actual Discord webhook URL
    webhook_url = "YOUR_DISCORD_WEBHOOK_URL"
    
    # Example message
    message = "Hello from the Discord Tools Plugin for Dify!"
    title = "Test Message"
    color = "5865F2"  # Discord blue color
    
    result = send_discord_message(webhook_url, message, title, color)
    print(json.dumps(result, indent=2))