# Personal Mnemonic Medium

[![PyPI](https://img.shields.io/pypi/v/personal-mnemonic-medium.svg)][pypi status]
[![Python Version](https://img.shields.io/pypi/pyversions/personal-mnemonic-medium)][pypi status]
[![documentation](https://github.com/MartinBernstorff/personal-mnemonic-medium/actions/workflows/documentation.yml/badge.svg)][documentation]
[![Tests](https://github.com/MartinBernstorff/personal-mnemonic-medium/actions/workflows/tests.yml/badge.svg)][tests]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]

[pypi status]: https://pypi.org/project/personal-mnemonic-medium/
[documentation]: https://MartinBernstorff.github.io/personal-mnemonic-medium/
[tests]: https://github.com/MartinBernstorff/personal-mnemonic-medium/actions?workflow=Tests
[black]: https://github.com/psf/black


<!-- start short-description -->

Extracting spaced repetition prompts (flashcards) from documents.

Adding knowledge to long-term memory builds fluency, since you don't have to pause and look things up. And being fluent at something makes it much more fun! The faster you can get from crawling to running, the more enjoyable it is. This means you can bootstrap into a new field rapidly.  

[Anki](https://apps.ankiweb.net) enables that is awesome. It's automated spaced repetition, allowing you to retain information for much longer than you would have before. But it's user interface isn't great, and not at all conducive to maintaining a cohesive set of knowledge.

A [Zettelkasten](https://medium.com/@martinbernstorf/why-you-need-an-idea-management-system-defb5de44746) solves this problem! The present package extracts Anki prompts from (markdown) documents.

This thinking is largely inspired by Andy Matuschak's [Personal Mnemonic Medium](https://notes.andymatuschak.org/The_mnemonic_medium_can_be_extended_to_one%E2%80%99s_personal_notes), and the code is based on the unmaintained [Ankdown](https://github.com/benwr/ankdown).

<!-- end short-description -->

## Installation


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

### Setting up a dev environment
1. Install [Orbstack](https://orbstack.dev/) or Docker Desktop. Make sure to complete the full install process before continuing.
2. If not installed, install VSCode
3. Press this [link](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/Aarhus-Psychiatry-Research/psycop-common)
4. Complete the setup process

## Usage

TODO: Add minimal usage example

To see more examples, see the [documentation].

# 📖 Documentation

| Documentation         |                                                          |
| --------------------- | -------------------------------------------------------- |
| 🔧 **[Installation]**  | Installation instructions on how to install this package |
| 📖 **[Documentation]** | A minimal and developing documentation                   |
| 👩‍💻 **[Tutorials]**     | Tutorials for using this package                         |
| 🎛️ **[API Reference]** | API reference for this package                           |
| 📚 **[FAQ]**           | Frequently asked questions                               |


# 💬 Where to ask questions

| Type                           |                        |
| ------------------------------ | ---------------------- |
| 📚 **FAQ**                      | [FAQ]                  |
| 🚨 **Bug Reports**              | [GitHub Issue Tracker] |
| 🎁 **Feature Requests & Ideas** | [GitHub Issue Tracker] |
| 👩‍💻 **Usage Questions**          | [GitHub Discussions]   |
| 🗯 **General Discussion**       | [GitHub Discussions]   |

[Documentation]: https://MartinBernstorff.github.io/personal-mnemonic-medium/index.html
[Installation]: https://MartinBernstorff.github.io/personal-mnemonic-medium/installation.html
[Tutorials]: https://MartinBernstorff.github.io/personal-mnemonic-medium/tutorials.html
[API Reference]: https://MartinBernstorff.github.io/personal-mnemonic-medium/references.html
[FAQ]: https://MartinBernstorff.github.io/personal-mnemonic-medium/faq.html
[github issue tracker]: https://github.com/MartinBernstorff/personal-mnemonic-medium/issues
[github discussions]: https://github.com/MartinBernstorff/personal-mnemonic-medium/discussions

