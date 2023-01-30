# pylint: disable=import-error
import pytest
from dj_raw_sql import execute_sql


from .functions import make_music, measure_execution_time


@pytest.fixture
def create_music(db):
    return make_music


@execute_sql()
def get_music_by_limit(limit: int):
    return "SELECT * FROM dj_app_music LIMIT ?", (limit,)


@pytest.mark.django_db
def test_get_music_10(create_music):
    create_music()
    measure_execution_time(get_music_by_limit, 10)
    assert 1 == 1


@pytest.mark.django_db
def test_get_music_100(create_music):
    create_music()
    measure_execution_time(get_music_by_limit, 100)
    assert 1 == 1


@pytest.mark.django_db
def test_get_music_1000(create_music):
    create_music()
    measure_execution_time(get_music_by_limit, 1000)
    assert 1 == 1


@pytest.mark.django_db
def test_get_music_5000(create_music):
    create_music()
    measure_execution_time(get_music_by_limit, 5000)
    assert 1 == 1
