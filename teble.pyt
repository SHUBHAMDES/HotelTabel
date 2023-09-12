from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample data (in-memory database)
orders = []

@app.route('/')
def index():
    return render_template('index.html', orders=orders)

@app.route('/add_order', methods=['POST'])
def add_order():
    data = request.get_json()
    order = {
        'id': len(orders) + 1,
        'table_number': data['table_number'],
        'items': data['items'],
        'status': 'Pending'
    }
    orders.append(order)
    return jsonify({'message': 'Order added successfully!'})

@app.route('/update_order/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    data = request.get_json()
    for order in orders:
        if order['id'] == order_id:
            order['items'] = data['items']
            order['status'] = data['status']
            return jsonify({'message': 'Order updated successfully!'})
    return jsonify({'error': 'Order not found'}), 404

@app.route('/delete_order/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    for order in orders:
        if order['id'] == order_id:
            orders.remove(order)
            return jsonify({'message': 'Order deleted successfully!'})
    return jsonify({'error': 'Order not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)