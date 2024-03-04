#!/usr/bin/env python3

import os

import github_api
import web_server
from dotenv import dotenv_values

def main():
    if os.getenv('GITHUB_TOKEN'):
        github_api.GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
    else:
        config = dotenv_values('.env')
        github_api.GITHUB_TOKEN = config['GITHUB_TOKEN']
    if not github_api.GITHUB_TOKEN:
        raise ValueError('GITHUB_TOKEN environment variable is not set')

    LISTEN_ADDR = os.getenv('LISTEN_ADDR', '')
    LISTEN_PORT = int(os.getenv('LISTEN_PORT', '8000'))
    web_server.start_web_server(LISTEN_ADDR, LISTEN_PORT)


if __name__ == '__main__':
    main()
