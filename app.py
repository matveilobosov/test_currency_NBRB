import logging

from flask import Flask, request, jsonify

from exceptions import InvalidApiRequestError
from currency_service import get_currency_rates_by_date, get_currency_rate_by_date_and_code
from utils import calculate_crc32


logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


app = Flask(__name__)


@app.route('/api/rates', methods=['GET'])
def get_rates():
    date = request.args.get('date')
    if not date:
        logging.warning('Date parameter is missing')
        return jsonify({'error': 'Date parameter is required'}), 400
    
    try:
        data = get_currency_rates_by_date(date)
        logging.info(f'Successfully fetched rates for date {date}')
    except InvalidApiRequestError:
        logging.error(f'Invalid API request for date {date}')
        return jsonify({'error': 'invalid request'}), 500
    
    if not data:
        logging.warning(f'No data found for date {date}')
        return jsonify({'error': 'No data for such request'}), 404

    response = jsonify(data)
    response.headers['X-CRC32'] = calculate_crc32(response.get_data(as_text=True))
    logging.info(f'Response for date {date} with CRC32 {response.headers["X-CRC32"]}')
    return response


@app.route('/api/rate', methods=['GET'])
def get_rate():
    date = request.args.get('date')
    currency_code = request.args.get('code')
    
    if not date or not currency_code:
        logging.warning('Date or currency code parameter is missing')
        return jsonify({'error': 'Date and currency code parameters are required'}), 400
    
    try:
        data = get_currency_rate_by_date_and_code(date, currency_code)
        logging.info(f'Successfully fetched rate for date {date} and code {currency_code}')
    except InvalidApiRequestError:
        logging.error(f'Invalid API request for date {date} and code {currency_code}')
        return jsonify({'error': 'invalid request'}), 500
    
    if not data:
        logging.warning(f'No data found for date {date} and code {currency_code}')
        return jsonify({'error': 'No data for such request'}), 404

    response = jsonify(data)
    response.headers['X-CRC32'] = calculate_crc32(response.get_data(as_text=True))
    logging.info(f'Response for date {date} and code {currency_code} with CRC32 {response.headers["X-CRC32"]}')
    return response


if __name__ == '__main__':
    app.run(debug=True)
