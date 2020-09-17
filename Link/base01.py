#coding=utf-8

from selenium import  webdriver
import time
from selenium.webdriver.common.keys import Keys
import os
from selenium.webdriver.common.action_chains import ActionChains


driver=webdriver.Chrome(executable_path=os.path.abspath('../file/chromedriver'))


supermarket={'url':'http://118.25.66.69:8080/supermarket/login','account':'cccs','password':'1qazxsw2'}  #超市系统
store={'url':'http://118.25.66.69:8080/store/login','account':'ccsc','password':'1qazxsw2'} #商超系统
planting={'url':'http://118.25.66.69:8080/planting/login','account':'cczz','password':'1qazxsw2'}  #种植系统
machining={'url':'http://118.25.66.69:8080/machining/login','account':'ccjg','password':'1qazxsw2'}#加工系统
farmersmarket={'url':'http://118.25.66.69:8080/farmersmarket/login','account':'ddnm','password':'1qazxsw2'}#农贸系统
wholesalemarket={'url':'http://118.25.66.69:8080/wholesalemarket/login','account':'ccpf','password':'1qazxsw2'}#批发系统
grouppurchasing={'url':'http://118.25.66.69:8080/grouppurchasing/login','account':'cctt','password':'1qazxsw2'}#团体系统

sku='sku00000'
goods_name='000'
supplier=u'种植系统测试0612'
supplier1=u'商超门店测试企业'
sku1='sku00001'
goods_name1=u'加工品001'
sku2='sku00002'


#登录系统
def login(system): #参数：url，用户名、密码
    driver.get(system["url"]) #输入登录系统的url
    driver.find_element_by_xpath('//*[@id="form1"]/div[1]/input').send_keys(system["account"]) #输入账号
    driver.find_element_by_xpath('//*[@id="form1"]/div[2]/input').send_keys(system['password']) #输入密码
    driver.find_element_by_xpath('//*[@id="form1"]/div[3]/div/button').click() #点击登录
    time.sleep(3)

#login(planting)


#种植新增产品

def add_goods_planting(sku,name,brand,code,entname,shelfLifeDay,price):
    #参数：sku、品名、品类、品牌、产品编码、保质期、供应商、生产企业名称、最佳口感期，单价
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[6]/a/span[1]').click()#点击产品管理
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[6]/ul/li/a').click() #点击产品管理子菜单
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="addProduct"]').click() #点击新增
    driver.find_element_by_xpath('//*[@id="productNo"]').send_keys(sku) #输入产品sku
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="productName"]').send_keys(name) #输入品名z
    driver.find_element_by_xpath('//*[@id="selectInput"]/input[1]').click() #点击品类下拉框
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="choice"]/li[1]/span').click() #选择蔬菜
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="01231017"]').click() #扁豆种子
    driver.find_element_by_xpath('//*[@id="productBrand"]').send_keys(brand) #输入品牌
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="productBrandCode"]').send_keys(code) # 输入品牌编码
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="entpName"]').send_keys(entname) #输入生产企业名称
    driver.find_element_by_xpath('//*[@id="shelfLifeDay"]').send_keys(shelfLifeDay) #输入最佳口感期
    driver.find_element_by_xpath('//*[@id="productPrice"]').send_keys(price) #输入价格
    driver.find_element_by_xpath('//*[@id="Submit"]').click() #点击保存
    time.sleep(4)

#add_goods_planting(sku,goods_name,u"大品牌",'1823849',u"企业名称","180",'23')

#种植采收
def recovery():
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[3]/a/span[1]').click()#点击采收管理
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="home"]/a').click() #点击采收管理子菜单
    driver.find_element_by_xpath('//*[@id="add_new"]').click() #点击新增
    driver.find_element_by_xpath('/html/body/div[1]/div/section[2]/div/div/div[1]/div[2]/div/div[1]/button').click()
    #点击选择产品
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="product_list"]/li[1]/div[1]').click() #选择刚添加的产品
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="product_list"]/li[1]/div[2]/input').send_keys('2000') #输入采收数量
    driver.find_element_by_xpath('//*[@id="sure"]').click()  #点击保存按钮
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="saveFrom"]').click()  #保存
    time.sleep(3)

#recovery()

