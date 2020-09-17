#coding=utf-8

#农贸系统

from selenium import  webdriver
import time
from selenium.webdriver.common.keys import Keys
import datetime

driver=webdriver.Chrome(executable_path='/Users/ph/Documents/chromedriver')
driver.get('http://118.25.66.69:8080/farmersmarket/login') #预发
#driver.get('http://saas.zhuisuyun.net/farmersmarket/login') #线上
driver.implicitly_wait(5)


#登录系统
def login(count,password): #参数：用户名、密码
    driver.find_element_by_xpath('//*[@id="form1"]/div[1]/input').send_keys(count) #输入账号
    driver.find_element_by_xpath('//*[@id="form1"]/div[2]/input').send_keys(password) #输入密码
    driver.find_element_by_xpath('//*[@id="form1"]/div[3]/div/button').click() #点击登录
    time.sleep(3)

login("ddnm","1qazxsw2")
account_name=u'董达农贸'


#修改企业基本信息
def edit_base_information(shortname,linkman,phone,law_person,address): #参数：企业简称、联系人、联系方式、法人代表、地址
    driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[7]/a/span[1]').click() #点击基础信息管理
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[7]/ul/li[1]/a').click() #点击基本信息管理
    time.sleep(3)

    driver.find_element_by_xpath('//*[@id="entpShortName"]').clear() #清除企业简称里的内容
    driver.find_element_by_xpath('//*[@id="entpShortName"]').send_keys(shortname) #输入新的企业简称
    driver.find_element_by_xpath('//*[@id="contactPerson"]').clear() #清除原来的联系人
    driver.find_element_by_xpath('//*[@id="contactPerson"]').send_keys(linkman) # 输入新的联系人
    driver.find_element_by_xpath('//*[@id="contactDetail"]').clear() #清除原来的联系方式
    driver.find_element_by_xpath('//*[@id="contactDetail"]').send_keys(phone) #输入新的联系方式
    driver.find_element_by_xpath('//*[@id="select2-entpType-container"]').click() #点击选择经营类型选择框
    driver.find_element_by_xpath('//*[@class="select2-results__option"]').click() #选择经营类型
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="select2-entpNature-container"]').click() #点击经营者性质栏
    time.sleep(2)
    driver.find_element_by_xpath('//*[@class="select2-results__option"]').click() #选择经营者性质
    driver.find_element_by_xpath('//*[@id="legalRepresentative"]').clear() #清除原来的法人代表
    driver.find_element_by_xpath('//*[@id="legalRepresentative"]').send_keys(law_person) #输入法人代表
    driver.find_element_by_xpath('//*[@id="baseForm"]/div/div[1]/div[2]/div[3]/div/div/div/div[4]/div/span/button').click()
    #点击地图按钮
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="suggestId"]').send_keys(address) #输入地址
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="tangram-suggestion--TANGRAM__1m-item0"]/i/b').click() #选择匹配出的结果
    driver.find_element_by_xpath('//*[@id="adressButton"]').click() #点击确认
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="datetimepicker1"]/span/span').click()  # 点击备案日期选择框
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[2]/div[3]/table/tbody/tr[2]/td[5]')  # 选择备案日期
    driver.find_element_by_xpath('/html/body/div[2]/div[3]/table/tbody/tr[5]/td[5]').click() #点击保存按钮
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="btnSave"]').click() #点击保存按钮

#edit_base_information(u"信息发展",u"陈先生",'17300000001',u"法人代表",u"天安门")


name="ph" #设置员工姓名
#新增员工 (确认密码输入框未定位到)

