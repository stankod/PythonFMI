import csv
from functools import reduce

fields = ['name', 'artist', 'genre', 'subgenre', 'tags']
class Song:
    def __init__(self, name, artist, genre, subgenre, tags):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.subgenre = subgenre
        self.tags = tags

class Collection:
    def __init__(self, file_contents_as_string, artist_tags):
        fnames = [field for field in fields if field != 'subgenre']
        dial = csv.Sniffer().sniff(file_contents_as_string, delimiters=';')
        reader = csv.DictReader(file_contents_as_string.split('\n'), fieldnames=fnames, dialect=dial)
        self._songs = dict()
        for attribute in fields:
            self._songs[attribute] = dict()
        for entry in reader:
            song = self._build_song(entry, artist_tags)
            for attribute in fields:
                attr = song.__getattribute__(attribute)
                if attr != None:
                    if not isinstance(attr, (list, tuple, set)):
                        attr = {attr}
                    for element in attr:
                        self._songs[attribute].setdefault(element, {}).add(song)

    def _build_song(self, song_items, artist_tags):
        genre, *subgenre = map(str.strip, song_items['genre'].split(','))
        subgenre = None if not subgenre else subgenre[0]
        tags = set(map(str.strip, song_items['tags'].split(',')))
        tags.update(artist_tags[song_items['artist']])
        tags.update({genre, subgenre})
        tags -= {None, ''}
        return Song(song_items['name'], song_items['artist'], genre, subgenre, tags)

    def find(self, result, **what):
        sets, neg, res  = [], [], []
        for k,v in what.items():
            if k != 'filter':
                if not isinstance(v, (list, tuple, set)):
                    v = [v]
                for attr in v:
                    if isinstance(attr, str):
                        if attr.endswith('!'):
                            attr = attr[:-1]
                            res_set = neg
                        else:
                            res_set = sets
                        attr_key = [k for k in self._songs[k].keys() if k.lower() ==\
                                attr.lower()][0]
                        res_set.append(self._songs[k].get(attr_key, {}))
                    else:
                        songs = [set(v) for k,v in self._songs[k].items() if\
                                attr.search(k)]
                        songs = set(reduce(set.union, songs))
                        sets.append(songs)
            else:
                if not isinstance(what['filter'], (list, set, tuple)):
                    what['filter'] = [what['filter']]
                sets.append({song for lst in self._songs['artist'] for song in\
                self._songs['artist'][lst] if all([f(song) for f in\
                    what['filter']])})

        if sets:
            res = list(reduce(set.intersection, sets))
        if neg:
            res = list(reduce(set.difference, neg, set(res)))

        if len(what) == 0:
            res = list({song for lst in self._songs['artist'] for song in\
                self._songs['artist'][lst]})

        if result != 'songs':
            res = list(set([getattr(song, result) for song in res])-{None})

        return res