#种植添加销售记录
def add_SalesRecord_planting(name):
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[4]/a/span[1]').click()  #点击销售记录
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[4]/ul/li/a').click()  # 点击销售记录子菜单
    driver.find_element_by_xpath('//*[@id="add_new"]').click() #点击新增
    driver.find_element_by_xpath('//*[@id="openProSelect"]').click() #点击"批次出库"按钮
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="keyWord"]').send_keys(name) #输入入库的产品
    time.sleep(2)
    driver.find_element_by_partial_link_text(name).click() #选择该产品
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="sure"]').click() #点击确认按钮
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="select2-employeeId-container"]').click() #点击选择登记人下拉框
    driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER) #点击电脑enter建
    driver.find_element_by_xpath('//*[@id="submit"]').click() #点击保存按钮
    time.sleep(3)
    code = driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[2]').text  # 获取出库单号


#add_SalesRecord_planting('sku00000')

#种植 删除与产品相关的批次
def delete_batch_planting(sku):
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[3]/a/span[1]').click()#点击采收管理
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="home"]/a').click() #点击采收管理子菜单
    driver.find_element_by_xpath('//*[@id="searchParam"]').send_keys(sku)  #搜索框输入sku
    driver.find_element_by_xpath('//*[@id="searchBtn"]').click()  #点击搜索
    time.sleep(4)
    driver.find_element_by_xpath('//*[@id="tables"]/thead/tr/th[1]/div[1]/input').click() #点击全选按钮
    driver.find_element_by_xpath('//*[@id="delete"]').click() #点击删除按钮

#delete_recovery(sku)


#种植 删除产品
def delete_goods_planting(sku):
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[6]/a/span[1]').click()#点击产品管理
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[6]/ul/li/a').click() #点击产品管理子菜单
    driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(sku)  #搜索框填入产品sku
    driver.find_element_by_xpath('//*[@id="btnSearch"]').click() #点击搜索按钮
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="del"]').click() #点击删除按钮
    time.sleep(2)
    driver.find_element_by_css_selector('.modal-footer:nth-child(2) > .btn-primary').click()  # 点击二次确认按钮

#delete_goods_planting(sku)


# 超市 添加进货登记
def stock_registration_supermarket(code): #参数：出库单号
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[4]/a/span[1]').click() #点击进货登记
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[4]/ul/li/a').click() #点击进货登记子菜单
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div/section[2]/div/div/div/div/div[2]/div/button[1]').click()
    time.sleep(3)
    #点击扫码登记
    driver.find_element_by_xpath('//*[@id="scanOutstockNo"]').send_keys(code) #输入种植系统出库单
    driver.find_element_by_xpath('//*[@id="sure"]').click() #点击保存按钮
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="baseForm"]/div/div/div/div[2]/div/div[2]/div/div/span/span[1]/span').click()  # 点击登记人下拉选择框
    driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER) #点击电脑enter建
    driver.find_element_by_xpath('//*[@id="submit"]').click()  # 点击保存
    time.sleep(3)


#stock_registration_supermarket('F3102219U1911000018')


#超市系统 查看产品管理列表是否添加了该产品
def check_goods_supermarket(goods):
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[7]/a/span[1]').click()  # 点击产品管理
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[7]/ul/li/a').click()  # 点击产品管理子菜单
    driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(sku) #输入要编辑商品的sku
    driver.find_element_by_xpath('//*[@id="btnSearch"]').click() #点击搜索按钮
    time.sleep(3)

#check_goods_supermarket(goods_name)

#超市系统查看是否添加了供应商

def check_supplier_supermarket(supplier):
    driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[8]/a/span[1]').click()  # 点击供应商管理
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/div/aside/section/ul/li[8]/ul/li/a").click()  # 点击供应商管理子菜单
    driver.find_element_by_xpath('//*[@id="searchbox"]').clear()
    driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(supplier) #在搜索中填入要编辑的供应商名称
    driver.find_element_by_xpath('//*[@id="btnSearch"]').click() #点击搜索按钮
    time.sleep(3)

#check_supplier_supermarket(supplier)

