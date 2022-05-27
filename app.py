from flask import Flask, render_template

app = Flask(__name__, static_url_path="")


@app.route("/")
def index(page="Beranda"):
    return render_template("index.html", page=page)


@app.route("/about")
def about(page="Tentang Kami"):
    return render_template("about.html", page=page)


@app.route("/program")
def program(page="Program Kami"):
    return render_template("program.html", page=page)


@app.route("/lowongan")
def career(page="Lowongan"):
    return render_template("career.html", page=page)


@app.route("/kegiatan")
def event(page="Kegiatan"):
    return render_template("event.html", page=page)


@app.route("/berita")
def news(page="Berita"):
    return render_template("news.html", page=page)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
