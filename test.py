# #!/usr/bin/python3
import os
from os import getenv
from google.cloud.translate_v2.client import Client

translate_client = Client()

string = 'Hello World'

translation = translate_client.translate(string, target_language='ja')

print(translation)
