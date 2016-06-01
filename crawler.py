# coding=utf-8
import requests
from bs4 import BeautifulSoup
import lxml

from sys import argv
import csv
import uniout
import string
from collections import defaultdict

d = {}


itemarray = []

f = open('test.csv', 'r')
for row in csv.DictReader(f, ["ItemName" , "ItemNumber"]):
    japan = "日本"
    # markup_com = ["價格" , "韓國"]
    markup_com = ["價格" , "週年慶" , "造型" , "台北" , "日本", "新竹","台中" , "醫" ,"韓","國", "澳", "電話","剪髮" ,"工作室"]
    if row["ItemNumber"] is not "1" and row["ItemName"].find(japan) == -1:
      for (index , i) in enumerate(markup_com):
        if row["ItemName"].find(i) != -1:
          break;
        elif row["ItemName"].find(i) == -1 and index == len(markup_com)-1:
          d.update({row["ItemName"] : row["ItemNumber"]})
          

    if int(row["ItemNumber"]) > 8:
    	itemarray.append(row["ItemName"])
  #   	item_name = row["ItemName"]
  #   	item = item_name.split( )
		# print item
f.close()

# print len(itemarray)

doc = defaultdict(list)
# print doc

f = open('makeup.csv', 'r')
for row in csv.DictReader(f, ["User_ID" , "Article_ID" , "Date" , "Time" , "Device" , "Classify" , "Keyword"]):
    for i in itemarray:
   		if i == row["Keyword"][1:]:
   			doc[i].append(row["Article_ID"])



f.close()

item = []
article_array = []


for x in doc:
  article_id = {}
  item.append(x)

  for i in doc[x]:
    t = article_id.setdefault(str(i))
    if t == None:
      article_id[str(i)] = 1
    else:
      article_id[str(i)] = t+1

  article_array.append(article_id)

# print article_array
# print x , doc[x]

# print len(doc)

# for x in d:
# 	print x , d[x]

target = open('crawler.json', 'w')

target.write(' {\n "name" :  "flare",\n "children": [ ')

for f, b in zip(item, article_array):
  target.write('{\n')
  target.write( '"name" : "' + f + '" ,\n' )
  target.write('"children": [\n{"name": "' + f +'",\n"children": [\n')
  for j in b:
    target.write('{"name" : "' + j + '",  "size":'+ str(b[j]) +'},\n')
  target.write(']\n},\n')
  target.write(']\n},\n')
# print len(d)
# 
target.write(']\n}\n')
target.close()



# #送出GET請求到遠端伺服器，伺服器接受請求後回傳<Response [200]>，代表請求成功
# res = requests.get("https://www.urcosme.com/search/product?keyword=捷諾妮絲")

# #經過BeautifulSoup內lxml編輯器解析的結果
# soup = BeautifulSoup(res.text,'lxml')

# #印出網頁內容
# # print soup 

# #使用select選取特定元素
# title = soup.select('.item-name')[0].text
# print title

# content = soup.select('.item-desc')[0].text
# print content

# score = soup.select('.uc-point')[0].text
# print score[:13]

