# Contributing to Discord Tools Plugin for Dify

Thank you for your interest in contributing to the Discord Tools Plugin for Dify! This document provides guidelines and instructions for contributing to this project.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/your-username/discord-tools-plugin.git`
3. Create a new branch for your feature or bugfix: `git checkout -b feature/your-feature-name`

## Development Environment Setup

1. Install Python 3.9 or higher
2. Install dependencies: `pip install -r requirements.txt`
3. Run the server locally: `python server.py`

## Testing

Before submitting a pull request, please run the tests to ensure your changes don't break existing functionality:

```
python -m unittest test_server.py
```

## Adding New Features

If you're adding a new feature:

1. Update the `manifest.json` file if you're adding new tools
2. Add appropriate tests in `test_server.py`
3. Update documentation in README.md and other relevant files
4. Add example usage if applicable

## Code Style

Please follow these guidelines for code style:

- Use 4 spaces for indentation
- Follow PEP 8 guidelines for Python code
- Include docstrings for functions and classes
- Keep lines under 100 characters when possible

## Pull Request Process

1. Update the README.md and documentation with details of changes if applicable
2. Make sure all tests pass
3. Submit a pull request with a clear description of the changes and any relevant issue numbers
4. Wait for review and address any feedback

## Feature Requests and Bug Reports

If you have ideas for new features or have found a bug:

1. Check existing issues to see if it has already been reported
2. If not, create a new issue with a clear description
3. For bugs, include steps to reproduce, expected behavior, and actual behavior
4. For feature requests, describe the feature and its benefits

## Code of Conduct

- Be respectful and inclusive in your communications
- Provide constructive feedback
- Focus on the issue, not the person

Thank you for contributing to make the Discord Tools Plugin for Dify better!