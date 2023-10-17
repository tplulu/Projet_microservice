from flask import Flask, render_template
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

@app.route('/products', methods=['GET'])
def list_products():
    products = Product.query.all()
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
