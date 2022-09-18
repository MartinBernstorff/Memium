# Anki 2.1 has mathjax built in, but ankidroid and other clients don't.
import textwrap


CARD_MATHJAX_CONTENT = textwrap.dedent(
    """\

"""
)

VERSION = "0.1"

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
