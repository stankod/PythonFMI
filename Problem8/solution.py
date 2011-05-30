import csv
from collections import namedtuple

Song = namedtuple('Song', ['name', 'artist', 'genre', 'subgenre', 'tags'])
Song.__hash__ = lambda self: (self.name, self.artist).__hash__()

class Collection:
    def __init__(self, file_contents_as_string, artist_tags):
        fnames = ['name', 'artist', 'genre', 'tags']
        dial = csv.Sniffer().sniff(file_contents_as_string, delimiters=';')
        reader = csv.DictReader(file_contents_as_string.split('\n'), fieldnames=fnames, dialect=dial)
        self._songs = dict()
        for entry in reader:
            song = self._build_song(entry, artist_tags)
            self._songs[song] = song

    def _build_song(self, song_items, artist_tags):
        genre, *subgenre = map(str.strip, song_items['genre'].split(','))
        subgenre = None if not subgenre else subgenre[0]
        tags = set(map(str.strip, song_items['tags'].split(',')))
        tags.union(artist_tags[song_items['artist']], genre)
        tags.add(subgenre)
        tags = tags - {None, ''}
        return Song(song_items['name'], song_items['artist'], genre, subgenre, tags)

    def _matcher(self, song, what):
        for field in song._fields:
            if what.get(field):
                if field == 'tags':
                    negative = {tag for tag in what['tags'] if tag.endswith('!')}
                    what[field] = set(what[field]) - negative
                    negative = {tag[:-1] for tag in negative}
                    if not set(what[field]) <= getattr(song, field):
                        return False
                    if negative and negative <= getattr(song, field):
                        return False
                else:
                    if what[field] != getattr(song, field):
                        return False
        return True


    def find(self, result, **what):
        res = [v for k, v in self._songs.items()\
                if self._matcher(v, what)]

        if result != 'songs':
            res = list(set([getattr(song, result) for song in res]))

        return res
