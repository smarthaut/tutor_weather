# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
#        with open('abc.txt', 'w') as file:
#            for i in item['city']:
#                file.write('city:' + str(i) + '\n\n')
#        with open('cba.txt','w')as file:
#            for i in item['url']:
#                file.write(str(i) + '\n')


class TutorWeatherPipeline(object):
    def process_item(self, item, spider):
        with open('weather.txt','w+')as file:
            city = item['city']
            url = item['url']
            desc = list(zip(city,url))
            for i in range(len(desc)):
                item = desc[i]
                d = item[0]
                dd = item[1]
                txt = 'city:{0}\t\turl:{1}\n\n'.format(d,dd)
                file.write(txt)
        return item
