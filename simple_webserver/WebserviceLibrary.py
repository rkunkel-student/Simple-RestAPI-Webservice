#
import requests
from app import app
from flask import request


class WebserviceLibrary(object):
    """
    Test library for testing *Webservice* business logic.
    """

    def __init__(self):
        self.url = 'http://localhost:5000/todo/api/v1.0/tasks'
        self._result = ''

    def sanity(self):
        self._result = '1'

    # // Tests

    def query_all_tasks(self):
        r = requests.get(f"{self.url}")
        r.json()
        self._result = str(r.status_code == requests.codes.ok)

    def query_specific_task(self, val):
        r = requests.get(f"{self.url}/{val}")
        r.json()
        self._result = str(r.status_code == requests.codes.ok)

    def create_new_task(self, title, description):
        payload = {
            'title': title,
            'description': description,
        }
        r = requests.post(f"{self.url}", json=payload)
        self._result = str(r.status_code == requests.codes.created)

    def update_specific_task(self, val, title=None, description=None, done=None):
        payload = dict()
        if title is not None:
            payload['title'] = title
        if description is not None:
            payload['description'] = description
        if done is not None:
            payload['done'] = done
        r = requests.put(f"{self.url}/{val}", json=payload)
        self._result = str(r.status_code == requests.codes.ok)

    def delete_specific_task(self, val):
        r = requests.delete(f"{self.url}/{val}")
        r.json()
        self._result = str(r.status_code == requests.codes.ok)

    # // End Tests

    def result_should_be(self, expected):
        if self._result != expected:
            raise AssertionError('%s != %s - better message here' % (self._result, expected))

    def shutdown_server(self):
        func = request.environ.get('werkzeug.server.shutdown')
        if func is None:
            raise RuntimeError('Not running with the Werkzeug Server')
        func()

    @app.route('/shutdown', methods=['POST'])
    def shutdown(self):
        self.shutdown_server()
        return 'Server shutting down...'
