#!/usr/bin/env python3
"""Ankdown: Convert Markdown files into anki decks.

Usage:
    ankdown.py [-r DIR] [-p PACKAGENAME] [--updatedOnly] [--config CONFIG_STRING] [--configFile CONFIG_FILE_PATH]

Options:
    -h --help     Show this help message
    --version     Show version

    -r DIR        Recursively visit DIR, accumulating cards from `.md` files.

    -p PACKAGE    Instead of a .txt file, produce a .apkg file. recommended.

    --updatedOnly  Only generate cards from updated `.md` files

    --config CONFIG_STRING  ankdown configuration as YAML string

    --configFile CONFIG_FILE_PATH   path to ankdown configuration as YAML file
"""

import hashlib
import json
import os
import re
import tempfile
import textwrap
from datetime import datetime
from shutil import copyfile

import genanki
import misaka
import yaml
from docopt import docopt

VERSION = "0.1"

# Anki 2.1 has mathjax built in, but ankidroid and other clients don't.
CARD_MATHJAX_CONTENT = textwrap.dedent(
    """\

"""
)

CONFIG = {
    "pkg_arg": "AnkdownPkg.apkg",
    "recur_dir": ".",
    "dollar": False,
    "updated_only": False,
    "version_log": ".mdvlog",
    "card_model_name_cloze": "Ankdown Cloze",
    "card_model_name_qa": "Ankdown QA",
    "card_model_name_qa_da": "Ankdown QA DA",
    "card_model_css": """
        .card {
            margin: 2em auto;
            display: block;
            font-family: New York, Georgia,
            baskerville,
            sans;
            font-size: 1.3em;
            text-align: left;
            background-color: white;
            line-height: 150%;
            width: 25em;
            height: 30 em;
            background-color: black;
            word-wrap: break-word;
            color: #D7DEE9;
        }

        div.highlight {
            background-color: rgba(255, 255, 255, 0.1) !important;
            font-family: Arial;
        }

        div.back div.question {
            font-size: 0.7em;
            line-height: 100%;
            color: rgba(255, 255, 255, 0.4);
	        margin-bottom: 1.4em;
        }

        div.extra {
            color: rgba(255, 0, 0, 0.1) ;
            font-weight: 0;
            font-style: italic;
            font-size: 0.7em;
        }

        div.extra h4.left {
            text-align: left;
            float: left;
            width: 60%;
        }

        h4 {
            color: rgba(255, 255, 255, 0);
            font-weight: 0;
            font-style: italic;
            font-size: 0.3em;
            line-height: 120%;
        }

        div.extra h4.right {
            text-align: right;
            width: 30%;
            float: right;
        }

        div.extra h4.right a {
            text-align: right;
            float: right;
            color: rgba(255, 255, 255, 0.25) !important;
            background-color: rgba(255, 40, 35, 0.15) !important;
            border: none;
            padding: 5px 8px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            margin: 4px 2px;
            border-radius: 200px;
        }

        .cloze,
        .cloze b,
        .cloze u,
        .cloze i {
            font-weight: bold;
            color: MediumSeaGreen !important;
            min-width: 30 em;
        }

        #extra,
        #extra i {
            font-size: 15px;
            color: #D7DEE9;
            font-style: italic;
        }

        img {
            display: block;
            max-width: 45em;
            max-height: none;
            margin-left: auto;
            margin: 10px auto 10px auto;
        }

        img:active {
            width: 100%;
        }

        tr {
            font-size: 12px;
        }

        /* COLOR ACCENTS FOR BOLD-ITALICS-UNDERLINE */
        b {
            color: #C695C6 !important;
        }

        /* BOLD STYLE */
        u {
            text-decoration: none;
            color: #5EB3B3;
        }

        /* UNDERLINE STYLE */
        i {
            color: IndianRed;
        }

        /* ITALICS STYLE */
        a {
            color: LightGray !important;
            text-decoration: none;
            font-size: 10px;
            font-style: normal;
        }

        /* LINK STYLE */
        .myCodeClass {
            padding: 5px;
            background-color: lightgrey;
            font-size: 18px
        }

        /* ADJUSTMENT FOR MOBILE DEVICES */
        .mobile .card {
            margin: 1em auto;
            width: 90%;
            font-size: 1.3em;
            line-height: 150%;
        }

        .mobile .tags:hover {
            opacity: 1;
            position: relative;
        }

        .mobile img {
            display: block;
            max-width: 100%;
            max-height: none;
            margin-left: auto;
            margin: 10px auto 10px auto;
        }

        .mobile .card img:active {
            width: inherit;
            max-height: none;
        }
        
        """,
    "card_model_fields_cloze": [{"name": "Text"}, {"name": "Extra"}, {"name": "Tags"}],
    "card_model_fields_qa": [
        {"name": "Question"},
        {"name": "Answer"},
        {"name": "Extra"},
    ],
    "card_model_template_qa": [
        {
            "name": "Ankdown QA Card",
            "qfmt": '<div class="front">{{{{Question}}}}{{{{tts en_US voices=Apple_Samantha speed=1.1:Question}}}}\n{0}</div>\n<div class="extra">{{{{Extra}}}}</div>'.format(
                CARD_MATHJAX_CONTENT
            ),
            "afmt": '<div class="back"><div class="question">{{{{Question}}}}</div><div class="answer">{{{{Answer}}}}{{{{tts en_US voices=Apple_Samantha speed=1.1:Answer}}}}</div>\n\n<div class="extra">{{{{Extra}}}}</div>{0}</div>'.format(
                CARD_MATHJAX_CONTENT
            ),
        }
    ],
    "card_model_template_qa_da": [
        {
            "name": "Ankdown QA DK Card",
            "qfmt": '<div class="front">{{{{Question}}}}{{{{tts da_DK  speed=1.4:Question}}}}\n{0}</div>\n<div class="extra">{{{{Extra}}}}</div>'.format(
                CARD_MATHJAX_CONTENT
            ),
            "afmt": '<div class="back"><div class="question">{{{{Question}}}}</div><div class="answer">{{{{Answer}}}}{{{{tts da_DK speed=1.4:Answer}}}}</div>\n\n<div class="extra">{{{{Extra}}}}</div>{0}</div>'.format(
                CARD_MATHJAX_CONTENT
            ),
        }
    ],
    "card_model_template_cloze": [
        {
            "name": "Ankdown Cloze Card",
            "qfmt": "{{{{cloze:Text}}}}\n<div class='extra'>{{{{Extra}}}}</div>\n{0}".format(
                CARD_MATHJAX_CONTENT
            ),
            "afmt": "{{{{cloze:Text}}}}\n<div class='extra'>{{{{Extra}}}}</div>\n{0}".format(
                CARD_MATHJAX_CONTENT
            ),
        }
    ],
}

