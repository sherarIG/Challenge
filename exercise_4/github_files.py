"""
This program will connect to GitHub with a provided ACCESS_TOKEN, REPOSITORY_PATH and A FOLDER that contains json files.
Once connected, it will iterate over the list of files in the FOLDER inside the REPOSITORY and execute the function on exercise_3
using the filter array called fields.
Parameters
----------
ACCESS_TOKEN str : The token to access GitHub
REPOSITORY_PATH str : The path to the specific repository
FOLDER str : The path to the folder inside the repository that has the json files.
"""

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
    # List of files inside json_files FOLDER
    contents = repo.get_contents(json_files_path)
    for content_file in contents:
        # GET THE json_obj OF EACH OF THE FILES
        try:
            json_obj = json.loads(content_file.decoded_content)
            # CALL THE FUNCTION FROM exercise_3. THE FUNCTION IS EXPECTING A STRING, SO I NEED TO CONVERT
            # THE json_obj TO STRING. THEN THE FUNCTION WILL MAKE IT A json_obj AGAIN. MAYBE NOT VERY EFFICIENT
            final_dict = f(json.dumps(json_obj), fields)
            print(final_dict)
        except ValueError:
            print('Invalid json file: ' + str(content_file))
