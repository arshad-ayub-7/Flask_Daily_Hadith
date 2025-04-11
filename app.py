from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hadiths.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Hadith(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)

@app.route('/')
def home():
    hadith = Hadith.query.order_by(db.func.random()).first()
    return render_template('hadith.html', text=hadith.text if hadith else "No hadiths yet!")

@app.route('/api/hadith')
def get_random_hadith():
    hadith = Hadith.query.order_by(db.func.random()).first()
    return jsonify({"hadith": hadith.text}) if hadith else jsonify({"message": "No hadiths found"})

@app.route('/add/<text>')
def add_hadith(text):
    new = Hadith(text=text)
    db.session.add(new)
    db.session.commit()
    return f"Added: {text}"
@app.route('/add_bulk')
def add_bulk():
    hadiths = [
        "Actions are judged by intentions.",
        "The best among you are those who have the best manners and character.",
        "Make things easy, not difficult.",
        "A good word is charity.",
        "He who does not thank people, does not thank Allah.",
        "None of you truly believes until he loves for his brother what he loves for himself.",
        "The strong is not the one who overcomes people by his strength, but the strong is the one who controls himself while in anger.",
        "Feed the hungry, visit the sick, and free the captive.",
        "Modesty brings nothing except good.",
        "The best of people are those that bring the most benefit to others.",
        "The most beloved of deeds to Allah are the most consistent of them, even if small.",
        "Allah does not look at your appearance or wealth but looks at your hearts and deeds.",
        "Whoever believes in Allah and the Last Day, let him speak good or remain silent.",
        "Smiling in the face of your brother is charity.",
        "The best wealth is the wealth of the soul.",
        "Do not waste water even if you perform ablution on the bank of a flowing river.",
        "The upper hand is better than the lower hand (giving is better than receiving).",
        "None of you should wish for death due to a calamity that has befallen him.",
        "Cleanliness is half of faith.",
        "Backbiting is worse than adultery.",
        "Love for people what you love for yourself.",
        "The world is a prison for the believer and a paradise for the disbeliever.",
        "He who guides others to a good deed will get a reward similar to the one who performs it.",
        "He who believes in Allah and the Last Day must not harm his neighbor.",
        "Avoid suspicion, for suspicion is the worst of false tales.",
        "Paradise lies at the feet of your mother.",
        "When a man dies, his deeds come to an end except for three: Sadaqah Jariyah, knowledge that is beneficial, or a righteous child who prays for him.",
        "The best form of worship is to wait patiently for relief.",
        "Be in this world as if you were a stranger or a traveler.",
        "The best of your leaders are those whom you love and who love you.",
        "The most perfect of the believers in faith is the one who is best in manners.",
        "He who is not merciful to others will not be treated mercifully.",
        "Seek knowledge from the cradle to the grave.",
        "The best of you are those who learn the Qur’an and teach it.",
        "Beware! Every one of you is a shepherd and every one of you is answerable with regard to his flock.",
        "Visit the sick, feed the hungry, and free the captives.",
        "The one who looks after and works for a widow and for a poor person is like a warrior fighting for Allah’s cause.",
        "The one who severs ties of kinship will not enter Paradise.",
        "The deeds most loved by Allah are those done regularly, even if they are small.",
        "If anyone travels on a road in search of knowledge, Allah will cause him to travel on one of the roads to Paradise.",
        "Give the worker his wages before his sweat dries.",
        "No one eats better food than that which he eats out of the work of his hand.",
        "A believer is not bitten from the same hole twice.",
        "Do not be people without minds of your own.",
        "Faith consists of more than sixty branches.",
        "Every act of kindness is charity.",
        "Speak the truth even if it is bitter.",
        "Part of someone being a good Muslim is leaving alone that which does not concern him."
    ]

    for text in hadiths:
        db.session.add(Hadith(text=text))
    db.session.commit()

    return f"{len(hadiths)} Hadiths added to the database!"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
