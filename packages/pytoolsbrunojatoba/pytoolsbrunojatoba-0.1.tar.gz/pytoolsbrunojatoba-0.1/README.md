# pytoolsbrunojatoba
Module is one exemple for biulding projects in Python from the Backend DevPro Course
In this course is taught how contributed in open source projects 

Link of the course [DevPro](https://plataforma.dev.pro.br/)

This project has support for Python 3 version

[![Updates](https://pyup.io/repos/github/brjatoba92/pytoolsbrunojatoba/shield.svg)](https://pyup.io/repos/github/brjatoba92/pytoolsbrunojatoba/)

[![Python 3](https://pyup.io/repos/github/brjatoba92/pytoolsbrunojatoba/python-3-shield.svg)](https://pyup.io/repos/github/brjatoba92/pytoolsbrunojatoba/)

Checklist topics of the course and commands necessary for job:

1. Git:

Local and remote branchs verification commands
``` console
git branch -all (check all branchs)
git remote -v (check all remotes branchs)
```

Steps for job local:

``` console
git fetch upstream (search for local branch updates of one remote repository)
git branch 1 (add a new local branch)
git checkout 1 (change from a main branch to branch 1) or
git checkout -b main upstream/main (make a new main branch from upstream main branch)
make one commit
git push upstream main (send the update to be accept in the GitHub forked repository of outher programmer)
git push origin main (send the code update only for your repositorio and after being submitted in upstream repository)
if accept make
git branch -D 1 (delete local branch 1)
git push --delete upstream 1(delete remote branch 1)
git push --delete origin 1(delete remote branch 1)
```

Final job:

```console
git fetch upstream (search update in the repository)
git merge (download code update)
```

.gitignore file:

Hide what should not be made available

```console
Pycharm files
.idea/
.classpath
.project
.settings/
bin/
*.sqlite3
```

```console
:wq (exit)
```

```console
git config --global core.excludesfile ~/.gitignore_global
```

2. Pyenv:

Install differents Python versions in one PC

Installation:

```console
bash <(curl -sSL https://raw.githubusercontent.com/zaemiel/ubuntu-pyenv-installer/master/ubuntu-pyenv-installer.sh) 
```

Edit the .bashrc file final in the vim: 

```console
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"
```

vim commands:

```console
vim .bashrc (open)
i (edition)
:wq (clone and save)
```

Commands:

```console
pyenv install -l (list everything that can be installed)
pyenv install 3.11.2 (Python 3.11.2 install)
pyenv versions (list all python versions avaliable for use)
pyenv global 3.11.2 (define global python the version 3.11.2)
which python (check which the global python path defined)
python -V (display how global python activated)
```


3. VirtualEnv:

Works with another python separate from system python
The aim is to create one virtual envieronmental for be install libs differents of the O.S Python

```console
python3 -m venv .venv
source .venv/bin/activate
deativate
```


4. Pip install, Requests and Flake8 libs, requirements.txt file:

First activate the virtualenv for use pip install

Requests (requirements.txt):

```console
pip install requests
```

Flake8 (requirements-dev.txt):

Check errors in the code(various or without spaces)

```console
pip install flake8
flake8
```

Requeriments:

Generate the file txt with libs to be made available in github repository 

```console
pip freeze > requirements.txt
pip freeze > requirements-dev.txt (flake8, delete requirements libs )
```

Install .venv libs of the requirements-dev.txt file

```console
pip install -r requirements-dev.txt
```

5. GitHub Actions
I'm using in place of the Travis CI
Create .github_actions.yml file in the .github/workflows folder
```console
name: Python application

on: [pull_request]

jobs:
  build:
    env:
      PIPENV_NO_INHERIT: 1
      PIPENV_IGNORE_VIRTUALENVS: 1
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v2
      - name: Set up Python 3.11.2
        uses: actions/setup-python@v1
        with:
          python-version: 3.11.2

      - name: Install dependencies
        run: |
          pip install -q -r requirements-dev.txt
      - name: Lint with flake8.
        run: |
          pipenv run flake8 .
```

5. Pypi:
Setup.py file
Create a new .venv out of the repository
```console
pip install -e ./pytoolsbrunojatoba/
```
