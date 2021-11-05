from flask import Flask, render_template, request, jsonify
from infrastructure.services import dashboard_service, report_service

app = Flask(__name__)


# Dashboard Query
@app.route('/v1/metadata', methods=['GET'])
def metadata():
    try:
        return dashboard_service.get_sales_dashboard()
    except Exception as error:
        app.logger.error(error)
        response = jsonify(({'Error': error}))
        response.status_code = 500
        return response


# Report Query
@app.route('/v1/report/sales', methods=['GET'])
def sales_report():
    try:
        from_date = request.args.get('from_date')
        to_date = request.args.get('to_date')
        print(to_date, from_date)
        return report_service.sales_report(from_date, to_date), 200
    except Exception as error:
        app.logger.error(error)
        response = jsonify({'Error': error})
        response.status_code = 500
        return response


@app.route('/', methods=['GET'])
def index():
    return "<!DOCTYPE html><html lang='en'><head><meta charset='UTF-8'><title>PlaceMe | Visualization Service API</title></head><body><h1>Visualization API | @2021</h1></body></html>"


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
