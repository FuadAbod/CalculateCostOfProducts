from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, product_table  
from flask import request
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = app.config['SQLALCHEMY_DATABASE_URI']="postgresql://postgres:1Advocate@localhost:5432/products"

migrate = Migrate(app, db)


@app.route('/', methods=('GET', 'POST'))
def index():
    data = request.form.to_dict()
    if not data:
        pass
    else:
        product = product_table(data['Product_name'], data['Product_price'])
        db.session.add(product)
        db.session.commit()
    return render_template('pricing.html')

@app.route('/calculate', methods=('GET', 'POST'))
def calculate():
    summary = db.session.query(product_table.price).all()
    total= 0
    for i in summary:
        for j in i:
            total+=j
    db.session.query(product_table).delete()
    db.session.commit()
    return render_template('calculate.html', summary=total)

if __name__ == '__main__':
    with app.app_context():
        db.init_app(app)
        db.create_all()
        app.run(debug=True)


