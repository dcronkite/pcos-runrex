from runrex.algo.pattern import Pattern
from runrex.text import Document
from runrex.algo.result import Status, Result
from runrex.terms import hypothetical, negation

instructions = r'(remember|recall|do not)'
side_effects = r'(side effects?)'

negation_group = (negation, hypothetical, instructions, side_effects)


class HyperandrogenismStatus(Status):
    EXPLORATORY = -1
    DX_CODE = 2
    ACNE = 30
    ACNE_HANDOUT = 31
    HIRSUTISM = 40
    ANDROGEN_EXCESS = 50
    BALD = 60  # alopetian/baldness


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

DX_CODE = Pattern(
    rf'\b(706.1|704.1|704.0)'
)

ACNE = Pattern(
    rf'acne',
    negates=negation_group,
)

ACNE_HANDOUT = Pattern(
    rf'('
    rf'acne : home treatment'
    rf'|more info'
    rf')'
)

HIRSUTISM = Pattern(
    rf'('
    rf'alopecia'
    rf'|hirsutism'
    rf'|hair loss'
    rf'|baldness'
    rf'|excess hair|hairy'
    rf'|male pattern'
    rf')',
    negates=negation_group,
)

ANDROGEN_EXCESS = Pattern(
    rf'('
    rf'(elevated|increased|excessive) (serum)? (testost\w+|dheas|dehyd\w+|androgen)'
    rf'|dheas|dehydroepiand\w+'
    rf'|androgen excess|excess androgen'
    rf')',
    negates=negation_group,
)


def _search_hyperandrogenism(document: Document):
    for sentence in document.iter_sentence_by_pattern(EXPLORATORY):
        sentence.reset_found_pattern()
        if DX_CODE.matches(sentence):  # this sentence is dx code
            yield HyperandrogenismStatus.DX_CODE, sentence.text
        if sentence.last_found:
            continue
        if ACNE_HANDOUT.matches(sentence):
            yield HyperandrogenismStatus.ACNE_HANDOUT, sentence.text
        if not sentence.last_found and ACNE.matches(sentence):
            yield HyperandrogenismStatus.ACNE, sentence.text
        if ANDROGEN_EXCESS.matches(sentence):
            yield HyperandrogenismStatus.ANDROGEN_EXCESS, sentence.text
        if not sentence.any_found:
            yield HyperandrogenismStatus.EXPLORATORY, sentence.text


def get_hyperandrogenism(document: Document, expected=None):
    for status, text in _search_hyperandrogenism(document):
        yield Result(status, status.value, expected=expected, text=text)
