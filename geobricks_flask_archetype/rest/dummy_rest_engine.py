from flask import Flask
from flask.ext.cors import CORS
from geobricks_mod16.rest.mod16_rest import mod16

app = Flask(__name__)
cors = CORS(app,
            resources={
                r'/*': {
                    'origins': '*',
                    'headers': ['Content-Type']
                }
            })
app.register_blueprint(mod16, url_prefix='/blueprint')

@app.route('/', methods=['GET'])
def say_hello():
    return 'Hello, Dummy REST Engine!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

def start_dummy_rest_engine():
    app = Flask(__name__)
    cors = CORS(app,
                resources={
                    r'/*': {
                        'origins': '*',
                        'headers': ['Content-Type']
                    }
                })
    app.register_blueprint(mod16, url_prefix='/blueprint')
    @app.route('/', methods=['GET'])
    def say_hello():
        return 'Hello, Dummy REST Engine!'
    app.run(host='0.0.0.0', debug=True)