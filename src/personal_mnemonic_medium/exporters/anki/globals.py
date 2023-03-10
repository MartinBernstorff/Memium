# Anki 2.1 has mathjax built in, but ankidroid and other clients don't.
import textwrap

from personal_mnemonic_medium.exporters.anki.anki_css import CARD_MODEL_CSS

CARD_MATHJAX_CONTENT = textwrap.dedent(
    """\

"""
)

VERSION = "0.1"


QA_MODEL_TEMPLATE = [
    {
        "name": "Ankdown QA Card",
        "qfmt": '<div class="front">{{{{Question}}}}{{{{tts en_US voices=Apple_Samantha speed=1.1:Question}}}}\n{0}</div>\n<div class="extra">{{{{Extra}}}}</div>'.format(
            CARD_MATHJAX_CONTENT
        ),
        "afmt": '<div class="back"><div class="question"></div><div class="answer">{{{{Answer}}}}{{{{tts en_US voices=Apple_Samantha speed=1.1:Answer}}}}</div>\n\n<div class="extra">{{{{Extra}}}}</div>{0}</div>'.format(
            CARD_MATHJAX_CONTENT
        ),
    }
]

QA_MODEL_TEMPLATE = [
    {
        "name": "Ankdown QA DK Card",
        "qfmt": '<div class="front">{{{{Question}}}}{{{{tts da_DK  speed=1.4:Question}}}}\n{0}</div>\n<div class="extra">{{{{Extra}}}}</div>'.format(
            CARD_MATHJAX_CONTENT
        ),
        "afmt": '<div class="back"><div class="question">{{{{Question}}}}</div><div class="answer">{{{{Answer}}}}{{{{tts da_DK speed=1.4:Answer}}}}</div>\n\n<div class="extra">{{{{Extra}}}}</div>{0}</div>'.format(
            CARD_MATHJAX_CONTENT
        ),
    }
]

CLOZE_MODEL_TEMPLATE = [
    {
        "name": "Ankdown Cloze Card",
        "qfmt": "{{{{cloze:Text}}}}\n<div class='extra'>{{{{Extra}}}}</div>\n{0}".format(
            CARD_MATHJAX_CONTENT
        ),
        "afmt": "{{{{cloze:Text}}}}\n<div class='extra'>{{{{Extra}}}}</div>\n{0}".format(
            CARD_MATHJAX_CONTENT
        ),
    }
]

CONFIG = {
    "pkg_arg": "AnkdownPkg.apkg",
    "recur_dir": ".",
    "dollar": False,
    "updated_only": False,
    "version_log": ".mdvlog",
    "card_model_name_cloze": "Ankdown Cloze",
    "card_model_name_qa": "Ankdown QA",
    "card_model_name_qa_da": "Ankdown QA DA",
    "card_model_css": CARD_MODEL_CSS,
    "card_model_fields_cloze": [{"name": "Text"}, {"name": "Extra"}, {"name": "Tags"}],
    "card_model_fields_qa": [
        {"name": "Question"},
        {"name": "Answer"},
        {"name": "Extra"},
    ],
    "card_model_template_qa": QA_MODEL_TEMPLATE,
    "card_model_template_qa_da": CLOZE_MODEL_TEMPLATE,
    "card_model_template_cloze": CLOZE_MODEL_TEMPLATE,
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