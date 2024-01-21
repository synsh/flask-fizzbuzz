```sh
# create virtual env
python3 -m venv .venv

# activate virtual env
. .venv/bin/activate

# install dependencies
pip install -r requirements.txt

# initialize SQLite DB
flask --app fizzbuzz init-db

# start the API server
flask --app fizzbuzz run

# run tests
pytest -v
```
