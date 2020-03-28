# Neo4jAPI
A REST API using Neo4j as database agent to interact with data contained in graphs.  
This project uses the Python Flask environment and furthermore Flask-restplus to perform http requests.

## Installation

If you don't have Python installed, [get it here](https://www.python.org/downloads)  
I recommend you to use the package manager [pip](https://pip.pypa.io/en/stable/) to setup a virtual environment. I personnaly used [virtualenv](https://virtualenv.pypa.io/en/latest), but you're free to choose the one that suits you best.  
Go to the project root folder and type the following commands :

```bash
pip install virtualenv
virtualenv venv
```
Then, install all packages in requirements.txt on your venv :  
```bash
pip install -r requirements.txt
```

## Setup project and flask env

The project needs a .env for configuration, it should contain :  
````bash
DB_URI = your neo4j graph database uri
USERNAME = username for authenication in the current graph
PASSWORD = password for authentication in the current graph
````

```python
import foobar

foobar.pluralize('word') # returns 'words'
foobar.pluralize('goose') # returns 'geese'
foobar.singularize('phenomena') # returns 'phenomenon'
```