VERSION_LOG = {}
Q_TYPE_TAG = {
    "G": "med/type/1_GP",
    "A": "med/type/2_Acute_care",
    "I": "med/type/3_Internal_medicine",
    "S": "med/type/4_Specialty",
    "D": "med/type/5_Disabled",
    ".": "",
}


def simple_hash(text):
    """MD5 of text, mod 2^63. Probably not a great hash function."""
    return int(hashlib.sha256(text.encode("utf-8")).hexdigest(), 16) % 10 ** 10


class Card(object):
    """A single anki card."""

    def __init__(self, filepath):
        self.fields = []
        self.filepath = filepath
        self.tags = []

    def append_tags(self, tags):
        self.tags.extend(tags)

    def deckdir(self):
        return os.path.dirname(self.filepath)

    def set_deck(self, subdeck):
        self.subdeck = subdeck

    def set_model(self, model_type="Cloze"):
        self.model_type = model_type

        if model_type == "Cloze":
            self.model = genanki.Model(
                model_id=simple_hash(CONFIG["card_model_name_cloze"]),
                name=CONFIG["card_model_name_cloze"],
                fields=CONFIG["card_model_fields_cloze"],
                templates=CONFIG["card_model_template_cloze"],
                css=CONFIG["card_model_css"],
                model_type=1,  # This is the model_type number for genanki, takes 0 for QA or 1 for cloze
            )
        elif model_type == "QA":
            self.model = genanki.Model(
                model_id=simple_hash(CONFIG["card_model_name_qa"]),
                name=CONFIG["card_model_name_qa"],
                fields=CONFIG["card_model_fields_qa"],
                templates=CONFIG["card_model_template_qa"],
                css=CONFIG["card_model_css"],
                model_type=0,
            )
        elif model_type == "QA_DA":
            self.model = genanki.Model(
                model_id=simple_hash(CONFIG["card_model_name_qa_da"]),
                name=CONFIG["card_model_name_qa_da"],
                fields=CONFIG["card_model_fields_qa"],
                templates=CONFIG["card_model_template_qa_da"],
                css=CONFIG["card_model_css"],
                model_type=0,
            )
        else:
            raise ValueError("model_type must be either Cloze or QA")

    def deckname(self):
        try:
            if len(self.subdeck) > 0:
                return (
                    "0. Don't click me::1. Active::Personal Mnemonic Medium::"
                    + self.subdeck
                )
            else:
                raise ValueError(
                    "Subdeck length is 0"
                )  # This is purposefully non-valid code
        except:
            return "0. Don't click me::1. Active::Personal Mnemonic Medium"

    def basename(self):
        with open(self.filepath, "r", encoding="utf8") as file:
            full_string = ""

            for line in file.readlines():
                full_string += line

            uid = re.findall(r"<!-- {BearID:.+} -->", full_string)[0]
            return uid

    def card_id(self):  # The identifier for cards
        if len(re.findall(r"{(?!BearID).[^}]*}", self.fields[0])) > 0:  # If cloze
            cloze = re.findall(r"{(?!BearID).[^}]*}", self.fields[0])[
                0
            ]  # Excludes bearID. We don't want clozes to update just because the surrounding information did.
            return simple_hash(
                "{}{}".format(cloze, self.basename())
            )  # Card ID is the cloze deletions + BearID
        else:  # If not cloze
            return simple_hash(
                "{}".format(self.fields[0])
            )  # Q/A cards should be unique from their phrasing. Now it's not tied to a given note.

    def guid(self):  # The identifier for notes
        return (
            self.card_id()
        )  # This is now the hash of the BearID and the cloze or question side

    def add_field(self, field, is_markdown=True):
        self.fields.append(compile_field(field, is_markdown))

    def has_cloze(self):
        return len(self.fields) > 0 and any("{" in s for s in self.fields)

    def has_front_and_back(self):
        return len(self.fields) >= 2

    def finalize(self):
        """Ensure proper shape, for extraction into result formats."""
        if len(self.fields) > 3:
            self.fields = self.fields[:3]
        else:
            while len(self.fields) < 3:
                self.fields.append("")

    def to_genanki_note(self):
        """Produce a genanki.Note with the specified guid."""
        return genanki.Note(
            model=self.model, fields=self.fields, guid=self.guid(), tags=self.tags
        )

    def make_ref_pair(self, filename):
        """Take a filename relative to the card, and make it absolute."""
        newname = "%".join(filename.split(os.sep))

        if os.path.isabs(filename):
            abspath = filename
        else:
            abspath = os.path.normpath(os.path.join(self.deckdir(), filename))
        return (abspath, newname)

    def determine_media_references(self):
        """Find all media references in a card"""
        for i, field in enumerate(self.fields):
            current_stage = field
            for regex in [
                r'src="([^"]*?)"'
            ]:  # TODO not sure how this should work:, r'\[sound:(.*?)\]']:
                results = []

                def process_match(m):
                    initial_contents = m.group(1)
                    abspath, newpath = self.make_ref_pair(initial_contents)
                    results.append((abspath, newpath))
                    return r'src="' + newpath + '"'

                current_stage = re.sub(regex, process_match, current_stage)

                for r in results:
                    yield r

            # Anki seems to hate alt tags :(
            self.fields[i] = re.sub(r'alt="[^"]*?"', "", current_stage)


