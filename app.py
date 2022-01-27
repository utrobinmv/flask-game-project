from flask import Flask, request, render_template, url_for, redirect
from forms import StartForm, GameForm
from config import FlaskConfig
from game import PotterCastle

app = Flask(__name__)
app.config.from_object(FlaskConfig)

@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    form = StartForm()
    if request.method == 'GET':
        form.size.data = '7x7'
    if form.validate_on_submit():
        size = request.form.get("size")
        url = url_for("game", size=size)
        print('url',url)
        return redirect(url)
    return render_template("index.html", form=form)

@app.route("/game/<string:size>", methods=["GET", "POST"])
def game(size):
    form = GameForm()
    
    if request.method == 'GET':
        form.number_steps.data = 1
        
    if form.validate_on_submit():
        gamestore = PotterCastle()
        way = request.form.get("way")
        number_steps = request.form.get("number_steps")
        for _ in range(int(number_steps)):
            gamestore.move_position(way)
       
    else:
        gamestore = PotterCastle(size)

    return render_template(
        "start.html",
        position=gamestore.position,
        rooms=gamestore.rooms,
        current_room=gamestore.get_name(),
        form=form,
        message=gamestore.message,
    )

if __name__ == "__main__":
    
    app.run(host='0.0.0.0',port=5000, debug=False)

