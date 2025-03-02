import pytest

from .hash_cleaned_str import clean_str, hash_str_to_int


def hash_cleaned_str(input_str: str) -> int:
    return hash_str_to_int(clean_str(input_str))


def test_hash_cleaned_str_should_ignore_punctuation():
    strings_should_hash_to_identical = ["this", "This"]

    punctuation = r"!().,:;/"
    strings_should_hash_to_identical += [
        f"{s}{punctuation}" for s in strings_should_hash_to_identical
    ]

    assert len({hash_str_to_int(clean_str(s)) for s in strings_should_hash_to_identical}) == 1


@pytest.mark.parametrize(("input_str", "hash_identical_str"), [("<p>Test</p>", "Test"), ("å", "å")])
def test_hash_cleaned_str_should_remove_html_tags(input_str: str, hash_identical_str: str):
    assert hash_cleaned_str(input_str) == hash_cleaned_str(hash_identical_str)


@pytest.mark.parametrize(
    ("input_str", "expected"),
    [
        ("Is <2, but >4", "is_2_but_4"),
        ("Q. ![](src). Question?", "q_src_question"),
        ("pre <img src='testsrc' /> post", "pre_testsrc_post"),
        ("\t", ""),
        ("\n", ""),
        ("""1. One\n\t2. Two""", "one_two"),
        ("""* One\n\t* Two""", "one_two"),
        ("""- One\n\t- Two""", "one_two"),
        ("[link1](blah) and [link2](blah)", "link1_and_link2"),
        ('<pre><code class="language-r">ls()</code></pre>', "ls"),
        (
            """```r
ls()
```""",
            "ls",
        ),
    ],
)
def test_str_cleaner(input_str: str, expected: str):
    assert clean_str(input_str) == expected


@pytest.mark.parametrize(
    ("markdown_str", "html"),
    [
        ('```df.select(["A", "B"])```', '<p><code>df.select(["A", "B"])</code></p>'),
        (
            """``` js
for (let i = 0; i < 4; i += 1) {
	console.log(i);
};
```""",
            """<pre><code class="language-js">for (let i = 0; i &lt; 4; i += 1) {
    console.log(i);
};
</code></pre>""",
        ),
        (
            """``` python
```""",
            """<pre><code class="language-python"></code></pre>""",
        ),
        (
            """```python
df.filter(pl.col("ID").is_in(ids_set))
```""",
            """<pre><code class="language-python">df.filter(pl.col("ID").is_in(ids_set))
</code></pre>""",
        ),
    ],
)
def test_str_cleaner_preserves_identity(markdown_str: str, html: str):
    cleaned_markdown = clean_str(markdown_str)
    cleaned_html = clean_str(html)
    assert cleaned_markdown == cleaned_html
    assert hash_cleaned_str(markdown_str) == hash_cleaned_str(html)
