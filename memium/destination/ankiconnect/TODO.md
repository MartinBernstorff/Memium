Tests:
* Full deploy requries CI: Enable local testing of docker container
* Iterating on card is hard: Generate a viewable html file from the current QA prompt 
* Deck generation can fail without test failure: Integration tests deck generation

Fix:
* Wiki-link followed by plural, [[Test]]s, does not italicise anything

Docs:
* All prompt contents should be valid markdown or html

## Maybe
Refactor: 
* Replace genanki with AnkiConnect: https://github.com/MartinBernstorff/Memium/issues/457

Feat:
* Use an LLM to rephrase questions and answers (perhaps for the next X days)
* Allow configurable CSS
* Use embedding model for syncing/deduplication