def add_staff(name,mobile,post,psw): #参数：姓名、联系方式、岗位、密码
    #driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[7]/a/span[1]').click() #点击基础数据管理
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[7]/ul/li[2]/a').click() #点击员工信息管理
    driver.find_element_by_xpath('//*[@id="btnAdd"]').click() #点击添加
    driver.find_element_by_xpath('//*[@id="fullName"]').send_keys(name) #输入姓名
    driver.find_element_by_xpath('//*[@id="mobilePhone"]').send_keys(mobile) #输入手机号
    driver.find_element_by_xpath('//*[@id="post"]').send_keys(post) #输入岗位

    driver.find_element_by_xpath('//*[@id="employeepwd"]').send_keys(psw) #输入密码
    driver.find_element_by_css_selector('.form-group > #confirmaPssword').send_keys(psw) # 输入确认密码


    driver.find_element_by_xpath('//*[@id="btnSave"]').click() #点击保存按钮
    time.sleep(3)


#add_staff(name,"1212",u"一般文员","1qazxsw2")


#通过姓名搜索员工
def search_staff(name):
    #driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[7]/a/span[1]').click() #点击基础数据管理
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[7]/ul/li[2]/a').click() #点击员工信息管理
    driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(name)  # 搜索框输入姓名
    driver.find_element_by_xpath('//*[@id="btnSearch"]').click()  # 点击搜索
    time.sleep(2)


#search_staff1(name)


#编辑员工信息
def edit_staff(name,post):
    #driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[7]/a/span[1]').click() #点击基础数据管理
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[7]/ul/li[2]/a').click() #点击员工信息管理
    driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(name) #搜索框输入姓名
    driver.find_element_by_xpath('//*[@id="btnSearch"]').click() #点击搜索
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td[7]/button[1]').click() #点击编辑按钮
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="post"]').clear() #清除职位
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="post"]').send_keys(post) #输入新的职位
    driver.find_element_by_xpath('//*[@id="btnSave"]').click()

#edit_staff(name,u"助理")

#删除员工
def delete_staff(name):
    #driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[7]/a/span[1]').click() #点击基础数据管理
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[7]/ul/li[2]/a').click() #点击员工信息管理
    driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(name)
    driver.find_element_by_xpath('//*[@id="btnSearch"]').click()
    time.sleep(3)
    driver.find_element_by_css_selector('tr:nth-child(1) .btn-danger').click()
    time.sleep(2)
    driver.find_element_by_css_selector('.btn-primary').click()

#delete_staff(name)


#菜单收起
def close_menu():
    driver.find_element_by_xpath('/html/body/div/header/nav/a').click()
    time.sleep(3)

#close_menu()

#菜单展开
def open_menu():
    driver.find_element_by_xpath('/html/body/div/header/nav/a').click()
    time.sleep(3)


#查看首页批次数
def get_batch():
    driver.find_element_by_xpath('/html/body/div/header/a/span[2]/span').click() #点击首页logo
    time.sleep(3)
    batch_1=driver.find_element_by_xpath('//*[@id="batch"]/div/div[2]/div[2]/ul/li[1]').text #获取当天批次数
    batch_7=driver.find_element_by_xpath('//*[@id="batch"]/div/div[2]/div[2]/ul/li[2]').text #获取7天内批次数
    batch_30=driver.find_element_by_xpath('//*[@id="batch"]/div/div[2]/div[2]/ul/li[3]').text #获取首页30天批次数
    batch_365=driver.find_element_by_xpath('//*[@id="batch"]/div/div[2]/div[2]/ul/li[4]').text #获取整年内批次数
    batch_total=driver.find_element_by_xpath('//*[@id="batch"]/div/div[2]/div[2]/ul/li[5]').text #获取总批次数
    print batch_1,batch_7,batch_30,batch_365,batch_total


#get_batch()

#查看首页赋码数
def get_coding():
    driver.find_element_by_xpath('/html/body/div/header/a/span[2]/span').click()  # 点击首页logo
    time.sleep(3)
    coding_1=driver.find_element_by_xpath('//*[@id="coding"]/div/div[2]/div[1]/p').text #获取当天赋码数
    coding_7=driver.find_element_by_xpath('//*[@id="coding"]/div/div[2]/div[2]/ul/li[1]').text #获取7天内赋码数
    coding_30=driver.find_element_by_xpath('//*[@id="coding"]/div/div[2]/div[2]/ul/li[2]').text #获取30天内赋码数
    coding_365=driver.find_element_by_xpath('//*[@id="coding"]/div/div[2]/div[2]/ul/li[3]').text #获取整年内赋码数
    coding_total=driver.find_element_by_xpath('//*[@id="coding"]/div/div[2]/div[2]/ul/li[4]').text #获取总赋码数
    print coding_1,coding_7,coding_30,coding_365,coding_total

