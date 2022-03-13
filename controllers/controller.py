from app import app
from flask import render_template, request 
from modules.player import Player
from modules.game import Game

@app.route("/game")
def main_page():
    return render_template("main.html")

@app.route("/game", methods=['POST'])
def store_player_choice():
    player1 = Player(request.form['player1_name'], request.form['player1_choice'])
    player2 = Player(request.form['player2_name'], request.form['player2_choice'])
    game = Game(player1, player2 )
    winner = game.compare()
    return render_template('result.html', winner=winner, player1=player1.name,player2=player2.name, player1_choice=player1.choice, player2_choice=player2.choice )
