# spectrometer2

### Installation
```
$ cd spectrometer2/
$ pip install -r requirements.txt
$ python dashboard/webapp.py
```

open a browswer
`http://127.0.0.1:5000/git/test`
must show commits log from local directory of spectrometer2.

### Usage
Add a repository address to etc/repositories.yaml
with the following format  
```
modulename:
  repo: path/to/bare_repo/directory
```
Now the flask application must be up and serve requests:
```
$ python dashboard/webapp.py
```
Now `http://127.0.0.1:5000/git/modulename` will return repository log of added repository address in *yaml* file.

### Contribuition
Style guide:
https://code.google.com/p/soc/wiki/PythonStyleGuide  
http://www.pocoo.org/internal/styleguide/#styleguide