class DeckCollection(dict):
    """Defaultdict for decks, but with stored name."""

    def __getitem__(self, deckname):
        if deckname not in self:
            deck_id = simple_hash(deckname)
            self[deckname] = genanki.Deck(deck_id, deckname)
        return super(DeckCollection, self).__getitem__(deckname)


def field_to_html(field):
    # Math processing
    """
    Need to extract the math in brackets so that it doesn't get markdowned.
    If math is separated with dollar sign it is converted to brackets.
    """
    if CONFIG["dollar"]:
        for (sep, (op, cl)) in [("$$", (r"\\[", r"\\]")), ("$", (r"\\(", r"\\)"))]:
            escaped_sep = sep.replace(r"$", r"\$")
            # ignore escaped dollar signs when splitting the field
            field = re.split(r"(?<!\\){}".format(escaped_sep), field)
            # add op(en) and cl(osing) brackets to every second element of the list
            field[1::2] = [op + e + cl for e in field[1::2]]
            field = "".join(field)
    else:
        for bracket in ["(", ")", "[", "]"]:
            field = field.replace(r"\{}".format(bracket), r"\\{}".format(bracket))
            # backslashes, man.

    for token in ["*", "/"]:
        if token == "/":
            replacement = "*"
        elif token == "*":
            replacement = "**"

        pattern = "\{}[^<>\-\n]+\{}".format(token, token)

        token_instances = re.findall(pattern, field)

        for instance in token_instances:
            field = field.replace(instance, replacement + instance[1:-1] + replacement)

    # Make sure every \n converts into a newline
    field = field.replace("\n", "  \n")

    return misaka.html(field, extensions=("fenced-code", "math"))


