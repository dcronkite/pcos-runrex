import pytest

from pcos_runrex.algo.menarche import MENARCHE_VALUE, VALUE_MENARCHE


@pytest.mark.parametrize(('text', 'value'), [
    ('menarche at age 13', 13),
    ('menses irregular since onset at age 13', 13),
])
def test_menarche_value(text, value):
    m = MENARCHE_VALUE.matchgroup(text, 'age')
    assert int(m) == value


@pytest.mark.parametrize(('text', 'value'), [
    ('age 13 y.o. at first menses', 13),
    ('13 yrs at onset of menses', 13),
])
def test_value_menarche(text, value):
    m = VALUE_MENARCHE.matchgroup(text, 'age')
    assert int(m) == value


