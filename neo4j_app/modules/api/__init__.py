from flask_restplus import Api


# API constructor
api = Api(
    title = "Neo4j API",
    description = "interact with data from Neo4j",
    version = 1.0
)


def register_api(app):
    """ Registering namespaces and the api to the app
    """
    from neo4j_app.modules.university import ns as ns_univ
    
    api.add_namespace(ns_univ)  # adding record namespace
    api.init_app(app)
