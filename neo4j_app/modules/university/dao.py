from flask import jsonify
from datetime import datetime




class UnivDAO(object):
    """
    """

    def __init__(self, database, namespace):
        """
        """
        self.db = database
        self.ns = namespace


    def exists(self, data):
        """ Check if a document already exists in collection

        Parameter
        -----
        data (dict, json): document to check

        Returns
        -----
        True if exists, else False
        """
        pass


    def serialize_node(self, node):
        """
        """
        return {
            'id'   : node.id,
            'name' : node['name']
        }


    def serialize_relation(self, relation):
        """
        """
        return {
            'id'    : relation.id,
            'type'  : relation.type,
            'nodes' : {
                'concerned'  : self.serialize_node(relation.nodes[0]),
                'related_to' : self.serialize_node(relation.nodes[1]),
                'relation'   : dict(relation)
            } 
        }


    #---------------------------------------------
    #   BY ID
    #---------------------------------------------

    def getByID(self, id):
        """Return data from one record

        Parameter
        ----
        id (int) : the document unique id
        
        """
        res = self.db.run('MATCH (n:university) WHERE ID(n)={} RETURN n'.format(id))
        if res :
            for r in res:
                record = self.serialize_node(r['n'])
            return jsonify(record)
        self.ns.abort(404, message="Id {} doesn't exist".format(id), data={})
        

    # def update(self, id, data):
    #     """Update a data collection"""
    #     crypto = self.getByID(id)
    #     self.db.update_one(crypto, data)


    # def delete(self, id):
    #     """Delete a data collection"""
    #     data = self.getByID(id)
    #     self.db.delete_one(data)


    #---------------------------------------------
    #   BY NAME
    #---------------------------------------------

    def getByName(self, name):
        """Get a node by its name

        Parameter
        ----
        name (string) : name of the node
        
        """
        res = self.db.run("MATCH (n:university {name:'%s'}) RETURN n" % name)
        if res :
            record = {}
            for r in res :
                record = self.serialize_node(r['n'])
            return jsonify(record)
        self.ns.abort(404, message="Name {} doesn't exist".format(name), data={})
    

    #---------------------------------------------
    #   COMMON CRUD
    #---------------------------------------------

    def getAllNodes(self):
        """ Get all nodes in database
        """
        res = self.db.run('MATCH (n:university) RETURN n')
        return jsonify( list(self.serialize_node(record['n']) for record in res) )


    def create_univ(self, name):
        """ Create a new university 
        """
        res = self.db.run("CREATE (n:university {name:'%s'}) RETURN n" % name)
        for record in res :
            return jsonify( self.serialize_node(record['n']) )
        self.ns.abort(409, message="University {} already exists".format(name))

    
    def delete_univ(self, name):
        """ Delete a university and remove all its relationships
        """
        self.db.run("MATCH (n:university {name:'%s'}) DETACH DELETE n" % name)
        return ''


    #---------------------------------------------
    #   RELATIONSHIPS
    #---------------------------------------------

    def create_relation(self, name1, name2, data):
        """ Create a relationship between two universities
        """
        querry_match  = "MATCH (n1:university {name:'%s'}), (n2:university {name:'%s'})" % (name1, name2)
        querry_create = "CREATE (n1)-[r:connects_in {miles:'%d'}]->(n2) RETURN r" % (data['miles'])
        res = self.db.run(querry_match + " " + querry_create)
        for record in res :
            return jsonify( self.serialize_relation(record['r']) )


    def delete_relation(self, name1, name2):
        """ Delete a relation between two universities
        """
        self.db.run("MATCH (n1:university {name:'%s'})-[r:connects_in]->(n2:university {name:'%s'}) DELETE r" % (name1, name2))
        return ''
 

    def delete_AllRelations(self, name):
        """ Delete all relations from a university
        """
        self.db.run("MATCH(n:university {name:'%s'})-[r]-(:university) DELETE r" % name)
        return ''


    def getAllRelationships(self):
        """ Get all relationships in the graph
        """
        res = self.db.run("MATCH(n:university)-[r]->(:university) RETURN n, r")
        return jsonify( list(self.serialize_relation(record['r']) for record in res) )


    def getRelById(self, id):
        """ Get a relationship by its id
        """
        res = self.db.run('MATCH (n:university)-[r]->(:university) WHERE ID(r)={} RETURN n, r'.format(id))
        return jsonify( list(self.serialize_relation(record['r']) for record in res) )


    def getRelByNodeId(self, id):
        """ Get a relationship by the id of a university
        """
        res = self.db.run('MATCH (n:university)-[r]->(:university) WHERE ID(n)={} RETURN n, r'.format(id))
        return jsonify( list(self.serialize_relation(record['r']) for record in res) )


    def getRelByName(self, name):
        """ Get a relationship by the name of a university
        """
        res = self.db.run("MATCH(n:university {name:'%s'})-[r]->(:university) RETURN n, r" % name)
        return jsonify( list(self.serialize_relation(record['r']) for record in res) )
