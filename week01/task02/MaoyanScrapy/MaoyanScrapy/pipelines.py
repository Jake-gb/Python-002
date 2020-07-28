# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pandas as pd

class MaoyanscrapyPipeline(object):
    def process_item(self, item, spider):
        mv_info=[]
        mv_name = item["mv_name"]
        mv_type = item["mv_type"]
        mv_time = item["mv_time"]
        mv_info.append((mv_name, mv_type, mv_time))

        top10=pd.DataFrame(mv_info)
        top10.to_csv("top10.csv",mode='a',encoding="utf-8",header=False,index=False)

        return item
    
    
    
    
