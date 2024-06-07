from jukebox.Dao_song import Dao_song
from jukebox.Song import Song

dao_song = Dao_song('mongodb://localhost:27017/')
def add():
    song = Song(input("Song Name: "), input("intepret: "), input("album: "), input("genere: "), input("erscheinungs_jahr"))
    dao_song.create(song)
def edit(id):
    song = dao_song.read_by_id(id)
    while True:
        match input("Was möchtest du updaten? (name, intepret, album, genere, erscheinungs_jahr, exit)"):
            case "name":
                song.name = input("Song Name: ")
            case "intepret":
                song.intepret = input("intepret: ")
            case "album":
                song.album = input("album: ")
            case "genere":
                song.genere = input("genere: ")
            case "erscheinungs_jahr":
                song.erscheinungs_jahr = input("erscheinungs_jahr: ")
            case "exit":
                break

    dao_song.update(song)

def player():
    results = dao_song.read_by_regex(input())
    for result in results:
        print(result)



while True:
    match input("Was möchtest du tun? (edit, read, add, delete, player, exit)"):
        case "edit":
            edit(input("Id: "))
        case "read":
            dao_song.read_by_id(2)
        case "add":
            add()
        case "delete":
            dao_song.delete(input('Id: '))
        case "player":
            player = input("Player: ")
        case "exit":
            break

