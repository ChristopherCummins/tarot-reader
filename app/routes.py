from flask import render_template
from app import app

from app import cardDeck
import random


@app.route('/')
@app.route('/index')
def index():
    pulls = [
        {
            'spread' : {'cardAmount' : 'Single Card'},
            'body': 'Click here for a a single card pull for a solution to a problem'
        },
        {
            'spread' : {'cardAmount' : 'Three Card'},
            'body': 'Click here for insight into the past, present, and future of an issue'
        }
    ]
    return render_template('index.html', title = 'Home', pulls = pulls)

@app.route('/single')
def single():
    thisDeck = cardDeck.getTarotDeck()
    thisCard = cardDeck.pullCard(thisDeck)
    return render_template('single.html', title = 'Single Card Pull',
                           name = thisCard[0]['name'],
                           position = thisCard[1],
                           uprightDescription = thisCard[0]['upright'],
                           reversedDescription = thisCard[0]['reversed'],
                           image = thisCard[0]['image'],
                           )
                           
@app.route('/three')
def three():
    thisDeck = cardDeck.getTarotDeck()
    spread = []
    for i in range(0,3):
        thisCard = cardDeck.pullCard(thisDeck)
        spread.append(thisCard)
    return render_template('three.html', spread = spread, title = 'Three Card Spread')