def replace_cloze_id_with_unique(string, selected_cloze=None):
    if selected_cloze is not None:
        selected_clozes = [selected_cloze]
    else:
        selected_clozes = re.findall(r"{(?!BearID).[^}]*}", string)

    for cloze in selected_clozes:
        hash = int(hashlib.sha256(cloze.encode("utf-8")).hexdigest(), 16) % 10 ** 3

        new_cloze = f"{{{{c{hash}::{cloze[1:-1]}}}}}"

        string = string.replace(cloze, new_cloze)

    return string


def compile_field(fieldtext, is_markdown):
    """Turn field lines into an HTML field suitable for Anki."""
    fieldtext_sans_wiki = fieldtext.replace("[[", "<u>").replace("]]", "</u>")

    if is_markdown == 0:
        return fieldtext
    else:
        return field_to_html(fieldtext_sans_wiki)


def has_cloze(string):
    if (
        len(re.findall(r"{.*}", string)) > 0
        and not "BearID" in string
        and not "$$" in string
    ):
        return True
    return False


def has_qa(string):
    if len(re.findall(r"^(?![:>]).*Q.{0,1}\. ", string, flags=re.DOTALL)) != 0:
        return True
    return False


def is_md_list(string):
    return bool(re.search(r"\d+\.", string))


def encode_string(string):
    return string.replace(" ", "%20").replace("/", "%2F")


def has_subdeck_tag(string):
    return len(re.findall(r"#anki\/deck\/\S+", string)) != 0


def get_subdeck_name(string):
    return (
        re.findall(r"#anki\/deck\/\S+", string)[0][11:]
        .replace("/", "::")
        .replace("#", "")
    )


def has_supplementary_tags(string):
    return len(re.findall(r"#anki\/tag\/\S+", string)) != 0


def gen_file_tags(string, import_time):
    file_tags = [import_time]

    if has_supplementary_tags(string):
        for tag in re.findall(r"#anki\/tag\/\S+", string):
            file_tags.append(tag[10:])

    return file_tags


def get_first_question(string) -> str:
    """
    Find the Anki question in a string.

    """
    question = re.findall(r"Q.{0,1}\.(?:(?!A\. ).)*", string, flags=re.DOTALL)[0]

    return question


def get_first_answer(string) -> str:
    """
    Find the Anki answer in a string.

    Returns:
        String
    """
    # I have to use positive lookahead to match code-blocks – to ensure the last answer is matched as well, I add 2 newlines to string. A little hacky.

    string_padded = f"{string.rstrip()}\n\n"

    answer = re.findall(r"\nA\.[ \n]+\n*.+", string_padded, re.DOTALL)[0]

    return answer


