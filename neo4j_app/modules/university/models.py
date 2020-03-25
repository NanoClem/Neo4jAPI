from flask_restplus import fields


def create_univ_model(ns):
    """
    """
    univ_model = ns.model('University', {
        'id'   : fields.Integer(description='university unique identifier'),
        'name' : fields.String(required=True, description='name of the university')
    })
    return univ_model


def create_distance_model(ns):
    """
    """
    dist_model = ns.model('Distance', {
        'miles' : fields.Integer(required=True, description="distance that separates two universities")
    })
    return dist_model


def create_relationship_model(ns, node_model, rel_elem_model):
    """
    """
    rel_model = ns.model('Relationship', {
        'id'    : fields.Integer(description='relationship unique identifier'),
        'type'  : fields.String(required=True, description='type of the relationship'),
        'nodes' : fields.Nested(ns.model('Rel_nodes', {
            'concerned'  : fields.Nested(node_model, required=True, description="Node directly concerned by the relationship"),
            'related_to' : fields.Nested(node_model, required=True, description="Node which the concerned one is connected to"),
            'relations'  : fields.Nested(rel_elem_model, required=True, description="Elements that connect nodes") 
        }), required=True)
    })
    return rel_model