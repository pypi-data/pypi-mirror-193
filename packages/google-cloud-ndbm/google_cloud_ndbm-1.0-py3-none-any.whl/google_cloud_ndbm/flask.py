"""Google cloud ndb binding for Flask."""
import os
from google.cloud import ndb


def ndb_wsgi_middleware(wsgi_app, client):
    """Flask middleware with ndb.Client context."""
    def middleware(environ, start_response):
        with client.context():
            return wsgi_app(environ, start_response)

    return middleware


def bind(app, gae_project_id):
    """Wrap the Flask app in middleware."""
    # https://stackoverflow.com/questions/43628002/google-vision-api-project-not-passed
    os.environ["GCLOUD_PROJECT"] = gae_project_id
    app.wsgi_app = ndb_wsgi_middleware(app.wsgi_app, ndb.Client())
    return app.wsgi_app
