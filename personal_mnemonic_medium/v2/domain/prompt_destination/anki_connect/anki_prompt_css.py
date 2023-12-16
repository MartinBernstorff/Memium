CARD_MODEL_CSS = """
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
            display: flex;
            align-items: center;
            justify-content: center;
            flex-direction: column;
        }
        div.extra h4.left {
            text-align: left;
            float: left;
            width: 60%;
        }
        h4 {
            color: rgba(120, 105, 200, 0);
            font-weight: 0;
            font-style: italic;
            font-size: 0.4em;
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
            background-color: rgba(100, 100, 100, 0.25) !important;
            border: none;
            padding: 7px 12px;
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
        """
