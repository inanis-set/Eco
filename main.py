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


def make_page(pname):
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
                return redirect(url_for(f'{pname}', is_exists=False))
            else:
                db.session.add(Article(visitor=visitor_addr))
                db.session.commit()
                likes = db.session.query(Article).count()
                return redirect(url_for(f'{pname}', is_exists=True))
        elif 'feedback' in request.form:
            feedback = request.form['message']
            bot.send_message(CHAT_ID, feedback)
            return redirect(url_for(f'{pname}'))
        else:
            pass # unknown
    return render_template(f'{pname}.html', likes=likes, is_exists=is_exists)


@site.route('/', methods=['POST', 'GET'])
def index():
    return make_page('index')


@site.route('/about', methods=['POST', 'GET'])
def about():
    return make_page('about')


@site.route('/photosystem', methods=['POST', 'GET'])
def photosystem():
    return make_page('photosystem')


@site.route('/history', methods=['POST', 'GET'])
def history():
    return make_page('history')


@site.route('/bioreactor', methods=['POST', 'GET'])
def bioreactor():
    return make_page('bioreactor')


@site.route('/hengine', methods=['POST', 'GET'])
def hengine():
    return make_page('hengine')


@site.route('/ecology', methods=['POST', 'GET'])
def ecology():
    return make_page('ecology')


@site.route('/economy', methods=['POST', 'GET'])
def economy():
    return make_page('economy')


@site.route('/faq', methods=['POST', 'GET'])
def faq():
    return make_page('faq')


@site.route('/timer', methods=['POST', 'GET'])
def timer():
    return make_page('timer')

if __name__ == '__main__':
    site.run(debug=False)
