# pylint: disable=import-error,redefined-outer-name,redefined-builtin
import pytest
from dj_app.models import Music
from dj_raw_sql import execute_sql


@pytest.fixture
def create_music(db):
    def make_music():
        Music.objects.create(name="King")
        Music.objects.create(name="Great night")
        Music.objects.create(name="Best day")

    return make_music


@execute_sql()
def get_music_by_id(id: int):
    return "SELECT * FROM dj_app_music WHERE id = %s", (id,)


@execute_sql(to_ordereddict=True)
def get_music_by_id__ordereddict(id: int):
    return "SELECT * FROM dj_app_music WHERE id = %s", (id,)


@pytest.mark.django_db
def test_get_music(create_music):
    create_music()
    king = get_music_by_id(1)
    assert king[0][0] == 1


@pytest.mark.django_db
def test_get_ordereddict(create_music):
    create_music()
    king = get_music_by_id__ordereddict(1)
    assert king[0]["id"] == 1
