from ..models import CrawlingData as CD

def save_db(contents):
    for index in range(2,len(contents)+1):
        CD.objects.create(title=contents['content_' + str(index)]['title'],
                          category=contents['content_' + str(index)]['category'],
                          write_date=contents['content_' + str(index)]['write_date'],
                          detail_link = contents['content_' + str(index)]['detail_link'],
                          prod_image = contents['content_' + str(index)]['prod_image'])
