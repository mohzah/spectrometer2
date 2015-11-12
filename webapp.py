from flask import Flask, json
import githelpers

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/git/<module_name>')
def git_stat(module_name):
    stats = githelpers.commits_stat(module_name)
    return json.dumps(stats)


@app.route('/gerrit/<module_name>')
def gerrit_stat():
    return "Not implemented"

if __name__ == '__main__':
    app.run(debug=True)
