from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS  # وارد کردن CORS

app = Flask(__name__)

# تنظیمات پایگاه داده
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# فعال کردن CORS
CORS(app)

# تعریف مدل پایگاه داده
class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    letter = db.Column(db.String(1), nullable=False)
    name = db.Column(db.String(100))
    family = db.Column(db.String(100))
    food = db.Column(db.String(100))
    city = db.Column(db.String(100))
    country = db.Column(db.String(100))

    def __repr__(self):
        return f'<Word {self.letter}>'

# ایجاد جداول پایگاه داده
with app.app_context():
    db.create_all()

@app.route('/api/words', methods=['GET'])
def get_words():
    letter = request.args.get('letter', '')
    word_data = Word.query.filter_by(letter=letter).first()
    if word_data:
        return jsonify({
            'name': word_data.name,
            'family': word_data.family,
            'food': word_data.food,
            'city': word_data.city,
            'country': word_data.country
        })
    else:
        return jsonify({})

if __name__ == '__main__':
    app.run(debug=True)
