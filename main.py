from crawler.artist import ArtistCrawler
from crawler.song import SongCrawler
from downloader.music_dl import MusicDownloader

def main():
    # 获取用户输入的歌手名称
    artist_name = input("请输入歌手名称: ")
    
    # 初始化爬虫
    artist_crawler = ArtistCrawler()
    song_crawler = SongCrawler()
    music_downloader = MusicDownloader()
    
    try:
        # 获取歌手信息
        artist_info = artist_crawler.search_artist(artist_name)
        if not artist_info:
            print("未找到该歌手信息")
            return
        
        # 获取歌曲列表
        songs = song_crawler.get_artist_songs(artist_info['id'])
        if not songs:
            print("未找到该歌手的歌曲")
            return
        
        # 下载歌曲
        music_downloader.download_songs(songs)
        
    except Exception as e:
        print(f"发生错误: {str(e)}")

if __name__ == "__main__":
    main()