from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://newbie8800:7JgKipt6hEZS@ep-rough-mouse-182744.us-east-2.aws.neon.tech/neondb"

db = SQLAlchemy(app)
# db.init_app(app)


class Bookests1234(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)

# db.create_all()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        title = request.form.get("book")
        book = Bookests1234(title=title)

        db.create_all()

        db.session.add(book)
        db.session.commit()
    books = Bookests1234.query.all()
    return render_template("index.html", books=books)

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)