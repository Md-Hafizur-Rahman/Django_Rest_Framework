import json 
with open(r'exam.json','r') as f:
    data=json.load(f)
print(data['education'][0]['location'])
