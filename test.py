import yaml
from pprint import pprint

with open('chat_id.yaml') as f:
    templates = yaml.safe_load(f)

# pprint(templates)
print(templates)
# chat_id=templates[to_chat_id]
# print(chat_id)
# print(templates[0]['name'],templates[0]['to_chat_id'])
