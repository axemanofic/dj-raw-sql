from datetime import datetime


def get_music_all():
    return "SELECT * FROM dj_app_music"


def get_music_by_id(id: int):
    return "SELECT * FROM dj_app_music WHERE id = %s", (id,)


def add_music(name: str):
    return (
        """
        INSERT INTO
            dj_app_music (name, create_at, update_at, is_delete)
        VALUES (%s, %s, %s, %s)
        """,
        (name, datetime.now(), datetime.now(), False),
    )
