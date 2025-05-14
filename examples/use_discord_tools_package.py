"""
Example script showing how to use the discord-tools-dify package
"""

# Import the package
from discord_tools_dify.server import app

def run_discord_tools_server():
    """Run the Discord Tools server"""
    print("Starting Discord Tools server...")
    app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
    run_discord_tools_server()