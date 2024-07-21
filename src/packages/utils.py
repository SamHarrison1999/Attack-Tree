"""Utility modules"""
import json



def read_json(file: str) -> dict[str]:
    """
    Read JSON file
    :param file: path to file
    :return: JSON file as dictionary
    """
    # Loads the json file into a dictionary
    with open(file, "r") as json_file:
        data = json.load(json_file)
        return data
