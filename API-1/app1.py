from flask import Flask, jsonify
# Create a Flask web application
app = Flask(__name__)


# Define a route and a function to handle requests to that route
@app.route('/')
def hello():
        data = {
            'message': 'Hello, this is flask api serving json output.',
            'data':{
                'name': 'srikanth'
             }
        }

        return jsonify(data)


# Run the application
if __name__ == '__main__':
    app.run(host="0.0.0.0")

