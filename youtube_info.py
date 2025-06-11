from tqdm import tqdm
from pytubefix import Playlist, YouTube


URL = 'https://www.youtube.com/watch?v=LkaOWVPS7PY'
# PLAYLIST_URL = 'https://www.youtube.com/watch?v=vCVZUMun37U&list=PLk4nzq9lMqGS_0xzQjCkKl_VssLYPWI9f'
PLAYLIST_URL = input("Enter the YouTube playlist URL: ")

def get_info(url: str) -> dict:
    """
    Fetches basic info about a YouTube video.

    Note:
        Returns 1. title, 2. author, 3. description, 4. views, 5. length, 
        6. publish_date, 7. thumbnail_url

    Args:
        url (str): The url of the video.
        
    Returns:
        dict: dictionary containing the video's title, author, description, 
        views, length, publish_date, thumbnail_url
    """
    yt = YouTube(url)
    data = {
        'title': yt.title,
        'author': yt.author,
        'description': yt.description,
        'views': yt.views,
        'length': yt.length,
        'publish_date': yt.publish_date.strftime('%Y-%m-%d') if yt.publish_date else None,
        'thumbnail_url': yt.thumbnail_url
    }
    return data

print(get_info(URL))

def get_playlist_info(pl_url: str) -> list:
    """
    Fetches basic info about a YouTube playlist.
   
    Args:
        pl (Playlist): The YouTube playlist object.
        
    Returns:
        dict: dictionary containing the playlist's videos' title, author, description, 
        views, length, publish_date, thumbnail_url
    """

    print('Fetching info for playlist: {pl_url}')

    pl = Playlist(pl_url)

    all_videos = []

    for video in tqdm(pl.video_urls):
        print('Fetching info for video: {video}')
        all_videos.append(get_info(video))
    all_videos.sort(key=lambda x: x['views'], reverse=True)

    return all_videos

if __name__ == '__main__':
    playlist_info = get_playlist_info(PLAYLIST_URL)
    print('Done')
    print(playlist_info)
