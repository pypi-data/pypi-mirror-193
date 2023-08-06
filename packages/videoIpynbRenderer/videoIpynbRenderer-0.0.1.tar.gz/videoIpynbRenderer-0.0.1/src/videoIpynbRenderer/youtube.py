from IPython import display
from ensure import ensure_annotations

from videoIpynbRenderer.customException import InvalidUrlException
from videoIpynbRenderer.logger import logger

from py_youtube import Data


@ensure_annotations
def render_youtube_videos(URL: str, width: int = 600, height: int = 300) -> str:
    try:
        if not URL:
            InvalidUrlException("URL is None or Invalid")
        data = Data(URL).data()
        if data["publishdate"]:
            time = get_time_info(URL)
            vid_ID = data["id"]
            embed_URL = f"https://www.youtube.com/embed{vid_ID}?start={time}"
            logger.info("embed URL: %s" % embed_URL)
            iframe = f"""
            <iframe width="{width}" height="{height}"
            src="{embed_URL}" title="YouTube video player"
            frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media;
            gyroscope; picture-in-picture" allowfullscreen></iframe>
            """
            display.display(display.HTML(iframe))
            return "success"
        else:
            raise InvalidUrlException()
    except Exception as exp:
        raise exp


@ensure_annotations
def get_time_info(URL: str) -> int:
    def verify_video_id_len(vid_id, __expected_len: int = 11):
        len_vid_id = len(vid_id)
        if len_vid_id != __expected_len:
            raise InvalidUrlException(
                f"Invalid Video ID with length {len_vid_id}. Expected length is {__expected_len}"
            )

    try:
        split_val = URL.split("=")
        if len(split_val) > 3:
            raise InvalidUrlException()
        if "watch" in URL:
            if "&t" in URL:
                vid_id, time = split_val[-2][:-2], int(split_val[-1][:-1])
                verify_video_id_len(vid_id)
                logger.info(f"video starts at: {time}")
                return time
            else:
                vid_id, time = split_val[-1], 0
                verify_video_id_len(vid_id)
                logger.info(f"video starts at: {time}")
                return time
        else:
            if "=" in URL and "?t" in URL:
                vid_id, time = split_val[0].split("/")[-1][:-2], int(split_val[-1])
                verify_video_id_len(vid_id)
                logger.info(f"video starts at: {time}")
                return time
            else:
                vid_id, time = URL.split("/")[-1], 0
                verify_video_id_len(vid_id)
                logger.info(f"video starts at: {time}")
                return time
    except Exception:
        raise InvalidUrlException()
