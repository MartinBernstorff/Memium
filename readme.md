# Personal Mnemonic Medium
![Tests](https://github.com/MartinBernstorff/personal-mnemonic-medium/actions/workflows/tests.yml/badge.svg)

Extracting spaced repetition prompts (flashcards) from documents.

Adding knowledge to long-term memory builds fluency, since you don't have to pause and look things up. And being fluent at something makes it much more fun! The faster you can get from crawling to running, the more enjoyable it is. This means you can bootstrap into a new field rapidly.  

[Anki](https://apps.ankiweb.net) enables that is awesome. It's automated spaced repetition, allowing you to retain information for much longer than you would have before. But it's user interface isn't great, and not at all conducive to maintaining a cohesive set of knowledge.

A [Zettelkasten](https://medium.com/@martinbernstorf/why-you-need-an-idea-management-system-defb5de44746) solves this problem! The present package extracts Anki prompts from (markdown) documents.

This thinking is largely inspired by Andy Matuschak's [Personal Mnemonic Medium](https://notes.andymatuschak.org/The_mnemonic_medium_can_be_extended_to_one%E2%80%99s_personal_notes), and the code is based on the unmaintained [Ankdown](https://github.com/benwr/ankdown).

FYI-style open source, maintenance is not guaranteed.

## Pipeline
The left path describes the abstract pipeline, the right path the current instantiation in this repo. 

```mermaid

graph TD 
	FD["File on disk"]
	FD -- Document factory --> Document
	Document -- Extractor --> Prompt
	Prompt -- Exporter --> Card 
 
	MD["Markdown file"]
	 Prompts["[QAPrompt | ClozePrompt]"]
  Cards["[AnkiQA | AnkiCloze]"]
 
	MD -- MarkdownNoteFactory --> Document
	Document -- "[QAExtractor, \nClozeExtractor]" --> Prompts
	Prompts -- AnkiPackageGenerator --> Cards
 ```

## Contributing
To get a full 

## Running through docker
To build and run the container, see `docker_cmd.sh`.

<!-- {BearID:ffeb2eba865d16361b47d522f39c3563} -->
