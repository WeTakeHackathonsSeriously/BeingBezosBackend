from google.cloud import vision
from get_net_worth import get_net_worth
from get_product_price import get_product_price

def get_objects(image, client):
    google_result = client.object_localization(image=image, max_results = 3)
    objects = google_result.localized_object_annotations

    objects_ = []
    for obj in objects:
        obj_ = make_json_object(obj)
        if obj_ != None:
            objects_.append(obj_)

    return objects_
    
def make_json_object(object_):
        vertices = [ object_.bounding_poly.normalized_vertices[0].x
                   , object_.bounding_poly.normalized_vertices[0].y
                   , object_.bounding_poly.normalized_vertices[2].x
                   , object_.bounding_poly.normalized_vertices[2].y
                   ]
        netw = get_net_worth()
        prod_price = get_product_price(object_.name)

        if netw == None or prod_price == None:
            return None

        json_object = { "item" : object_.name
            , "box"  : vertices
            , "rel"  : prod_price / netw
            }

        return json_object
