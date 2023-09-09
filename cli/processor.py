from cli.db import read_from_json, write_to_json

family_tree = read_from_json()

def add_person(name, father=None, mother=None):
    if name not in family_tree["persons"]:
        family_tree["persons"][name] = {
            "name": name,
            "children": {"sons":[], "daughters":[]},
            "father": father,
            "mother": mother,
            "wives":[],
            "husbands":[]
        }


def add_relationship(name):
    if name not in family_tree["relationship"]:
        family_tree["relationship"].append(name)


def process_add_command_queries(parsed_args):
   
    if parsed_args.entity_type == "person":
        add_person(parsed_args.name) 
    elif parsed_args.entity_type == "relationship":
        add_relationship(parsed_args.name)

    write_to_json(family_tree)

def process_connect_command_queries(parsed_args):

    
    first_person = parsed_args.first_person
    second_person = parsed_args.second_person
    relationship_name = parsed_args.relationship_name

    if relationship_name not in family_tree.get('relationship'):
        print(f"Can't add connection as relationship {relationship_name} doesn't exist in family_tree ")
    
    #working on four relationship type - son, daughter, mother, father, husbands, wives
    elif relationship_name == "son" or relationship_name == "daughter":
        if first_person not in family_tree["persons"]:
            family_tree["persons"][first_person] = {
            "name": first_person,
            "children": {"sons":[], "daughters":[]},
            "father": second_person,
            "mother": "",
            "wives":[],
            "husbands":[]
        }
        else:
            # assuming default is father
            family_tree["persons"][first_person]["father"]= second_person
        
        if relationship_name == "son":
            sons = [first_person]
            daughters = []
        else:
            daughters = [first_person]
            sons = []

        if second_person not in family_tree["persons"]:
            family_tree["persons"][second_person] = {
            "name": second_person,
            "children": {"sons":sons, "daughters":daughters},
            "father": "",
            "mother": "",
            "wives":[],
            "husbands":[]
        }
            
        else:
            family_tree["persons"][second_person]["children"].get("sons").extend(sons)
            family_tree["persons"][second_person]["children"].get("daughters").extend(daughters)

        
    
    elif relationship_name == "mother" or relationship_name == "father":

        #Assuming father/mother of default to be son 
        if first_person not in family_tree["persons"]:
            family_tree["persons"][first_person] = {
            "name": first_person,
            "children": {"sons":[second_person], "daughters":[]},
            "father": "",
            "mother": "",
            "wives":[],
            "husbands":[]
        }
        else:
            family_tree["persons"][first_person]["children"].get("sons").extend([second_person])
        
        if relationship_name == "mother":
            mother = first_person
            father = family_tree["persons"][second_person]["father"]
        else:
            mother = family_tree["persons"][second_person]["mother"]
            father = first_person

        if second_person not in family_tree["persons"]:
            family_tree["persons"][second_person] = {
            "name": second_person,
            "children": {"sons":[], "daughters":[]},
            "father": father,
            "mother": mother,
            "wives":[],
            "husbands":[]
        }
            
        else:
            family_tree["persons"][second_person]["father"] = father
            family_tree["persons"][second_person]["mother"] = mother

    elif relationship_name == "wife":
        
        if first_person not in family_tree["persons"]:
            family_tree["persons"][first_person] = {
            "name": first_person,
            "children": {"sons":[], "daughters":[]},
            "father": "",
            "mother": "",
            "wives":[],
            "husbands":[second_person]
        }
        else:
            family_tree["persons"][first_person]["husbands"].extend([second_person])

        if second_person not in family_tree["persons"]:
            family_tree["persons"][second_person] = {
            "name": second_person,
            "children": {"sons":[], "daughters":[]},
            "father": father,
            "mother": mother,
            "wives":[first_person],
            "husbands":[]
        }
            
        else:
            family_tree["persons"][second_person]["wives"].extend([first_person])

    elif relationship_name == "husband":
        if first_person not in family_tree["persons"]:
            family_tree["persons"][first_person] = {
            "name": first_person,
            "children": {"sons":[], "daughters":[]},
            "father": "",
            "mother": "",
            "wives":[second_person],
            "husbands":[]
        }
        else:
            family_tree["persons"][first_person]["wives"].extend([second_person])

        if second_person not in family_tree["persons"]:
            family_tree["persons"][second_person] = {
            "name": second_person,
            "children": {"sons":[], "daughters":[]},
            "father": father,
            "mother": mother,
            "wives":[],
            "husbands":[first_person]
        }
            
        else:
            family_tree["persons"][second_person]["husbands"].extend([first_person])

    write_to_json(family_tree)
    

def process_count_command_queries(parsed_args):
    
    person_name = parsed_args.name
    entity_type = parsed_args.entity_type
    count = 0
    if person_name not in family_tree["persons"]:
        print(f"Person doesn't exist in our family tree. Can't provide count of {entity_type} for person {person_name}")

    elif entity_type == "sons":
        count = len(family_tree["persons"][person_name].get("children",{}).get("sons",[]))
    elif entity_type == "daughters":
        count = len(family_tree["persons"][person_name].get("children",{}).get("daughters",[]))
    elif entity_type == "wives":
        count = len(family_tree["persons"][person_name].get("wives",[]))
    elif entity_type == "husbands":
        count = len(family_tree["persons"][person_name].get("husbands",[]))

    print(f"Count of {entity_type} for person {person_name} is : {count}")
    

def process_father_command_queries(parsed_args):
    person_name = parsed_args.name

    if person_name not in family_tree["persons"]:
        print(f"Person doesn't exist in our family tree. Can't provide father name for person {person_name}")
    else:
        father = family_tree["persons"][person_name]["father"]
        print(f"{father} is father of person {person_name}")
