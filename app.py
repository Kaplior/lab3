from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

db_params = {
    'dbname': 'mydatabase',
    'user': 'lol',
    'password': 'Kaplior0909',
    'host': 'localhost',
    'port': 5432
}

def connect_to_db():
    try:
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()
        return conn, cursor
    except Exception as e:
        print("Error connecting to the database:", e)
        return None, None

@app.route('/data', methods=['GET'])
def get_all_data():
    try:
        conn, cursor = connect_to_db()
        if conn is None or cursor is None:
            return jsonify({'status': 500, 'message': 'Internal server error'})

        cursor.execute('SELECT id, city FROM table1')
        data = [{'id': row[0], 'city': row[1]} for row in cursor.fetchall()]

        conn.close()

        return jsonify({'data': data}), 200
    except Exception as e:
        print("Error retrieving data from database:", e)
        return jsonify({'error': 'Failed to retrieve data'}), 500

@app.route('/databyid/<int:city_id>', methods=['GET'])
def get_data_by_id(city_id):
    try:
        conn, cursor = connect_to_db()
        if conn is None or cursor is None:
            return jsonify({'status': 500, 'message': 'Internal server error'})

        cursor.execute('SELECT id, city FROM table1 WHERE id = %s', (city_id,))
        data = cursor.fetchone()
        if data:
            result = {'id': data[0], 'city': data[1]}
            conn.close()
            return jsonify(result), 200
        else:
            conn.close()
            return jsonify({'error': 'City not found'}), 404

    except Exception as e:
        print("Error retrieving data from database:", e)
        return jsonify({'error': 'Failed to retrieve data'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

