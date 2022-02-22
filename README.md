# Utils 
Various miscellaneous python scripts that might be useful to a variety of projects.

# Contents
dataclean
Process text to remove punctuation, lower, etc. Removes NLTK's stopwords (stopwords.obj) and, optionally, additional, user-supplied stopwords.

pickle_it
Shortcut wrapper to save a Python object into a pickle file.

scoreModel
Some utilities to score Gensim Doc2Vec models.

whoopsie
Print (error) messages and append them to a text file. Synchronous & asynchronous versions of whoopsie.

# Getting Started
TODO: Guide users through getting your code up and running on their own system. In this section you can talk about:
1.	Installation process: https://git-scm.com/book/en/v2/Git-Tools-Submodules#_git_submodules
        1. TLDR: git submodule add [URL to the submodule's git repository]
        2. To use: from utils.pickle_it import pickle_it
2.	Software dependencies
        Python 3.8
3.	Latest releases
4.	API references

NB: If you've cloned a repository that used this repository as a submodule then you may already have a utils folder, but it may be empty. git rm utils, then git submodule add this repository.