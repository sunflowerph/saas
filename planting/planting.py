#coding=utf-8

#种植系统
import base2
import unittest
import time
import datetime


class TestPlanting(unittest.TestCase):
#登录商超门店
    def test_aa_login(self):
        base2.login("cczz","1qazxsw2") #预发环境
        #base2.login('ph01','1qazxsw2') #线上
        time.sleep(2)
        text=base2.driver.find_element_by_xpath('//*[@id="passwordFrom"]/div/ul/li[1]/a/span').text
        try:
            assert text==base2.account_name
            print 'test_aa_login test pass'
        except:
            print 'test_aa_login test fail'
#
#退出浏览器
    def test_z_quit(self):
        base2.driver.quit()
        print 'test_z_quit test pass'



# 修改企业基本信息 #参数：企业简称、联系人、联系方式、法人代表、地址
    def test_ab_editbase_information(self):
        try:
            base2.edit_base_information(u"中信商超门店", u"李先生", "17301691111", u'张先生', u"五角场")
            print "test_ab_edit_base_information test pass"
        except:
            print 'test_ab_edit_base_information test fail'
        time.sleep(2)

#修改企业主体编码为已存在的企业主体编码
    def test_ac_edit(self):
        base2.edit()
        try:
            base2.driver.find_element_by_css_selector('.toast-message')
            print 'test_ac_edit test pass'
        except:
            print 'test_ac_edit test fail'
        time.sleep(10)

#新增员工
    def test_ba_add_staff(self):
        base2.add_staff(base2.name, "9874352935", u"经理助理", "1qazxsw2")
        text=base2.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[2]').text
        try:
            assert text==base2.name
            print "test_ba_add_staff test pass"
        except:
            print "test_ba_add_staff test fail"
        time.sleep(2)


#通过姓名搜索员工
    def test_bb_search_staff1(self):
        base2.search_staff(base2.name)
        text=base2.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td[2]').text
        try:
            assert text == base2.name
            print 'test_bb_search_staff1 test pass'
        except:
            print 'test_bb_search_staff1 test fail'
        time.sleep(2)

#通过电话搜索员工
    def test_bc_search_staff2(self):
        base2.search_staff('9874352935')
        text = base2.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td[2]').text
        try:
            assert text == base2.name
            print 'test_bc_search_staff1 test pass'
        except:
            print 'test_bc_search_staff1 test fail'
        time.sleep(2)


#精确搜索
    def test_bd_search_staff3(self):
        base2.search_staff(base2.name)
        text=base2.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td[2]').text
        try:
            assert text == base2.name
            print 'test_bd_search_staff1 test pass'
        except:
            print 'test_bd_search_staff1 test fail'
        time.sleep(2)


#模糊搜索
    def test_be_search_staff4(self):
        base2.search_staff('p')
        text=base2.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td[2]').text
        try:
            assert text in base2.name
            print 'test_be_search_staff1 test pass'
        except:
            print 'test_be_search_staff1 test fail'
        time.sleep(2)

#编辑员工信息
    def test_bf_edit_staff(self):
        base2.edit_staff(base2.name, u"助理")
        time.sleep(2)
        text=base2.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[4]').text
        try:
            assert text==u"助理"
            print "test_bf_edit_staff test pass"
        except:
            print "test_bf_edit_staff test fail"

        time.sleep(2)

#删除员工
    def test_bg_delete_staff(self):
        base2.delete_staff(base2.name)
        time.sleep(2)
        base2.driver.find_element_by_xpath('//*[@id="searchbox"]').clear()
        base2.driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys('ph')
        base2.driver.find_element_by_xpath('//*[@id="btnSearch"]').click()
        try:
            base2.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td')
            print 'test_bg_delete_staff test pass'
        except:
            print 'test_bg_delete_staff test fail'
        time.sleep(3)


#菜单收起
    def test_ca_close_menu(self):
        base2.close_menu()
        time.sleep(3)
        try:
            assert base2.driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[1]').text ==u"菜单"
            #如果能找到"菜单"这个元素说明菜单收起失败
            print "test_ca_close_menu test fail"
        except:
            print "test_ca_close_menu test pass"
        time.sleep(3)



#菜单展开
    def test_cb_open_menu(self):
        base2.open_menu()
        time.sleep(3)
        try:
            base2.driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[1]') ##如果能找到"菜单"这个元素说明菜单打开成功
            print "test_cb_open_menu test pass"
        except:
            print "test_cb_open_menu test fail"
        time.sleep(3)


#新增供应商
    def test_da_add_supplier(self):
        base2.add_supplier(base2.supplier1,u"供商5",u'彭女士','17301000000','123445958',u'法人彭女士',u'大渡河')
        #执行新增供应商操作
        time.sleep(3)
        base2.driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(base2.supplier1) #在列表中搜索该供应商
        base2.driver.find_element_by_xpath('//*[@id="btnSearch"]').click() #点击搜索按钮
        text=base2.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td[2]').text #获取搜索出来的供应商名称
        #断言：新增的供应商是否存在
        try:
            assert text==base2.supplier1
            print " test_da_add_supplier test pass"
        except:
            print "test_da_add_supplier test fail"
        time.sleep(3)


