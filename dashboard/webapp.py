import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from flask import Flask, json, jsonify, Response
# todo: http://flask.pocoo.org/snippets/83/
from helpers.githelpers import GitHandler

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/git/<module_name>')
def git_stat(module_name):
    git_handle = GitHandler(module_name)
    stats = git_handle.get_commits_stat()
    # return Response(response=json.dumps(stats,indent=2, separators=(',', ': ')), status=200, mimetype='application/json')
    return jsonify(stats)

@app.route('/gerrit/<module_name>')
def gerrit_stat():
    return "Not implemented"

if __name__ == '__main__':
    app.run(debug=True)
