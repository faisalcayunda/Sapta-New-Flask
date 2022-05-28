from datetime import datetime
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path="")
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:root@localhost/sapta_devel'
app.config['SECRET_KEY'] = "random string"
db = SQLAlchemy(app)


class Clients(db.Model):
    __tablename__ = "clients"
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(50))
    desc = db.Column('desc', db.Text)
    pict = db.Column('pict', db.String(100))

    def __repr__(self) -> str:
        return "<Name %r>" % self.name


@app.route("/")
def index(page="Beranda"):
    return render_template("index.html", page=page)


@app.route("/about")
def about(page="Tentang Kami"):

    klien = Clients.query.order_by(Clients.id).all()
    print(klien)
    return render_template("about.html", page=page, client=klien)


@app.route("/program")
def program(page="Program Kami"):
    return render_template("program.html", page=page)


@app.route("/lowongan")
def career(page="Lowongan"):
    return render_template("career.html", page=page)


@app.route("/kegiatan")
def event(page="Kegiatan"):
    tanggal = datetime.now()
    return render_template("event.html", page=page, date_now=tanggal.strftime("%A, %B %Y"))


@app.route("/berita")
def news(page="Berita"):
    return render_template("news.html", page=page)


if __name__ == '__main__':
    app.run(debug=False)