def break_string_by_two_or_more_newlines(string):
    """
    Break string into a list every time there are at least two newlines in a row.
    """
    return re.split(r"(\n\n)+", string)


def gen_bear_button_html(filepath):

    bear_base = "bear://x-callback-url/open-note?title="
    filename = os.path.basename(filepath)[:-3]
    bear_extension = "&show_window=yes&new_window=yes&edit=yes"

    href = bear_base + filename + bear_extension

    return f'<h4 class="right"><a href="{href}">Bear</a></h4>'


def get_q_type_tag(question_string):
    q_type_letter = re.findall(r"Q\w{0,1}\.", question_string)[0][1]
    return Q_TYPE_TAG[q_type_letter]


def produce_qa_card_from_block(
    filepath, subdeck, file_tags: list, block_string, extra_string
):
    current_card = Card(filepath)

    question_string = get_first_question(block_string)
    answer_string = get_first_answer(block_string)

    # Metadata handling
    current_card.set_deck(subdeck)

    question_type_tag = get_q_type_tag(question_string)

    file_tags.append(question_type_tag)  # Handle the "I" in "QI."

    current_card.append_tags(file_tags)

    # Content handling
    question_content = re.sub(r"Q.{0,1}\.", "", question_string)
    answer_content = answer_string[4:]

    for field_content in [question_content, answer_content]:
        current_card.add_field(field_content)

    current_card.add_field(extra_string, is_markdown=False)

    if subdeck == "Medicine" or subdeck == "Danish":
        current_card.set_model("QA_DA")
    else:
        current_card.set_model("QA")

    return current_card


def produce_cloze_cards_from_block(
    filepath: str, subdeck: str, file_tags: list, block_string: str, extra_string: str
) -> list:
    clozes = re.findall(r"{(?!BearID).[^}]*}", block_string)

    cards = []

    for selected_cloze in clozes:
        current_card = Card(filepath)

        # Metadata handling
        current_card.set_model("Cloze")
        current_card.set_deck(subdeck)
        current_card.append_tags(file_tags)

        # Content handling
        """Create one note for each cloze to only updates note if the cloze itself has changed, not its surrounding clozes"""
        card_string = replace_cloze_id_with_unique(
            block_string, selected_cloze=selected_cloze
        )

        # Remove the unused-clozes from the card
        non_selected_clozes = re.findall(r"{(?!BearID)(?!{)(?!c\d).[^}]*}", card_string)

        for non_selected_cloze in non_selected_clozes:
            card_string = card_string.replace(
                non_selected_cloze, non_selected_cloze[1:-1]
            )

        current_card.add_field(card_string)
        current_card.add_field(extra_string, is_markdown=False)

        cards.append(current_card)

    return cards


def strip_header(string):
    """Strip first occurrence of a markdown level 1 header"""
    return re.sub(r"^#.*\n", "", string)


def strip_backlinks(string):
    """Strip anything showing up after ## Backlinks"""

    return re.sub(r"## Backlinks.*", "", string, flags=re.DOTALL)


def get_content_only(string):
    string_stripped = strip_header(strip_backlinks(string))

    return string_stripped


def produce_cards_from_file(filepath: str, import_time):
    """
    Parameters:
        Filename as a string
    Returns:
        A generator yielding genanki cards
    """

    with open(filepath, "r", encoding="utf8") as f:
        file_string = f.read()

        # Metadata handling
        if has_subdeck_tag(file_string):
            subdeck = get_subdeck_name(file_string)
        else:
            subdeck = "Default"

        file_tags = gen_file_tags(file_string, import_time)

        extra_string = gen_bear_button_html(filepath)

        # Content
        content_string = get_content_only(file_string)

        blocks = break_string_by_two_or_more_newlines(content_string)

        for block_string in blocks:
            # QA processing
            if has_qa(block_string):
                card = produce_qa_card_from_block(
                    filepath, subdeck, file_tags, block_string, extra_string
                )
                yield card

            elif has_cloze(block_string):
                cards = produce_cloze_cards_from_block(
                    filepath, subdeck, file_tags, block_string, extra_string
                )

                for card in cards:
                    yield card


