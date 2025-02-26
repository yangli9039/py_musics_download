import os
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from typing import List, Dict
from tqdm import tqdm
from utils.common import RequestHandler, sanitize_filename

class MusicDownloader:
    def __init__(self):
        self.request_handler = RequestHandler()
        self.download_path = Path.home() / "Downloads" / "music"
        self.max_workers = 3
        
    def download_song(self, song: Dict) -> bool:
        """
        下载单首歌曲
        """
        try:
            # 创建下载目录
            self.download_path.mkdir(parents=True, exist_ok=True)
            
            # 构建文件名
            filename = sanitize_filename(f"{song['artist']} - {song['name']}.mp3")
            file_path = self.download_path / filename
            
            # 如果文件已存在，跳过下载
            if file_path.exists():
                print(f"文件已存在: {filename}")
                return True
                
            # 下载文件
            response = self.request_handler.get(song['download_url'])
            
            # 写入文件
            with open(file_path, 'wb') as f:
                f.write(response.content)
                
            return True
            
        except Exception as e:
            print(f"下载歌曲失败 {song['name']}: {str(e)}")
            return False
            
    def download_songs(self, songs: List[Dict]) -> None:
        """
        并发下载多首歌曲
        """
        print(f"\n开始下载 {len(songs)} 首歌曲...")
        
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            list(tqdm(
                executor.map(self.download_song, songs),
                total=len(songs),
                desc="下载进度"
            ))
            
        print("\n下载完成！文件保存在:", self.download_path)