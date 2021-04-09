import pyodbc
import json  
import requests

#Webaccess Headers
headers = {
    'Content-Type' : 'application/json; charset=utf-8; LoginType=view;',
    'Authorization' : 'Basic YWRtaW4' #登入使用者名稱與密碼,需使用Basic 64 解碼轉換
}

#Webaccess登入

url_Log="http://localhost/WaWebService/JSON/Login"
r = requests.get(url_Log, auth=('username','password'))
#print(r.status_code)
#print(r.text.encode('utf8'))

#寫入數值
""" 
setvalue_tagname='Test_00001'
setvalue_tag_on='1'
setvalue_tag_off='0'
url_set_value="http://localhost/WaWebService/Json/SetTagValue/Zimi_Mixxer/"
url_setvalue=url_set_value+'/'+setvalue_tagname+'/'+setvalue_tag_off
r_setvalue = requests.get(url_setvalue, auth=('admin',''))
print(r_setvalue.status_code)
print(r_setvalue.text.encode('utf8'))
 """
""" 
########################混合槽1########################
#磷酸取得數值 QTY1
url_TagValue='http://localhost/WaWebService/Json/GetTagValue/Zimi_Mixxer'
mixxer1_phosphoric = requests.post(url_TagValue, headers = headers, auth=('admin',''), json={"Tags":[{"Name":"Mix_a_phosphoric" }]} )
mixxer1_phosphoric_tag=mixxer1_phosphoric.text.encode('utf8')
mixxer1_phosphoric_json_TagValue=json.loads(mixxer1_phosphoric_tag)
mixxer1_phosphoric_tag1=mixxer1_phosphoric_json_TagValue["Values"]
print(mixxer1_phosphoric_tag1)
mixxer1_phosphoric_clist=mixxer1_phosphoric_tag1
for mixxer1_phosphoric_tag2 in mixxer1_phosphoric_clist:
    print(mixxer1_phosphoric_tag2)
mixxer1_phosphoric_gettag=mixxer1_phosphoric_tag2["Value"]
print('磷酸:',mixxer1_phosphoric_gettag)

#醋酸取得數值 QTY2
mixxer1_acetic = requests.post(url_TagValue, headers = headers, auth=('admin',''), json={"Tags":[{"Name":"Mix_a_acetic" }]} )
mixxer1_acetic_tag=mixxer1_acetic.text.encode('utf8')
mixxer1_acetic_json_TagValue=json.loads(mixxer1_acetic_tag)
mixxer1_acetic_tag1=mixxer1_acetic_json_TagValue["Values"]
print(mixxer1_acetic_tag1)
mixxer1_acetic_clist=mixxer1_acetic_tag1
for mixxer1_acetic_tag2 in mixxer1_acetic_clist:
    print(mixxer1_acetic_tag2)
mixxer1_acetic_gettag=mixxer1_acetic_tag2["Value"]
print('醋酸:',mixxer1_acetic_gettag)

#硝酸取得數值 QTY3
mixxer1_nitric = requests.post(url_TagValue, headers = headers, auth=('admin',''), json={"Tags":[{"Name":"Mix_a_nitric" }]} )
mixxer1_nitric_tag=mixxer1_nitric.text.encode('utf8')
mixxer1_nitric_json_TagValue=json.loads(mixxer1_nitric_tag)
mixxer1_nitric_tag1=mixxer1_nitric_json_TagValue["Values"]
print(mixxer1_nitric_tag1)
mixxer1_nitric_clist=mixxer1_nitric_tag1
for mixxer1_nitric_tag2 in mixxer1_nitric_clist:
    print(mixxer1_nitric_tag2)
mixxer1_nitric_gettag=mixxer1_nitric_tag2["Value"]
print('硝酸:',mixxer1_nitric_gettag)

#Ro水取得數值 QTY4
mixxer1_water = requests.post(url_TagValue, headers = headers, auth=('admin',''), json={"Tags":[{"Name":"Mix_a_water" }]} )
mixxer1_water_tag=mixxer1_water.text.encode('utf8')
mixxer1_water_json_TagValue=json.loads(mixxer1_water_tag)
mixxer1_water_tag1=mixxer1_water_json_TagValue["Values"]
print(mixxer1_water_tag1)
mixxer1_water_clist=mixxer1_water_tag1
for mixxer1_water_tag2 in mixxer1_water_clist:
    print(mixxer1_water_tag2)
mixxer1_water_gettag=mixxer1_water_tag2["Value"]
print('水:',mixxer1_water_gettag)

#a 總重
mixxer1_total = requests.post(url_TagValue, headers = headers, auth=('admin',''), json={"Tags":[{"Name":"Mix_a_comp_weight" }]} )
mixxer1_total_tag=mixxer1_total.text.encode('utf8')
mixxer1_total_json_TagValue=json.loads(mixxer1_total_tag)
mixxer1_total_tag1=mixxer1_total_json_TagValue["Values"]
print(mixxer1_total_tag1)
mixxer1_total_clist=mixxer1_total_tag1
for mixxer1_total_tag2 in mixxer1_total_clist:
    print(mixxer1_total_tag2)
mixxer1_total_gettag=mixxer1_total_tag2["Value"]
print(mixxer1_total_gettag)



#完成時間
mixxer1_time = requests.post(url_TagValue, headers = headers, auth=('admin',''), json={"Tags":[{"Name":"Mix_a_comp_time" }]} )
mixxer1_time_tag=mixxer1_time.text.encode('utf8')
mixxer1_time_json_TagValue=json.loads(mixxer1_time_tag)
mixxer1_time_tag1=mixxer1_time_json_TagValue["Values"]
print(mixxer1_time_tag1)
mixxer1_time_clist=mixxer1_time_tag1
for mixxer1_time_tag2 in mixxer1_time_clist:
    print(mixxer1_time_tag2)
#時間處理
mixxer1_time_gettag_str=str(mixxer1_time_tag2["Value"])
mixxer1_time_gettag=mixxer1_time_gettag_str[0]+mixxer1_time_gettag_str[1]+':'+mixxer1_time_gettag_str[2]+mixxer1_time_gettag_str[4]
print('時間:',mixxer1_time_gettag)


#完成日期 年
mixxer1_year = requests.post(url_TagValue, headers = headers, auth=('admin',''), json={"Tags":[{"Name":"Mix_a_year" }]} )
mixxer1_year_tag=mixxer1_year.text.encode('utf8')
mixxer1_year_json_TagValue=json.loads(mixxer1_year_tag)
mixxer1_year_tag1=mixxer1_year_json_TagValue["Values"]
print(mixxer1_year_tag1)
mixxer1_year_clist=mixxer1_year_tag1
for mixxer1_year_tag2 in mixxer1_year_clist:
    print(mixxer1_year_tag2)
mixxer1_year_gettag=mixxer1_year_tag2["Value"]
#print(mixxer1_year_gettag)

#完成日期 月
mixxer1_month = requests.post(url_TagValue, headers = headers, auth=('admin',''), json={"Tags":[{"Name":"Mix_a_month" }]} )
mixxer1_month_tag=mixxer1_month.text.encode('utf8')
mixxer1_month_json_TagValue=json.loads(mixxer1_month_tag)
mixxer1_month_tag1=mixxer1_month_json_TagValue["Values"]
print(mixxer1_month_tag1)
mixxer1_month_clist=mixxer1_month_tag1
for mixxer1_month_tag2 in mixxer1_month_clist:
    print(mixxer1_month_tag2)
mixxer1_month_gettag=mixxer1_month_tag2["Value"]
#print(mixxer1_month_gettag)

#完成日期 日
mixxer1_day = requests.post(url_TagValue, headers = headers, auth=('admin',''), json={"Tags":[{"Name":"Mix_a_day" }]} )
mixxer1_day_tag=mixxer1_day.text.encode('utf8')
mixxer1_day_json_TagValue=json.loads(mixxer1_day_tag)
mixxer1_day_tag1=mixxer1_day_json_TagValue["Values"]
print(mixxer1_day_tag1)
mixxer1_day_clist=mixxer1_day_tag1
for mixxer1_day_tag2 in mixxer1_day_clist:
    print(mixxer1_day_tag2)
mixxer1_day_gettag=mixxer1_day_tag2["Value"]
#print(mixxer1_day_gettag)
#日期處理
mixxer1_date='20'+str(mixxer1_year_gettag)+'/' + str(mixxer1_month_gettag) + '/' + str(mixxer1_day_gettag)
print('現在日期:',mixxer1_date) """



