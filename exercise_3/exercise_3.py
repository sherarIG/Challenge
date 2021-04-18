import json


def filter_json(input_json_string, json_keys):
    """ create a dictionary with the key / values of the keys listed in b based on the json file provided
        In this particular case, we are considering the index that the key could have (example 'content.entities[2]')
            :param input_json: Json file with an specific structure
            :param json_keys: list of keys that we want to filter from the json file
            :return: A dictionary with Key/Values considering the keys received in b and input_json
    """
    json_obj = json.loads(input_json_string)
    alt_dict = {}

    def json_recursive_path(x, name=''):
        """ Receives a dict or a list or a string and a key and populates a dictionary if the key matches
            with one provided in the list of keys
            :param x: a dict or a list or a string (depending of the piece of data of the json file we
            are on.
            :param name: Originally an empty string, it will get the value of the different keys
            available.
            :return:
        """
        # IF x IS A DICTIONARY
        if type(x) is dict:
            # IF name IS LISTED IN b ADD THE PAIR key = name[:-1], value = dict TO OUR FINAL DICTIONARY
            if name[:-1] in json_keys:
                alt_dict[name[:-1]] = x
            for a in x:
                # RECURSIVELY ITERATE OVER THE ELEMENTS OF x, BECAUSE x IS A dict
                # FORMAT name TO MATCH WHAT's EXPECTED IN b
                json_recursive_path(x[a], name + a + '.')
        # IF x IS A LIST
        elif type(x) is list:
            # IF THE NAME (WITHOUT ANY INDEX) IS LISTED IN b, ADD THE PAIR key = name, value = list of values
            if name[:-1] in json_keys:
                alt_dict[name[:-1]] = x
            i = 0
            for a in x:
                # RECURSIVELY ITERATE OVER THE ELEMENTS OF x, BECAUSE IT IS A list
                # FORMAT name TO MATCH WHAT's EXPECTED IN b
                json_recursive_path(a, name[:-1] + '[' + str(i) + '].')
                i += 1
        else:
            if name[:-1] in json_keys:
                alt_dict[name[:-1]] = x

    # CALL json_recursive_path FOR THE FIRST TIME
    json_recursive_path(json_obj)

    return alt_dict


if __name__ == "__main__":
    string = '''{
            "guid": "1234",
            "content": {
                        "type": "text/html",
                        "title": "Challenge 1",
                        "entities": [ "1.2.3.4", "wannacry" , "malware.com"]
                        },
            "score": 74,
            "time": 1574879179
        }'''
    b = ["guid", "content.entities[2]", "score", "score.sign"]

    final_dict = filter_json(string, b)
    print(final_dict)
