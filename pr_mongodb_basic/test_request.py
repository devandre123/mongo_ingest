import requests
import json
import os
from datetime import datetime

os.makedirs("/home/andre/Documents/projetos/2025/pr_mongodb_basic/output", exist_ok=True)

response = requests.get("https://fakestoreapi.com/products")
res_file = response.json()


response_file = "/home/andre/Documents/projetos/2025/pr_mongodb_basic/output"
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

file_path = os.path.join(response_file, f"data_{timestamp}.json")

with open(file_path, 'w') as file:
    json.dump(res_file, file)

print(f"Saved JSON to {file_path}")