#超市查看批次信息是否正确
def check_batch_supermarket(sku):
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[5]/a/span[1]').click() #点击批次管理
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[5]/ul/li/a').click() #点击批次管理子菜单
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="searchParam"]').send_keys(sku) #输入要搜索的批次产品的sku
    driver.find_element_by_xpath('//*[@id="searchBtn"]').click()#点击搜索按钮
    time.sleep(3)

#check_batch_supermarket(sku)

#查看超市H5信息
def preview_H5_supermarket(sku):
    #driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[5]/a/span[1]').click() #点击批次管理
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[5]/ul/li/a').click() #点击批次管理子菜单
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="searchParam"]').send_keys(sku) #输入要搜索的批次产品的sku
    driver.find_element_by_xpath('//*[@id="searchBtn"]').click()#点击搜索按钮
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[10]/button[1]').click()  # 点击预览二维码按钮
    time.sleep(3)
    text = driver.find_element_by_xpath('//*[@id="qrcode"]').get_attribute("value")  # 获取批次链接
    time.sleep(240)
    driver.get(text)
    time.sleep(5)



#preview_H5(sku)



#超市系统产品出库
def add_SalesRecord_supermarket(goods,tester):
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[3]/a/span[1]').click()  #点击销售记录
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[3]/ul/li/a').click()  # 点击销售记录子菜单
    driver.find_element_by_xpath('//*[@id="add_new"]').click() #点击新增
    driver.find_element_by_xpath('//*[@id="openProSelect"]').click() #点击"批次出库"按钮
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="keyWord"]').send_keys(goods)
    time.sleep(3)
    driver.find_element_by_partial_link_text(goods).click()  # 选择该产品
    driver.find_element_by_xpath('//*[@id="sure"]').click() #点击确认按钮
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="select2-employeeId-container"]').click() #点击选择登记人下拉框
    driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER) #点击电脑enter建
    driver.find_element_by_xpath('//*[@id="submit"]').click() #点击保存按钮
    time.sleep(3)

#add_SalesRecord_supermarket(sku,'test')

#超市系统 删除进货登记
def delete_registration_supermarket(sku): #参数：供应商
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[4]/a/span[1]').click() #点击进货登记
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[4]/ul/li/a').click() #点击进货登记子菜单
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(sku) #输入sku
    driver.find_element_by_xpath('//*[@id="search"]').click()  #点击搜索
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td[7]/button[2]').click()  #点击删除
    time.sleep(2)
    driver.find_element_by_css_selector('.modal-footer:nth-child(2) > .btn:nth-child(2)').click()
    time.sleep(2)


#delete_registration_supermarket(sku)


#超市系统 删除产品
def delete_goods_supermarket():
    check_goods_supermarket(goods_name)
    driver.find_element_by_xpath('//*[@id="del"]').click() #点击删除按钮
    time.sleep(2)
    driver.find_element_by_css_selector('.modal-footer:nth-child(2) > .btn-primary').click()
    time.sleep(3)

#delete_goods_supermarket()



#超市系统 删除供应商

def delete_supplier_supermarket():
    check_supplier_supermarket(supplier1) #调用查看超市系统添加供应商
    driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td[6]/button[2]').click() #点击删除按钮
    time.sleep(2)
    driver.find_element_by_css_selector('.btn-primary').click() #二次确认
    time.sleep(2)

#delete_supplier_supermarket()

#商超门店添加产品
def add_goods_store(sku,name,supplier):
    #参数：sku、品名、供应商、
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[7]/a/span[1]').click()#点击产品管理
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[7]/ul/li/a').click() #点击产品管理子菜单
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="addProduct"]').click() #点击新增
    driver.find_element_by_xpath('//*[@id="productNo"]').send_keys(sku) #输入产品sku
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="productName"]').send_keys(name) #输入品名
    driver.find_element_by_xpath('//*[@id="selectInput"]/input[1]').click()  # 点击品类下拉框
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="choice"]/li[1]/span').click() #选择蔬菜
    time.sleep(2)
    driver.find_element_by_xpath("//dd[@id='01231017']").click() #选择佛手瓜

    driver.find_element_by_xpath('//*[@id="openSupplierSelect"]').click()#点击新增供应商
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="keyWord"]').send_keys(supplier) #输入要选择的供应商
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="suppliercbee240b-f268-426f-af86-458fe5d92710"]').click() #添加所选择的供应商
    driver.find_element_by_xpath('//*[@id="sure"]').click() #点击保存
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="Submit"]').click() #点击保存
    time.sleep(4)

