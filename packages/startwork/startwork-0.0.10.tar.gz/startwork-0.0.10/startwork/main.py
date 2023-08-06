import sys
from pathlib import Path
from subprocess import check_call

from .actions.select_project import select_project
from .actions.create_project import create_project
from .actions.delete_project import delete_project
from .constants.__version__ import __version__

project_list_path = Path(__file__).parent / "projects_list.json"
scripts_path = Path(__file__).parent / "scripts" / "work.sh"

def get_help():
  print("avaliable options:") 
  print("  default: run\n")  
  print("  create: create a new project\n") 
  print("  delete: delete a project\n") 

def main():
  if len(sys.argv) < 2:
    selected_project = select_project(project_list_path)
    start_work_script = [scripts_path, selected_project["project_path"]]

    for line in open('requirements.txt'):
      requirement_name = line.split("=")
      if requirement_name == "flask":
        start_work_script.append("flask")
        break

    check_call(start_work_script)
    return


  option = sys.argv[1]

  if option == "create":
    return create_project(project_list_path)

  if option == "delete":
    return delete_project(project_list_path)

  if option == "--version":
    print(f'version: {__version__}\n')  
    return

  if option == "--help":
    get_help()
    return
  
  print(f'Unknown option: {option}')
  print('Try one of the following:')
  get_help()


if __name__ == "__main__":
  main()
