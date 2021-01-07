import requests


# def download_video():
#     # header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#     url = "http://192.168.0.101"
#     r = requests.get(url, stream=True)
#     with open('test.mp4', "wb") as fp:
#         for chunk in r.iter_content(chunk_size=1024 * 1024):
#             if chunk:
#                 fp.write(chunk)

def download_video(url):
    ret = requests.get(url, stream=True)
    with open("test.mp4", 'rb') as fp:
        for chunk in ret.iter_content(chunk_size=1024 * 1024):
            if chunk:
                fp.write(chunk)


if __name__ == "__main__":
    download_video("http://127.0.0.1")


