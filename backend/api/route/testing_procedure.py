from flask import Blueprint, request, jsonify
from api.procedure.chi import chi
from api.procedure.poker import poker
from api.procedure.ks import ks
from api.procedure.mean import mean
from api.procedure.variance import variance

ALLOWED_EXTENSIONS = {'txt'}
ALFA = 0.05
CONFIDENCE = 0.95

testing_api = Blueprint('api', __name__)


@testing_api.route('/health-check', methods=['GET'])
def check_api_health():
    return 'cool'


@testing_api.route('/', methods=['POST'])
def upload_test_data():
    file = request.files['file']
    min_limit = request.form.get('minLimit')
    max_limit = request.form.get('maxLimit')
    interval_range = request.form.get('intervalRange')
    test = request.args.get('test')
    if file and __allowed_file(file.filename):
        data = __read_data_file(file.read())
        response = __route_test_procedure(test, data, int(min_limit), int(max_limit), int(interval_range))
        return jsonify(response)
    return jsonify({"error": "Problems reading file."})


def __allowed_file(filename: str):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def __read_data_file(file):
    return file.decode("utf-8").replace(',', '.').replace('\t', '').split('\n')


def __route_test_procedure(test, data, min_limit, max_limit, interval_range):
    print(test)
    switcher = {
        'chi': chi,
        'poker': poker,
        'ks': ks,
        'mean': mean,
        'variance': variance
    }
    func = switcher.get(test, "Invalid Procedure")
    return func(data, ALFA, CONFIDENCE, interval_range, min_limit, max_limit)

