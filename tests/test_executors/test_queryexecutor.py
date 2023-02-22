import pytest
from dj_app.models import Music
from dj_raw_sql import QueryExecutor

from .queries import (
    get_music_all,
    get_music_by_id,
    add_music,
)


@pytest.fixture
def create_music(db):
    def make_music():
        Music.objects.create(name="King")
        Music.objects.create(name="Great night")
        Music.objects.create(name="Best day")

    return make_music


@pytest.mark.django_db
def test_get_all_music(create_music):
    create_music()
    king = QueryExecutor.fetchall(get_music_all)
    assert type(king) is list
    assert type(king[0]) is tuple
    assert king[0][0] == 1


@pytest.mark.django_db
def test_get_music(create_music):
    create_music()
    king = QueryExecutor.fetchone(get_music_by_id, id=1)
    assert type(king) is tuple
    assert king[0] == 1


@pytest.mark.django_db
def test_add_music(create_music):
    create_music()
    QueryExecutor.execute(add_music, name="SomeName")
    music = QueryExecutor.fetchone(get_music_by_id, id=4)
    assert type(music) is tuple
    assert music[1] == "SomeName"
