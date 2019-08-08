import redis
import json

def diff_data(contents, host):
    # redis에서 캐시를 불러와 업데이트 한 데이터와 비교한다.
    conn = redis.StrictRedis(host=host, port=6379)
    # in 함수로 중복여부를 판단하기 위해서
    # 캐시는 비교 값인 title로 구성된 list를 만든다.
    cache_title = []
    # 메일 발송에 필요한 정보는 dict가 필요함
    new_datas = {}
    # redis에서 마지막에 저장된 캐시를 불러옴
    # 캐시 데이터의 상태가 FAILURE인 경우 오류가 발생하기 때문에
    # celery 캐시 데이터의 갯수를 가지고와서
    # 최근순으로 읽어들인다.
    # 모두 오류이거나 없다면 cache_title은 빈 리스트를 반환한다.
    if conn.keys('celery*'):
        key_length = len(conn.keys('celery*'))
        for i in range(key_length - 1, 0, -1):
            before_cache = json.loads(conn.get(conn.keys('celery*')[i]))
            if before_cache['status'] == 'FAILURE':
                pass
            before_cache = before_cache['result']
            for key in before_cache:
                cache_title.append(before_cache[key]['title'])
    # 캐시 데이터와 업데이트 데이터를 비교한다.
    # return -> dict
    for key in contents:
        if contents[key]['title'] in cache_title:
            pass
        else:
            new_datas[key] = contents[key]
    return new_datas
