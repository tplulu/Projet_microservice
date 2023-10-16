from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root_password@mysql/products'
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

@app.route('/add_product', methods=['POST'])
def add_product():
    data = request.get_json()
    new_product = Product(name=data['name'])

    try:
        db.session.add(new_product)
        db.session.commit()
        return jsonify({'message': 'Product added successfully'}), 201
    except Exception as e:
        print("Error adding product:", str(e))
        return jsonify({'message': 'Error adding product'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