#add_goods(sku2,u'大西瓜',u"供应商03")


#商超添加进货登记（扫码登记）
def stock_registration_store(code): #参数：上个系统的出库单号
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[4]/a/span[1]').click() #点击进货登记
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[4]/ul/li/a').click() #点击进货登记子菜单
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div/section[2]/div/div/div/div/div[2]/div/button[1]').click()
    time.sleep(3)
    # 点击扫码登记
    driver.find_element_by_xpath('//*[@id="scanOutstockNo"]').send_keys(code)  # 输入种植系统出库单
    driver.find_element_by_xpath('//*[@id="sure"]').click()  # 点击保存按钮
    time.sleep(3)
    driver.find_element_by_xpath(
        '//*[@id="baseForm"]/div/div/div/div[2]/div/div[2]/div/div/span/span[1]/span').click()  # 点击登记人下拉选择框
    driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)  # 点击电脑enter建
    driver.find_element_by_xpath('//*[@id="submit"]').click()  # 点击保存
    time.sleep(3)

#stock_registration_store('F3115714612U1910000036')


#商超门店添加进货登记（手动登记）

def stock_registration_store1(): #参数：供应商、登记人
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[4]/a/span[1]').click() #点击进货登记
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[4]/ul/li/a').click() #点击进货登记子菜单
    driver.find_element_by_xpath('//*[@id="add_new"]').click() #点击手动登记
    time.sleep(3)
    try:
        driver.find_element_by_xpath('//*[@id="konwit"]').click()
    except:
        pass
    driver.find_element_by_xpath('//*[@id="select2-supplierEntpId-container"]').click() #点击供应商下拉框
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u'供应商03') #输入要选择的供应商
    driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="select2-employeeId-container"]').click() #点击登记人下拉选择框
    driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER) #输入登记人

    driver.find_element_by_xpath('//*[@id="openProSelect"]').click()  #点击选择产品
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="addAllProduct"]').click()  #点击全部添加
    driver.find_element_by_xpath('//*[@id="sure"]').click() #点击选择产品中的保存按钮
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="submit"]').click() #点击保存
    time.sleep(3)


#stock_registration_store1()


#商超门店  查看产品管理列表是否添加该产品
def check_goods_store(sku):
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[7]/a/span[1]').click()  # 点击产品管理
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[7]/ul/li/a').click()  # 点击产品管理子菜单
    driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(sku) #输入要编辑商品的sku
    driver.find_element_by_xpath('//*[@id="btnSearch"]').click() #点击搜索按钮
    time.sleep(3)

#check_goods_store(sku)

#商超门店 查看是否添加了供应商
def check_supplier_sotre(supplier):
    driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[8]/a/span[1]').click()  # 点击供应商管理
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/aside/section/ul/li[8]/ul/li/a").click()  # 点击供应商管理子菜单
    driver.find_element_by_xpath('//*[@id="searchbox"]').clear()
    driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(supplier) #在搜索中填入要编辑的供应商名称
    driver.find_element_by_xpath('//*[@id="btnSearch"]').click() #点击搜索按钮
    time.sleep(3)

#check_supplier_sotre(supplier)



#商超门店 查看批次信息是否正确
def check_batch_sotre(sku):
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[5]/a/span[1]').click()  # 点击批次管理
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[5]/ul/li/a').click()  # 点击批次管理子菜单
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="searchParam"]').send_keys(sku) #输入sku
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="searchBtn"]').click()  #点击搜索
    time.sleep(3)

#check_batch_sotre(sku)


#商超门店添加销售记录（出库）
def add_SalesRecord_store(goods):
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[3]/a/span[1]').click()  # 点击销售记录
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[3]/ul/li/a').click()  # 点击销售记录子菜单
    driver.find_element_by_xpath('//*[@id="add_new"]').click() #点击新增
    driver.find_element_by_xpath('//*[@id="openProSelect"]').click() #点击"批次出库"按钮
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="keyWord"]').send_keys(goods)
    time.sleep(2)
    driver.find_element_by_partial_link_text(goods).click() #选择该产品
    driver.find_element_by_xpath('//*[@id="sure"]').click() #点击确认按钮
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="select2-employeeId-container"]').click() #点击选择登记人下拉框
    driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER) #点击电脑enter建
    driver.find_element_by_xpath('//*[@id="submit"]').click() #点击保存按钮
    time.sleep(3)

