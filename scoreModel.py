#!/usr/bin/env python
# coding: utf-8

# scoreModel.py
# Score Model
# Takes a trained Gensim Doc2Vec model, its training corpus, a sample proportion, and number of workers to use. Prints the percentage of time the most similar document to a document was that same document.
# Requires: Gensim, sklearn.model_selection, & concurrent.futures

# To Do:
# I guess modules don't print. Fine. Instead print to string and return that.

import concurrent.futures, gensim, time
from sklearn import model_selection




# process the score for a chunk of training corpus, docSims, & firstSims, where that chunk is a portion of the training corpus, a list of Gensim tagged documents
# doc.tags is the list of the tags, in this case the only tag is the document's metadata index value
# docSims is the list of most similar documents, made by calling model.docvecs.most_similar on on a document's inferred vector
def process_score(chunk, model):
    docSims = [None] * len(chunk)
    firstSims = [None] * len(chunk)
    for c in range(len(chunk)):
        doc = chunk[c]
        # Note: model.docvecs.most_similar for Gensim 3, possibly model.dv.most_similar for Gensim 4
        docSims[c] = model.docvecs.most_similar([model.infer_vector(doc.words)], topn=1)

        # This line asks whether the index of the tagged doc we're currently iterating on is the same as the index of that doc's most similar, and then assigns the answer to firstSims[c]
        firstSims[c] = doc.tags[0] == docSims[c][0][0]
        if c % 100 == 0:
            print(f"Progress: {c} in {len(chunk)}, {round(c / len(chunk)*100)}% of thie worklist done.")
    # Return a tuple of the sum of correct sims and the total number of cases
    return (sum(firstSims), len(chunk))

# Setup the scoring sample, scoreList
def scoreModel(model, training_corpus, sampleProportion=0.1, numWorkers=7):

    remainder, scoreList = model_selection.train_test_split(training_corpus, random_state=42, test_size=sampleProportion)

    total = len(scoreList)
    workPackageSize = total // numWorkers
    workLists = []
    for n in range(numWorkers):
        workLists.append(scoreList[workPackageSize * n : workPackageSize * (n + 1)])
    workLists[-1] = workLists[-1] + scoreList[workPackageSize * numWorkers:]

    t0 = time.time()
    results = []
    # We can use a with statement to ensure threads are cleaned up promptly
    with concurrent.futures.ThreadPoolExecutor(max_workers=7) as executor:
        # Start the process operations and mark each future with its worklist
        future_to_wl = {executor.submit(process_score, wl, model): wl for wl in workLists}
        for future in concurrent.futures.as_completed(future_to_wl):
            try:
                future
            except Exception as exc:
                print('exception: %s' % (exc))
            else:
                results.append(future.result())
    t1 = time.time()
    res = list(zip(*results))
    print(f"Accuracy: {round((sum(res[0]) / sum(res[1]))*100)}% in {round(t1-t0)} s for a random sample of {sum(res[1])} cases out of {len(training_corpus)} total.")
    # return "Accuracy: " + round((sum(res[0]) / sum(res[1]))*100) + "% in " + round(t1-t0) + " s for a random sample of " + sum(res[1]) + " cases out of " + len(training_corpus) + " total."
