from flask_restplus import Namespace

from neo4j_app import get_db
from .models import create_univ_model, create_distance_model, create_relationship_model
from .dao import UnivDAO


# NAMESPACE
ns = Namespace('api/univ', 
                description = 'Universities related operations', 
                endpoint='univ')

db = get_db()               # db graph
DAO = UnivDAO(db, ns)       # univ controller

# MODELS
univ_model = create_univ_model(ns)
rel_param  =  create_distance_model(ns)  
rel_model  = create_relationship_model(ns, univ_model, rel_param)


from .routes import *