#add_SalesRecord_store(sku)


#商超删除进货登记
def delete_stock_store(sku):
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[4]/a/span[1]').click()  # 点击进货登记
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[4]/ul/li/a').click()  # 点击进货登记子菜单
    driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(sku)
    driver.find_element_by_xpath('//*[@id="search"]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[7]/button[2]').click() #点击删除按钮
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/button[2]').click() #点击二次确认

#delete_stock_store(sku)

#商超删除产品
def delete_goods_store(sku):
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[7]/a/span[1]').click()  # 点击产品管理
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[7]/ul/li/a').click()  # 点击产品管理子菜单
    driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(sku)  # 输入要编辑商品的sku
    driver.find_element_by_xpath('//*[@id="btnSearch"]').click()  # 点击搜索按钮
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="del"]').click() #点击删除按钮
    time.sleep(3)
    driver.find_element_by_css_selector('.modal-footer:nth-child(2) > .btn-primary').click() #二次确认
    time.sleep(3)

#delete_goods_store('sku')

#删除商超供应商
def delete_supplier_store(supplier):
    driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[8]/a/span[1]').click()  # 点击供应商管理
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/aside/section/ul/li[8]/ul/li/a").click()  # 点击供应商管理子菜单
    driver.find_element_by_xpath('//*[@id="searchbox"]').clear()
    driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(supplier)  # 在搜索中填入要删除的供应商名称
    driver.find_element_by_xpath('//*[@id="btnSearch"]').click()  # 点击搜索按钮
    time.sleep(4)
    driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td[7]/button[2]').click() #点击删除按钮
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/button[2]').click() #点击二次确认按钮
    time.sleep(3)

#delete_supplier_store(supplier)

#加工系统进货登记
def stock_registration_machining(code):
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[5]/a/span[1]').click() #点击进货登记
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[5]/ul/li/a').click() #点击进货登记子菜单
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div/section[2]/div/div/div/div/div[2]/div/button[1]').click()
    time.sleep(3)
    #点击扫码登记
    driver.find_element_by_xpath('//*[@id="scanOutstockNo"]').send_keys(code) #输入种植系统出库单
    driver.find_element_by_xpath('//*[@id="sure"]').click() #点击保存按钮
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="baseForm"]/div/div/div/div[2]/div/div[2]/div/div/span/span[1]/span').click()  # 点击登记人下拉选择框
    driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER) #点击电脑enter建
    driver.find_element_by_xpath('//*[@id="submit"]').click()  # 点击保存
    time.sleep(3)

#stock_registration_machining('F3102894U1911000003')

#加工系统 检测原辅料管理产品是否添加
def check_goods_machining(sku):
    driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[8]/a/span[1]').click()  # 点击产品管理
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[8]/ul/li[1]/a').click()  # 点击原辅料管理子菜单
    driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(sku)  #在搜索框输入需要查询的sku
    driver.find_element_by_xpath('//*[@id="btnSearch"]').click()  #点击搜索按钮
    time.sleep(3)

#check_goods_machining(sku)

#加工系统 检测供应商是否添加
def check_supplier_machining(supplier):
    driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[9]/a/span[1]').click()  # 点击供应商管理
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/div/aside/section/ul/li[9]/ul/li/a").click()  # 点击供应商管理子菜单
    # driver.find_element_by_xpath('//*[@id="searchbox"]').clear()
    driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(supplier) #在搜索中填入要编辑的供应商名称
    driver.find_element_by_xpath('//*[@id="btnSearch"]').click() #点击搜索按钮
    time.sleep(3)

#check_supplier_machining(supplier)

#加工查看批次信息是否正确
def check_batch_machining(sku):
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[7]/a/span[1]').click() #点击批次管理
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[7]/ul/li/a').click() #点击产品批次管理子菜单
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="searchParam"]').send_keys(sku) #输入要搜索的批次产品的sku
    driver.find_element_by_xpath('//*[@id="searchBtn"]').click()#点击搜索按钮
    time.sleep(3)

