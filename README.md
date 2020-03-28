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
Now to setup the flask env, you'll find a default .flaskenv file to the project root folder with :  
````bash
FLASK_APP = neo4j_app (don't change it unless you know what you're doing)
FLASK_RUN_PORT = port on which flask is running
FLASK_RUN_HOST = host on which flask is running
FLASK_ENV = development (here debug mode is enabled, change it according to your development stade)
````
Finally, run the following command to start your flask app :  
````bash
flask run
````
