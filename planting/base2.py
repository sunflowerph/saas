#coding=utf-8

#种植系统

from selenium import  webdriver
import time
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path='/Users/ph/Documents/chromedriver')
driver.get('http://118.25.66.69:8080/planting/login') #预发
#driver.get('https://cloud.cesgroup.com.cn:8888/tenant/ces/loginpage?flash')
#driver.get('http://saas.zhuisuyun.net/planting/login') #线上
driver.implicitly_wait(5)
driver.set_window_size(1366,768)
driver.execute_script('window.scrollTo(0,768)')#滑动屏幕到指定位置

x = driver.get_window_size()["width"]  # 获取当前屏幕的宽
y = driver.get_window_size()["height"]  # 获取当前屏幕的高
print(x,y)


#登录系统
def login(count,password): #参数：用户名、密码
    driver.find_element_by_xpath('//*[@id="form1"]/div[1]/input').send_keys(count) #输入账号
    driver.find_element_by_xpath('//*[@id="form1"]/div[2]/input').send_keys(password) #输入密码
    driver.find_element_by_xpath('//*[@id="form1"]/div[3]/div/button').click() #点击登录
    time.sleep(3)

login("cczz","1qazxsw2")
account_name=u'陈唯'

#修改企业基本信息
def edit_base_information(shortname,linkman,phone,law_person,address): #参数：企业简称、联系人、联系方式、法人代表、地址
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[9]/a/span[1]').click() #点击基础信息管理
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[9]/ul/li[1]/a').click() #点击基本信息管理
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

#修改企业主体编码为已存在的企业主体编码
def edit():
    #driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[9]/a/span[1]').click()  # 点击基础信息管理
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[9]/ul/li[1]/a').click()  # 点击基本信息管理
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="entpQrCode"]').clear()
    driver.find_element_by_xpath('//*[@id="entpQrCode"]').send_keys(u'061904493Y')
    driver.find_element_by_xpath('//*[@id="btnSave"]').click()  # 点击保存按钮

#edit()



name="ph" #设置员工姓名
#新增员工 (确认密码输入框未定位到)

def add_staff(name,mobile,post,psw): #参数：姓名、联系方式、岗位、密码
    #driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[9]/a/span[1]').click() #点击基础数据管理
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[9]/ul/li[3]/a').click() #点击员工信息管理
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
    # driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[9]/a/span[1]').click() #点击基础数据管理
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[9]/ul/li[2]/a').click()  # 点击员工信息管理
    driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(name)  # 搜索框输入姓名
    driver.find_element_by_xpath('//*[@id="btnSearch"]').click()  # 点击搜索
    time.sleep(2)


#search_staff1(name)


#编辑员工信息
def edit_staff(name,post):
    #driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[9]/a/span[1]').click()  # 点击基础数据管理
    # time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[9]/ul/li[2]/a').click()  # 点击员工信息管理
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
    # driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[9]/a/span[1]').click()  # 点击基础数据管理
    # time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[9]/ul/li[2]/a').click()  # 点击员工信息管理
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


