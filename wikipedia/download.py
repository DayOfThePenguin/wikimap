'''
    1. Retrieving information about a particular json file
    2. Parsing information a json file into a Python object (To be implemented later)
'''

from __future__ import print_function, division

from urllib import URLopener

import pytest
import logging

#####
# Testing
#####

def setup_module(module):
    logging.basicConfig(filename='mediaWiki.py.log',
                        level=logging.DEBUG)
    logging.debug("NEW PyTest run")

def teardown_module(module):
    logging.debug("Finished last PyTest run")
    
class TestMediaWiki:
    
    def test_generate_download_string_title(self):
        expected = ("action=query"
                    + "&titles=Quantum mechanics&prop=links&pllimit=10"
                    + "&format=json&formatversion=2&continue=")
        generated = generate_link_download_string("Quantum mechanics")
        assert(expected == generated)

    def test_generate_download_string_all_params(self):
        expected = ("action=query"
                    + "&titles=Quantum mechanics&prop=links&pllimit=200"
                    + "&format=json&formatversion=2&continue=")
        generated = generate_link_download_string("Quantum mechanics",
                                                  "", 200, "query",
                                                  "json", 2)
        assert(expected == generated)

#####
# Application Code
#####

# https://en.wikipedia.org/w/api.php?action=query&titles=Quantum%20mechanics
# &prop=links&pllimit=10&format=jsonfm&formatversion=2&continue=
        
def generate_link_download_string(page_name, cont="", limit="10",
                                  action="query", return_format="json",
                                  format_version=2):
    """ This function generates the download string (the part
    that comes after the "/w/api.php?" in a call to the Wikimedia API)
    """
    download_string = (("action=%s" +
                        "&titles=%s" +
                        "&prop=links" +
                        "&pllimit=%s" +
                        "&format=%s" +
                        "&formatversion=%s" +
                        "&continue=%s") %
                       (action, page_name, limit, return_format,
                        format_version, cont)
    )
    logging.debug("Generated download string was:\n\t%s"
                  % download_string)
    return(download_string)

def download_raw_link_data(prefix, page_name, cont=""):
    X = URLopener()
    download_string = generate_link_download_string(page_name, cont)
    url = prefix + download_string
    socket = X.open(url)
    raw_data = socket.read()
    return(raw_data)

def download_raw_link_socket(prefix, page_name, cont=""):
    X = URLopener()
    download_string = generate_link_download_string(page_name, cont)
    url = prefix + download_string
    socket = X.open(url)
    return(socket)


if __name__ == "__main__":
    raw_data = download_raw_link_data("https://en.wikipedia.org/w/api.php?", "Quantum mechanics")
    print(raw_data)
