import json

langs = {
        "C/C++": "HARD",
        "Java": "Intermediate",
        "Python": "Easy",
        "Pascal": "Intermediate",
        "HTML": "Structured",
        "Go": "New"
}

with open("langs.json", "w") as file:
    json.dump(langs, file)
