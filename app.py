from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

order_book = {
    'buy': [],
    'sell': [],
}

@app.route('/')
def index():
    return render_template('index.html', order_book=order_book)

@app.route('/add_order', methods=['POST'])
def add_order():
    data = request.form
    order_type = data['type']
    price = float(data['price'])
    quantity = int(data['quantity'])

    order = {'price': price, 'quantity': quantity}

    order_book[order_type].append(order)

    return jsonify({'message': 'Order added successfully'})

if __name__ == '__main__':
    app.run(debug=True)
