from __future__ import print_function, division

import json

#For experimental purposes.  Should not be long-term solution
import download

import pytest
import logging

#####
# Testing
#####

def setup_module(module):
    logging.basicConfig(filename='json_tools.py.log',
                        level=logging.DEBUG)
    logging.debug("NEW PyTest run")

def teardown_module(module):
    logging.debug("Finished last PyTest run")

class TestJsonTools:
    
    def test_parse_valid(self):
        test_file = open("test_data/test_data_valid.json")
        parse(test_file)
        
        assert False

    def test_parse_needs_redirect(self):
        test_file = open("test_data/test_data_needs_redirect.json")
        
        with pytest.raises(NameError):
            parse(test_file)
        
        test_file.close()
        assert False

    def test_parse_no_such_page(self):
        test_file = open("test_data/test_data_no_such_page.json")

        with pytest.raises(NameError):
            parse(test_file)
        
        test_file.close()
        assert False

#####
# Appliction Code
#####

def parse_links(socket):
    """
    USE THIS FOR EVERYTHING AFTER THE INITIAL QUERY HAS BEEN VALIDATED
    WITH validate()
    """

def validate(socket):
    """
    ONLY RUN THIS AGAINST THE INITIAL QUERY BECAUSE AFTER THAT, WE
    ASSUME THAT PAGES ON WIKIPEDIA WILL ONLY LINK TO OTHER VALID
    WIKIPEDIA PAGES

    Takes a socket from the "download_raw_link_socket()" in
    "download.py"

    If the document contains no errors (no redirect or similar
    problems), the parser will return a dictionary of the links in the
    file and the data available about them.  It will also return a
    string containing the continue (or "" if there is no continue)
    """
    json_dict = json.load(socket)
    socket.close()
    links = ""
    ###
    # Verify whether the page exists on Wikipedia
    ###
    try:
        links = json_dict["query"]["pages"][0]["links"]
    except KeyError: # if no links entry is found in the dictionary
        missing = json_dict["query"]["pages"][0]["missing"]
        # if some error occurs here, something funny and
        # unexpected is going on...
        if missing:
            raise LookupError("The requested page does not exist"
                              + " on Wikipedia")
    ###
    # Checks whether the page needs a redirect (due to bad spelling)
    ###
    needs_redirect = False
    for link in links:
        if (link["title"] == "Category:Redirects from other capitalisations"):
            needs_redirect = True
            break
    # If @needs_redirect, searches for the proper spelling of the title
    if needs_redirect:
        current_title = json_dict["query"]["pages"][0]["title"]
        normalized_current_title = current_title.upper()
        for link in links:
            if link["title"].upper() == normalized_current_title:
                return(link["title"]) # proper spelling of the page's title
    #
    # If all that worked, for now, that means we have a valid page
    # and that the script can go ahead and start making requests with
    # a pllimit of 500, knowing that the links returned will be for
    # a valid page
    #
    return(True)

if __name__ == "__main__":
    # X = open("test_data/test_data_no_such_page.json", "r") # KeyError
    X = open("test_data/test_data_needs_redirect.json", "r") # No error
    is_valid = validate(X)
    print(is_valid)