#农资管理-供应商管理
supplier1=u'供应商00002' #设置供应商名称
#添加供应商
def add_supplier(name,shortname,linkman,phonenumber,bizRegNumber,LawPerson,address):
    #参数：供应商名称、企业简称、联系人、联系方式、供商注册号、法人代表、地址
    driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[8]/a/span[1]').click() #点击农资管理
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/aside/section/ul/li[8]/ul/li[2]/a").click() #点击供应商管理子菜单
    driver.find_element_by_xpath('//*[@id="btnAdd"]').click()  #点击新增
    driver.find_element_by_xpath('//*[@id="entpName"]').send_keys(name)  #输入企业名称
    driver.find_element_by_xpath('//*[@id="entpShortName"]').send_keys(shortname) #输入简称
    driver.find_element_by_xpath('//*[@id="contactPerson"]').send_keys(linkman) #输入联系人
    driver.find_element_by_xpath('//*[@id="permanent"]').click() #证件有效期选择永久
    driver.find_element_by_xpath('//*[@id="contactDetail"]').send_keys(phonenumber) #输入联系方式
    driver.find_element_by_xpath('//*[@id="bizRegNumber"]').send_keys(bizRegNumber) #输入工商注册号
    driver.find_element_by_xpath('//*[@id="select2-entpType-container"]').click() #点击经营类型下拉框
    time.sleep(2)
    driver.find_element_by_xpath('//*[@class="select2-results__option"]').click() #选择其中一种经营类型
    driver.find_element_by_xpath('//*[@id="legalRepresentative"]').send_keys(LawPerson) #填写法人代表
    driver.find_element_by_xpath('//*[@id="select2-entpNature-container"]').click() #点击经营者性质下拉框
    time.sleep(3)
    driver.find_element_by_xpath('//*[@class="select2-results__option"]').click() #选择一种经营性质

    driver.find_element_by_xpath('//*[@id="baseForm"]/div/div[1]/div[2]/div[3]/div/div/div/div[4]/div/span/button').click()
    #点击地图
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="suggestId"]').send_keys(address) #输入地址
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="tangram-suggestion--TANGRAM__1m-item0"]/i').click() #选择定位到的地址
    driver.find_element_by_xpath('//*[@id="adressButton"]').click() #点击确认
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="btnSave"]').click() #点击保存
    #time.sleep(4)


#add_supplier(supplier1,u"供商5",u"彭女士",'17301000000','123445958',u'法人彭女士',u'大渡河')

#编辑供应商
def edit_supplier1(supplier,linkerman1,short_name):
    #driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[8]/a/span[1]').click()  # 点击农资管理
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/aside/section/ul/li[8]/ul/li[2]/a").click()  # 点击供应商管理子菜单
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


#edit_supplier1(supplier1,'17300023',u"供商3")


#搜索供应商
def search_supplier(supplier):
    #driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[8]/a/span[1]').click()  # 点击农资管理
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/aside/section/ul/li[8]/ul/li[2]/a").click()  # 点击供应商管理子菜单
    driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(supplier)  # 在搜索中填入要编辑的供应商名称
    driver.find_element_by_xpath('//*[@id="btnSearch"]').click()  # 点击搜索按钮
    time.sleep(3)


#search_supplier(supplier1)


#删除供应商
def delete_supplier(supplier):
    #driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[8]/a/span[1]').click()  # 点击农资管理
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/aside/section/ul/li[8]/ul/li[2]/a").click()  # 点击供应商管理子菜单
    driver.find_element_by_xpath('//*[@id="searchbox"]').clear()
    driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(supplier)  # 在搜索中填入要删除的供应商名称
    driver.find_element_by_xpath('//*[@id="btnSearch"]').click()  # 点击搜索按钮
    time.sleep(4)
    driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td[6]/button[2]').click() #点击删除按钮
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/button[2]').click() #点击二次确认按钮
    time.sleep(3)

#delete_supplier(supplier1)



sku='sku006' #产品sku

#新增产品(手动输入)

def add_goods(sku,name,brand,code,durabilityDay,entname,shelfLifeDay):
    #参数：sku、品名、品类、品牌、产品编码、保质期、供应商、生产企业名称、最佳口感期，单价
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[6]/a/span[1]').click()#点击产品管理
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[6]/ul/li/a').click() #点击产品管理子菜单
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="addProduct"]').click() #点击新增
    driver.find_element_by_xpath('//*[@id="productNo"]').send_keys(sku) #输入产品sku
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="productName"]').send_keys(name) #输入品名
    driver.find_element_by_xpath('//*[@id="selectInput"]/input[1]').click() #点击品类下拉框
    driver.find_element_by_xpath('//*[@id="choice"]/li[1]/span').click() #选择蔬菜
    driver.find_element_by_xpath('//*[@id="01231017"]').click() #扁豆种子
    driver.find_element_by_xpath('//*[@id="selectInput"]/input[1]').click() #点击品类下拉框
    driver.find_element_by_xpath('//*[@id="choice"]/li[1]/span').click() #选择蔬菜
    driver.find_element_by_xpath('//*[@id="01231017"]').click() #扁豆种子
    driver.find_element_by_xpath('//*[@id="productBrand"]').send_keys(brand) #输入品牌
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="productBrandCode"]').send_keys(code) # 输入品牌编码
    driver.find_element_by_xpath('//*[@id="durabilityDay"]').send_keys(durabilityDay) #输入保质期
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="entpName"]').send_keys(entname) #输入生产企业名称
    driver.find_element_by_xpath('//*[@id="shelfLifeDay"]').send_keys(shelfLifeDay) #输入最佳口感期
    driver.find_element_by_xpath('//*[@id="Submit"]').click() #点击保存
    time.sleep(4)

