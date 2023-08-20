from rest_framework import serializers

from .models import Album, Artist, Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"


class AlbumSerializer(serializers.ModelSerializer):
    artist = serializers.PrimaryKeyRelatedField(queryset=Artist.objects.all())

    class Meta:
        model = Album
        fields = "__all__"


class ArtistSerializer(serializers.ModelSerializer):
    songs = serializers.SerializerMethodField()

    class Meta:
        model = Artist
        fields = ["id", "name", "songs"]

    def get_songs(self, obj):
        songs = []
        albums = Album.objects.filter(artist=obj)
        for album in albums:
            songs.extend(album.song_set.all())
        return [song.title for song in songs]
