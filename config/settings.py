import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# JSON schema settings
JSON_FILE_PATH = os.path.join(ROOT_DIR, 'config', 'data.json')
JSON_SCHEMA_VERSION = os.getenv("JSON_SCHEMA_VERSION", 1)
JSON_SCHEMA = {
    "version": JSON_SCHEMA_VERSION,
    "links": []
}

def load_config():
    config = {}
    for key, value in globals().items():
        if key.isupper():
            config[key] = value
    return config
