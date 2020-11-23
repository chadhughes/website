#!/usr/bin/env python3
import requests

passphrase = 'foobarfoo'
plaintext = '''The quick brown fox...
...jumped over the lazy dog.
hello world!
'''

r = requests.post('https://chadhughes.com/api_v1', data = {'plaintext':plaintext, 'passphrase':passphrase})
#r.encoding = 'utf-8'
#print(r.text)
#print(r.content)
#print(r.json())
#print(type(r.json()))
#print(r.json()["results"][0])
plaintext = r.json()["results"][0]["plaintext"]
ciphertext = r.json()["results"][0]["ciphertext"]
print('plaintext: ')
print(plaintext)
print('')
print('ciphertext: ')
print(ciphertext)
