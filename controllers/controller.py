from app import app
from flask import render_template, request 
from modules.player import Player
from modules.game import Game
import random

@app.route("/game")
def main_page():
    return render_template("main.html")

@app.route("/game", methods=['POST'])
def play_game():
    player1 = Player(request.form['player1_name'], request.form['player1_choice'])
    player2 = Player(request.form['player2_name'], request.form['player2_choice'])
    game = Game(player1, player2 )
    return render_template('result.html', winner=game.compare(), player1=player1.name,player2=player2.name, player1_choice=player1.choice, player2_choice=player2.choice )

@app.route("/welcome")
def rules_page():
    return render_template("welcome.html")

@app.route("/play")
def vs_com_page():
    return render_template("play.html")

@app.route('/play', methods=["POST"])
def play_game_vs_com():
    player = Player(request.form["player1_name"], request.form['player1_choice'])
    com_choice = random.choice(['rock', 'paper', 'scissors'])
    game = Game(player, Player("Com", com_choice))
    return render_template('result.html', winner=game.compare(), player1=player.name,player2='Com', player1_choice=player.choice, player2_choice=com_choice )