def complex_hash(text):
    """MD5 of text, mod 2^63. Probably not a great hash function."""
    return int(hashlib.sha256(text.encode("utf-8")).hexdigest(), 16) % 10 ** 15


def add_uid(filepath):
    with open(filepath, "r", encoding="utf8") as f:
        prefix = f.readline()[0:5]
        if prefix != "#####":
            file_id = complex_hash(filepath)
            line_prepender(filepath, "###### " + str(file_id))
            return


def line_prepender(filename, line):
    with open(filename, "r+") as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip("\r\n") + "\n" + content)


def produce_cards_from_dir(dirname):
    """Walk a directory and produce the cards found there, one by one."""
    global VERSION_LOG
    global CONFIG
    for parent_dir, _, files in os.walk(dirname):
        for fn in sorted(files):
            if fn.endswith(".md") or fn.endswith(".markdown"):
                filepath = os.path.join(parent_dir, fn)
                old_hash = VERSION_LOG.get(filepath, None)
                cur_hash = simple_hash(open(filepath, "r").read())

                if old_hash != cur_hash or not CONFIG["updated_only"]:
                    print("Processing {}".format(filepath))
                    try:
                        for card in produce_cards_from_file(
                            filepath, import_time=IMPORT_TIME
                        ):
                            yield card
                    except:
                        print("Didn't yield any cards in {}".format(filepath))
                else:
                    VERSION_LOG[filepath] = cur_hash


def cards_to_apkg(cards, output_name):
    """Take an iterable of the cards, and put a .apkg in a file called output_name.

    NOTE: We _must_ be in a temp directory.
    """
    decks = DeckCollection()

    media = set()

    for card in cards:
        card.finalize()
        for abspath, newpath in card.determine_media_references():
            copyfile(
                abspath, newpath
            )  # This is inefficient but definitely works on all platforms.
            media.add(newpath)
        decks[card.deckname()].add_note(card.to_genanki_note())

    if len(decks) == 0:
        print("Warning: No decks generated")

    package = genanki.Package(deck_or_decks=decks.values(), media_files=list(media))
    package.write_to_file(output_name)


def apply_arguments(arguments):
    global CONFIG
    if arguments.get("--configFile") is not None:
        config_file_path = os.path.abspath(
            os.path.expanduser(arguments.get("--configFile"))
        )
        with open(config_file_path, "r") as config_file:
            CONFIG.update(yaml.load(config_file))
    if arguments.get("--config") is not None:
        CONFIG.update(yaml.load(arguments.get("--config")))
    if arguments.get("-p") is not None:
        CONFIG["pkg_arg"] = arguments.get("-p")
    if arguments.get("-r") is not None:
        CONFIG["recur_dir"] = arguments.get("-r")
    if arguments.get("--updatedOnly"):
        CONFIG["updated_only"] = True


def load_version_log(version_log):
    global VERSION_LOG
    if os.path.exists(version_log):
        VERSION_LOG = json.load(open(version_log, "r"))


def main():
    """Run the thing."""
    apply_arguments(docopt(__doc__, version=VERSION))
    # print(yaml.dump(CONFIG))
    initial_dir = os.getcwd()
    recur_dir = os.path.abspath(os.path.expanduser(CONFIG["recur_dir"]))
    pkg_arg = os.path.abspath(os.path.expanduser(CONFIG["pkg_arg"]))
    version_log = os.path.abspath(os.path.expanduser(CONFIG["version_log"]))

    global IMPORT_TIME
    IMPORT_TIME = "{}".format(
        datetime.now().strftime("%Y.%m/%d_%H:%M")
    )  # Init as global to avoid each card getting separate times

    load_version_log(version_log)

    with tempfile.TemporaryDirectory() as tmpdirname:
        os.chdir(tmpdirname)  # genanki is very opinionated about where we are.

        card_iterator = produce_cards_from_dir(recur_dir)
        cards_to_apkg(card_iterator, pkg_arg)

        os.chdir(initial_dir)

    json.dump(VERSION_LOG, open(version_log, "w"))


if __name__ == "__main__":
    exit(main())
