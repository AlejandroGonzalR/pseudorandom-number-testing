from flask import Flask
from api.route.testing_procedure import testing_api


def create_app():
    app = Flask(__name__)
    app.register_blueprint(testing_api, url_prefix='/api')
    return app


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    api = create_app()
    api.run(host='0.0.0.0', port=port)