########################混合槽2########################

#磷酸取得數值 QTY1
url_TagValue='http://localhost/WaWebService/Json/GetTagValue/Zimi_Mixxer'
mixxer2_phosphoric = requests.post(url_TagValue, headers = headers, auth=('admin',''), json={"Tags":[{"Name":"Mix_b_phosphoric"}]} )
mixxer2_phosphoric_tag=mixxer2_phosphoric.text.encode('utf8')
mixxer2_phosphoric_json_TagValue=json.loads(mixxer2_phosphoric_tag)
mixxer2_phosphoric_tag1=mixxer2_phosphoric_json_TagValue["Values"]
print(mixxer2_phosphoric_tag1)
mixxer2_phosphoric_clist=mixxer2_phosphoric_tag1
for mixxer2_phosphoric_tag2 in mixxer2_phosphoric_clist:
    print(mixxer2_phosphoric_tag2)
mixxer2_phosphoric_gettag=mixxer2_phosphoric_tag2["Value"]
print(mixxer2_phosphoric_gettag)

#醋酸取得數值 QTY2
mixxer2_acetic = requests.post(url_TagValue, headers = headers, auth=('admin',''), json={"Tags":[{"Name":"Mix_b_acetic" }]} )
mixxer2_acetic_tag=mixxer2_acetic.text.encode('utf8')
mixxer2_acetic_json_TagValue=json.loads(mixxer2_acetic_tag)
mixxer2_acetic_tag1=mixxer2_acetic_json_TagValue["Values"]
print(mixxer2_acetic_tag1)
mixxer2_acetic_clist=mixxer2_acetic_tag1
for mixxer2_acetic_tag2 in mixxer2_acetic_clist:
    print(mixxer2_acetic_tag2)
