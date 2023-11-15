# SETUP
## Classic setup

- .\venv\Scripts\activate

- deactivate
- pip freeze > requirements.txt
# Poetry
    python.exe -m pip install --upgrade pip
	pip install poetry
	poetry config --local virtualenvs.in-project true
	touch README.md
	poetry init -n
	poetry install
    poetry add pytest --dev
