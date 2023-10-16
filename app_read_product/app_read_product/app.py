from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root_password@mysql/products'
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

@app.route('/read_product', methods=['GET'])
def read_product():
    products = Product.query.all()
    product_list = []
    for product in products:
        product_list.append({'id': product.id, 'name': product.name})
    return jsonify({'products': product_list})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