mixxer2_acetic_gettag=mixxer2_acetic_tag2["Value"]
print(mixxer2_acetic_gettag)

#硝酸取得數值 QTY3
mixxer2_nitric = requests.post(url_TagValue, headers = headers, auth=('admin',''), json={"Tags":[{"Name":"Mix_b_nitric" }]} )
mixxer2_nitric_tag=mixxer2_nitric.text.encode('utf8')
mixxer2_nitric_json_TagValue=json.loads(mixxer2_nitric_tag)
mixxer2_nitric_tag1=mixxer2_nitric_json_TagValue["Values"]
print(mixxer2_nitric_tag1)
mixxer2_nitric_clist=mixxer2_nitric_tag1
for mixxer2_nitric_tag2 in mixxer2_nitric_clist:
    print(mixxer2_nitric_tag2)
mixxer2_nitric_gettag=mixxer2_nitric_tag2["Value"]
print(mixxer2_nitric_gettag)

#Ro水取得數值 QTY4
mixxer2_water = requests.post(url_TagValue, headers = headers, auth=('admin',''), json={"Tags":[{"Name":"Mix_b_water" }]} )
mixxer2_water_tag=mixxer2_water.text.encode('utf8')
mixxer2_water_json_TagValue=json.loads(mixxer2_water_tag)
mixxer2_water_tag1=mixxer2_water_json_TagValue["Values"]
print(mixxer2_water_tag1)
mixxer2_water_clist=mixxer2_water_tag1
for mixxer2_water_tag2 in mixxer2_water_clist:
    print(mixxer2_water_tag2)
