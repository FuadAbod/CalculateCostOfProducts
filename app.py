from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, product_table  
from flask import request
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://anpovvgsbmrjhx:8dc85beb3e58bb37eb132b5fa40fd833378f46346e269fe74f296abc664f199d@ec2-3-219-135-162.compute-1.amazonaws.com:5432/dek5bptg3n886s"
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