#get_coding()


#查看首页进货登记次数
def get_egistration():
    driver.find_element_by_xpath('/html/body/div/header/a/span[2]/span').click()  # 点击首页logo
    time.sleep(3)
    egistration_1=driver.find_element_by_xpath('//*[@id="purchaseRegistration"]/div/div[2]/div[2]/ul/li[1]').text
    egistration_7=driver.find_element_by_xpath('//*[@id="purchaseRegistration"]/div/div[2]/div[2]/ul/li[2]').text
    egistration_30=driver.find_element_by_xpath('//*[@id="purchaseRegistration"]/div/div[2]/div[2]/ul/li[3]').text
    egistration_365=driver.find_element_by_xpath('//*[@id="purchaseRegistration"]/div/div[2]/div[2]/ul/li[4]').text
    egistration_total=driver.find_element_by_xpath('//*[@id="purchaseRegistration"]/div/div[2]/div[2]/ul/li[5]').text
    print egistration_1,egistration_7,egistration_30,egistration_365,egistration_total

#get_egistration()

#获取首页产品数
def get_goods_number():
    driver.find_element_by_xpath('/html/body/div/header/a/span[2]/span').click()  # 点击首页logo
    time.sleep(3)
    goods_number_total=driver.find_element_by_xpath('//*[@id="product"]/div/div[2]/div[1]/p').text #获取总产品数
    goods_number_1=driver.find_element_by_xpath('//*[@id="product"]/div/div[2]/div[2]/ul/li[1]').text #获取top1产品数
    goods_number_2=driver.find_element_by_xpath('//*[@id="product"]/div/div[2]/div[2]/ul/li[2]').text #获取top2产品数
    goods_number_3=driver.find_element_by_xpath('//*[@id="product"]/div/div[2]/div[2]/ul/li[3]').text #获取top3产品数
    goods_number_4=driver.find_element_by_xpath('//*[@id="product"]/div/div[2]/div[2]/ul/li[4]').text #获取top4产品数
    goods_number_5=driver.find_element_by_xpath('//*[@id="product"]/div/div[2]/div[2]/ul/li[5]').text #获取top5产品数
    print goods_number_total,goods_number_1,goods_number_2,goods_number_3,goods_number_4,goods_number_5

#get_goods_number()

#获取首页供应商数
def get_supplier():
    driver.find_element_by_xpath('/html/body/div/header/a/span[2]/span').click()  # 点击首页logo
    time.sleep(3)
    supplier_number=driver.find_element_by_xpath('//*[@id="supplier"]/div/div[2]/div/p').text #获取供应商数
    print u"供应商数： "+supplier_number

#get_supplier()

#获取首页中散货数量
def get_bulk_cargo():
    driver.find_element_by_xpath('/html/body/div/header/a/span[2]/span').click()  # 点击首页logo
    time.sleep(3)
    bulk_cargo_number=driver.find_element_by_xpath('//*[@id="batch"]/div/div[2]/div[1]/div/span[1]').text #获取散货数量
    print u"散货数： "+bulk_cargo_number #打印散货数量
    time.sleep(3)

#get_bulk_cargo()

#获取首页中预包装货物数量
def get_prepackaging():
    driver.find_element_by_xpath('/html/body/div/header/a/span[2]/span').click()  # 点击首页logo
    time.sleep(3)
    prepackaging_number=driver.find_element_by_xpath('//*[@id="batch"]/div/div[2]/div[1]/div/span[2]').text #获取预包装数量
    print u"预包装数： "+prepackaging_number #打印预包装数量
    time.sleep(3)
