# Написать платформу для прослушивания музыки
# 1) Класс Пользователь с юзернеймом, возраст, эл. почтой и подпиской(по дефолту - Без подписки, если подписка не оформлена, то с каждым прослушиванием появялется реклама, спам), плейлист(по дефолту - пустой список). Можно дополнительно еще пароль сделать, с валидацией, вся информация должна быть приватной.
# Метод для оформления подписки, для добавления в пейлист песни, 
# метод для прослушивания песни, 
# метод который прослушивает весь плейлист по очередно
# 2) Класс жанр в названием
# 3) Класс музыка с названием, автором, жанром, длительностью
# 4) Класс работник, который наследуется от Пользователя, но у него есть доп атрибут - роль (например админ), и платформа где он работает
# 5) Класс платформа для прослушивания музыки, например - Spotify, у которого должны быть списки песен, жанры, список пользователей с полпиской и без
# методы для  просмотра всех песен,
# методы для просмотра песен по определенному жанру,
# метод для оформления подписки у пользователя, если
# метод для поиска песни по названию
# метод для добавления определенной песни в плейлист пользователя
# метод удаления, добавления песни, жанра из списка Платформы, которую может сделать только админ этой платформы 

from enum import Enum
class Role(Enum):
    ADMIN = 1
    USER = 2
class Platform(Enum):
    SPOTIFY = 1

import re
class User:
    
    def __init__(self, user, email, password):
        self.user = user
        self.__email = email
        self.__subscription = False
        self.__playlist = {}
        pattern_password = re.compile(r'^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)[0-9a-zA-Z]{8,}$')
        self.__role = Role.USER
        
        if (bool(pattern_password.match(password))):
            self.__password = password
        else:
            print('password is not hard')
    def add_music(self, value):
        self.__playlist[value.autor] = value.name
        print('nice u add the music')
    @property
    def subs(self):
        return self.__subscription
    

    def add_subscription(self, new_vall):
        self.__subscription = new_vall
    
    
    def play_music(self):
        song_counter = 0
        for title, name in self.__playlist.items():
            song_counter += 1
            if song_counter-1 != 3:
                print('user song: ', title, name)
                
            else:
                if  self.__subscription == False:
                    print('ADVERTISEMENT')
                    song_counter = 0
    @property
    def playlist(self):
        return self.__playlist
 
class  Genre:
    def __init__(self, genre_name):
        self.genre_name = genre_name

class Music:
    def __init__(self, autor, name, genre, duration):
        self.autor = autor
        self.name = name
        self.duration = duration # minut
        self.genre = genre

class Employee(User):
    def __init__(self, user, email, password, role, platform):
        super().__init__(user, email,  password)
        self.role = role
        self.platform = platform

some_employee = Employee('anarbek', 'some@gmail.com','abcFF123', Role.ADMIN, Platform.SPOTIFY)

class Platform:
    def __init__(self, name):
        self.name=name
        self.musics= []
        self.genre = set()
        self.users = []
    def show_all_users(self):
        for i in self.users:
            print(i.user)
    def add_users(self, user):
        self.users.append(user)

    def add_genre(self, *genre):
        self.genre.append(genre)
        
    def show_all_songs(self):
        for i in self.musics:
            print('name: ', i.name,', autor: ',i.autor,', genre: ', i.genre.genre_name)
    def search_by_genre(self, genre):
        if genre not in [g.genre_name for g in self.genre]:
             return "This genre is absent."
        else:
            songs=[i for i in self.musics if i.genre.genre_name == genre]
            print(songs[0].name, songs[0].autor)
    def add_subs(self, user, role):

        if not user.subs and role.role == Role.ADMIN:
            user.add_subscription(True)
            print('subs add')
        else:
            print('wrong')

    def search_by_song_name(self):
        song_name = input("Enter a song's name: ")
        found = False
        for music in self.musics:
            if song_name in music.title.lower():
                 print(f"Found the following songs with this title:\n{music}")
                 found = True
        if not found:
            print("No such song.")
    
    def remove_platforme_music(self, name, user):
        if name in self.musics and user.role == Role.ADMIN:
            del  self.musics[name]
            return f"The music has been deleted by admin - {user}"
        else:
            print('music is not have or u are no admin')

    def add_music_on_platform(self, music, user):
        if user.role == Role.ADMIN:
            self.musics.append(music)
            self.genre.add(music.genre)
            return f"The music has been add by admin - {user}"
        else:
            print('music is not true or u are no admin')

    def  add_to_user_playlist(self, user, song):
        if user in self.users and song in self.musics:
            user.add_music(song)
            
        else:
            print('wrong all your life')


genre1 = Genre("Rock")
music1 = Music("Queen1", "We are well", genre1, 240)
music2 = Music("Queen2", "We are well", genre1, 240)
music3 = Music("Queen3", "We are well", genre1, 240)
music4 = Music("Queen4", "We are well", genre1, 240)
music5 = Music("Queen5", "We are well", genre1, 240)



platform1 = Platform("Spotify")
platform1.add_music_on_platform(music1, some_employee)
for i in [music2, music3, music4, music5]:
    platform1.add_music_on_platform(i,some_employee)


user1 = User('anario', 'astana@gmail.com', 'absghk4D')
platform1.add_users(user1)


platform1.show_all_users()
platform1.add_to_user_playlist(user1, music1)

for i in [music2,music3,music4,music5]:
    platform1.add_to_user_playlist(user1, i)


user1.play_music()


platform1.show_all_songs()
platform1.search_by_genre("Rock")

platform1.add_subs(user1, some_employee)

user1.play_music()
print(user1.subs)



























