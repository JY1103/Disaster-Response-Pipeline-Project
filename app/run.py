import json
import plotly
import pandas as pd
import numpy as np

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

from flask import Flask
from flask import render_template, request, jsonify
from plotly.graph_objs import Bar
from plotly.graph_objs import Pie
from sklearn.externals import joblib
from sqlalchemy import create_engine


app = Flask(__name__)

def tokenize(text):
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens

# load data
engine = create_engine('sqlite:///../data/DisasterResponse.db')
df = pd.read_sql_table('DisasterResponse', engine)

# load model
model = joblib.load("../models/classifier.pkl")


# index webpage displays cool visuals and receives user input text for model
@app.route('/')
@app.route('/index')
def index():
    
    # extract data needed for visuals
    # TODO: Below is an example - modify to extract data for your own visuals
    genre_counts = df.groupby('genre').count()['message']
    genre_names = list(genre_counts.index)
<<<<<<< HEAD
    
    total_message_count = len(df)
    top15_message_names = list(df.loc[:,'related':].sum().sort_values(ascending=False)[0:15].index)
    top15_message_counts = df.loc[:,'related':].sum().sort_values(ascending=False)[0:15].values/total_message_count*100
    
    least15_message_names = list(df.loc[:,'related':].sum().sort_values()[0:15].index)
    least15_message_counts = df.loc[:,'related':].sum().sort_values()[0:15].values/total_message_count*100
=======
    top15_message_names = list(df.loc[:,'related':].sum().sort_values(ascending=False)[0:15].index)
    message_names = top15_message_names + ['Others']
    top15_message_counts = df.loc[:,'related':].sum().sort_values(ascending=False)[0:15].values
    other_counts=np.sum(df.loc[:,'related':].sum().sort_values(ascending=False).values) - np.sum(top15_message_counts)
    message_counts = list(top15_message_counts) + [other_counts]
>>>>>>> 28759aa8dff3266882b28f3ac8adbf8b87fcfeb9
    
    # create visuals
    # TODO: Below is an example - modify to create your own visuals
    graphs = [
        {
<<<<<<< HEAD
        'data': [
            Pie(
                values= genre_counts,
                labels= genre_names
            )
        ],

        'layout': {
            'title': 'Distribution of Message Genre'
        }
    },
        {
            'data': [
                Bar(
                    x=top15_message_names,
                    y=top15_message_counts
=======
            'data': [
                Bar(
                    x=genre_names,
                    y=genre_counts
>>>>>>> 28759aa8dff3266882b28f3ac8adbf8b87fcfeb9
                )
            ],

            'layout': {
<<<<<<< HEAD
                'title': 'Distribution of Most Represented Message Categories',
                'yaxis': {
                    'title': "Percentage (%)"
                },
                'xaxis': {
                    'title': "Message Categories"
                }
            }
        },
         {
            'data': [
                Bar(
                    x=least15_message_names,
                    y=least15_message_counts
                )
            ],

            'layout': {
                'title': 'Distribution of Least Represented Message Categories',
                'yaxis': {
                    'title': "Percentage (%)"
                },
                'xaxis': {
                    'title': "Message Categories"
                }
            }
        }
=======
                'title': 'Distribution of Message Genres',
                'yaxis': {
                    'title': "Count"
                },
                'xaxis': {
                    'title': "Genre"
                }
            }
        },
        {
        'data': [
            Pie(
                values= message_counts,
                labels= message_names
            )
        ],

        'layout': {
            'title': 'Distribution of Message Categories'
        }
    }
>>>>>>> 28759aa8dff3266882b28f3ac8adbf8b87fcfeb9
    ]
    
    # encode plotly graphs in JSON
    ids = ["graph-{}".format(i) for i, _ in enumerate(graphs)]
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    
    # render web page with plotly graphs
    return render_template('master.html', ids=ids, graphJSON=graphJSON)


# web page that handles user query and displays model results
@app.route('/go')
def go():
    # save user input in query
    query = request.args.get('query', '') 

    # use model to predict classification for query
    classification_labels = model.predict([query])[0]
    classification_results = dict(zip(df.columns[4:], classification_labels))

    # This will render the go.html Please see that file. 
    return render_template(
        'go.html',
        query=query,
        classification_result=classification_results
    )


def main():
    app.run(host='0.0.0.0', port=3001, debug=True)


if __name__ == '__main__':
    main()