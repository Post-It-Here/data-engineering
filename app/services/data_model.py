from pathlib import Path

import pandas as pd
from compress_pickle import load

path = Path("app/services/reddit_model.plk.gz")

model = load(path)


def post_predictions(post, answers=1):
    """ takes a post and returns the top categories it fits in """

    post = [post]
    # get the predicted probabilities for each class
    preds = pd.Series(model.predict_proba(post)[0])

    # save each class to the Series index
    preds.index = model.classes_

    # sort to get the most likely classes
    preds = preds.sort_values(ascending=False)

    # return the top num_answers results in dict format
    return preds[:answers]