mixxer2_water_gettag=mixxer2_water_tag2["Value"]
print(mixxer2_water_gettag)


#B 總重
mixxer2_total = requests.post(url_TagValue, headers = headers, auth=('admin',''), json={"Tags":[{"Name":"Mix_b_comp_weight" }]} )
mixxer2_total_tag=mixxer2_total.text.encode('utf8')
mixxer2_total_json_TagValue=json.loads(mixxer2_total_tag)
mixxer2_total_tag1=mixxer2_total_json_TagValue["Values"]
print(mixxer2_total_tag1)
mixxer2_total_clist=mixxer2_total_tag1
for mixxer2_total_tag2 in mixxer2_total_clist:
    print(mixxer2_total_tag2)
mixxer2_total_gettag=mixxer2_total_tag2["Value"]
print(mixxer2_total_gettag)


#完成時間
mixxer2_time = requests.post(url_TagValue, headers = headers, auth=('admin',''), json={"Tags":[{"Name":"Mix_b_comp_time" }]} )
mixxer2_time_tag=mixxer2_time.text.encode('utf8')
mixxer2_time_json_TagValue=json.loads(mixxer2_time_tag)
mixxer2_time_tag1=mixxer2_time_json_TagValue["Values"]
print(mixxer2_time_tag1)
mixxer2_time_clist=mixxer2_time_tag1
for mixxer2_time_tag2 in mixxer2_time_clist:
    print(mixxer2_time_tag2)
mixxer2_time_gettag_str=str(mixxer2_time_tag2["Value"])
mixxer2_time_gettag=mixxer2_time_gettag_str[0]+mixxer2_time_gettag_str[1]+':'+mixxer2_time_gettag_str[2]+mixxer2_time_gettag_str[3]
print(mixxer2_time_gettag)


#完成日期 年
mixxer2_year = requests.post(url_TagValue, headers = headers, auth=('admin',''), json={"Tags":[{"Name":"Mix_b_year" }]} )
mixxer2_year_tag=mixxer2_year.text.encode('utf8')
mixxer2_year_json_TagValue=json.loads(mixxer2_year_tag)
mixxer2_year_tag1=mixxer2_year_json_TagValue["Values"]
print(mixxer2_year_tag1)
mixxer2_year_clist=mixxer2_year_tag1
for mixxer2_year_tag2 in mixxer2_year_clist:
    print(mixxer2_year_tag2)
mixxer2_year_gettag=mixxer2_year_tag2["Value"]
print(mixxer2_year_gettag)

#完成日期 月
mixxer2_month = requests.post(url_TagValue, headers = headers, auth=('admin',''), json={"Tags":[{"Name":"Mix_b_month" }]} )
mixxer2_month_tag=mixxer2_month.text.encode('utf8')
mixxer2_month_json_TagValue=json.loads(mixxer2_month_tag)
mixxer2_month_tag1=mixxer2_month_json_TagValue["Values"]
print(mixxer2_month_tag1)
mixxer2_month_clist=mixxer2_month_tag1
for mixxer2_month_tag2 in mixxer2_month_clist:
    print(mixxer2_month_tag2)
mixxer2_month_gettag=mixxer2_month_tag2["Value"]
print(mixxer2_month_gettag)

#完成日期 日
mixxer2_day = requests.post(url_TagValue, headers = headers, auth=('admin',''), json={"Tags":[{"Name":"Mix_b_day" }]} )
mixxer2_day_tag=mixxer2_day.text.encode('utf8')
mixxer2_day_json_TagValue=json.loads(mixxer2_day_tag)
mixxer2_day_tag1=mixxer2_day_json_TagValue["Values"]
print(mixxer2_day_tag1)
mixxer2_day_clist=mixxer2_day_tag1
for mixxer2_day_tag2 in mixxer2_day_clist:
    print(mixxer2_day_tag2)
