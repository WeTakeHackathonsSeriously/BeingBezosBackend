from google.cloud import vision
import get_net_worth

def get_objects(image, client):
    google_result = client.object_localization(image=image, max_results = 3)
    objects = result.localized_object_annotations

    return [make_json_object(obj) for obj in objects]
    
def make_json_object(object_):
        vertices = [ object_.bounding_poly.normalized_vertices[0].x
                   , object_.bounding_poly.normalized_vertices[0].y
                   , object_.bounding_poly.normalized_vertices[2].x
                   , object_.bounding_poly.normalized_vertices[2].y
                   ]
        netw = get_net_worth()
        prod_price = get_product_price(object_.name)
        json_object =
            { "item" : object_.name
            , "box"  : vertices
            , "rel"  : relative_price
            }

        return json_object
