#coding=utf-8

#农贸系统

import base3
import unittest
import time
import datetime


class TestStore(unittest.TestCase):
#登录商超门店
    def test_aa_login(self):
        base3.login("ddnm","1qazxsw2")  #预发/线上
        time.sleep(2)
        try:
            text = base3.driver.find_element_by_xpath('//*[@id="passwordFrom"]/div/ul/li[1]/a/span').text #获取登录名
            assert text==base3.account_name
            print 'test_aa_login test pass'
        except:
            print 'test_aa_login test fail'


#退出浏览器
    def test_z_quit(self):
        try:
            base3.driver.quit()
            print 'test_z_quit test pass'
        except:
            print 'test_z_quit test pass'


# 修改企业基本信息 #参数：企业简称、联系人、联系方式、法人代表、地址
    def test_ab_editbase_information(self):
        try:
            base3.edit_base_information(u"中信商超门店", u"李先生", "17301691111", u'张先生', u"五角场")
            print "test_ab_edit_base_information test pass"
        except:
            print 'test_ab_edit_base_information test fail'
        time.sleep(2)

#新增员工
    def test_ba_add_staff(self):
        base3.add_staff(base3.name, "9874352935", u"经理助理", "1qazxsw2")
        try:
            text = base3.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[2]').text
            assert text==base3.name
            print "test_ba_add_staff test pass"
        except:
            print "test_ba_add_staff test fail"
        time.sleep(2)


#通过姓名搜索员工
    def test_bb_search_staff1(self):
        base3.search_staff(base3.name)
        try:
            text = base3.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td[2]').text
            assert text == base3.name
            print 'test_bb_search_staff1 test pass'
        except:
            print 'test_bb_search_staff1 test fail'
        time.sleep(2)


#通过电话搜索员工
    def test_bc_search_staff2(self):
        base3.search_staff('9874352935')
        try:
            text = base3.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td[2]').text
            assert text == base3.name
            print 'test_bc_search_staff1 test pass'
        except:
            print 'test_bc_search_staff1 test fail'
        time.sleep(2)


#精确搜索
    def test_bd_search_staff3(self):
        base3.search_staff(base3.name)
        try:
            text = base3.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td[2]').text
            assert text == base3.name
            print 'test_bd_search_staff1 test pass'
        except:
            print 'test_bd_search_staff1 test fail'
        time.sleep(2)


#模糊搜索
    def test_be_search_staff4(self):
        base3.search_staff('p')
        try:
            text = base3.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td[2]').text
            assert text in base3.name
            print 'test_be_search_staff1 test pass'
        except:
            print 'test_be_search_staff1 test fail'
        time.sleep(2)

#编辑员工信息
    def test_bf_edit_staff(self):
        base3.edit_staff(base3.name, u"助理")
        time.sleep(2)
        try:
            text = base3.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[4]').text
            assert text==u"助理"
            print "test_bf_edit_staff test pass"
        except:
            print "test_bf_edit_staff test fail"
        time.sleep(2)

#删除员工
    def test_bg_delete_staff(self):
        base3.delete_staff(base3.name)
        time.sleep(2)
        base3.driver.find_element_by_xpath('//*[@id="searchbox"]').clear()
        base3.driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys('ph')
        base3.driver.find_element_by_xpath('//*[@id="btnSearch"]').click()
        try:

            base3.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td')
            print 'test_bg_delete_staff test pass'
        except:
            print 'test_bg_delete_staff test fail'
        time.sleep(3)

#
#菜单收起
    def test_ca_close_menu(self):
        base3.close_menu()
        time.sleep(3)
        try:
            assert base3.driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[1]').text ==u"菜单"
            #如果能找到"菜单"这个元素说明菜单收起失败
            print "test_ca_close_menu test fail"
        except:
            print "test_ca_close_menu test pass"
        time.sleep(3)



#菜单展开
    def test_cb_open_menu(self):
        base3.open_menu()
        time.sleep(3)
        try:
            base3.driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[1]') ##如果能找到"菜单"这个元素说明菜单打开成功
            print "test_cb_open_menu test pass"
        except:
            print "test_cb_open_menu test fail"
        time.sleep(3)


#查看首页批次数
    def test_da_get_batch(self):
        try:
            base3.get_batch()
            print "test_da_get_batch test pass"
        except:
            print "test_da_get_batch test fail"
        time.sleep(3)

