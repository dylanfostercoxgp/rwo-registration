#!/usr/bin/env python3
"""One-time upload script for index.html to GitHub. Run: python3 upload.py"""
import json, base64, urllib.request, getpass, os

OWNER = 'dylanfostercoxgp'
REPO = 'rwo-registration'
FILE = 'index.html'

token = getpass.getpass('Paste your GitHub token (hidden): ')

# Get current SHA
url = f'https://api.github.com/repos/{OWNER}/{REPO}/contents/{FILE}'
req = urllib.request.Request(url, headers={'Authorization': f'token {token}', 'Accept': 'application/vnd.github.v3+json'})
resp = urllib.request.urlopen(req)
sha = json.loads(resp.read())['sha']
print(f'Current SHA: {sha}')

# Read local file
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), FILE), 'r') as f:
    content = f.read()
encoded = base64.b64encode(content.encode('utf-8')).decode('utf-8')

# Upload
payload = json.dumps({'message': 'Update: race-specific print/PDF, token in localStorage, race grid fix', 'content': encoded, 'sha': sha}).encode('utf-8')
req2 = urllib.request.Request(url, data=payload, method='PUT', headers={'Authorization': f'token {token}', 'Accept': 'application/vnd.github.v3+json', 'Content-Type': 'application/json'})
resp2 = urllib.request.urlopen(req2)
result = json.loads(resp2.read())
print(f'Uploaded! New SHA: {result["content"]["sha"]}')
print('Live site will update in 60-90 seconds.')

# Clean up this script
os.remove(os.path.abspath(__file__))
print('Upload script auto-deleted.')
