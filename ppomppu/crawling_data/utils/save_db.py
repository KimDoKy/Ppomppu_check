from ..models import CrawlingData as CD

def save_db(contents):
    for index in range(2,len(contents)+1):
        obj, obj_bool = CD.objects.get_or_create(title=contents['content_' + str(index)]['title'],
                          category=contents['content_' + str(index)]['category'],
                          write_date=contents['content_' + str(index)]['write_date'],
                          detail_link = contents['content_' + str(index)]['detail_link'],
                          prod_image = contents['content_' + str(index)]['prod_image'])
        # 새로운 게시물인지 DB에 기록
        if obj_bool:
            obj.status = True
            obj.save()
        elif obj_bool == False:
            obj.status = False
            obj.save()
