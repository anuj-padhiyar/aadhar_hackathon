import pandas as pd
import json
from  pandas import Series, DataFrame
import re
from flask import Flask, render_template, jsonify
app = Flask(__name__)

@app.route("/")
def home():
    result = pd.read_csv("Address_data.csv")
    header = result.columns.values;
    print(header)
    data = [ i for i in result.values]

    final = []
    for row in data:
        words = []
        tempWords = []
        for a in row: 
            words.append(re.sub("[^\w]", " ", str(a)).split())
            tempWords = tempWords + re.sub("[^\w]", " ", str(a)).split()
        
        tempWords = list(dict.fromkeys(tempWords))
        tempWords.reverse()
        words.reverse()
        for a in words:
            if(header[words.index(a)] != "locality" and header[words.index(a)] != "district" and header[words.index(a)] != "state"):
                for b in a:
                    if b!="nan":
                        if b in tempWords: 
                            tempWords.remove(b)
                        else:
                            del a[:]
        words.reverse()
        temp = []
        for a in words:
            string = " "
            temp.append(string.join(a))
        line = { header[k] : temp[k] for k in range(0,len(row)) }
        final.append(line)
    return jsonify(final)

if __name__ == "__main__":
    app.run(debug = True)
