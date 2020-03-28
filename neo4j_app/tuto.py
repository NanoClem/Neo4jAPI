import os
from dotenv import load_dotenv
from neo4j import GraphDatabase, basic_auth



load_dotenv('.env')
DB_URI      = os.getenv('DB_URI')
DB_PASSWORD = os.getenv('DB_PASSWORD')

# AUTH
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')


neo4j_driver = GraphDatabase.driver(DB_URI, auth=basic_auth(USERNAME, PASSWORD), encrypted=False)



def serialize_node(node):
        """
        """
        return {
            'id'   : node.id,
            'name' : node['name']
        }


def serialize_relation(relation):
    return {
        'id'    : relation.id,
        'type'  : relation.type,
        'nodes' : {
            'concerned'  : serialize_node(relation.nodes[0]),
            'related_to' : serialize_node(relation.nodes[1]),
            'relation'   : dict(relation)
        } 
    }



if __name__ == "__main__":
    
    db_driver = neo4j_driver
    with db_driver.session() as db_session:
        results = db_session.run("MATCH(n:university {name:'Poltech'}) RETURN n")
        for r in results:
            print(serialize_node(r['n']))