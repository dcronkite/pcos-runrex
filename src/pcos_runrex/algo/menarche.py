import re

from runrex.algo.pattern import Pattern
from runrex.algo.result import Status, Result
from runrex.terms import hypothetical, negation
from runrex.text import Document


class MenarchyStatus(Status):
    NONE = -1
    EXPLORATORY = 1
    FOUND_GRADE = 2
    FOUND_AGE = 3
    STRUCTURED = 4
    LATE = 5


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
age_capture = r'(?P<age>\d+ ((-|/|or|to) (\d+|older|younger))?)'
AT_AGE = re.compile(fr'{at_age}\W*{age_capture}', re.I)
at_grade = '(in|(at)? (the)? (start|end) of)'

grade_number = rf'(the )?' \
               rf'(\d+(\W?th)?|first|second|third|fourth|fifth|sixth|seventh|eighth|nine?th|tenth|eleventh|twelfth)'
grade = r'(' \
        rf'{grade_number} grade' \
        r'|grade \d+' \
        r')'
AT_GRADE = re.compile(f'{grade}', re.I)
grade_capture = rf'(?P<grade>(' \
                rf'{grade} (or ({grade}|\d+))?' \
                rf'|\d+ (-|or) \d+ grade' \
                rf'|grade \d+ (-|or) \d+' \
                rf'|{grade_number} (-|or) {grade}' \
                rf'))'

LATE = Pattern(
    rf'('
    rf'late ((onset|first) menses|menarche)'
    rf')'
)

MENARCHE_GRADE = Pattern(
    rf'('
    rf'('
    rf'menarche (was )?{at_grade}?'
    rf'|menarche'
    rf'|(first|onset|began|start\w*) menses {at_grade}?'
    rf'|menses (\w+ ){{0,3}} (onset|since) {at_grade}?'
    rf') {grade_capture}'
    rf')'
)

GRADE_MENARCHE = Pattern(
    rf'{grade_capture}'
    rf'('
    rf' (\w+)? (onset of|first) menses'
    rf')'
)

MENARCHE_AGE = Pattern(
    rf'('
    rf'('
    rf'menarche (was )?{at_age}?'
    rf'|age (of|at) menarche'
    rf'|menarche'
    rf'|(first|onset|began|start\w*) menses {at_age}?'
    rf'|menses (\w+ ){{0,3}} (onset|since) {at_age}?'
    rf') {age_capture}'
    rf')'
)

AGE_MENARCHE = Pattern(
    rf'{age_capture}'
    rf' {years_old}?'
    rf'('
    rf' (at)? (onset of|first) menses'
    rf')'
)


def find_subpattern(pat, text, group_name):
    m = pat.search(text)
    if m:
        return m.group(group_name)


def _search_menarche(document: Document):
    for i, sentence in enumerate(document.iter_sentence_by_pattern(FILTER)):
        for _grade, start, end in sentence.get_patterns(MENARCHE_GRADE, GRADE_MENARCHE, index='grade'):
            age = find_subpattern(AT_AGE, sentence.text[end:], 'age')
            yield MenarchyStatus.FOUND_GRADE, sentence.text, age, _grade
        if sentence.last_found:
            continue
        for age, start, end in sentence.get_patterns(MENARCHE_AGE, AGE_MENARCHE, index='age'):
            _grade = find_subpattern(AT_GRADE, sentence.text[end:], 'grade')
            yield MenarchyStatus.FOUND_AGE, sentence.text, _grade, age
        if sentence.last_found:
            continue
        for _, start, end in sentence.get_patterns(STRUCTURED):
            yield MenarchyStatus.STRUCTURED, sentence.text, None, None
        if sentence.last_found:
            continue
        for _, start, end in sentence.get_patterns(LATE):
            yield MenarchyStatus.LATE, sentence.text, None, None
        if sentence.last_found:
            continue
        if sentence.has_patterns(EXPLORATORY):
            yield MenarchyStatus.EXPLORATORY, document.neighbors_text(i), None, None


def get_menarche(document: Document, expected=None):
    for status, text, age, _grade in _search_menarche(document):
        yield Result(status, status.value, expected=expected, text=text, extras={'age': age, 'grade': _grade})
