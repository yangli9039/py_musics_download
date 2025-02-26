import requests
from typing import Dict, Any

class RequestHandler:
    @staticmethod
    def get(url: str, params: Dict[str, Any] = None, headers: Dict[str, Any] = None) -> requests.Response:
        default_headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
        }
        
        if headers:
            default_headers.update(headers)
            
        response = requests.get(url, params=params, headers=default_headers)
        response.raise_for_status()
        return response

def sanitize_filename(filename: str) -> str:
    """清理文件名，移除非法字符"""
    return "".join([c for c in filename if c.isalnum() or c in (' ', '-', '_')]).strip()