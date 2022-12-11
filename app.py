import re
import textwrap
import numpy as np
import pandas as pd
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import glob
import matplotlib.pyplot as plt
from PIL import Image
import pdfplumber
from flask import Flask, render_template, url_for, request, redirect
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image
from collections import defaultdict
import math

CUTOFF = 5
dramas = list()
imagesNames = list()

class my_dictionary(dict):

    # __init__ function
    def __init__(self):
        self = dict()

        # Function to add key:value

    def add(self, key, value):
        self[key] = value



def getDramas():
    file = open('IndexingOfDramas1.txt', 'r')
    global dramas
    dramas.clear()
    i = 0
    for line in file:
        data = line.strip('\n').split('*')

        if i==0:
            i += 1
            continue
        data.append((data[1] + ".jpeg").lower())
        dramas.append(data)


    return dramas



def getImages():
    global imagesNames
    imagesNames = glob.glob("static/images/*")
    dramaImages = list()
    for image in imagesNames:
        data = image.split("/")

        dramaImages.append(data[2].split('.')[0])



def call_counter(func):
    def helper(*args, **kwargs):
        helper.calls += 1
        return func(*args, **kwargs)

    helper.calls = 0
    helper.__name__ = func.__name__

    return helper


def memoize(func):
    mem = {}

    def memoizer(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in mem:
            mem[key] = func(*args, **kwargs)
        return mem[key]

    return memoizer


@call_counter
@memoize
def levenshtein(s, t):
    if s == "":
        return len(t)
    if t == "":
        return len(s)
    if s[-1] == t[-1]:
        cost = 0
    else:
        cost = 1

    res = min([levenshtein(s[:-1], t) + 1,
               levenshtein(s, t[:-1]) + 1,
               levenshtein(s[:-1], t[:-1]) + cost])

    return res


def getMinimum(query, dramasList, searchBy):
    global CUTOFF
    k = -1
    if searchBy == 'dramaName':
        k = 1
        CUTOFF = 5
    elif searchBy == 'writer':
        k = 5
        CUTOFF = 7
    elif searchBy=='director':
        k=4
    elif searchBy =='year':
        k=2
        CUTOFF = 2

    elif searchBy == 'genre':
        k=6
        CUTOFF = 5
    else:
        k=1
        CUTOFF = 4


    dramasDict = list()
    query = query.lower()
    editDistances  = []
    minEditDrama = list()
    minEditDist = levenshtein(query, dramasList[0][k])

    for drama in dramasList:
        editDist = levenshtein(query,drama[k].lower())
        dramasDict.append([editDist, drama])
        if minEditDist > editDist:
            minEditDist = editDist
            minEditDrama.clear()
            minEditDrama.append(drama)


    dramasDict.sort()
    minEditDramas = list()
    for item in dramasDict:
        if item[0] < CUTOFF:
            minEditDramas.append(item[1])
    if len(minEditDramas) > 0:
        return minEditDramas
    return -1

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':

        global imagesNames, dramas
        getImages()

        query = request.form['query']
        searchBy = request.form['searchBy']

        dramaInfo = getMinimum(query, getDramas(), searchBy)
        print(query)
        print(dramaInfo)

        return render_template('showDrama.html', query=query, dramaInfo=dramaInfo, searchBy = searchBy)

    else:

        return render_template('index.html')

    


if __name__== "__main__":
    app.run(debug=True)

