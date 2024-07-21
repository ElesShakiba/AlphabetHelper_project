from app import app, db, Word

# ایجاد پایگاه داده و افزودن داده‌ها
with app.app_context():
    db.create_all()

    def add_word(letter, name, family, food, city, country):
        word = Word(
            letter=letter,
            name=name,
            family=family,
            food=food,
            city=city,
            country=country
        )
        db.session.add(word)
        db.session.commit()

    # اضافه کردن داده‌های نمونه
    add_word('ا', 'احمد', 'امیری', 'آش', 'اصفهان', 'ایران')
    add_word('ب', 'بهروز', 'بخشی', 'باقالی‌پلو', 'بندرعباس', 'بحرین')
    # اضافه کردن داده‌های بیشتر...
