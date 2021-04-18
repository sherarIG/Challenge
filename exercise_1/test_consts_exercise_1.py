string_json_1 = '''{
            "guid": "1234",
            "content": {
                        "type": "text/html",
                        "title": "Challenge 1",
                        "entities": [ "1.2.3.4", "wannacry" , "malware.com"]
                        },
            "score": 74,
            "time": 1574879179
        }'''
list_of_keys_1 = ["guid", "content.entities", "score", "score.sign"]

expected_result_1 = {'guid': '1234', 'content.entities': ['1.2.3.4', 'wannacry', 'malware.com'], 'score': 74}

string_json_2 = '''
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
}
'''
list_of_keys_2 = ["quiz.sport.q1", "quiz.sport", "quiz.maths"]

expected_result_2 = {'quiz.sport': {'q1': {'question': 'Which one is correct team name in NBA?', 'options': ['New York Bulls', 'Los Angeles Kings', 'Golden State Warriros', 'Huston Rocket'], 'answer': 'Huston Rocket'}}, 'quiz.sport.q1': {'question': 'Which one is correct team name in NBA?', 'options': ['New York Bulls', 'Los Angeles Kings', 'Golden State Warriros', 'Huston Rocket'], 'answer': 'Huston Rocket'}, 'quiz.maths': {'q1': {'question': '5 + 7 = ?', 'options': ['10', '11', '12', '13'], 'answer': '12'}, 'q2': {'question': '12 - 8 = ?', 'options': ['1', '2', '3', '4'], 'answer': '4'}}}

string_json_3 = '''
{
    "firstName": "Rack",
    "lastName": "Jackon",
    "gender": "man",
    "age": 24,
    "address": {
        "streetAddress": "126",
        "city": "San Jone",
        "state": "CA",
        "postalCode": "394221"
    },
    "phoneNumbers": [
        { "type": "home", "number": "7383627627" }
    ]
}
'''
list_of_keys_3 = ["phoneNumbers.type", "firstName", "age", "address"]

expected_result_3 = {'firstName': 'Rack', 'age': 24, 'address': {'streetAddress': '126', 'city': 'San Jone', 'state': 'CA', 'postalCode': '394221'}, 'phoneNumbers.type': 'home'}
