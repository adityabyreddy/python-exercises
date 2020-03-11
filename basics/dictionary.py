"""

Key value data structure

var = {"key1": "value1", "key2": "value2"}

var.keys() - Returns all the keys - ["key1", "key2"]

var["key1"] - returns value assoicated with key1

"""

menu = {
    "DOSA": 30,
    "VADA": 10,
    "IDLY": 20,
    "PONGAL": 30
}
print(menu.keys())

print(menu["VADA"]+menu["DOSA"])