#编辑供应商
    def test_db_edit_supplier(self):
        time.sleep(2)
        base2.edit_supplier1(base2.supplier1, '17300023', u"供商3") #执行编辑供应商操作
        time.sleep(2)
        text=base2.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[3]').text #获取联系人信息
        #断言：联系人是否是改过之后的
        try:
            assert text=="17300023"
            print " test_db_edit_supplier test pass"
        except:
            print "test_db_edit_supplier test fail"
        time.sleep(3)


#搜索供应商
    def test_dc_search_supplier(self):
        base2.search_supplier(base2.supplier1)
        time.sleep(2)
        try:
            text=base2.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td[2]').text
            assert text==base2.supplier1
            print 'test_dc_search_supplier test pass'
        except:
            print 'test_dc_search_supplier test fail'


#删除供应商
    def test_dd_delete_supplier(self):
        base2.delete_supplier(base2.supplier1) #执行删除供应商操作
        time.sleep(2)
        # 断言："没有找到匹配的记录"元素是否存在
        try:
            base2.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td')
            print "test_dd_delete_supplier test pass"
        except:
            print "test_dd_delete_supplier test fail"
        time.sleep(3)


#新增产品
    def test_ea_add_goods(self):
        base2.add_goods(base2.sku,u'大西瓜',u"大品牌",'1823849','180',u"商超门店002",u"企业名称","180",'23')
        #新增产品操作
        time.sleep(2)
        text=base2.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text #获取新增产品sku
        #断言：该sku的新增产品是否存在
        try:
            assert text==base2.sku
            print " test_ea_add_goods test pass"
        except:
            print "test_ea_add_goods test fail"
        time.sleep(3)

#编辑产品
    def test_eb_edit_goods(self):
        base2.edit_goods(base2.sku, u'新名') #编辑产品操作
        text=base2.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[4]').text #获取该产品更改后的产品名
        #断言该产品名是否是更改后的
        try:
            assert text == u"新名"
            print " test_eb_edit_goods test pass"
        except:
            print "test_eb_edit_goods test fail"
        time.sleep(3)

#下架产品
    def test_ec_sold_out_goods(self):
        base2.sold_out_goods(base2.sku) #下架产品操作
        #断言是否看到"上架"按钮
        try:
            base2.driver.find_element_by_xpath('//*[@class="btn btn-onSale btn-onSale-up"]').text
            print "test_ec_sold_out_goods test pass"
        except:
            print "test_ec_sold_out_goodst fail"
        time.sleep(3)

#上架产品
    def test_ed_putaway_goods(self):
        base2.putaway_goods(base2.sku) #上架产品操作
        #断言是否看到"下架"按钮
        try:
            base2.driver.find_element_by_xpath('//*[@class="btn btn-onSale btn-onSale-down"]').text
            print "test_ed_putaway_goods test pass"
        except:
            print "test_ed_putaway_goods fail"
        time.sleep(3)




#删除商品
    def test_ee_delete_goods1(self):
        base2.delete_goods1(base2.sku)
        try:
            base2.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td') #是否出现"没有找到匹配的记录"字段
            print "test_ee_delete_goods1 test pass"
        except:
            print "test_ee_delete_goods1 fail"
        time.sleep(3)

#按照搜索供应商查找产品
    def test_ef_select_goods1(self):
        base2.select_goods1(u'商超门店003')
        time.sleep(2)
        try:
            text1=base2.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[9]').text#获取搜索结果的供应商名称
            assert text1==u'商超门店003'
            print 'test_ef_select_goods1 test pass'
        except:
            try:
                text2=base2.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td').text#获取搜索结果提示文案
                assert text2==u"没有找到匹配的记录"
                print 'test_ef_select_goods1 test pass'
            except:
                print 'test_ef_select_goods1 test fail'


#产品列表中筛选预包装类型的产品
    def test_eg_product_type_1(self):
        base2.product_type_1(u"预包装")
        time.sleep(3)
        text=base2.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[6]').text #查看列表中产品的包装类型
        try:
            assert text==u'预包装'
            print 'test_eg_product_type_1 test pass'
        except:
            print 'test_eg_product_type_1 test fail'
        time.sleep(3)

#产品列表中筛选散货类型的产品
    def test_eh_product_type_2(self):
        base2.product_type_2(u"散货")
        time.sleep(3)
        text=base2.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[6]').text #查看列表中产品的包装类型
        try:
            assert text==u'散货'
            print 'test_eh_product_type_2 test pass'
        except:
            print 'test_eh_product_type_2 test fail'
        time.sleep(3)


