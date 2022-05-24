from flask import Flask, render_template, url_for, request, redirect
import telebot
from flask_sqlalchemy import SQLAlchemy

bot = telebot.TeleBot('TOKEN')
site = Flask(__name__)
site.secret_key = 'VERY_SECRET_KEY'
site.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///likes.db'
db = SQLAlchemy(site)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    visitor = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<Article %r>' % self.id


@site.route('/')
def index():
    return render_template('index.html')


@site.route('/about')
def about():
    return render_template('about.html')


@site.route('/photosystem')
def photosystem():
    return render_template('photosystem.html')


@site.route('/history')
def history():
    return render_template('history.html')


@site.route('/bioreactor')
def bioreactor():
    return render_template('bioreactor.html')


@site.route('/hengine')
def hengine():
    return render_template('hengine.html')


@site.route('/ecology')
def ecology():
    return render_template('ecology.html')


@site.route('/economy')
def economy():
    return render_template('economy.html')


@site.route('/faq')
def faq():
    return render_template('faq.html')


@site.route('/timer', methods=['POST', 'GET'])
def timer():
    likes = db.session.query(Article).count()
    visitor_addr = request.environ['HTTP_X_FORWARDED_FOR']
    #visitor_addr = request.environ['REMOTE_ADDR']
    existence = Article.query.filter_by(visitor=visitor_addr).first()
    is_exists = bool(existence)
    if request.method == 'POST':
        if 'like_button' in request.form:
            if is_exists:
                db.session.delete(Article.query.get(existence.id))
                db.session.commit()
                likes = db.session.query(Article).count()
                return redirect(url_for('timer', is_exists=False))
            else:
                db.session.add(Article(visitor=visitor_addr))
                db.session.commit()
                likes = db.session.query(Article).count()
                return redirect(url_for('timer', is_exists=True))
        elif 'feedback' in request.form:
            feedback = request.form['message']
            bot.send_message(CHAT_ID, feedback)
            return redirect(url_for('timer'))
        else:
            pass # unknown
    return render_template('timer.html', likes=likes, is_exists=is_exists)

if __name__ == '__main__':
    site.run(debug=False)
