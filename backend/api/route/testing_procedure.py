from flask import Blueprint, request, jsonify
from pandas import read_csv

ALLOWED_EXTENSIONS = {'txt'}

testing_api = Blueprint('api', __name__)


@testing_api.route('/health-check', methods=['GET'])
def check_api_health():
    return 'cool'


@testing_api.route('/', methods=['POST'])
def upload_test_data():
    file = request.files['file']
    if file and __allowed_file(file.filename):
        __read_data_file(file)
        return jsonify({"error": "Problems reading file."})
    return jsonify({"error": "Problems reading file."})


def __allowed_file(filename: str):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def __read_data_file(file):
    df = read_csv(file, header=None)
    for index, row in df.iterrows():
        print(f'abbie {row[0]} {row[1]}')

