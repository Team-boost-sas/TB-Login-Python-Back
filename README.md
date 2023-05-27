# tb-login-python-back

## Installation

### Prerequisite

Make sure you have the following installed outside the current project directory and available in your `GOPATH`

    - [Python](https://www.python.org/)  v3.10 python version recommended


### Create virtual environment
Create a virtual environment and activate it

```

$ python -m venv venv

windows
$ venv\Scripts\activate.bat

linux
$ source venv/bin/activate

```

### Install packages
```
$ pip install -r requirements.txt
```
### start Proyect
```
$ python src/main.py
```

## Test the endpoints

with the vscode [REST Cliente](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) extension try to send the requests that are in the `./request/request.http` file.