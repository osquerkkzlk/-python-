import json
from datetime import datetime
from typing import Any

# 混入类：提供序列化功能
class JsonSerialable_Mixin:
    def to_json(self):
        """将对象序列化为 JSON 字符串，处理 Song 对象"""
        data = self.__dict__.copy()
        if "songs" in data:
            data["songs"] = [song.to_json() for song in data["songs"]]
        return json.dumps(data, ensure_ascii=False)

# 混入类：提供日志功能
class Log_Mixin:
    def log(self,message:str):
        """记录日志"""
        print(f"[ LOG ]:{datetime.now()} —— {message}")

# 歌曲类
class Song:
    def __init__(self,title,artist,duration):
        self.title=title
        self.artist=artist
        self.duration=duration  #单位(秒)

    def __eq__(self, other):
        if not isinstance(other,Song):
            return NotImplemented
        return self.title==other.title and self.artist ==other.artist

    def __lt__(self, other):
        if not isinstance(other,Song):
            return NotImplemented
        return self.duration < other.duration

    # 格式化显示
    def __format__(self,format_spec:str):
        if format_spec=="short":
            return f"{self.title} by {self.artist}"
        return f"{self.title} by {self.artist} ,duration is {self.duration}"

    def __repr__(self):
        return f"[Song]: {self.title} by {self.artist} ,{self.duration}"

    # 添加 JSON 序列化支持
    def to_json(self):
        """返回可序列化的字典"""
        return {"title": self.title, "artist": self.artist, "duration": self.duration}
# 播放类——直接切片、运算符重载、动态协议
class Player(JsonSerialable_Mixin,Log_Mixin):
    _playlist_count=0

    def __init__(self,name:str):
        self.name=name
        self.songs=[]
        Player._playlist_count+=1
        self.log(f"Created Player List {self.name}")

    @classmethod
    def from_songs(cls,name,songs:list):
        playlist=cls(name)
        playlist.songs.extend(songs)
        playlist.log(f"Initalized with {len(songs)} songs")
        return playlist

    @ property
    def playlist_count(self):
        return self._playlist_count

    #容器协议支持切片和索引
    def __getitem__(self, item):
        if isinstance(item,slice):
            start,stop,step=item.indices(len(self.songs))
            sliced_songs=self.songs[start:stop:step]
            new_player=Player(f"{self.name}_sliced_{start}:{stop}_by{step}")
            new_player.songs=sliced_songs
            new_player.log(f"[Create slic]: {start}:{stop}:{step}")
            return new_player
        else:
            return self.songs[item]

    def __len__(self):
        return len(self.songs)

    def __iter__(self):
        return iter(self.songs)

    def __add__(self, other):
        if not isinstance(other,Player):
            return NotImplemented
        new_player=Player(f"{self.name}_plus_{other.name}")
        new_player.songs = self.songs+other.songs
        new_player.log(f"Merged {self.name} and {other.name}")
        return new_player

    def __eq__(self, other):
        """不在乎 log 属性"""
        if not isinstance(other,Player):
            return NotImplemented
        return self.name==other.name and self.songs ==other.songs

    def __format__(self, format_spec=""):
        if format_spec=="short":
            return f"[Player_Short]: {len(self.songs)} in {self.name} "
        return (f"[Player_Long]: < {self.name} >\n"
                "\n".join(f"{song.title}" for song in self.songs))

    def add_songs(self,songs:list[Song]):
        for song in songs:
            self.songs.append(song)
            self.log(f"[Adding Song]: {song.title}")

    def sort(self,reverse:bool=False):
        self.songs.sort(key =lambda song:song.duration,reverse=reverse)
        self.log(f"[Sorted] :{"Reversed" if reverse else "Not Reversed"}")

if __name__ == '__main__':
    # 创建歌曲
    songs=[Song("A","alpha",167),
           Song("B","beita",129),
           Song("C","beita",143),]
    player_P=Player.from_songs("Populayer songs",songs)
    player_R=Player("Rock Classics")
    player_R.add_songs([Song("D","theta",206)])

    # 测试切片
    sliced=player_P[0:2]
    print(f"[Sliced]: {sliced:short}")

    # 测试合并（知识点：__add__）
    merged_playlist = player_P + player_R
    print(f"Merged Playlist:\n{merged_playlist}")

    # 测试排序（知识点：__lt__）
    merged_playlist.sort()
    print(f"Sorted Merged Playlist:\n{merged_playlist}")

    # 测试序列化（知识点：混入类）
    print(f"JSON: {merged_playlist.to_json()}")

    # 测试类属性（知识点：类属性）
    print(f"Total Playlists: {player_P.playlist_count}")


    # 测试动态协议（知识点：动态协议，鸭子类型）
    def play(playlist: Any):
        # 运行时检查是否支持迭代（无需显式协议）
        if not hasattr(playlist, '__iter__'):
            raise AttributeError("Playlist must support iteration")
        for song in playlist:
            print(f"Playing: {song:short}")


    play(player_P)



