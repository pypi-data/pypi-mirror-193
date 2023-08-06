function try_python() {
  which python3
  exit_code=$?

  if ![[ $exit_code == 0 ]]
    then exit "Missing dependence: python3"
  fi

  if ![[ -f "venv/bin/activate" ]]
    then
      echo "starting new venv"
      python3 -m venv venv
  fi

  source venv/bin/activate
  echo "install requirements..."
  python3 -m pip install -r requirements.txt

  if [[ "$1" == "flask" ]]
    then flask run
  fi
}
