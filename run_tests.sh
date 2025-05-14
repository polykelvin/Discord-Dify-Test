#!/bin/bash
# Install the package in development mode
pip install -e .

# Run the tests
python -m unittest test_server.py