#产品列表中筛选标品类型的产品
    def test_ei_product_type_3(self):
        base2.product_type_3(u"标品")
        time.sleep(3)
        text = base2.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[6]').text #查看列表中产品的包装类型
        try:
            assert text==u'标品'
            print 'test_ei_product_type_3 test pass'
        except:
            print 'test_ei_product_type_3 test fail'
        time.sleep(3)



#新增销售记录
    def test_fa_add_SalesRecord(self):
        try:
            base2.add_SalesRecord(u'王格必')
            print "test_fa_add_SalesRecord test pass"
        except:
            print "test_fa_add_SalesRecord test fail"
        time.sleep(3)


#编辑销售记录
    def test_fb_edit_SalesRecord(self):
        # text=base.driver.find_element_by_css_selector('#tables tr:nth-child(1) > td:nth-child(6)').text
        # print text
        try:
            base2.edit_SalesRecord('17300000000')
            print "test_fb_edit_SalesRecord test pass"
        except:
            print "test_fb_edit_SalesRecord test fail"
        time.sleep(3)


#删除销售记录
    def  test_fc_delete_SalesRecord(self):
        try:
            base2. delete_SalesRecord()
            print "test_fc_delete_SalesRecord test pass"
        except:
            print "test_fc_delete_SalesRecord test fail"
        time.sleep(3)


#添加销售记录-文档导入
    def test_fd_import_txt(self):
        try:
            base2.import_txt()
            print "test_fd_import_txt test pass"
        except:
            print "test_fd_import_txt test fail"


# 查找出库记录，自定义搜索时间范围
    def test_fe_search_SalesRecord1(self):
        base2.search_SalesRecord1('2019-08-13', '2019-10-16')
        try:
            time0=base2.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[3]').text #获取搜索结果的出库时间
            time0 = datetime.datetime.strptime(time0, '%Y-%m-%d')
            time1=datetime.datetime.strptime('2019-08-13', '%Y-%m-%d')
            time2=datetime.datetime.strptime('2019-10-13', '%Y-%m-%d')
            assert time1<=time0<=time2
            print 'test_fe_search_SalesRecord test pass'
        except:
            try:
                base2.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td')
                print 'test_fe_search_SalesRecord test pass'
            except:
                print 'test_fe_search_SalesRecord test fail'

        time.sleep(3)

#根据出库单号搜索销售记录
    def test_ff_search_SalesRecord2(self):
        try:
            base2.search_SalesRecord2()
            print 'test_ff_search_SalesRecord2 test pass'
        except:
            print 'test_ff_search_SalesRecord2 test fail'


#新增检测报告
    def test_ga_testreport(self):
        base2.add_testreport(base2.reportname, '112121231', u'王格必')
        text=base2.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[2]').text
        try:
            assert text==base2.reportname
            print "test_ga_add_testreport test pass"
        except:
            print "test_ga_add_testreport test fail"
        time.sleep(3)

#根据检测名称搜索检测报告
    def test_gb_search_testreport2(self):
        base2.search_testreport2(base2.reportname)
        text=base2.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[2]').text
        try:
            assert text==base2.reportname
            print "test_gb_search_testreport2 test pass"
        except:
            print "test_gb_search_testreport2 test fail"
        time.sleep(3)

#编辑检测报告
    def test_gc_edit_report(self):
        try:
            base2.edit_report(base2.reportname)
            print "test_gc_edit_report test pass"
        except:
            print "test_gc_edit_report test fail"
        time.sleep(3)

#删除检测报告
    def test_gd_delete_report(self):
        base2.delete_report(base2.reportname)
        time.sleep(2)
        base2.driver.find_element_by_xpath('//*[@id="searchbox"]').clear()
        base2.driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(base2.reportname)
        base2.driver.find_element_by_xpath('//*[@id="btnSearch"]').click()
        time.sleep(2)
        try:
            base2.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td')
            print "test_gd_delete_report test pass"
        except:
            print "test_gd_delete_report test fail"
        time.sleep(3)

#自定义时间搜索检测报告
    def test_ge_search_SalesRecord1(self):
        base2.search_testreport1('2019-08-13', '2019-10-13')
        try:
            time0=base2.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[6]').text #获取搜索结果的出库时间
            time0 = datetime.datetime.strptime(time0, '%Y-%m-%d')
            time1=datetime.datetime.strptime('2019-08-13', '%Y-%m-%d')
            time2=datetime.datetime.strptime('2019-10-13', '%Y-%m-%d')
            assert time1<=time0<=time2
            print 'test_ge_search_SalesRecord1 test pass'
        except:
            try:
                base2.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td')
                print 'test_ge_search_SalesRecord test pass'
            except:
                print 'test_ge_search_SalesRecord test fail'
        time.sleep(3)






if __name__ =="__main__":
    unittest.main()
