arr = [{"height": 160, "weight": 60, "age": 25}, {"height": 180, "weight": 80, "age": 35}]
print(max(arr, key= lambda i: i["height"]))