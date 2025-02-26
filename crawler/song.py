from utils.common import RequestHandler
from typing import List, Dict
import json

class SongCrawler:
    def __init__(self):
        self.request_handler = RequestHandler()
        self.artist_songs_url = "https://music.91q.com/v1/artist/songs"
        
    def get_artist_songs(self, artist_id: str) -> List[Dict]:
        """
        获取歌手的所有歌曲
        """
        all_songs = []
        page = 1
        page_size = 50
        
        while True:
            params = {
                'artistId': artist_id,
                'page': page,
                'size': page_size
            }
            
            try:
                response = self.request_handler.get(self.artist_songs_url, params=params)
                data = response.json()
                
                if data['code'] != 200:
                    break
                    
                songs = data['data']['songs']
                if not songs:
                    break
                    
                all_songs.extend([{
                    'id': song['id'],
                    'name': song['name'],
                    'artist': song['artistName'],
                    'download_url': song['url']
                } for song in songs])
                
                if len(songs) < page_size:
                    break
                    
                page += 1
                
            except Exception as e:
                print(f"获取歌曲列表失败: {str(e)}")
                break
                
        return all_songs