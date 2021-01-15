import yaml

def get_settings():
    try:
        with open(r"local_settings.yml") as file:
            settings = yaml.full_load(file)
            return settings
    except FileNotFoundError as e:
        print("local_settings.yml not found at root!")
        raise e