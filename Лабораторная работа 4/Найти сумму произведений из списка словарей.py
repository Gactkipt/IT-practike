# TODO решите задачу
import json
def task() -> float:
    json_file = "input.json"
    with open(json_file, 'r') as file:
        infomation = json.load(file)
        ware = sum(item["score"] * item["weight"] for item in infomation)
    return round(ware, 3)
print(task())
