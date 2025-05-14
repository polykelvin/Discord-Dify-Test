import os
import json
from flask import Flask, request, jsonify
import requests
from discord_webhook import DiscordWebhook, DiscordEmbed

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Discord Tools Plugin for Dify is running!'

@app.route('/manifest', methods=['GET'])
def manifest():
    with open('./manifest.json', 'r') as f:
        manifest = json.load(f)
    return jsonify(manifest)

@app.route('/api/send-message', methods=['POST'])
def send_message():
    """Send a message to a Discord channel using webhook URL"""
    try:
        data = request.json
        webhook_url = data.get('webhook_url')
        message = data.get('message')
        title = data.get('title', 'Message from Dify')
        color = data.get('color', '03b2f8')  # Default Discord blue color
        
        if not webhook_url or not message:
            return jsonify({
                'success': False,
                'message': 'webhook_url and message are required'
            }), 400
        
        # Create webhook instance
        webhook = DiscordWebhook(url=webhook_url)
        
        # Create embed object
        embed = DiscordEmbed(title=title, description=message, color=color)
        
        # Add embed object to webhook
        webhook.add_embed(embed)
        
        # Execute webhook
        response = webhook.execute()
        
        if response.status_code >= 200 and response.status_code < 300:
            return jsonify({
                'success': True,
                'message': 'Message sent successfully'
            })
        else:
            return jsonify({
                'success': False,
                'message': f'Failed to send message: {response.text}'
            }), response.status_code
            
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error: {str(e)}'
        }), 500

@app.route('/api/read-messages', methods=['POST'])
def read_messages():
    """Read messages from a Discord channel using bot token and channel ID"""
    try:
        data = request.json
        bot_token = data.get('bot_token')
        channel_id = data.get('channel_id')
        limit = data.get('limit', 10)  # Default to 10 messages
        
        if not bot_token or not channel_id:
            return jsonify({
                'success': False,
                'message': 'bot_token and channel_id are required'
            }), 400
        
        # Discord API endpoint for channel messages
        url = f'https://discord.com/api/v10/channels/{channel_id}/messages'
        
        # Set up headers with authorization
        headers = {
            'Authorization': f'Bot {bot_token}',
            'Content-Type': 'application/json'
        }
        
        # Parameters for the request
        params = {
            'limit': limit
        }
        
        # Make the request to Discord API
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code == 200:
            messages = response.json()
            # Format messages for easier consumption
            formatted_messages = []
            for msg in messages:
                formatted_messages.append({
                    'id': msg.get('id'),
                    'content': msg.get('content'),
                    'author': {
                        'id': msg.get('author', {}).get('id'),
                        'username': msg.get('author', {}).get('username'),
                        'discriminator': msg.get('author', {}).get('discriminator')
                    },
                    'timestamp': msg.get('timestamp')
                })
            
            return jsonify({
                'success': True,
                'messages': formatted_messages
            })
        else:
            return jsonify({
                'success': False,
                'message': f'Failed to read messages: {response.text}'
            }), response.status_code
            
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error: {str(e)}'
        }), 500

def main():
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)