#check_batch_machining(sku)

#加工系统 新增加工品
def add_machining_goods(sku,name):
    driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[8]/a/span[1]').click()  # 点击产品管理
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[8]/ul/li[2]/a').click()  # 点击加工品管理子菜单
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="addProduct"]').click()  # 点击新增
    driver.find_element_by_xpath('//*[@id="productNo"]').send_keys(sku)  # 输入产品sku
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="productName"]').send_keys(name)  # 输入品名
    driver.find_element_by_xpath('//*[@id="selectInput"]/input[1]').click()  # 点击品类下拉框
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="select1"]').send_keys(u'扁豆种子')
    driver.find_element_by_xpath('//*[@id="01231017"]').click()
    driver.find_element_by_xpath('//*[@id="Submit"]').click()  # 点击保存
    time.sleep(3)


#add_machining_goods(sku1,goods_name1)


#加工系统加工品添加到bom管理
def add_bom_machining(sku1,sku):
    driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[4]/a/span[1]').click()  # 点击加工管理
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[4]/ul/li[1]/a').click()  # 点击bom管理子菜单
    driver.find_element_by_xpath('//*[@id="add"]').click() #点击新增
    driver.find_element_by_xpath('//*[@id="select2-baseProduct-container"]').click() #点击产品名称
    driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(sku1) #输入需要选择的加工品的sku
    driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="openProSelect"]').click() #bom表点击选择产品
    handles = driver.window_handles
    for handle in handles:
        if handle != driver.current_window_handle:
            driver.switch_to.window(handle)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="keyWord"]').send_keys(sku) #输入要选择的原辅料
    driver.find_element_by_xpath('//*[@id="prob053ee11-eebd-40e3-9fd9-d0f9c6f03120"]/a').click() #点击添加
    driver.find_element_by_xpath('//*[@id="sure"]').click() #点击保存
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="submit"]').click() #提交
    time.sleep(2)

#add_bom_machining(sku1,sku)

#加工系统加工品入库
def add_batch_machining(sku1):
    #driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[4]/a/span[1]').click()  # 点击加工管理
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[4]/ul/li[2]/a').click()  # 点击加工批次管理子菜单
    driver.find_element_by_xpath('//*[@id="add_new"]').click() #点击新增
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="select2-baseProduct-container"]').click() #点击请选择
    driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(sku1) #输入需要选择的加工品sku
    driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="productionVolume"]').send_keys('322') #输入数量
    driver.find_element_by_xpath('//*[@id="submit"]').click() #点击保存
    time.sleep(2)


#add_batch_machining(sku1)

#加工添加销售记录

def add_SalesRecord_machining(sku):
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[3]/a/span[1]').click()  #点击销售记录
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[3]/ul/li/a').click()  # 点击销售记录子菜单
    driver.find_element_by_xpath('//*[@id="add_new"]').click() #点击新增
    driver.find_element_by_xpath('//*[@id="openProSelect"]').click() #点击"批次出库"按钮
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="keyWord"]').send_keys(sku) #输入入库的产品
    time.sleep(2)
    driver.find_element_by_partial_link_text(sku).click()  # 选择该产品
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="sure"]').click() #点击确认按钮
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="select2-employeeId-container"]').click() #点击选择登记人下拉框
    driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER) #点击电脑enter建
    driver.find_element_by_xpath('//*[@id="submit"]').click() #点击保存按钮
    time.sleep(3)
    code = driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[2]').text  # 获取出库单号
    print code
    time.sleep(2)


#add_SalesRecord_machining(sku1)


#加工系统查看H5信息

def preview_H5_machining(sku):
    driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[8]/a/span[1]').click() #点击产品管理
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[8]/ul/li[2]/a').click() #点击加工品管理
    driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(sku) #在输入框输入要查询的产品的sku
    driver.find_element_by_xpath('//*[@id="btnSearch"]').click() #点击搜索
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[9]/button[1]').click()  # 点击预览二维码按钮
    time.sleep(3)
    text = driver.find_element_by_xpath('//*[@id="qrcode"]').get_attribute("value")  # 获取批次链接
    time.sleep(240)
    driver.get(text)
    time.sleep(5)