#查看首页赋码数
    def test_db_get_coding(self):
        try:
            base3.get_coding()
            print "test_db_get_coding test pass"
        except:
            print "test_db_get_coding test fail"
        time.sleep(3)

#查看首页进货登记次数
    def test_dc_get_egistration(self):
        try:
            base3.get_egistration()
            print "test_dc_get_egistration test pass"
        except:
            print "test_dc_get_egistration test"

        time.sleep(3)

#获取首页产品数
    def test_dd_get_goods_number(self):
        try:
            base3.get_goods_number()
            print "test_dd_get_goods_number test pass"
        except:
            print "test_dd_get_goods_number test fail"

        time.sleep(3)

#获取首页供应商数
    def test_de_get_supplier(self):
        try:
            base3.get_supplier()
            print "test_de_get_supplier test pass"
        except:
            print "test_de_get_supplier test fail"
        time.sleep(3)

#获取首页中散货数量
    def test_df_get_bulk_cargo(self):
        try:
            base3.get_bulk_cargo()
            print "test_df_get_bulk_cargo test pass"
        except:
            print "test_df_get_bulk_cargo test fail"
        time.sleep(3)

#获取首页中预包装货物数量
    def test_dg_get_prepackaging(self):
        try:
            base3. get_prepackaging()
            print "test_dg_get_prepackaging test pass"
        except:
            print "test_dg_get_prepackaging test fail"
        time.sleep(3)



#新增供应商
    def test_ea_add_supplier(self):
        base3.add_supplier(base3.supplier1,u"供商5",u'彭女士','17301000000','123445958',u'法人彭女士',u'大渡河')
        #执行新增供应商操作
        time.sleep(3)
        base3.driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(base3.supplier1) #在列表中搜索该供应商
        base3.driver.find_element_by_xpath('//*[@id="btnSearch"]').click() #点击搜索按钮
        text=base3.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td[2]').text #获取搜索出来的供应商名称
        #断言：新增的供应商是否存在
        try:
            assert text==base3.supplier1
            print " test_ea_add_supplier test pass"
        except:
            print "test_ea_add_supplier test fail"
        time.sleep(3)

#编辑供应商
    def test_eb_edit_supplier(self):
        time.sleep(2)
        base3.edit_supplier1(base3.supplier1, '17300023', u"供商3") #执行编辑供应商操作
        time.sleep(2)
        text=base3.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[3]').text #获取联系人信息
        #断言：联系人是否是改过之后的
        try:
            assert text=="17300023"
            print " test_eb_edit_supplier test pass"
        except:
            print "test_eb_edit_supplier test fail"
        time.sleep(3)



#搜索供应商
    def test_ec_search_supplier(self):
        base3.search_supplier(base3.supplier1)
        time.sleep(2)
        try:
            text=base3.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td[2]').text
            assert text==base3.supplier1
            print 'test_ec_search_supplier test pass'
        except:
            print 'test_ec_search_supplier test fail'



#删除供应商
    def test_ed_delete_supplier(self):
        base3.delete_supplier(base3.supplier1) #执行删除供应商操作
        time.sleep(2)
        # 断言："没有找到匹配的记录"元素是否存在
        try:
            base3.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td')
            print "test_ed_delete_supplier test pass"
        except:
            print "test_ed_delete_supplier test fail"
        time.sleep(3)

#新增检测报告
    def test_fa_add_testreport(self):
        base3.add_testreport(base3.reportname, '112121231', u'试试看')
        text=base3.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[2]').text
        try:
            assert text==base3.reportname
            print "test_fa_add_testreport test pass"
        except:
            print "test_fa_add_testreport test fail"
        time.sleep(3)

#根据检测名称搜索检测报告
    def test_fb_search_testreport2(self):
        base3.search_testreport2(base3.reportname)
        text=base3.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[2]').text
        try:
            assert text==base3.reportname
            print "test_fb_search_testreport2 test pass"
        except:
            print "test_fb_search_testreport2 test fail"
        time.sleep(3)

#编辑检测报告
    def test_fc_edit_report(self):
        try:
            base3.edit_report(base3.reportname)
            print "test_fc_edit_report test pass"
        except:
            print "test_fc_edit_report test fail"
        time.sleep(3)

