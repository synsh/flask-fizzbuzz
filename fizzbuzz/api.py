from flask import Blueprint, request, jsonify
from http import HTTPStatus as HTTP_STATUS
from fizzbuzz.util import fizzbuzzer
from fizzbuzz.db import get_db


bp = Blueprint('auth', __name__, url_prefix='/api')


@bp.route('/search', methods=['GET'])
def api_search():
    int1 = request.args.get('int1', type=int)
    int2 = request.args.get('int2', type=int)
    limit = request.args.get('limit', type=int)
    str1 = request.args.get('str1', type=str)
    str2 = request.args.get('str2', type=str)

    # Validation starts here
    errors = {}
    INT_MAX_VAL= 1000
    STR_MAX_LEN = 10
    INT_ERR_MSG = 'The value must be a valid integer between 1 and {}'
    STR_ERR_MSG = 'The value must be a valid string with a max length of {} chars'

    if not limit or type(limit) != int or limit < 1 or limit > INT_MAX_VAL:
        errors['limit'] = INT_ERR_MSG.format(INT_MAX_VAL)
    if not int1 or type(int1) != int or int1 < 1 or int1 > INT_MAX_VAL:
        errors['int1'] = INT_ERR_MSG.format(INT_MAX_VAL)
    if not int2 or type(int2) != int or int2 < 1 or int2 > INT_MAX_VAL:
        errors['int2'] = INT_ERR_MSG.format(INT_MAX_VAL)
    if not str1 or type(str1) != str or len(str1) == 0 or len(str1) > STR_MAX_LEN:
        errors['str1'] = STR_ERR_MSG.format(STR_MAX_LEN)
    if not str2 or type(str2) != str or len(str2) == 0 or len(str2) > STR_MAX_LEN:
        errors['str2'] = STR_ERR_MSG.format(STR_MAX_LEN)

    if len(errors) > 0:
        return jsonify({ 'message': 'Validation failure', 'errors': errors }), HTTP_STATUS.BAD_REQUEST
    # Validation ends here


    try:
        db = get_db()
        sql = 'INSERT INTO requests (param_int1, param_int2, param_limit, param_str1, param_str2) VALUES (?, ?, ?, ?, ?)'
        db.execute(sql, (int1, int2, limit, str1, str2))
        db.commit()
    except Exception as e:
        print(e)
        return jsonify({'message': 'Something went wrong, please try again later.'}), HTTP_STATUS.INTERNAL_SERVER_ERROR        


    try:
        result = fizzbuzzer(limit=limit, int1=int1, int2=int2, str1=str1, str2=str2)
    except Exception as e:
        print(e)
        return jsonify({'message': 'Something went wrong, please try again later.'}), HTTP_STATUS.INTERNAL_SERVER_ERROR

    return jsonify({ 'result': result })


@bp.route('/statistics', methods=['GET'])
def api_stats():
    stats = {}

    try:
        db = get_db()

        sql = """
            SELECT param_int1, param_int2, param_limit, param_str1, param_str2
            FROM requests
            GROUP BY param_int1, param_int2, param_limit, param_str1, param_str2
            ORDER BY COUNT(1) DESC
            LIMIT 1
        """
        
        result = db.execute(sql)
        if result:
            stats = dict(result.fetchone())

    except Exception as e:
        print(e)
        return jsonify({'message': 'Something went wrong, please try again later.'}), HTTP_STATUS.INTERNAL_SERVER_ERROR

    return jsonify(stats)