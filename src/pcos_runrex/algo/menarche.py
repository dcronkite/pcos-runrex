from runrex.algo.pattern import Pattern
from runrex.algo.result import Status, Result
from runrex.terms import hypothetical, negation
from runrex.text import Document


class MenarchyStatus(Status):
    NONE = -1
    EXPLORATORY = 1
    FOUND = 2
    STRUCTURED = 3
    LATE = 4


FILTER = Pattern(
    rf'(menarche|menses)'
)

EXPLORATORY = Pattern(
    rf'('
    rf'menarche|first menses|start\w* menses'
    rf')',
    # negates=(negation, hypothetical)
)
STRUCTURED = Pattern(
    rf'('
    rf'menarche/menses|age (of|at) menarche|age at first menses'
    rf'):'
)

years_old = '(y o|years old|years?|yrs?|yrs old)'
at_age = '(at age|around|at|age)'
age_capture = r'(?P<age>\d+)'

LATE = Pattern(
    rf'('
    rf'late ((onset|first) menses|menarche)'
    rf')'
)

MENARCHE_VALUE = Pattern(
    rf'('
    rf'('
    rf'menarche {at_age}?'
    rf'|age (of|at) menarche'
    rf'|menarche'
    rf'|(first|onset|start\w*) menses {at_age}?'
    rf'|menses (\w+ ){{0,3}} (onset|since) {at_age}?'
    rf') {age_capture}'
    rf')'
)

VALUE_MENARCHE = Pattern(
    rf'{age_capture}'
    rf' {years_old}?'
    rf'('
    rf' (at)? (onset of|first) menses'
    rf')'
)


def _search_menarche(document: Document):
    for i, sentence in enumerate(document.iter_sentence_by_pattern(FILTER)):
        for captured, start, end in sentence.get_patterns(MENARCHE_VALUE, VALUE_MENARCHE, index='age'):
            yield MenarchyStatus.FOUND, sentence.text, int(captured)
        if sentence.last_found:
            continue
        for _, start, end in sentence.get_patterns(STRUCTURED):
            yield MenarchyStatus.STRUCTURED, sentence.text, ''
        if sentence.last_found:
            continue
        for _, start, end in sentence.get_patterns(LATE):
            yield MenarchyStatus.LATE, sentence.text, ''
        if sentence.last_found:
            continue
        if sentence.has_patterns(EXPLORATORY):
            yield MenarchyStatus.EXPLORATORY, document.neighbors_text(i), ''


def get_menarche(document: Document, expected=None):
    for status, text, value in _search_menarche(document):
        yield Result(status, status.value, expected=expected, text=text, extras=value)
