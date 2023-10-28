# Personal Mnemonic Medium

[![Open in Dev Container](https://img.shields.io/static/v1?label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)][dev container]
[![PyPI](https://img.shields.io/pypi/v/personal-mnemonic-medium.svg)][pypi status]
[![Python Version](https://img.shields.io/pypi/pyversions/personal-mnemonic-medium)][pypi status]
[![Tests](https://github.com/MartinBernstorff/personal-mnemonic-medium/actions/workflows/tests.yml/badge.svg)][tests]

[dev container]: https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/MartinBernstorff/personal-mnemonic-medium/
[pypi status]: https://pypi.org/project/personal-mnemonic-medium/
[documentation]: https://MartinBernstorff.github.io/personal-mnemonic-medium/
[tests]: https://github.com/MartinBernstorff/personal-mnemonic-medium/actions?workflow=Tests


<!-- start short-description -->

Extracting spaced repetition prompts (flashcards) from written notes.

When you have to stop and look things up, it breaks up your flow. Adding this knowledge to long-term memory builds fluency, and being fluent at something makes it much more fun! The faster you can get from crawling to running, the more enjoyable it is. This means you can bootstrap into a new field rapidly.  

[Anki](https://apps.ankiweb.net) enables rapid bootstrapping. It's automated [spaced repetition](https://notes.andymatuschak.org/Spaced_repetition_memory_systems_make_memory_a_choice), allowing you to retain information for much longer with much fewer repetitions. But Anki's user interface isn't great, and not at all conducive to maintaining a cohesive set of knowledge.

A [Zettelkasten](https://medium.com/@martinbernstorf/why-you-need-an-idea-management-system-defb5de44746) solves this problem! The present package extracts Anki prompts from (markdown) documents.

This thinking is largely inspired by Andy Matuschak's [Personal Mnemonic Medium](https://notes.andymatuschak.org/The_mnemonic_medium_can_be_extended_to_one%E2%80%99s_personal_notes), and the code is based on the unmaintained [Ankdown](https://github.com/benwr/ankdown).

<!-- end short-description -->

## Use as an application
If you want to sync markdown notes to Anki, here's how to get started!

1. In Anki, install the [AnkiConnect](https://ankiweb.net/shared/info/2055492159) add-on
2. Install [Orbstack](https://orbstack.dev/) or Docker Desktop
Then run:
```bash
docker run -itd \
  -v YOUR_INPUT_FOLDER_HERE:/input \
  -v $HOME/ankidecks:/output \
  --restart unless-stopped \
  ghcr.io/martinbernstorff/personal-mnemonic-medium:latest \
  python application/main.py /input/ $HOME/ankidecks --watch
```

This will start a docker container which watches YOUR_INPUT_FOLDER_HERE every 60 seconds. In case of updated files, it will sync the difference (create new prompts and delete deleted prompts) to Anki.

## Use as library
If you would like to build build your own Python application on top of the abstractions added here, you can install the library from pypi:
```bash
pip install personal-mnemonic-medium
```


### Pipeline abstractions
The library is built as a pipeline illustrated below. The left path describes the abstract pipeline, defined by abstract interfaces. The right path describes implementation I use, and which is part of this repo. 

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
### Setting up a dev environment
1. Install [Orbstack](https://orbstack.dev/) or Docker Desktop. Make sure to complete the full install process before continuing.
2. If not installed, install VSCode
3. Press this [link](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/MartinBernstorff/personal-mnemonic-medium/)
4. Complete the setup process

### Submitting a PR
Feel free to submit pull requests! If you want to run the entire pipeline locally, run:

```bash
make validate
```

And, if you have the github CLI installed, we can even create the PR in your browser for you:
```bash
make pr
```

# 💬 Where to ask questions

| Type                           |                        |
| ------------------------------ | ---------------------- |
| 🚨 **Bug Reports**              | [GitHub Issue Tracker] |
| 🎁 **Feature Requests & Ideas** | [GitHub Issue Tracker] |
| 👩‍💻 **Usage Questions**          | [GitHub Discussions]   |
| 🗯 **General Discussion**       | [GitHub Discussions]   |

[github issue tracker]: https://github.com/MartinBernstorff/personal-mnemonic-medium/issues
[github discussions]: https://github.com/MartinBernstorff/personal-mnemonic-medium/discussions

