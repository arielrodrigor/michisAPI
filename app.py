from flask import Flask, jsonify, request
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/cats', methods=['GET'])
def fetch_data_cats():
    # Make the RESTful API call
    response = requests.get('https://api.thecatapi.com/v1/images/search?limit=10')

    # Check the status code of the response
    if response.status_code == 200:
        # Extract the data from the response
        data = response.json()

        # Return the data as a JSON response
        return jsonify(data)
    else:
        # Return an error message if the request fails
        return jsonify({'error': 'Failed to fetch data'})

@app.route('/cats/breed', methods=['GET'])
def fetch_data_cats_breed():
    # Make the RESTful API call
    response = requests.get('https://api.thecatapi.com/v1/breeds')

    # Check the status code of the response
    if response.status_code == 200:
        # Extract the data from the response
        data = response.json()

        # Return the data as a JSON response
        return jsonify(data)
    else:
        # Return an error message if the request fails
        return jsonify({'error': 'Failed to fetch data'})


@app.route('/dogs', methods=['GET'])
def fetch_data_dogs():
    # Make the RESTful API call
    response = requests.get('https://dog.ceo/api/breeds/list/all')

    # Check the status code of the response
    if response.status_code == 200:
        # Extract the data from the response
        data = response.json()

        # Return the data as a JSON response
        return jsonify(data)
    else:
        # Return an error message if the request fails
        return jsonify({'error': 'Failed to fetch data'})


if __name__ == '__main__':
    app.run()