#get_prepackaging()

supplier1=u'供应商00002' #设置供应商名称
#添加供应商
def add_supplier(name,shortname,linkman,phonenumber,bizRegNumber,LawPerson,address):
    #参数：供应商名称、企业简称、联系人、联系方式、供商注册号、法人代表、地址
    driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[7]/a/span[1]').click()  # 点击基础数据管理
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/aside/section/ul/li[7]/ul/li[3]/a").click() #点击供应商管理子菜单
    driver.find_element_by_xpath('//*[@id="btnAdd"]').click()  #点击新增
    driver.find_element_by_xpath('//*[@id="entpName"]').send_keys(name)  #输入企业名称
    driver.find_element_by_xpath('//*[@id="entpShortName"]').send_keys(shortname) #输入简称
    driver.find_element_by_xpath('//*[@id="contactPerson"]').send_keys(linkman) #输入联系人
    driver.find_element_by_xpath('//*[@id="permanent"]').click() #证件有效期选择永久
    driver.find_element_by_xpath('//*[@id="contactDetail"]').send_keys(phonenumber) #输入联系方式
    driver.find_element_by_xpath('//*[@id="bizRegNumber"]').send_keys(bizRegNumber) #输入工商注册号
    driver.find_element_by_xpath('//*[@id="select2-entpType-container"]').click() #点击经营类型下拉框
    time.sleep(2)
  #  s1=Select(driver.find_element_by_id("select2-entpType-results"))
  #  s1.select_by_id('select2-entpType-result-7dcb-101')
    driver.find_element_by_xpath('//*[@class="select2-results__option"]').click() #选择其中一种经营类型
    driver.find_element_by_xpath('//*[@id="legalRepresentative"]').send_keys(LawPerson) #填写法人代表
    driver.find_element_by_xpath('//*[@id="select2-entpNature-container"]').click() #点击经营者性质下拉框
    time.sleep(3)
    driver.find_element_by_xpath('//*[@class="select2-results__option"]').click() #选择一种经营性质
    # driver.find_element_by_xpath('//*[@id="addEntpImg"]').click() #点击添加企业图片
    #time.sleep(3)
    # driver.switch_to.window('${win4943}')
    # driver.find_element_by_xpath('//*[@id="fileUpload"]').click()
    # driver.find_element_by_xpath('//*[@id="formFileUpload"]/div/div[1]/div[3]/div[1]').send_keys('QQ20190919_094243.png')
    # #上传企业图片
    # #点击上传按钮

    driver.find_element_by_xpath('//*[@id="baseForm"]/div/div[1]/div[2]/div[3]/div/div/div/div[4]/div/span/button').click()
    #点击地图
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="suggestId"]').send_keys(address) #输入地址
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="tangram-suggestion--TANGRAM__1m-item0"]/i').click() #选择定位到的地址
    driver.find_element_by_xpath('//*[@id="adressButton"]').click() #点击确认
    time.sleep(3)
    # driver.find_element_by_css_selector('html').send_keys(u'这是一段简介')
    driver.find_element_by_xpath('//*[@id="btnSave"]').click() #点击保存
    #time.sleep(4)


#add_supplier(supplier1,u"供商5",u"彭女士",'17301000000','123445958',u'法人彭女士',u'大渡河')

#编辑供应商
def edit_supplier1(supplier,linkerman1,short_name):
    #driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[7]/a/span[1]').click()  # 点击基础数据管理
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/aside/section/ul/li[7]/ul/li[3]/a").click() #点击供应商管理子菜单
    driver.find_element_by_xpath('//*[@id="searchbox"]').clear()
    driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(supplier) #在搜索中填入要编辑的供应商名称
    driver.find_element_by_xpath('//*[@id="btnSearch"]').click() #点击搜索按钮
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td[6]/button[1]').click() #点击编辑按钮
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="contactPerson"]').clear()  # 清除原来的联系人信息
    driver.find_element_by_xpath('//*[@id="contactPerson"]').send_keys(linkerman1) #填写新的联系人信息
    driver.find_element_by_xpath('//*[@id="entpShortName"]').clear()  # 清除原来的企业简称
    driver.find_element_by_xpath('//*[@id="entpShortName"]').send_keys(short_name) #填写新的企业简称
    driver.find_element_by_xpath('//*[@id="btnSave"]').click() #点击保存按钮
    time.sleep(3)


