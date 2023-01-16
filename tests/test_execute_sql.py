# pylint: disable=import-error

import pytest

from dj_app.models import Music


@pytest.mark.django_db
def test_create_music():
    Music.objects.create(name="ololo")
    print(Music.objects.all())
    assert Music.objects.count() == 1
