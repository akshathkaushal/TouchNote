# TouchNote
[![Build Status](https://travis-ci.com/akshathkaushal/TouchNote.svg?branch=master)](https://travis-ci.com/akshathkaushal/TouchNote)

![alt text](https://cdn.icon-icons.com/icons2/1494/PNG/512/touch_102928.png)

TouchNote is a simple and lightweight ToDo-List app which is helpful in keeping small notes and ideas handy.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.
Docker and docker-compose are required for running the application.

```bash
pip3 install docker
pip3  install docker-compose
```

## Usage

```python
docker-compose build    # builds the Docker image and attaches it to the container
docker-compose up       # starts the docker container
```
    The app is now running on localhost:8000

## Creating and Running Tests
### Creating a test:
```python
cd app/TouchNote/
```
Create a new test in the file tests.py

### Running a test:
```python
cd app/
python3 manage.py test
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