#add_goods(sku,u'大西瓜',u"大品牌",'1823849','180',u"企业名称","180")


#编辑产品
def edit_goods(sku,productname):
    #driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[6]/a/span[1]').click()#点击产品管理
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[6]/ul/li/a').click() #点击产品管理子菜单

    driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(sku) #输入要编辑商品的sku
    driver.find_element_by_xpath('//*[@id="btnSearch"]').click() #点击搜索按钮
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[10]/button[2]').click() #点击编辑按钮
    time.sleep(4)
    handles=driver.window_handles #获取当前两个窗口的句柄
    #切换到编辑窗口
    for handle in handles:
        if handle != driver.current_window_handle:
            driver.switch_to.window(handle)
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="productName"]').clear() #清除原来的产品名称
    driver.find_element_by_xpath('//*[@id="productName"]').send_keys(productname) #填写新的产品名称
    driver.find_element_by_xpath('//*[@id="Submit"]').click() #点击保存按钮
    time.sleep(3)


#edit_goods(sku,u'新名')


#下架产品
def sold_out_goods(sku): #参数：sku
    # driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[6]/a/span[1]').click()#点击产品管理
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[6]/ul/li/a').click() #点击产品管理子菜单
    driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(sku)  # 输入要编辑商品的sku
    driver.find_element_by_xpath('//*[@id="btnSearch"]').click()  # 点击搜索按钮
    time.sleep(3)
    driver.find_element_by_xpath('//*[@class="btn btn-onSale btn-onSale-down"]').click() #点击下架按钮
    time.sleep(3)

#sold_out_goods(sku)

#上架产品
def putaway_goods(sku): #参数：sku
    # driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[6]/a/span[1]').click()#点击产品管理
    # time.sleep(2)
    # driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[6]/ul/li/a').click() #点击产品管理子菜单
    # driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(sku)  # 输入要编辑商品的sku
    driver.find_element_by_xpath('//*[@id="btnSearch"]').click()  # 点击搜索按钮
    time.sleep(3)
    driver.find_element_by_xpath('//*[@class="btn btn-onSale btn-onSale-up"]').click()  # 点击上架按钮
    time.sleep(3)

#putaway_goods(sku)

#删除产品
def delete_goods1(sku):
    # driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[6]/a/span[1]').click()#点击产品管理
    # time.sleep(2)
    # driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[6]/ul/li/a').click() #点击产品管理子菜单
    # driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(sku)  # 输入要编辑商品的sku
    # driver.find_element_by_xpath('//*[@id="btnSearch"]').click()  # 点击搜索按钮
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="del"]').click() #点击删除按钮
    time.sleep(3)
    driver.find_element_by_css_selector('.modal-footer:nth-child(2) > .btn-primary').click() #二次确认
    time.sleep(3)

#delete_goods('sku')

#按照搜索供应商查找产品
def select_goods1(supplier):
    # driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[6]/a/span[1]').click()#点击产品管理
    # time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[6]/ul/li/a').click() #点击产品管理子菜单
    driver.find_element_by_xpath \
        ('/html/body/div/div/section[2]/div/div/div/div/div[1]/div[1]/div/div/span/span[1]/span/span[2]').click()#点击下拉框
    driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(supplier) #输入供应商名称
    driver.find_element_by_xpath('//*[@class="select2-results__option select2-results__option--highlighted"]').click()
    #点击所选的供应商


