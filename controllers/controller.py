from app import app
from flask import render_template, request 
from modules.player import Player

@app.route("/game")
def main_page():
    return render_template("main.html")

@app.route("/game", methods=['POST'])
def store_player_choice():
    player1 = Player(request.form['player1_name'], request.form['player1_choice'])
    player2 = Player(request.form['player2_name'], request.form['player2_choice'])
    return f"{request.form['player1_name']} chose {request.form['player1_choice']}"