mixxer2_day_gettag=mixxer2_day_tag2["Value"]
print(mixxer2_day_gettag)

#日期處理
mixxer2_date='20'+str(mixxer2_year_gettag)+'/' + str(mixxer2_month_gettag) + '/' + str(mixxer2_day_gettag)
print('現在日期:',mixxer2_date)



#紀錄編號
mix_record = requests.post(url_TagValue, headers = headers, auth=('admin',''), json={"Tags":[{"Name":"Mix_record_no" }]} )
mix_record_tag=mix_record.text.encode('utf8')
mix_record_json_TagValue=json.loads(mix_record_tag)
mix_record_tag1=mix_record_json_TagValue["Values"]
print(mix_record_tag1)
mix_record_clist=mix_record_tag1
for mix_record_tag2 in mix_record_clist:
    print(mix_record_tag2)
mix_record_gettag=mix_record_tag2["Value"]
print(mix_record_gettag)
mix_record_gettag_srt='PLC20'+str(mix_record_gettag)
print('紀錄編號:',mix_record_gettag_srt)

#生產批號
mix_product = requests.post(url_TagValue, headers = headers, auth=('admin',''), json={"Tags":[{"Name":"Mix_product_no" }]} )
mix_product_tag=mix_product.text.encode('utf8')
mix_product_json_TagValue=json.loads(mix_product_tag)
mix_product_tag1=mix_product_json_TagValue["Values"]
print(mix_product_tag1)
mix_product_clist=mix_product_tag1
for mix_product_tag2 in mix_product_clist:
    print(mix_product_tag2)
mix_product_gettag=mix_product_tag2["Value"]
print('生產批號:',mix_product_gettag)







# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'server IP/address' 
database = 'database name' 
username = 'username' 
password = 'password' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()


#測試連線
""" 
cursor.execute("SELECT @@version;") 
row = cursor.fetchone() 
while row: 
    print(row[0])
    row = cursor.fetchone()
 """


#新增資料庫數據
#PLCF001 紀錄編號
#PLC_DATE 紀錄日期
#PLC_TIME 紀錄時間
#PDTNO 桶槽編號
#PDTQTY 數量
#QTY1=磷酸   QTY2=醋酸  QTY3=硝酸   QTY4=水
mixtanka='混合槽A'
mixtankb='混合槽B'
mix2a=mix_record_gettag_srt
mix2b=mixxer2_date
mix2c=mixxer2_time_gettag
mix2d=mixtankb
mix2e=mix_product_gettag
mix2f=mixxer2_total_gettag
mix2g=mixxer2_phosphoric_gettag
mix2h=mixxer2_acetic_gettag
mix2i=mixxer2_nitric_gettag
mix2j=mixxer2_water_gettag

cursor.execute("insert into PLCF001A(PLCF001,PLC_DATE,PLC_TIME,PDTNO,PBNNO,PDTQTY,QTY1,QTY2,QTY3,QTY4) values (?,?,?,?,?,?,?,?,?,?)",mix2a,mix2b,mix2c,mix2d,mix2e,mix2f,mix2g,mix2h,mix2i,mix2j)
cnxn.commit()


#查詢資料庫標題
""" 
cursor.execute("SELECT * FROM PLCF001A")
field_name = [des[0] for des in cursor.description]
print(field_name)
cnxn.commit() """


#查詢資料庫數據
""" cursor.execute('SELECT * FROM PLCF001A')
for row1 in cursor:
    print(row1)
cnxn.commit() """


#查詢資料庫第一筆數據
"""

cursor.execute('SELECT * FROM PLCF001A'')
row2=cursor.fetchone()
print(row2)
cnxn.commit()
"""

#關閉資料庫連線
cnxn.close()
