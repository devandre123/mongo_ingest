from pymongo import MongoClient
import json
import os
from opp import operations
import certifi
ca = certifi.where()

password = operations.access.password

response_file = "/home/andre/Documents/projetos/2025/pr_mongodb_basic/output"

client = MongoClient(f"mongodb+srv://deolliveira:{password}@clusterandre.lvkcqfg.mongodb.net/?retryWrites=true&w=majority&appName=ClusterAndre",\
                     tlsCAFile=ca)
print(client)
db = client['sample_test']
collection = db['products']

def get_latest_file(directory):
    files_ = [os.path.join(directory, f) for f in os.listdir(directory)]
    if not files_:
        return None
    latest_file = max(files_, key=os.path.getmtime)
    return latest_file


latest = get_latest_file(response_file)


with open(latest, 'r') as fj:
    file_data = json.load(fj)

collection.insert_many(file_data)

print(f"Successfully imported {file_data} bytes of JSON data")