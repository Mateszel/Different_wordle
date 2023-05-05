from flask import Flask, render_template, request, url_for, flash, redirect
import os
import random

dictionary = []
with open('words_eng.txt', 'r') as file:
    for line in file.readlines():
        for word in line.split():
            dictionary.append(word)

dictionary.sort()
x = random.randrange(0, len(dictionary), 1)
chosen_word = dictionary[x]
chosen_letters = list(chosen_word)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'm1357924680'
words = []
print(chosen_word)
info_exist = []
info_order = []
info_rejected = []
info_words_tried = ['****']

@app.route("/")
def index():
    return render_template('index.html', messages=words, info_order=info_order, info_exist=info_exist, info_words_tried=info_words_tried)

@app.route('/winner/', methods=('GET', 'POST'))
def winner():
    return render_template('winner.html', messages=words)

@app.route('/loser/', methods=('GET', 'POST'))
def loser():
    return render_template('loser.html', messages=words)


@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        letter_1 = request.form['letter_1']
        letter_2 = request.form['letter_2']
        letter_3 = request.form['letter_3']
        letter_4 = request.form['letter_4']
        letter_5 = request.form['letter_5']
        letter_1 = letter_1.upper()
        word_buf = letter_1+letter_2+letter_3+letter_4+letter_5
        letters_buf = list(word_buf)
        correct_order = []
        correct_exist = []
        order = ''
        exist = ''
        is_word = 0
        for i in range(len(dictionary)):
            if word_buf == dictionary[i]:
                is_word = 1
        if is_word == 1:
            for i in range(len(info_words_tried)):
                if info_words_tried[i] == '****':
                    info_words_tried[i] = chosen_word
            info_words_tried.append(word_buf)
            info_words_tried.sort()
            for i in range(len(info_words_tried)):
                if info_words_tried[i] == chosen_word:
                    info_words_tried[i] = '****'
            words.append(word_buf)
            for i in range(5):
                if letters_buf[i] == chosen_letters[i]:
                    order = order + chosen_letters[i] + ' '
                else:
                    break
            info_exist.append(exist)
            info_order.append(order)
            if word_buf == chosen_word:
                return redirect(url_for('winner'))
            elif len(info_words_tried) > 14:
                return redirect(url_for('loser'))
            else:
                return redirect(url_for('index'))
        else:
            flash('Content is required!')







    return render_template('create.html')

app.run(debug=True)