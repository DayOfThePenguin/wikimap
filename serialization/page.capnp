struct Page {
    title @0 :Text; # from title attribute in json
    pageid @0 :Int32; # from pageid attribute in json
    links @0 :List(Link); # list of the links in the page
}

struct Link {
    title @0 :Text; # title of the link
}
