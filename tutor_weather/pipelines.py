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
        with open('weather.txt','a')as file:
            city = item['city']
            date = item['date']
            desc = item['dayDesc']
            dayDesc = desc[1::2]
            nightDesc = desc[0::2]
            dayTemp = item['dayTemp'][0]
            dayTemp = dayTemp.split('/')
            dt = dayTemp[0]
            nt = dayTemp[1]
            txt = 'city:{0}\n\ndate:{1}\n\nday:{2}({3})\t\tnight:{4}({5})\n\n'.format(city[0],date[0],dayDesc[0],
                dt,nightDesc[0],nt)
            file.write(txt)
        return item
