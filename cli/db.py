import json
file_name = 'family_tree_data.json'

def read_from_json():
    try:
        with open(file_name,'r', encoding='utf-8') as json_file:
            family_tree = json.load(json_file)
            # print(family_tree)
            return family_tree
    except FileNotFoundError:
        with open(file_name, "w") as json_file:
            family_tree = {
                            "persons":{},
                            "relationship":[]
                            }
            json.dump(family_tree, json_file)
            # print("File didn't exist. Created with default data:", family_tree)
            return family_tree

def write_to_json(family_data:dict):
    with open(file_name, "w") as json_file:
        json.dump(family_data, json_file)
        #DEBUG
        # print(f"Done writing {family_data} to the file system.")