#preview_H5_machining(sku1)


#农贸系统 扫码入库
def stock_registration_farmersmarket(code): #参数：出库单号
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[3]/a/span[1]').click() #点击进货登记
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[3]/ul/li/a/i').click() #点击进货登记子菜单
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div/section[2]/div/div/div/div/div[2]/div/button[1]').click()
    time.sleep(3)
    #点击扫码登记
    driver.find_element_by_xpath('//*[@id="scanOutstockNo"]').send_keys(code) #输入种植系统出库单
    driver.find_element_by_xpath('//*[@id="sure"]').click() #点击保存按钮
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="baseForm"]/div/div/div/div[2]/div/div[2]/div/div/span/span[1]/span').click()  # 点击经营户下拉选择框
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u'奥拓')  #输入经营户
    driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER) #点击电脑enter建
    driver.find_element_by_xpath('//*[@id="baseForm"]/div/div/div/div[2]/div/div[2]/div[2]/div/span/span[1]/span').click() #点击登记人下拉选择框
    driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER) #点击电脑enter建

    driver.find_element_by_xpath('//*[@id="submit"]').click()  # 点击保存
    time.sleep(3)



#stock_registration_farmersmarket('F3102894U1912000003')

#删除bom管理里该产品
def delete_bom_machining(sku1):
    driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[4]/a/span[1]').click()  # 点击加工管理
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[4]/ul/li[1]/a').click()  # 点击bom管理子菜单
    driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(sku1) #搜索框输入该产品sku
    driver.find_element_by_xpath('//*[@id="btnSearch"]').click() #点击搜索
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[7]/button[2]').click() #点击删除按钮
    time.sleep(2)
    driver.find_element_by_css_selector('.btn-primary').click() #点击二次确认按钮

#delete_bom_machining(sku1)

#批发系统扫码入库
def stock_registration_wholesalemarket(code): #参数：出库单号
    driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[3]/a/span[1]').click() #点击进货登记
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[3]/ul/li/a/i').click() #点击进货登记子菜单
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div/section[2]/div/div/div/div/div[2]/div/button[1]').click()
    time.sleep(3)
    #点击扫码登记
    driver.find_element_by_xpath('//*[@id="scanOutstockNo"]').send_keys(code) #输入商超门店出库单
    driver.find_element_by_xpath('//*[@id="sure"]').click() #点击保存按钮
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="baseForm"]/div/div/div/div[2]/div/div[2]/div/div/span/span[1]/span').click()  # 点击经营户下拉选择框
    driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u'梦梦批发') #输入经营户
    driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER) #点击电脑enter键
    driver.find_element_by_xpath('//*[@id="baseForm"]/div/div/div/div[2]/div/div[2]/div[2]/div/span/span[1]/span').click() #点击登记人下拉选择框
    driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER) #点击电脑enter键
    driver.find_element_by_xpath('//*[@id="submit"]').click()  # 点击保存
    time.sleep(3)

#stock_registration_wholesalemarket('F3116227195U1911000004')

#批发系统添加销售记录（出库）
def add_SalesRecord_wholesalemarket(goods):
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[4]/a').click()  # 点击销售记录
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[4]/ul/li/a').click()  # 点击销售记录子菜单
    driver.find_element_by_xpath('//*[@id="add_new"]').click() #点击新增
    driver.find_element_by_xpath('//*[@id="select2-agencyId-container"]').click() #点击经营户选择框
    driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u'梦梦批发') #输入要选择的经营户
    driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)

    driver.find_element_by_xpath('//*[@id="openProSelect"]').click() #点击"批次出库"按钮
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="keyWord"]').send_keys(goods)
    time.sleep(2)
    driver.find_element_by_partial_link_text(goods).click()  # 选择该产品
    driver.find_element_by_xpath('//*[@id="sure"]').click() #点击确认按钮
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="select2-employeeId-container"]').click() #点击选择出库员下拉框
    driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER) #点击电脑enter建
    driver.find_element_by_xpath('//*[@id="submit"]').click() #点击保存按钮
    time.sleep(3)

