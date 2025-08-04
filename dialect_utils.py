# Simple slang-to-English mapping
dialect_map = {
    "romba kashtam": "very painful",
    "semma mokkai": "very boring",
    "enna da": "what's up",
    "suthama puriyala": "I don't understand at all"
}

def normalize_input(text):
    for slang, standard in dialect_map.items():
        text = text.replace(slang, standard)
    return text
