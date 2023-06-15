# Persian Search Engine

This is a search engine project for the Persian language, implemented in Python using the Hazm library. Currently, it only supports boolean queries and raw-text queris for ranked retrieval.

## Prerequisites

- Python 3.6 or higher
- Hazm library (can be installed via pip: `pip install hazm`)

## Usage

1. Clone this repository: `git clone https://github.com/yourusername/persian-search-engine.git`
2. Move into the project directory: `cd persian-search-engine/p1`
3. Run the search engine: `python main.py`

The search engine will prompt you to enter your query. Queries should be formatted as boolean expressions, using the following operators:

- AND (e.g., "word1 word2")
- NOT (e.g., "! word1")
- Phrase (e.g., word1 ' '/ ! "phrse")
- Ranked Retrieval (e.g., word1 word2 ... wordn, 'cos' or 'J', 'n' or 'chmp')


The search engine will then return the documents that match the query.

## Phase 1
Using Positional Index For Bool Retrieval
## Phase 2
Using Vector Space Model and TFIDF for Rank Retrieval
