from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/git/<module_name>')
def git_stat(module_name):
    #get_modules_repo(module_name)


@app.route('/gerrit/<module_name>')
def gerrit_stat():
    return "Not implemented"

if __name__ == '__main__':
    app.run()
