# THIS IS A VALID JSON FILE WITH A LIST OF OBJECTS AS THE ROOT
string_json_1 = '''
[
    {
        "id": "0001",
        "type": "donut",
        "name": "Cake",
        "ppu": 0.55,
        "batters":
            {
                "batter":
                    [
                        { "id": "1001", "type": "Regular" },
                        { "id": "1002", "type": "Chocolate" },
                        { "id": "1003", "type": "Blueberry" },
                        { "id": "1004", "type": "Devil's Food" }
                    ]
            },
        "topping":
            [
                { "id": "5001", "type": "None" },
                { "id": "5002", "type": "Glazed" },
                { "id": "5005", "type": "Sugar" },
                { "id": "5007", "type": "Powdered Sugar" },
                { "id": "5006", "type": "Chocolate with Sprinkles" },
                { "id": "5003", "type": "Chocolate" },
                { "id": "5004", "type": "Maple" }
            ]
    },
    {
        "id": "0002",
        "type": "donut",
        "name": "Raised",
        "ppu": 0.55,
        "batters":
            {
                "batter":
                    [
                        { "id": "1001", "type": "Regular" }
                    ]
            },
        "topping":
            [
                { "id": "5001", "type": "None" },
                { "id": "5002", "type": "Glazed" },
                { "id": "5005", "type": "Sugar" },
                { "id": "5003", "type": "Chocolate" },
                { "id": "5004", "type": "Maple" }
            ]
    },
    {
        "id": "0003",
        "type": "donut",
        "name": "Old Fashioned",
        "ppu": 0.55,
        "batters":
            {
            "batter":
                [
                        { "id": "1001", "type": "Regular" },
                        { "id": "1002", "type": "Chocolate" }
                    ]
            },
        "topping":
            [
                { "id": "5001", "type": "None" },
                { "id": "5002", "type": "Glazed" },
                { "id": "5003", "type": "Chocolate" },
                { "id": "5004", "type": "Maple" }
            ]
    }
]'''
# SUPPOSE I WANT TO GET batters.batter[0].type of the THIRD element of the list, I COULD DO IT LIKE THIS:
list_of_keys_1 = ["[2].batters.batter[0].type"]
# AND MY CODE WILL WORK, SO I BELIEVE THIS IS NOT AN EXCEPTION.
expected_result_1 = {'[2].batters.batter[0].type': 'Regular'}

list_of_keys_2 = ["[2].topping[3].id", "[2].type"]
expected_result_2 = {'[2].type': 'donut', '[2].topping[3].id': '5004'}

string_json_3 = '''
{
"problems": [{
    "Diabetes":[{
        "medications":[{
            "medicationsClasses":[{
                "className":[{
                    "associatedDrug":[{
                        "name":"asprin",
                        "dose":"",
                        "strength":"500 mg"
                    }],
                    "associatedDrug#2":[{
                        "name":"somethingElse",
                        "dose":"",
                        "strength":"500 mg"
                    }]
                }],
                "className2":[{
                    "associatedDrug":[{
                        "name":"asprin",
                        "dose":"",
                        "strength":"500 mg"
                    }],
                    "associatedDrug#2":[{
                        "name":"somethingElse",
                        "dose":"",
                        "strength":"500 mg"
                    }]
                }]
            }]
        }],
        "labs":[{
            "missing_field": "missing_value"
        }]
    }],
    "Asthma":[{}]
}]} '''

list_of_keys_3 = ["problems[0].Diabetes[0]", "problems[0].labs[0]"]

expected_result_3 = {'problems[0].Diabetes[0]': {'medications': [{'medicationsClasses': [{'className': [{'associatedDrug': [{'name': 'asprin', 'dose': '', 'strength': '500 mg'}], 'associatedDrug#2': [{'name': 'somethingElse', 'dose': '', 'strength': '500 mg'}]}], 'className2': [{'associatedDrug': [{'name': 'asprin', 'dose': '', 'strength': '500 mg'}], 'associatedDrug#2': [{'name': 'somethingElse', 'dose': '', 'strength': '500 mg'}]}]}]}], 'labs': [{'missing_field': 'missing_value'}]}}

