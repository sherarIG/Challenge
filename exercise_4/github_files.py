from github import Github
import json
from exercise_3.exercise_3 import filter_json as f

# PARAMETERS
# ACCESS TOKEN for gitHub
ACCESS_TOKEN = ''
# Repository path
repository_path = 'mitre/cti'
# JSON files path
json_files_path = "enterprise-attack/attack-pattern"
# Array of requested fields
fields = ["id", "objects[0].kill_chain_phases"]

# Create a Github instance:
if ACCESS_TOKEN:
    try:
        g = Github(ACCESS_TOKEN)
    except SystemExit:
        print('Unable to initialize the Github instance')
        g = False
else:
    print('Please provide a valid ACCESS_TOKEN')
    g = False

if g:
    # Get Repo
    try:
        repo = g.get_repo(repository_path)
    except SystemExit:
        print('Invalid repo')
        repo = False
else:
    repo = False

if repo:
    # List of files inside path
    contents = repo.get_contents(json_files_path)
    for content_file in contents:
        # Convert each content file to a json object
        try:
            json_obj = json.loads(content_file.decoded_content)
            final_dict = f(json_obj, fields)
            print(final_dict)
        except ValueError:
            print('Invalid json file: ' + content_file)