# select_goods1(u'供应商03')
#产品列表中筛选预包装类型的产品
def product_type_1(type):
    # driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[6]/a/span[1]').click()#点击产品管理
    # time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[6]/ul/li/a').click() #点击产品管理子菜单
    driver.find_element_by_xpath('//*[@id="select2-productType-container"]').click() #点击产品类型下拉框
    driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(type)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@class="select2-results__option select2-results__option--highlighted"]').click()


#product_type_1(u"预包装")

#产品列表中筛选散货类型的产品
def product_type_2(type):
    # driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[6]/a/span[1]').click()#点击产品管理
    # time.sleep(2)
    # driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[6]/ul/li/a').click() #点击产品管理子菜单
    driver.find_element_by_xpath('//*[@id="select2-productType-container"]').click() #点击产品类型下拉框
    driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(type)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@class="select2-results__option select2-results__option--highlighted"]').click()

#product_type_2(u"散货")


#产品列表中筛选标品类型的产品
def product_type_3(type):
    # driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[6]/a/span[1]').click()#点击产品管理
    # time.sleep(2)
    # driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[6]/ul/li/a').click() #点击产品管理子菜单
    driver.find_element_by_xpath('//*[@id="select2-productType-container"]').click() #点击产品类型下拉框
    driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(type)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@class="select2-results__option select2-results__option--highlighted"]').click()

#product_type_3(u"标品")


#添加销售记录
def add_SalesRecord(tester):
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[4]/a/span[1]').click()  #点击销售记录
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[4]/ul/li/a').click()  # 点击销售记录子菜单
    driver.find_element_by_xpath('//*[@id="add_new"]').click() #点击新增
    driver.find_element_by_xpath('//*[@id="openProSelect"]').click() #点击"批次出库"按钮
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="pro00353654-3da6-44be-a20e-61d6cf23e04c"]/a/span').click() #选择一种产品
    driver.find_element_by_xpath('//*[@id="sure"]').click() #点击确认按钮
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="select2-employeeId-container"]').click() #点击选择登记人下拉框
    driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(tester) #输入登记人
    driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER) #点击电脑enter建
    driver.find_element_by_xpath('//*[@id="submit"]').click() #点击保存按钮
    time.sleep(3)

#add_SalesRecord(u'王格必')

#编辑销售记录
def edit_SalesRecord(phonenumber):
    # driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[4]/a/span[1]').click()  #点击销售记录
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[4]/ul/li/a').click()  # 点击销售记录子菜单
    driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[7]/button[2]').click()
    driver.find_element_by_xpath('//*[@id="contactDetail"]').clear()
    driver.find_element_by_xpath('//*[@id="contactDetail"]').send_keys(phonenumber)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="submit"]').click()
    time.sleep(3)

#edit_SalesRecord('12344555')

#删除销售记录
def delete_SalesRecord():
    # driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[4]/a/span[1]').click()  #点击销售记录
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[4]/ul/li/a').click()  # 点击销售记录子菜单
    driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[7]/button[3]').click() #点击删除按钮
    time.sleep(2)
    driver.find_element_by_css_selector('.btn-primary:nth-child(2)').click()  # 点击二次确认按钮
    time.sleep(2)

#delete_SalesRecord()

#添加销售记录-文档导入
def import_txt():
    # driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[4]/a/span[1]').click()  #点击销售记录
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[4]/ul/li/a').click()  # 点击销售记录子菜单
    driver.find_element_by_xpath('//*[@id="toolbar"]/div/button[2]').click() #点击文档导入按钮
    handles = driver.window_handles
    for handle in handles:
        if handle != driver.current_window_handle:
            driver.switch_to.window(handle)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="newFileUpload"]').send_keys('/Users/ph/Desktop/SAASproject/file/outstocktemp (1).xlsx')
    #选择导入的文件

    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="newExcelModal"]/div/div/div[2]/form/div/div/div[3]/div[2]/a/i').click()
    time.sleep(10)
    #点击上传按钮

#import_txt()

