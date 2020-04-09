import pytest

from pcos_runrex.algo.menarche import MENARCHE_AGE, AGE_MENARCHE, MENARCHE_GRADE, GRADE_MENARCHE


@pytest.mark.parametrize(('text', 'value'), [
    ('menarche at age 13', 13),
    ('menses irregular since onset at age 13', 13),
])
def test_menarche_numeric_age(text, value):
    m = MENARCHE_AGE.matchgroup(text, 'age')
    assert int(m) == value


@pytest.mark.parametrize(('text', 'value'), [
    ('age at first menses : 13 - 14 years', '13 - 14'),
])
def test_menarche_age(text, value):
    m = MENARCHE_AGE.matchgroup(text, 'age')
    assert m == value


@pytest.mark.parametrize(('text', 'value'), [
    ('age 13 y.o. at first menses', 13),
    ('13 yrs at onset of menses', 13),
])
def test_age_numeric_menarche(text, value):
    m = AGE_MENARCHE.matchgroup(text, 'age')
    assert int(m) == value


@pytest.mark.parametrize(('text', 'grade'), [
    ('menarche in sixth grade', 'sixth grade'),
    ('menses irregular since onset in 6th grade', '6th grade'),
])
def test_menarche_grade(text, grade):
    m = MENARCHE_GRADE.matchgroup(text, 'grade')
    assert m.strip() == grade


@pytest.mark.parametrize(('text', 'grade'), [
    ('was in grade 6 at onset of menses', 'grade 6'),
])
def test_grade_menarche(text, grade):
    m = GRADE_MENARCHE.matchgroup(text, 'grade')
    assert m.strip() == grade
