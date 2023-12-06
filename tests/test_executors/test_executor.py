from collections import OrderedDict

import pytest
from dj_app.models import Music # pyright: ignore
from dj_raw_sql.executors import Executor

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
    query = get_music_all()
    all_music = Executor().fetchall(query).query_result
    assert isinstance(all_music, list)
    assert isinstance(all_music[0], OrderedDict)
    assert all_music[0]["id"] == 1


@pytest.mark.django_db
def test_get_music(create_music):
    create_music()
    query = get_music_by_id(id=1)
    music = Executor().fetchone(query).query_result
    assert isinstance(music, OrderedDict)
    assert music["id"] == 1


@pytest.mark.django_db
def test_add_music(create_music):
    create_music()

    executor = Executor()
    query = add_music(name="SomeName")
    executor.execute(query)
    
    query = get_music_by_id(id=4)
    music = executor.fetchone(query).query_result

    assert isinstance(music, OrderedDict)
    assert music["name"] == "SomeName"
