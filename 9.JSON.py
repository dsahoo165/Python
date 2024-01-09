
import json

# JSON String:
tools =  '["Maven", "Jira", "Kubernetes", "Docker"]'

# JSON string to python dictionary:
lst1 = json.loads(tools)
print(lst1)



# python dictionary
lst2 = ['Maven', 'Jira', 'Kubernetes', 'Docker']

# Convert Python dict to JSON
jsonObj = json.dumps(lst2)
print(jsonObj)