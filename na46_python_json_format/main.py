import json

data = {
    "name": "Bruno Fernandez",
    "affiliation": ["Manchester United", "Portugal"]
}

jstr = json.dumps(data)
print(jstr)

data = [
    {
        "faction": "Horde",
        "color": "red",
        "founding_members": [
            "Orc",
            "Undead",
            "Tauren",
            "Troll",
            "Blood Elf",
            "Goblin"
        ],
        "total_members": 13,
        "active": True,
    },
    {
        "faction": "Alliance",
        "color": "blue",
        "founding_members": [
            "Human",
            "Dwarf",
            "Night Elf",
            "Gnome",
            "Draenei",
            "Worgen"
        ],
        "total_members": 13,
        "active": True
    }
]

jstr = json.dumps(data)
print(jstr)

jstr1 = '{ "name": "Maiev Shadowsong", "affliations": ["Warden", "Alliance"], "age": 10000, "active": true }'
data1 = json.loads(jstr1)

print(f"type: {type(data1).__name__}")

for key in data1:
    print(f"{key}: {data1[key]}")