import json
from inquirer import List, Confirm, prompt

def delete_project(project_list_path):
  projects_list = []

  with open(project_list_path, 'r') as openfile:
    projects_list = json.load(openfile)
  
  projects_keys=[project["name"] for project in projects_list]

  questions = [
    List(
      'selected_project',
      message="Delete a project",
      choices=projects_keys,
    ),
    Confirm(
      'delete_confirmed',
      message="This project will be deleted. Continue?",
      default=False
    ),
    Confirm(
      'delete_confirmed2',
      message="ARE YOU SURE???",
      default=False
    )
  ]

  answers = prompt(questions)
  
  if answers['delete_confirmed'] and answers['delete_confirmed2']:
    raise Exception("Deletion Aborted!")

  projects_list = list(
    filter(
      lambda project: project['name'] != answers['selected_project'],
      projects_list
    )
  )

  with open(project_list_path, "w") as outfile:
    outfile.write(json.dumps(projects_list, indent=4))
  
  print(f'Project named as "{answers["selected_project"]}" has been deleted!')
