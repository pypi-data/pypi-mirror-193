#!/usr/bin/env python3

import sys
import argparse
import json
from copy import deepcopy
from enum import Enum


class ExitCodes(Enum):
    SUCCESS = 0
    BAD_ARGUMENT = 1
    BAD_CHOICE = 2
    FILE_ERROR = 3
    JSON_ERROR = 4


def exit_with_error(message, exit_code):
    """Prints an error message and exits with the specified exit code."""
    print(message, file=sys.stderr)
    print("See usage with: --help")
    sys.exit(exit_code.value)


def has_key(obj, key):
    """Returns True if the object has the specified key."""
    return key in obj


def get_main_domain(certificate):
    """Returns the main domain of the certificate."""
    return certificate.get("domain", {}).get("main")


def main():
    parser = argparse.ArgumentParser(description="Do one thing well.")
    parser.add_argument("-j", "--json", help="the JSON file with the Let's Encrypt certificates", required=True)
    parser.add_argument("-r", "--resolver", help="the resolver for the certificates in the Let's Encrypt JSON file", required=True)
    parser.add_argument("-o", "--out", help="the output file where to save the pruned content", required=True)
    args = parser.parse_args()

    infile = None
    try:
        with open(args.json, 'r') as file:
            infile = json.load(file)
    except FileNotFoundError:
        exit_with_error(f"File not found: {args.json}", ExitCodes.FILE_ERROR)
    except json.JSONDecodeError as e:
        exit_with_error(f"Invalid JSON file: {args.json} - {str(e)}", ExitCodes.JSON_ERROR)

    resolver = args.resolver
    if not has_key(infile, resolver):
        exit_with_error(f"Resolver {resolver} does not exist in file {args.json}", ExitCodes.BAD_ARGUMENT)

    haystack = infile[resolver].get("Certificates", [])
    if not isinstance(haystack, list):
        exit_with_error(f"Invalid JSON structure: 'Certificates' is not a list in resolver {resolver} of file {args.json}", ExitCodes.JSON_ERROR)

    outfile = deepcopy(infile)
    outfile[resolver]["Certificates"] = []

    choices = {}
    certificates = {}
    for idx, certificate in enumerate(haystack):
        domain = get_main_domain(certificate)
        if not domain:
            exit_with_error(f"Invalid JSON structure: 'domain[main]' is not defined.", ExitCodes.JSON_ERROR)
        certificates[idx] = certificate
        choices[idx] = domain

    if not choices:
        exit_with_error(f"No valid certificates found in resolver {resolver} of file {args.json}", ExitCodes.JSON_ERROR)

    print("The JSON files contains these certificates:")
    print()
    for idx, choice in choices.items():
        print(f"{idx} - {choice};")
    print()

    try:
        choice = int(input("Which certificate do you want to remove? "))
    except ValueError:
        exit_with_error("Invalid choice.", ExitCodes.BAD_CHOICE)

    if choice < 0 or choice >= len(choices):
        exit_with_error("Invalid choice.", ExitCodes.BAD_CHOICE)

    print(f"Removing certificate for domain: {choices[choice]}")
    del certificates[choice]

    for idx, certificate in certificates.items():
        outfile[resolver]["Certificates"].append(certificate)

    try:
        with open(args.out, 'w') as f:
            f.write(json.dumps(outfile))
    except IOError as e:
        exit_with_error(f"Error writing to file: {e}", ExitCodes.FILE_ERROR)

    print(f"Pruned content saved to: {args.out}.")
    print()
    print("Please do have a good day!")

    sys.exit(ExitCodes.SUCCESS.value)


if __name__ == '__main__':
    if __debug__:
        print("Debug messages enabled.")
    main()

