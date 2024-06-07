class Song:
    def __init__(self, name, interpret, album=None, genere=None, erscheinungs_jahr=None, _id=None):
        self.name = name
        self.intepret = interpret
        if album is not None:
            self.album = album
        if genere is not None:
            self.genere = genere
        if erscheinungs_jahr is not None:
            self.erscheinungs_jahr = erscheinungs_jahr
        if _id is not None:
            self._id = _id