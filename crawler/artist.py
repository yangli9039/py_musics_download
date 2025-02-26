import time

from utils.common import RequestHandler
from typing import Dict, Optional
import json

class ArtistCrawler:
    def __init__(self):
        self.request_handler = RequestHandler()
        self.search_url = "https://music.91q.com/v1/artist/search"
        self.base_url = "https://music.91q.com"
        
    def search_artist(self, artist_name: str) -> Optional[Dict]:
        """
        搜索歌手信息
        """
        params = {
            'keyword': artist_name,
            'from': 'web',
            'pageNo': 1,
            'pageSize': 20,
            "sign": '3253958e353005b8057d30c84621d3aa',#7725beb716c6d4f590f59ee3f60f96c2,
            'type':'',
            'appid': '16073360',
            'timestamp': int(time.time()),
        }
        
        headers = {
            'Referer': self.base_url,
            'Origin': self.base_url,
            'Accept': 'application/json, text/plain, */*'
        }
        
        try:
            response = self.request_handler.get(
                self.search_url, 
                params=params,
                headers=headers
            )
            data = response.json()
            
            if data.get('success') and data.get('data', {}).get('list'):
                artist = data['data']['list'][0]
                return {
                    'id': artist['artistId'],
                    'name': artist['artistName']
                }
            return None
            
        except Exception as e:
            print(f"搜索歌手失败: {str(e)}")
            return None