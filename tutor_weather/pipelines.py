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
            file.write(city[0])
            date = item['date']
            desc = item['dayDesc']
            dayDesc = desc[1::2]
            nightDesc = desc[0::2]
            dayTemp = item['dayTemp']
            weaitem = list(zip(date,dayDesc,nightDesc,dayTemp))
            for i in range(len(weaitem)):
                item = weaitem[i]
                d = item[0]
                dd = item[1]
                nd = item[2]
                ta = item[3].split('/')
                dt = ta[0]
                nt = ta[1]
                txt = '\n\ndate:{0}\t\tday:{1}({2})\t\tnight:{3}({4})\n\n'.format(
                    d,
                    dd,
                    dt,
                    nd,
                    nt
                )
                file.write(txt)
        return item