#删除检测报告
    def test_fd_delete_report(self):
        base3.delete_report(base3.reportname)
        time.sleep(2)
        base3.driver.find_element_by_xpath('//*[@id="searchbox"]').clear()
        base3.driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(base3.reportname)
        base3.driver.find_element_by_xpath('//*[@id="btnSearch"]').click()
        time.sleep(2)
        try:
            base3.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td')
            print "test_fd_delete_report test pass"
        except:
            print "test_fd_delete_report test fail"
        time.sleep(3)

#自定义时间搜索检测报告
    def test_fe_search_SalesRecord1(self):
        base3.search_testreport1('2019-08-13', '2019-10-13')
        try:
            time0=base3.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[6]').text #获取搜索结果的出库时间
            time0 = datetime.datetime.strptime(time0, '%Y-%m-%d')
            time1=datetime.datetime.strptime('2019-08-13', '%Y-%m-%d')
            time2=datetime.datetime.strptime('2019-10-13', '%Y-%m-%d')
            assert time1<=time0<=time2
            print 'test_ge_search_SalesRecord1 test pass'
        except:
            try:
                base3.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td')
                print 'test_fe_search_SalesRecord test pass'
            except:
                print 'test_fe_search_SalesRecord test fail'
        time.sleep(3)



#查看预警信息（营业执照过期）
    def test_ga_warning_query1(self):
        try:
            base3.warning_query1()
            print 'test_ga_warning_query1 test pass'
        except:
            print 'test_ga_warning_query1 test fail'


#查看预警信息（食品经营许可证过期）
    def test_gb_warning_query2(self):
        try:
            base3.warning_query2()
            print "test_gb_warning_query2 test pass"
        except:
            print 'test_gb_warning_query2 test fail'
        time.sleep(2)

#预警信息按时间从大到小排序
    def test_gc_orderby_time1(self):
        base3.orderby_time1()
        time.sleep(2)



#预警信息按时间从小到大排序
    def test_gd_orderby_time2(self):
        base3.orderby_time2()
        time.sleep(2)

#查看营业执照过期的全部供应商
    def test_ge_warning_view0(self):
        try:
            base3.warning_view0()
            print 'test_ge_warning_view0 test pass'
        except:
            print 'test_ge_warning_view0 test fail'
        time.sleep(2)

#查看营业执照即将在一个月内过期的供应商
    def test_gf_warning_view1(self):
        try:
            base3.warning_view1()
            print 'test_gf_warning_view1 test pass'
        except:
            print 'test_gf_warning_view1 test fail'
        time.sleep(2)

#查看营业执照即将在两个月内过期的供应商
    def test_gg_warning_view2(self):
        try:
            base3.warning_view2()
            print 'test_gg_warning_view2 test pass'
        except:
            print 'test_gg_warning_view2 test fail'
        time.sleep(2)

#查看营业执照即将在三个月内过期的供应商
    def test_gh_warning_view3(self):
        try:
            base3.warning_view3()
            print 'test_gh_warning_view3 test pass'
        except:
            print 'test_gh_warning_view3 test fail'
        time.sleep(2)

#查看食品经营许可证的全部供应商
    def test_gi_warning_view4(self):
        try:
            base3.warning_view4()
            print 'test_gi_warning_view4 test pass'
        except:
            print 'test_gi_warning_view4 test fail'
        time.sleep(2)

#查看食品经营许可证即将在一个月内过期的供应商
    def test_gj_warning_view5(self):
        try:
            base3.warning_view5()
            print 'test_gj_warning_view5 test pass'
        except:
            print 'test_gj_warning_view5 test fail'
        time.sleep(2)

#查看食品经营许可证即将在两个月内过期的供应商
    def test_gk_warning_view6(self):
        try:
            base3.warning_view6()
            print 'test_gk_warning_view6 test pass'
        except:
            print 'test_gk_warning_view6 test fail'
        time.sleep(2)

#查看食品经营许可证即将在三个月内过期的供应商
    def test_gl_warning_view7(self):
        try:
            base3.warning_view7()
            print 'test_gl_warning_view7 test pass'
        except:
            print 'test_gl_warning_view7 test fail'
        time.sleep(2)

#通过搜索供应商搜索预警信息
    def test_gm_search_warning(self):
        base3.search_warning()
        text=base3.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td[2]').text
        try:
            assert text==u'测试超市企业账号'
            print 'test_gm_search_warning test pass'
        except:
            try:
                base3.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td')
                print 'test_gm_search_warning test pass'
            except:
                print 'test_gm_search_warning test fail'









if __name__ =="__main__":
    unittest.main()
