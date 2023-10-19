from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root_password@mysql/products'
db = SQLAlchemy(app)

class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)  
    prix = db.Column(db.DECIMAL(10, 2), nullable=False)

@app.route('/add_product', methods=['POST']) # route de l'API en POST 
def add_product():
    data = request.get_json()
    new_product = Product(
        name=data['name'],
        description=data['description'],
        prix=data['prix'] 
    )

    try:
        db.session.add(new_product)
        db.session.commit()
        return jsonify({'message': 'Product added successfully'}), 201
    except Exception as e:
        print("Error adding product:", str(e))
        return jsonify({'message': 'Error adding product'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
