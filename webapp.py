from flask import Flask, json, jsonify, Response
import githelpers

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/git/<module_name>')
def git_stat(module_name):
    stats = githelpers.commits_stat(module_name)
    # return Response(response=json.dumps(stats,indent=2, separators=(',', ': ')), status=200, mimetype='application/json')
    return jsonify(stats)

@app.route('/gerrit/<module_name>')
def gerrit_stat():
    return "Not implemented"

if __name__ == '__main__':
    app.run(debug=True)
