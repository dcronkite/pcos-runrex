from runrex.algo.pattern import Pattern
from runrex.text import Document
from runrex.algo.result import Status, Result
from runrex.terms import hypothetical, negation


class HyperandrogenismStatus(Status):
    NONE = -1
    EXPLORATORY = 1


EXPLORATORY = Pattern(
    rf'('
    rf'acne|vulgaris'
    rf'|hirsui?t\w+'
    rf'|hyperandrogenism'
    rf'|androgenetic'
    rf'|hypertrichosis'
    rf'|alopecia|areata|704.00'
    rf'|hair\W?loss|baldness'
    rf'|androgen excess|excess androgen'
    rf'|(shav|electrolys|laser)\w+ (chin|face|facial|hair)|(face|chin) hair'
    rf'|excess hair|hairy|male pattern'
    rf'|(elevated|increased|excessive) (serum)? (testost\w+|dheas|dehyd\w+|androgen)'
    rf'|dheas|dehydroepiand\w+'
    rf')',
    # negates=(negation, hypothetical)
)


def _search_hyperandrogenism(document: Document):
    for sentence in document.select_sentences_with_patterns(EXPLORATORY, neighboring_sentences=1):
        yield HyperandrogenismStatus.EXPLORATORY, sentence.text


def get_hyperandrogenism(document: Document, expected=None):
    for status, text in _search_hyperandrogenism(document):
        yield Result(status, status.value, expected=expected, text=text)
