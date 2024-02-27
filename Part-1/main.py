
from seed import search_quotes
import connect
from connect import connect
from pathlib import Path
import json
from models import Author, Quote



while True:
    command = input("Enter command (name/tag/tags: value) or 'exit' to quit: ")
    if command.lower() == 'exit':
        break
    search_quotes(command)