#edit_supplier(supplier1,'17300023',u"供商3")

#搜索供应商
def search_supplier(supplier):
    #driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[7]/a/span[1]').click()  # 点击基础数据管理
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/aside/section/ul/li[7]/ul/li[3]/a").click() #点击供应商管理子菜单
    driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(supplier)  # 在搜索中填入要编辑的供应商名称
    driver.find_element_by_xpath('//*[@id="btnSearch"]').click()  # 点击搜索按钮
    time.sleep(3)


#search_supplier(supplier1)


#删除供应商
def delete_supplier(supplier):
    #driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[7]/a/span[1]').click()  # 点击基础数据管理
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/aside/section/ul/li[7]/ul/li[3]/a").click() #点击供应商管理子菜单
    driver.find_element_by_xpath('//*[@id="searchbox"]').clear()
    driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(supplier)  # 在搜索中填入要删除的供应商名称
    driver.find_element_by_xpath('//*[@id="btnSearch"]').click()  # 点击搜索按钮
    time.sleep(4)
    driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td[6]/button[2]').click() #点击删除按钮
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/button[2]').click() #点击二次确认按钮
    time.sleep(3)

#delete_supplier(supplier1)
#delete_supplier(u'文档导入的供应商')


#检测管理
reportname=u"检测名字啊"
#新增检测报告
def add_testreport(testname,testnumber,tester):
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[4]/a/span[1]').click() #点击检测管理
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[4]/ul/li/a').click() #点击检测报告管理
    driver.find_element_by_xpath('//*[@id="add"]').click() #点击新增
    driver.find_element_by_xpath('//*[@id="select2-detectionType-container"]').click() #点击检测类型下拉框
    driver.find_element_by_xpath('//*[@class="select2-results__option"]').click() #选择型式检测
    driver.find_element_by_xpath('//*[@id="detectionName"]').send_keys(testname) #输入检测名称
    driver.find_element_by_xpath('//*[@id="detectionNo"]').send_keys(testnumber) #输入检测编号
    time.sleep(3)
    #driver.find_element_by_xpath('//*[@class="select2-results__option select2-results__option--highlighted"]').click()
    #点击选择的检测员
    driver.find_element_by_xpath('//*[@id="select2-agencyId-container"]').click() #点击产品所属企业
    driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u'接口测试')
    driver.find_element_by_xpath('//*[@class="select2-results__option select2-results__option--highlighted"]').click()
    driver.find_element_by_xpath('//*[@id="faropenProSelect"]').click() #点击绑定产品
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="probc5c8c4b-1352-43fa-a45d-b95f45ea2aca"]/a/span').click() #点击添加
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="sure"]').click() #点击选择产品里的保存
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="select2-employeeId-container"]').click()  # 点击检测员下拉框
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(tester)  # 输入要选择的检测员
    driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="submit"]').click()# 点击保存
    time.sleep(3)


#add_testreport(u"检测名字啊",'112121',u'试试看')


#根据检测名称搜索检测报告
def search_testreport2(testname):
    #driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[4]/a/span[1]').click() #点击检测管理
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[4]/ul/li/a').click() #点击检测报告管理
    driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(testname)  # 输入要编辑的检测报告名称
    driver.find_element_by_xpath('//*[@id="btnSearch"]').click()  # 点击搜索

#search_testreport2()


