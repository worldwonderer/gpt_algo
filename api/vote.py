import redis

from .config import REDIS_SETTINGS


redis_client = redis.Redis(host=REDIS_SETTINGS['host'], port=REDIS_SETTINGS['port'],
                           db=REDIS_SETTINGS['db'], password=REDIS_SETTINGS['password'], decode_responses=True)


def get_likes_count(title_slug):
    return int(redis_client.get(f'likes:{title_slug}') or 0)


def get_dislikes_count(title_slug):
    return int(redis_client.get(f'dislikes:{title_slug}') or 0)


def incr_likes_count(title_slug):
    return int(redis_client.incr(f'likes:{title_slug}'))


def incr_dislikes_count(title_slug):
    return int(redis_client.incr(f'dislikes:{title_slug}'))
