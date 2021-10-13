import requests
import json
from argparse import ArgumentParser
import netifaces as ni

def post_to_slack(url, message):
    if url:
        requests.post(url, headers={'content-type': 'application/json'}, data=json.dumps({'text': message}))

def get_ip(interface):
    return ni.ifaddresses(interface)[ni.AF_INET][0]['addr']

def main():
    parser = ArgumentParser()
    parser.add_argument('interface')
    parser.add_argument('-s', '--slack')
    parser.add_argument('--debug', action='store_true', default=False)
    args = parser.parse_args()

    ip = get_ip(args.interface)
    msg_list = [f'[INFO] IP address: {ip}']

    if msg_list:
        post_to_slack(args.slack, '\n'.join(msg_list))

if __name__ == '__main__':
    main()