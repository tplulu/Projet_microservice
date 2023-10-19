from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root_password@mysql/products'
db = SQLAlchemy(app)

class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)  # Nouvelle colonne description
    prix = db.Column(db.DECIMAL(10, 2), nullable=False)  # Nouvelle colonne prix

@app.route('/read_product', methods=['GET']) # route de l'API en GET 
def read_product():
    products = Product.query.all()
    product_list = []
    for product in products:
        product_data = {
            'id': product.id,
            'name': product.name,
            'description': product.description,  
            'prix': product.prix
        }
        product_list.append(product_data)
    return jsonify({'products': product_list})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
