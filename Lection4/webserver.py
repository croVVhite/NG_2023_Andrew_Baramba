from flask import Flask, render_template, request
import os

servak = Flask("Lection4")
imgNumberToShow = 0
imagesQuantity = 3
imagesList = os.listdir('../Lection4/static/images')

@servak.route("/")
def index():
    return render_template("index.html")


@servak.route("/calculator")
def calculator():
    return render_template("calculator.html")


@servak.route("/calculate")
def calculate():
    firstNumber = float(request.args.get("firstNum"))
    secondNumber = float(request.args.get("secondNum"))
    operation = request.args.get("operation")

    match operation:
        case "+": 
            return str(firstNumber + secondNumber) 
        case "-":
            return str(firstNumber - secondNumber)
        case "*":
            return str(firstNumber * secondNumber)
        case "/":
            return str(firstNumber / secondNumber)
        case "^":
            return str(firstNumber ** secondNumber)
        case "root":
            return str(firstNumber ** (1/secondNumber))


@servak.route("/game")
def game():
    return render_template("game.html")


@servak.route("/gallery")
def gallery():
    return render_template("gallery.html")


@servak.route("/show_image")
def show_image():
    global imgNumberToShow
    global imagesQuantity

    if request.args.get("show") == 'next':
        imgNumberToShow += 1
        if imgNumberToShow > imagesQuantity - 1:
            imgNumberToShow = 0
    elif request.args.get("show") == 'previous':
        imgNumberToShow -= 1
        if imgNumberToShow < 0:
            imgNumberToShow = imagesQuantity - 1
    return "<div style=\"text-align: center;\"><img src=\"static/images/" + str(imagesList[imgNumberToShow]) + "\" , height=\"980px\"</div>"


servak.run(host="0.0.0.0", port=8080)