#查找出库记录，自定义搜索时间范围
def search_SalesRecord1(time1,time2):
    # driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[4]/a/span[1]').click()  #点击销售记录
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[4]/ul/li/a').click()  # 点击销售记录子菜单
    driver.find_element_by_xpath('//*[@id="whole"]/li[2]').click() #点击自定义按钮
    driver.find_element_by_xpath('//*[@id="dateStart"]').send_keys(time1) #输入开始时间
    driver.find_element_by_xpath('//*[@id="dateEnd"]').send_keys(time2) #输入结束时间
    driver.find_element_by_xpath('//*[@id="search"]').click() #点击搜索

#search_SalesRecord1('2019-08-13','2019-10-16')

#根据出库单号搜索销售记录
def search_SalesRecord2():
    # driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[4]/a/span[1]').click()  #点击销售记录
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[4]/ul/li/a').click()  # 点击销售记录子菜单
    text=driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[2]').text
    driver.find_element_by_xpath('//*[@id="searchParam"]').send_keys(text)
    driver.find_element_by_xpath('//*[@id="search"]').click()
    time.sleep(2)
    text1=driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td[2]').text

#search_SalesRecord2()



#检测管理
reportname=u"检测名字啊"
#新增检测报告
def add_testreport(testname,testnumber,tester):
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[5]/a/span[1]').click() #点击检测管理
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[5]/ul/li/a').click() #点击检测报告管理
    driver.find_element_by_xpath('//*[@id="add"]').click() #点击新增
    driver.find_element_by_xpath('//*[@id="select2-detectionType-container"]').click() #点击检测类型下拉框
    driver.find_element_by_xpath('//*[@class="select2-results__option"]').click() #选择型式检测
    driver.find_element_by_xpath('//*[@id="detectionName"]').send_keys(testname) #输入检测名称
    driver.find_element_by_xpath('//*[@id="detectionNo"]').send_keys(testnumber) #输入检测编号
    time.sleep(3)
    #driver.find_element_by_xpath('//*[@class="select2-results__option select2-results__option--highlighted"]').click()
    #点击选择的检测员

    driver.find_element_by_xpath('//*[@id="openProSelect"]').click() #点击选择产品
    time.sleep(3)
    driver.find_element_by_css_selector('#pro00353654-3da6-44be-a20e-61d6cf23e04c span').click() #点击添加
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="sure"]').click() #点击选择产品里的保存
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="select2-employeeId-container"]').click()  # 点击检测员下拉框
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(tester)  # 输入要选择的检测员
    driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="submit"]').click()# 点击保存
    time.sleep(3)


#add_testreport(u"检测名字啊",'112121',u'王格必')


#根据检测名称搜索检测报告
def search_testreport2(testname):
    #driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[5]/a/span[1]').click() #点击检测管理
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[5]/ul/li/a').click() #点击检测报告管理
    driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(testname)  # 输入要编辑的检测报告名称
    driver.find_element_by_xpath('//*[@id="btnSearch"]').click()  # 点击搜索

#search_testreport2()


#编辑检测报告
def edit_report(testname):#登记人没显示
    #driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[5]/a/span[1]').click() #点击检测管理
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[5]/ul/li/a').click() #点击检测报告管理
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
    #driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[5]/a/span[1]').click() #点击检测管理
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[5]/ul/li/a').click() #点击检测报告管理
    driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(testname)  # 输入要编辑的检测报告名称
    driver.find_element_by_xpath('//*[@id="btnSearch"]').click() #点击搜索
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[7]/button[2]').click() #点击删除按钮
    time.sleep(2)
    driver.find_element_by_css_selector('.btn-primary').click() #点击二次确认按钮

#delete_report(u"检测名字啊")

#自定义时间搜索检测报告
def search_testreport1(time1,time2):
    #driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[5]/a/span[1]').click() #点击检测管理
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[5]/ul/li/a').click() #点击检测报告管理
    driver.find_element_by_xpath('//*[@id="whole"]/li[2]').click() #点击自定义按钮
    driver.find_element_by_xpath('//*[@id="dateStart"]').send_keys(time1) #输入开始时间
    driver.find_element_by_xpath('//*[@id="dateEnd"]').send_keys(time2) #输入结束时间
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="btnSearch"]').click() #点击搜索

#search_testreport1('2019-08-13','2019-10-13')


