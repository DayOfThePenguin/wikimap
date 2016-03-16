# Step 8
import logging

import os
import urlparse
from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.wsgi import SharedDataMiddleware
from werkzeug.utils import redirect
from jinja2 import Environment, FileSystemLoader

class Shortly(object):

    def __init__(self):
        logging.basicConfig(filename='wikimap.py.log', level=logging.DEBUG)
        template_path = os.path.join(os.path.dirname(__file__),
                                     "templates")
        self.jinja_env = Environment(loader=FileSystemLoader(template_path),
                                     autoescape=True)
        self.url_map = Map([
            Rule("/", endpoint="home_page"),
            Rule("/map_view", endpoint="map_view"),
        ])

    def dispatch_request(self, request):# good
        adapter = self.url_map.bind_to_environ(request.environ)
        try:
            endpoint, values = adapter.match()
            return getattr(self, "on_"+endpoint)(request, **values)
        except HTTPException, e:
            return e

    def render_template(self, template_name, **context):# good
        t = self.jinja_env.get_template(template_name)
        return Response(t.render(context), mimetype="text/html")

#####
# VIEWS
#####
    def on_home_page(self, request):
        error = None
        page = ''
        if request.method == "POST":
            page = request.form["page"]
            logging.debug(page)
            if not is_valid_page(page):
                error = "Please enter the name of a valid page on Wikipedia"
            else:
                return redirect("/map_view")
        return self.render_template("home_page.html", error=error) 
    
    def on_map_view(self, request): # TODO FINISH FIXING THIS
        return self.render_template("map_view.html") 
#####
# END VIEWS
#####

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)    

## End Shortly class
    
def create_app(with_static=True):
    app = Shortly()
    if with_static:
        app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
            "/static": os.path.join(os.path.dirname(__file__),
                                    "static")
        })
    return app

def is_valid_page(page): # TODO Implement this...
    return True


## End application code

if __name__ == "__main__":
    from werkzeug.serving import run_simple
    app = create_app()
    run_simple("127.0.0.1", 5100, app, use_debugger=True,
               use_reloader=True)
