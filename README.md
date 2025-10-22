# Async vs Sync HTTP Requests Performance Comparison

This demo shows the performance difference between asynchronous and synchronous HTTP requests using Python.

## Overview
- **Async requests**: Using `aiohttp` library for concurrent HTTP calls
- **Sync requests**: Using `requests` library for sequential HTTP calls
- Demonstrates how async programming can significantly improve performance for I/O-bound tasks

## Key Findings
Async requests run concurrently and complete in roughly the time of the slowest single request, while sync requests run sequentially and take the sum of all request times.

## Technologies Used
- Python 3
- asyncio
- aiohttp
- requests

## Contact
- Telegram: https://t.me/eweraohw
