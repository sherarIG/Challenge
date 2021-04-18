import json


def filter_json(input_json, json_keys):
    """ create a dictionary with the key / values of the keys listed in b based on the json file provided
            :param input_json: Json file with an specific structure
            :param json_keys: list of keys that we want to filter from the json file
            :return: A dictionary with Key/Values considering the keys received in b and input_json
    """
    result_dict = {}

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
            # IF name IS LISTED IN b, ADD THE PAIR key = name[:-1], value = x TO final_dict
            if name[:-1] in json_keys:
                result_dict[name[:-1]] = x
            for a in x:
                # RECURSIVELY ITERATE OVER THE ELEMENTS OF x, BECAUSE x IS A dict
                # FORMAT name TO MATCH WHAT's EXPECTED IN b
                json_recursive_path(x[a], name + a + '.')
        # IF x IS A LIST
        elif type(x) is list:
            # IF THE NAME IS LISTED IN b, ADD THE PAIR key = name[:-1], value = list of values
            if name[:-1] in json_keys:
                result_dict[name[:-1]] = x
            i = 0
            for a in x:
                # RECURSIVELY ITERATE OVER THE ELEMENTS OF x, BECAUSE x IS A list
                json_recursive_path(a, name + str(i) + '_')
                i += 1
        else:
            # FINALLY, x COULD ONLY BE A STRING, IF name[:-1] MATCHES ANY KEY ON b,
            # ADD THE PAIR key/value TO result_dict
            if name[:-1] in json_keys:
                result_dict[name[:-1]] = x
    # CALL json_recursive_path FOR THE FIRST TIME
    json_recursive_path(input_json)

    return result_dict


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
    b = ["guid", "content.entities", "score", "score.sign"]

    new_string = '''
        {
            "quiz": {
                "sport": {
                    "q1": {
                        "question": "Which one is correct team name in NBA?",
                        "options": [
                            "New York Bulls",
                            "Los Angeles Kings",
                            "Golden State Warriros",
                            "Huston Rocket"
                        ],
                        "answer": "Huston Rocket"
                    }
                },
                "maths": {
                    "q1": {
                        "question": "5 + 7 = ?",
                        "options": [
                            "10",
                            "11",
                            "12",
                            "13"
                        ],
                        "answer": "12"
                    },
                    "q2": {
                        "question": "12 - 8 = ?",
                        "options": [
                            "1",
                            "2",
                            "3",
                            "4"
                        ],
                        "answer": "4"
                    }
                }
            }
        }'''

    c = ["quiz.maths.q1.question", "quiz.maths.q2"]

    json_obj = json.loads(new_string)
    final_dict = filter_json(json_obj, c)
    print(final_dict)
