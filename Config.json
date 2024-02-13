import random
import string
import json

def load_config(config_file):
    with open(config_file, "r") as file:
        return json.load(file)

def generate_gift_card_code(platform_config):
    code = ''.join(random.choices(
                string.ascii_uppercase + string.digits, 
                k=platform_config["length"]
            ))

    if "format" in platform_config:
        parts = [code[i:i + platform_config["format"]["segment_length"]] 
                    for i in range(0, len(code), platform_config["format"]["segment_length"])]
        code = platform_config["format"]["separator"].join(parts)

    return platform_config["prefix"] + code

def generate_and_save_codes(config, num_codes, filename, batch_range=None):
    generated_codes = set()

    if batch_range:
        start, end = batch_range
        for _ in range(start, end + 1):
            while True:
                platform_config = random.choice(config["platforms"] + config["custom_stores"]) 
                code = generate_gift_card_code(platform_config)
                if code not in generated_codes:
                    generated_codes.add(code)
                    break
    else:
        # ... (Your existing code for normal mode) ...

    # ... (Your file writing code) ... 

config = load_config('config.json') 
