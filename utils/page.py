"""
module with scripts for dealing with capnp messages

"""

import capnp
import wikimap.serialization.page_capnp as page_capnp

def capnp_from_json(json_data):
    """ generate a capnp buffer from a json dictionary
    
    Parameters
    ----------
    json_data : dictionary containing a json object
    The data in this object should represent a complete page
    (with all of the continues followed and appended into the 
    links directory).  In the tree of the json data returned by
    wikimedia, this dictionary should have the attributes
    "pageid" and "title" and the list "links" as top-level
    elements
    
    Returns
    -------
    page : capnp serialized version of json_data
    """ 
    # create the objects and allocate the memory for the links
    page = page_capnp.Page.new_message() # page is a new Page object
    links = page.init("links", len(json_data["links"]))
    
    # add the attributes from the json
    page.pageid = json_data["pageid"]
    page.title = json_data["title"]
    
    # load the links
    for i in range(len(json_data["links"])):
        link = links[i]
        link.title = json_data["links"][i]["title"]
        
    return page
