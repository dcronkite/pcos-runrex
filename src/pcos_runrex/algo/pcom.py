from runrex.algo.pattern import Pattern
from runrex.text import Document
from runrex.algo.result import Status, Result
from runrex.terms import hypothetical, negation


class PcomStatus(Status):
    NONE = -1
    EXPLORATORY = 1
    PCOS = 2
    MEASURE = 3


EXPLORATORY = Pattern(
    rf'('
    rf'rotterdam'
    rf'|(consistent with|possible|charact\w+ of) pco[sm]\b'
    rf'|\bpcom\b'
    rf'|polycyst\w+ ovarian morph\w+'
    rf')',
    # negates=(negation, hypothetical)
)

PCOS = Pattern(
    rf'('
    rf'\bpco[ms]?\b'
    rf'|polycystic ovarian'
    rf')'
)

cyst = '(follicle|cyst)s?'

MEASURE = Pattern(
    rf'('
    rf'{cyst} (\w+ ){{,3}} (peripher\w+|ovar\w+ periphery|subcort\w+|(under|beneath) cortex)'
    rf'|multifolli\w+ pattern'
    rf'|\d+ (mm|cm)? {cyst}'
    rf'|volume of ovar'
    rf'|ovarian volume'
    rf'|ovarian ratio'
    rf'|\bs/a\b'
    rf')'
)


def _search_pcom(document: Document):
    for sentence in document.select_sentences_with_patterns(EXPLORATORY, neighboring_sentences=1):
        yield PcomStatus.EXPLORATORY, sentence.text
    for sentence in document.select_sentences_with_patterns(PCOS, neighboring_sentences=1):
        yield PcomStatus.PCOS, sentence.text
    for sentence in document.select_sentences_with_patterns(MEASURE, neighboring_sentences=1):
        yield PcomStatus.PCOS, sentence.text


def get_pcom(document: Document, expected=None):
    for status, text in _search_pcom(document):
        yield Result(status, status.value, expected=expected, text=text)