#编辑检测报告
def edit_report(testname):#登记人没显示
    #driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[4]/a/span[1]').click() #点击检测管理
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[4]/ul/li/a').click() #点击检测报告管理
    driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(testname) #输入要编辑的检测报告名称
    driver.find_element_by_xpath('//*[@id="btnSearch"]').click() #点击搜索按钮
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[7]/button[1]').click() #点击编辑按钮
    driver.find_element_by_xpath('//*[@id="detectionNo"]').clear()
    driver.find_element_by_xpath('//*[@id="detectionNo"]').send_keys('1343534232')  # 输入新的检测编号
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="submit"]').click()  # 点击保存
    time.sleep(2)


#edit_report(u"检测名字啊")


#删除检测报告
def delete_report(testname):
    #driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[4]/a/span[1]').click() #点击检测管理
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[4]/ul/li/a').click() #点击检测报告管理
    driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(testname)  # 输入要编辑的检测报告名称
    driver.find_element_by_xpath('//*[@id="btnSearch"]').click() #点击搜索
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[7]/button[2]').click() #点击删除按钮
    time.sleep(2)
    driver.find_element_by_css_selector('.btn-primary').click() #点击二次确认按钮

#delete_report(u"检测名字啊")

#自定义时间搜索检测报告
def search_testreport1(time1,time2):
    #driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[4]/a/span[1]').click() #点击检测管理
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[4]/ul/li/a').click() #点击检测报告管理
    driver.find_element_by_xpath('//*[@id="whole"]/li[2]').click() #点击自定义按钮
    driver.find_element_by_xpath('//*[@id="dateStart"]').send_keys(time1) #输入开始时间
    driver.find_element_by_xpath('//*[@id="dateEnd"]').send_keys(time2) #输入结束时间
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="btnSearch"]').click() #点击搜索

#search_testreport1('2019-08-13','2019-10-13')


#预警信息导出（营业执照过期）
def warning_query1():
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[2]/a/span[1]').click() #点击综合预警
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[2]/ul/li/a').click() #点击预警查询
    time.sleep(3)
    driver.find_element_by_name('btSelectAll').click() #点击全选按钮
    driver.find_element_by_xpath('//*[@id="exportBtn"]').click() #点击导出按钮

#warning_query1()

#预警信息导出（食品经营许可证过期）
def warning_query2():
    #driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[2]/a/span[1]').click() #点击综合预警
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[2]/ul/li/a').click() #点击预警查询
    driver.find_element_by_css_selector('#whole > .category_li:nth-child(3)').click() #选择食品经营许可证
    time.sleep(2)
    driver.find_element_by_name('btSelectAll').click()  #点击全选按钮  # 点击全选按钮
    driver.find_element_by_xpath('//*[@id="exportBtn"]').click()  # 点击导出按钮

#warning_query2()

#预警信息按时间从大到小排序
def orderby_time1():
    #driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[2]/a/span[1]').click() #点击综合预警
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[2]/ul/li/a').click() #点击预警查询
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="tables"]/thead/tr/th[6]/div[1]').click() #点击时间
    time.sleep(2)
    a=driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[6]').text
    b=driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[2]/td[6]').text
    d1 = datetime.datetime.strptime(a, '%Y-%m-%d')
    d2 = datetime.datetime.strptime(b, '%Y-%m-%d')

    if d1>=d2:
        print 'test_gc_orderby_time1 test pass'
    else:
        print 'test_gc_orderby_time1 test fail'

#orderby_time1()


#预警信息按时间从小到大排序
def orderby_time2():
    #driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[2]/a/span[1]').click() #点击综合预警
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[2]/ul/li/a').click() #点击预警查询
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="tables"]/thead/tr/th[6]/div[1]').click() #点击时间
    time.sleep(2)
    a=driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[6]').text
    b=driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[2]/td[6]').text
    d1 = datetime.datetime.strptime(a, '%Y-%m-%d')
    d2 = datetime.datetime.strptime(b, '%Y-%m-%d')

    if d1<=d2:
        print "test_gd_orderby_time2 test pass"
    else:
        print "test_gd_orderby_time2 test fail"

