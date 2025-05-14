import unittest
import json
from unittest.mock import patch, MagicMock
from server import app

class TestDiscordToolsPlugin(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        
    def test_hello_endpoint(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Discord Tools Plugin for Dify is running!')
        
    def test_manifest_endpoint(self):
        with patch('builtins.open', unittest.mock.mock_open(read_data='{"name": "discord_tools"}')):
            response = self.app.get('/manifest')
            self.assertEqual(response.status_code, 200)
            data = json.loads(response.data)
            self.assertEqual(data['name'], 'discord_tools')
            
    @patch('server.DiscordWebhook')
    def test_send_message_success(self, mock_webhook):
        # Mock the webhook execution response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_webhook.return_value.execute.return_value = mock_response
        
        test_data = {
            'webhook_url': 'https://discord.com/api/webhooks/test',
            'message': 'Test message',
            'title': 'Test Title'
        }
        
        response = self.app.post('/api/send-message', 
                                json=test_data,
                                content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data['success'])
        self.assertEqual(data['message'], 'Message sent successfully')
        
    @patch('server.DiscordWebhook')
    def test_send_message_failure(self, mock_webhook):
        # Mock the webhook execution response for failure
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = 'Invalid webhook URL'
        mock_webhook.return_value.execute.return_value = mock_response
        
        test_data = {
            'webhook_url': 'https://discord.com/api/webhooks/invalid',
            'message': 'Test message'
        }
        
        response = self.app.post('/api/send-message', 
                                json=test_data,
                                content_type='application/json')
        
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data['success'])
        
    def test_send_message_missing_params(self):
        # Test with missing webhook_url
        test_data = {
            'message': 'Test message'
        }
        
        response = self.app.post('/api/send-message', 
                                json=test_data,
                                content_type='application/json')
        
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data['success'])
        
    @patch('server.requests.get')
    def test_read_messages_success(self, mock_get):
        # Mock the Discord API response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {
                'id': '123456789',
                'content': 'Hello world',
                'author': {
                    'id': '987654321',
                    'username': 'testuser',
                    'discriminator': '1234'
                },
                'timestamp': '2023-05-01T12:00:00.000Z'
            }
        ]
        mock_get.return_value = mock_response
        
        test_data = {
            'bot_token': 'test_token',
            'channel_id': '123456789',
            'limit': 5
        }
        
        response = self.app.post('/api/read-messages', 
                                json=test_data,
                                content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data['success'])
        self.assertEqual(len(data['messages']), 1)
        self.assertEqual(data['messages'][0]['content'], 'Hello world')
        
    @patch('server.requests.get')
    def test_read_messages_failure(self, mock_get):
        # Mock the Discord API response for failure
        mock_response = MagicMock()
        mock_response.status_code = 401
        mock_response.text = 'Unauthorized'
        mock_get.return_value = mock_response
        
        test_data = {
            'bot_token': 'invalid_token',
            'channel_id': '123456789'
        }
        
        response = self.app.post('/api/read-messages', 
                                json=test_data,
                                content_type='application/json')
        
        self.assertEqual(response.status_code, 401)
        data = json.loads(response.data)
        self.assertFalse(data['success'])
        
    def test_read_messages_missing_params(self):
        # Test with missing bot_token
        test_data = {
            'channel_id': '123456789'
        }
        
        response = self.app.post('/api/read-messages', 
                                json=test_data,
                                content_type='application/json')
        
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data['success'])

if __name__ == '__main__':
    unittest.main()