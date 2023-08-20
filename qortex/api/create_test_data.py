from faker import Faker

from .models import Album, Artist, Song

fake = Faker()


def create_fake_data(count):
    for _ in range(count):
        artist_name = fake.name()
        artist = Artist.objects.create(name=artist_name)
        album_title = fake.word()
        release_year = fake.random_int(min=1990, max=2023)
        album = Album.objects.create(
            title=album_title, artist=artist, release_year=release_year
        )
        song_title = fake.catch_phrase()
        track_number = fake.random_int(min=1, max=15)
        Song.objects.create(title=song_title, album=album, track_number=track_number)
    print(f"{count} fake entries created successfully.")


create_fake_data(10)