#orderby_time2()


#查看营业执照过期的全部供应商
def warning_view0():
    #driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[2]/a/span[1]').click() #点击综合预警
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[2]/ul/li/a').click() #点击预警查询
    driver.find_element_by_xpath('/html/body/div/div/section[2]/div/div/div/div/div[3]/ul/li[1]').click() #点击全部按钮
    time.sleep(2)

#warning_view0()

#查看营业执照即将在一个月内过期的供应商
def warning_view1():
    #driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[2]/a/span[1]').click() #点击综合预警
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[2]/ul/li/a').click() #点击预警查询
    driver.find_element_by_xpath('/html/body/div/div/section[2]/div/div/div/div/div[3]/ul/li[3]').click() #点击一个月
    time.sleep(2)

#warning_view1()

#查看营业执照即将在两个月内过期的供应商
def warning_view2():
    #driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[2]/a/span[1]').click() #点击综合预警
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[2]/ul/li/a').click() #点击预警查询
    driver.find_element_by_xpath('/html/body/div/div/section[2]/div/div/div/div/div[3]/ul/li[4]').click() #点击两个月
    time.sleep(2)

#warning_view2()

#查看营业执照即将在三个月内过期的供应商
def warning_view3():
    #driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[2]/a/span[1]').click() #点击综合预警
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[2]/ul/li/a').click() #点击预警查询
    driver.find_element_by_xpath('/html/body/div/div/section[2]/div/div/div/div/div[3]/ul/li[5]').click() #点击三个月
    time.sleep(2)

#warning_view3()

#查看食品经营许可证的全部供应商
def warning_view4():
    #driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[2]/a/span[1]').click() #点击综合预警
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[2]/ul/li/a').click() #点击预警查询
    driver.find_element_by_xpath('/html/body/div/div/section[2]/div/div/div/div/div[3]/ul/li[1]').click() #点击全部按钮
    driver.find_element_by_css_selector('#whole > .category_li:nth-child(3)').click()  # 选择食品经营许可证
    time.sleep(2)

#warning_view4()

#查看食品经营许可证即将在一个月内过期的供应商
def warning_view5():
    #driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[2]/a/span[1]').click() #点击综合预警
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[2]/ul/li/a').click() #点击预警查询
    driver.find_element_by_xpath('/html/body/div/div/section[2]/div/div/div/div/div[3]/ul/li[3]').click() #点击一个月
    driver.find_element_by_css_selector('#whole > .category_li:nth-child(3)').click()  # 选择食品经营许可证
    time.sleep(2)

#warning_view5()

#查看食品经营许可证即将在两个月内过期的供应商
def warning_view6():
    #driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[2]/a/span[1]').click() #点击综合预警
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[2]/ul/li/a').click() #点击预警查询
    driver.find_element_by_xpath('/html/body/div/div/section[2]/div/div/div/div/div[3]/ul/li[4]').click() #点击两个月
    driver.find_element_by_css_selector('#whole > .category_li:nth-child(3)').click()  # 选择食品经营许可证
    time.sleep(2)

#warning_view6()

#查看食品经营许可证即将在三个月内过期的供应商
def warning_view7():
    #driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[2]/a/span[1]').click() #点击综合预警
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[2]/ul/li/a').click() #点击预警查询
    driver.find_element_by_xpath('/html/body/div/div/section[2]/div/div/div/div/div[3]/ul/li[5]').click() #点击三个月
    driver.find_element_by_css_selector('#whole > .category_li:nth-child(3)').click()  # 选择食品经营许可证
    time.sleep(2)

#warning_view7()
#通过搜索供应商搜索预警信息
def search_warning():
    #driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[2]/a/span[1]').click() #点击综合预警
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[2]/ul/li/a').click() #点击预警查询

    driver.find_element_by_xpath('//*[@id="searchParam"]').send_keys(u'测试超市企业账号')
    driver.find_element_by_xpath('//*[@id="searchBtn"]').click()

#search_warning()

