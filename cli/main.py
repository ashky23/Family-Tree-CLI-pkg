#!/usr/bin/env python


#The implementation is limited to the name which don't contain space

import argparse
from cli.processor import *

def main():
    parser = argparse.ArgumentParser(description="Family Tree CLI Tool")
    subparsers = parser.add_subparsers(title="subcommands", dest="command")

    # Add subcommand: add
    parser_add = subparsers.add_parser("add", help="Add a person/relationship to the family tree")
    parser_add.add_argument("entity_type", choices=["person", "relationship"], help="Type of entity to add")
    parser_add.add_argument("name", help="Name of the person or relationship")

    # Add subcommand: connect
    parser_connect = subparsers.add_parser("connect", help="connect relationships")
    parser_connect.add_argument("first_person", help="Name of the first person")
    parser_connect.add_argument("as", choices=["as"], help="Specify the relationship (e.g., son, daughter, mother, father)")
    parser_connect.add_argument("relationship_name", help="Specify the relationship (e.g., son, daughter, mother, father)")
    parser_connect.add_argument("of", choices=["of"], help="Specify the relationship (e.g., son, daughter, mother, father)")
    parser_connect.add_argument("second_person", help="Name of the second person")    

    # Add query: count
    parser_count = subparsers.add_parser("count", help="Query maximum relationships")
    parser_count.add_argument("entity_type", choices=["sons", "daughters", "wives", "husbands"], help="Type of entity to add")
    parser_count.add_argument("of", choices=["of"], help="Type of entity to add")
    parser_count.add_argument("name", help="Name of the person")

    # Add query: father of
    parser_father_of = subparsers.add_parser("father", help="Query maximum relationships")
    parser_father_of.add_argument("of", choices=["of"], help="Type of entity to add")
    parser_father_of.add_argument("name", help="Name of the person")


    args = parser.parse_args()
    # print(args)
    if args.command == "add":
        process_add_command_queries(args)
    elif args.command == "connect":
        process_connect_command_queries(args)
    elif args.command == "count":
        process_count_command_queries(args)
    elif args.command == "father":
        process_father_command_queries(args)
    else:
        print("Please provide me a valid input!")    


if __name__ == "__main__":
    main()