#add_SalesRecord_wholesalemarket(u'大苹果')



#批发删除进货登记
def delete_registration_wholesalemarket(sku): #参数：供应商
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[3]/a/span[1]').click() #点击进场登记
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[3]/ul/li/a/i').click() #点击进场登记子菜单
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(sku) #输入sku
    driver.find_element_by_xpath('//*[@id="search"]').click()  #点击搜索
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[6]/button[2]').click()  #点击删除
    time.sleep(2)
    driver.find_element_by_css_selector('.modal-footer:nth-child(2) > .btn:nth-child(2)').click()
    time.sleep(3)

#delete_registration_wholesalemarket(sku2)

#批发删除供应商
def delete_supplier_wholesalemarket(supplier):
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[8]/a/span[1]').click()#点击基本信息管理
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[8]/ul/li[3]/a').click() #点击供应商管理子菜单
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(supplier) #输入供应商
    driver.find_element_by_xpath('//*[@id="btnSearch"]').click() #点击搜索
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td[6]/button[2]').click() #点击删除按钮
    time.sleep(2)
    driver.find_element_by_css_selector('.btn-primary').click() #二次确认
    time.sleep(2)

#delete_supplier_wholesalemarket(u'商超门店测试企业')


#团采添加进货登记
def stock_registration_grouppurchasing(code): #参数：出库单号
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[4]/a/span[1]').click() #点击进货登记
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[4]/ul/li/a').click() #点击进货登记子菜单
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div/section[2]/div/div/div/div/div[2]/div/button[1]').click()
    time.sleep(3)
    #点击扫码登记
    driver.find_element_by_xpath('//*[@id="scanOutstockNo"]').send_keys(code) #输入种植系统出库单
    driver.find_element_by_xpath('//*[@id="sure"]').click() #点击保存按钮
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="baseForm"]/div/div/div/div[2]/div/div[2]/div/div/span/span[1]/span').click()  # 点击登记人下拉选择框
    driver.find_element_by_xpath('/html/body/span/span/span[1]/input').click() #点击登记人输入框
    driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER) #点击电脑enter建
    driver.find_element_by_xpath('//*[@id="submit"]').click()  # 点击保存
    time.sleep(3)

#stock_registration_grouppurchasing('F3102894U1912000010')

#查看团采H5信息
def preview_H5_grouppurchasing(sku):
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[3]/a/span[1]').click() #点击批次管理
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[3]/ul/li/a').click() #点击批次管理子菜单
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="searchParam"]').send_keys(sku) #输入要搜索的批次产品的sku
    driver.find_element_by_xpath('//*[@id="searchBtn"]').click()#点击搜索按钮
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[10]/button[1]').click()  # 点击预览二维码按钮
    time.sleep(3)
    text = driver.find_element_by_xpath('//*[@id="qrcode"]').get_attribute("value")  # 获取批次链接
    time.sleep(240)
    driver.get(text)
    time.sleep(5)

#preview_H5_grouppurchasing(sku2)

#团采删除进货登记
def delete_registration_grouppurchasing(sku): #参数：供应商
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[4]/a/span[1]').click() #点击进货登记
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[4]/ul/li/a').click() #点击进货登记子菜单
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(sku) #输入sku
    driver.find_element_by_xpath('//*[@id="search"]').click()  #点击搜索
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td[7]/button[2]').click()  #点击删除
    time.sleep(2)
    driver.find_element_by_css_selector('.modal-footer:nth-child(2) > .btn:nth-child(2)').click()
    time.sleep(2)

#delete_registration_grouppurchasing(sku2)

#团采删除供应商
def delete_supplier_grouppurchasing(supplier):
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[7]/a/span[1]').click()#点击供应商管理
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[7]/ul/li/a').click() #点击供应商管理子菜单
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(supplier) #输入供应商
    driver.find_element_by_xpath('//*[@id="btnSearch"]').click() #点击搜索
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td[6]/button[2]').click() #点击删除按钮
    time.sleep(2)
    driver.find_element_by_css_selector('.btn-primary').click() #二次确认
    time.sleep(2)

#delete_supplier_grouppurchasing(u'上海艺杏食品股份有限公司')

