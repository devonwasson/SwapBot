import sys
sys.path.insert(0, '.')
from server import JsonHelper
import requests
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('sub_name', metavar='C', type=str)
parser.add_argument('username', metavar='C', type=str)
parser.add_argument('swap_text', metavar='C', type=str)
args = parser.parse_args()
request_url = "http://0.0.0.0:8000"
json_helper = JsonHelper()
requests.post(request_url + "/add-swap/", {'sub_name': args.sub_name.lower(), 'username': args.username.lower(), 'swap_text': args.swap_text.lower()})
