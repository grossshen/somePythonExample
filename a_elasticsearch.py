from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

from a_sina_news import getNewsdetail


class ElasticObj:
    def __init__(self,index_name,index_type,ip="172.26.117.33"):
        self.index_name=index_name
        self.index_type=index_type
        # self.es=Elasticsearch([ip],http_auth=('',''),port=9200)
        self.es=Elasticsearch(ip+":"+"9200")
    # 不怎么重要
    def create_index(self,index_name="test",index_type="test_type"):
        _index_mappings={
            "mappings":{
                self.index_type:{
                    "properties":{
                        "title":"text",
                        "index":True,
                    },
                    "article":{
                        "type":"text",
                        "analyzer": "ik_max_word",
                        "search_analyzer": "ik_smart"
                    }
                }
            }
        }

    # 插入一条默认数据
    def insert_single(self):
        data={
            "title":"title2",
            "article":"article context2"
        }
        self.es.index(index="test",doc_type="test_type",body=data)
    # 插入一条指定数据
    def insert_single(self,list:list):
        data={
            "title":list[0],
            "article":list[1]
        }
        self.es.index(index="test", doc_type="test_type", body=data)
    # 批量插入
    def insert_batch(self,list):
        package=[]
        for i in list:
            package.append(i)
        actions=[
            {
                '_op_type':'index',
                '_index':'test',
                '_type':'test_type',
                '_source':d
            }
            for d in package
        ]
        self.es.bulk(self.es,actions)

esObj=ElasticObj("test","test_type")
esObj.insert_single(getNewsdetail("userless"))