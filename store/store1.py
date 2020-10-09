#coding=utf-8
#商超门店自动化测试用例

import base1
import unittest
import time
import datetime
# import HTMLTestRunner


class TestStore(unittest.TestCase):
# #登录商超门店
    def test_aa_login(self):
        #base1.login(base1.test) #k8s
        #base1.login(base1.test)  #预发
        base1.login(base1.online) #线上
        time.sleep(2)
        text = base1.driver.find_element_by_xpath('//*[@id="passwordFrom"]/div/ul/li[1]/a/span').text #获取登录名
        assert text == base1.account_name

# 修改企业基本信息 #参数：企业简称、联系人、联系方式、法人代表、地址
    def test_ab_editbase_information(self):
        base1.edit_base_information(u"中信商超门店", u"李先生", "17301691111", u'张先生', u"五角场")
        time.sleep(2)
#
# #修改企业主体编码为已存在的企业主体编码
#     def test_ac_edit(self):
#         base1.edit()
#         time.sleep(3)
#         base1.driver.find_element_by_xpath('//*[@id="btnSave"]')
#         time.sleep(10)
#
# #新增员工
#     def test_ba_add_staff(self):
#         base1.add_staff(base1.name, "9874352935", u"经理助理", "1qazxsw2")
#         text = base1.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[2]').text
#         assert text == base1.name
#         time.sleep(2)
#
#
# #通过姓名搜索员工
#     def test_bb_search_staff1(self):
#         base1.search_staff(base1.name)
#         text = base1.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td[2]').text
#         assert text == base1.name
#         time.sleep(2)
#
#
# #通过电话搜索员工
#     def test_bc_search_staff2(self):
#         base1.search_staff('9874352935')
#         text = base1.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td[2]').text
#         assert text == base1.name
#         time.sleep(2)
#
#
# #精确搜索
#     def test_bd_search_staff3(self):
#         base1.search_staff(base1.name)
#         text = base1.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td[2]').text
#         assert text == base1.name
#         time.sleep(2)
#
# #模糊搜索
#     def test_be_search_staff4(self):
#         base1.search_staff('p')
#         text = base1.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td[2]').text
#         assert text in base1.name
#
#
# #编辑员工信息
#     def test_bf_edit_staff(self):
#         base1.edit_staff(base1.name, u"助理")
#         time.sleep(3)
#         text = base1.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[4]').text
#         assert text==u"助理"
#         time.sleep(2)
#
# #删除员工
#     def test_bg_delete_staff(self):
#         base1.delete_staff(base1.name)
#         time.sleep(2)
#         base1.driver.find_element_by_xpath('//*[@id="searchbox"]').clear()
#         base1.driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys('ph')
#         base1.driver.find_element_by_xpath('//*[@id="btnSearch"]').click()
#         base1.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td')
#         time.sleep(3)
#
#
# #菜单收起
#     def test_ca_close_menu(self):
#         base1.close_menu()
#         time.sleep(3)
#         if base1.driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[1]').text == u"菜单":
#             #如果能找到"菜单"这个元素说明菜单收起失败
#             return False
#         else:
#             return True
#         time.sleep(3)
#
#
#
# #菜单展开
#     def test_cb_open_menu(self):
#         base1.open_menu()
#         time.sleep(3)
#         base1.driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[1]') ##如果能找到"菜单"这个元素说明菜单打开成功
#         time.sleep(3)
# #
# #查看首页批次数
#     def test_da_get_batch(self):
#         base1.get_batch()
#         time.sleep(3)
#
# #查看首页赋码数
#     def test_db_get_coding(self):
#         base1.get_coding()
#         time.sleep(3)
#
# #查看首页进货登记次数
#     def test_dc_get_egistration(self):
#         base1.get_egistration()
#         time.sleep(3)
#
# #获取首页产品数
#     def test_dd_get_goods_number(self):
#         base1.get_goods_number()
#         time.sleep(3)
#
# #获取首页供应商数
#     def test_de_get_supplier(self):
#         base1.get_supplier()
#         time.sleep(3)
#
# #获取首页中散货数量
#     def test_df_get_bulk_cargo(self):
#         base1.get_bulk_cargo()
#         time.sleep(3)
#
# #获取首页中预包装货物数量
#     def test_dg_get_prepackaging(self):
#         base1. get_prepackaging()
#         time.sleep(3)
#
#
# #新增供应商
#     def test_ea_add_supplier(self):
#         base1.add_supplier(base1.supplier1, u"供商5", u'彭女士', '17301000000', '12344444445958', u'法人彭女士', u'大渡河')
#         #执行新增供应商操作
#         time.sleep(5)
#         base1.driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(base1.supplier1) #在列表中搜索该供应商
#         base1.driver.find_element_by_xpath('//*[@id="btnSearch"]').click() #点击搜索按钮
#         time.sleep(3)
#         text=base1.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td[2]').text #获取搜索出来的供应商名称
#         #断言：新增的供应商是否存在
#         assert text == base1.supplier1
#         time.sleep(3)
#
# #新增已存在的供应商
#     def test_eb_add_supplier1(self):
#         base1.add_supplier(base1.supplier1, u"供商5", u'彭女士', '17301000000', '123445958', u'法人彭女士', u'大渡河')
#         time.sleep(3)
#         base1.driver.find_element_by_xpath('//*[@id="btnSave"]')
#         time.sleep(10)
#
#
# #编辑供应商
#     def test_ec_edit_supplier(self):
#         time.sleep(2)
#         base1.edit_supplier1(base1.supplier1, '17300023', u"供商3") #执行编辑供应商操作
#         time.sleep(3)
#         text=base1.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[3]').text #获取联系人信息
#         #断言：联系人是否是改过之后的
#         assert text=="17300023"
#
#         time.sleep(3)
#
# #编辑供应商时把供应商名称修改为已存在的名称
#
#     def test_ed_edit_supplier1(self):
#
#         base1.edit_supplier2(base1.supplier1)  # 执行编辑供应商操作
#         time.sleep(3)
#         base1.driver.find_element_by_xpath('//*[@id="btnSave"]')
#         time.sleep(10)
#
# #文档导入供应商
#     def test_ee_import_supplier(self):
#         base1.import_supplier()
#         time.sleep(2)
#
# #导入已存在的供应商
#     def test_ef_import_supplier1(self):
#         base1.import_supplier()
#         time.sleep(4)
#         base1.driver.find_element_by_xpath('//*[@id="excelModal"]/div/div/div[1]/button/span').click()
#         time.sleep(3)
#
#
# #搜索供应商
#     def test_eg_search_supplier(self):
#         base1.search_supplier(base1.supplier1)
#         time.sleep(2)
#
#         text=base1.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td[2]').text
#         assert text == base1.supplier1
#
#
# #下载导入模板
#     def test_eh_download_template(self):
#
#         base1.download_template()
#         time.sleep(3)
#         base1.driver.find_element_by_xpath('//*[@id="excelModal"]/div/div/div[1]/button/span').click()
#         time.sleep(2)
#
#
# #删除供应商
#     def test_ei_delete_supplier(self):
#         base1.delete_supplier(base1.supplier1) #执行删除供应商操作
#         base1.delete_supplier(u'导入的供应商')
#         time.sleep(2)
#         # 断言："没有找到匹配的记录"元素是否存在
#
#         base1.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td')
#
#         time.sleep(3)
#
#
# #新增产品
#     def test_fa_add_goods(self):
#         base1.add_goods(base1.sku, u'大西瓜', u"大品牌", '1823849', '180', u"商超门店002", u"企业名称", "180", '23')
#         #新增产品操作
#         time.sleep(3)
#         text=base1.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text #获取新增产品sku
#         #断言：该sku的新增产品是否存在
#         assert text == base1.sku
#
# #编辑产品
#     def test_fb_edit_goods(self):
#         base1.edit_goods(base1.sku, u'新名') #编辑产品操作
#         time.sleep(3)
#         text=base1.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[4]').text #获取该产品更改后的产品名
#         #断言该产品名是否是更改后的
#         assert text == u"新名"
#
#         time.sleep(3)
#
# #下架产品
#     def test_fc_sold_out_goods(self):
#         base1.sold_out_goods(base1.sku) #下架产品操作
#         #断言是否看到"上架"按钮
#         base1.driver.find_element_by_xpath('//*[@class="btn btn-onSale btn-onSale-up"]').text
#         time.sleep(3)
#
# #上架产品
#     def test_fd_putaway_goods(self):
#         base1.putaway_goods(base1.sku) #上架产品操作
#         #断言是否看到"下架"按钮
#         base1.driver.find_element_by_xpath('//*[@class="btn btn-onSale btn-onSale-down"]').text
#
#         time.sleep(3)
#
#
#
#
# #删除商品
#     def test_fe_delete_goods1(self):
#         base1.delete_goods1(base1.sku)
#         base1.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td') #是否出现"没有找到匹配的记录"字段
#
#         time.sleep(3)
#
# #删除绑定批次的产品
#     def test_ff_delete_goods2(self):
#         base1.delete_goods2('sku0001')
#         time.sleep(3)
#         base1.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/button').click()
#         time.sleep(3)
#
# #同一个供应商下，新增产品SKU与数据库相同
#     def test_fg_add_goods1(self):
#         base1.add_goods1('sku0001', u'大西瓜', u"王婷2223")
#         base1.driver.find_element_by_xpath('//*[@id="Submit"]')
#
#         time.sleep(10)
#
# #下载导入模板
#     def test_fh_download_templet1(self):
#
#         base1.download_templet1()
#         base1.driver.find_element_by_xpath('//*[@id="excelModal"]/div/div/div[1]/button/span').click()
#         time.sleep(3)
#
#
#
# #批量导入产品
#     def test_fi_import_goods(self):
#         base1.import_goods()
#         goods1=base1.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[4]').text
#         goods2=base1.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[4]').text
#         goods3=base1.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[3]/td[4]').text
#         assert u"导入的商品" in goods1 and u"导入的商品" in goods2 and u"导入的商品" in goods3
#
#         time.sleep(3)
#
# #下载标品导入模板
#     def test_fj_download_templet2(self):
#         base1.download_templet2()
#         base1.driver.find_element_by_xpath('//*[@id="excelModalBP"]/div/div/div[1]/button/span').click()
#         time.sleep(3)
#
#
#
#
# #标品导入
#     def test_fk_import_bp(self):
#         base1.import_bp()
#         goods=base1.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[4]').text
#         assert  goods==u"导入的商品标品"
#
#
# #同一个供应商下，导入数据库中已存在的SKU产品
#     def test_fl_import2(self):
#         base1.import_bp1()
#         time.sleep(2)
#         base1.driver.find_element_by_xpath('//*[@id="excelModalBP"]/div/div/div[2]/form/div/div/div[1]/div[2]/div[4]/ul/li')
#         time.sleep(2)
#         base1.driver.find_element_by_xpath('//*[@id="excelModalBP"]/div/div/div[1]/button/span').click()
#         time.sleep(10)
#
#
# #全选删除产品
#     def test_fm_alldelete_goods(self):
#         base1.alldelete_goods(u"导入的商品")
#         time.sleep(3)
#         text=base1.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td').text
#         assert text == u"没有找到匹配的记录"
#         time.sleep(3)
#
#
# #点击下载产品二维码
#     def test_fn_download_ewm(self):
#         base1.download_ewm()
#         time.sleep(2)
#
# # 通过产品链接查看产品H5信息
#     def test_fo_goods_information(self):
#         base1.goods_information()
#         time.sleep(3)
#
# #按照搜索供应商查找产品
#     def test_fp_select_goods1(self):
#         base1.select_goods1(u'王婷2223')
#         time.sleep(2)
#         if  u"text1"==base1.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[9]').text:
#             return True
#         elif u"没有找到匹配的记录"==base1.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td').text:
#             return True
#         else:
#             return False
#
#
# #产品列表中筛选预包装类型的产品
#     def test_fqa_product_type_1(self):
#         base1.product_type_1(u"预包装")
#         time.sleep(3)
#         text=base1.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[6]').text #查看列表中产品的包装类型
#         print text
#         assert text==u"预包装"
#         time.sleep(3)
#
# #产品列表中筛选散货类型的产品
#     def test_fqb_product_type_2(self):
#         base1.product_type_2(u"散货")
#         time.sleep(3)
#         text=base1.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[6]').text #查看列表中产品的包装类型
#         assert text==u'散货'
#         time.sleep(3)
#
#
# #产品列表中筛选标品类型的产品
#     def test_fqc_product_type_3(self):
#         base1.product_type_3(u"标品")
#         time.sleep(3)
#         text = base1.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[6]').text #查看列表中产品的包装类型
#         assert text==u'标品'
#         time.sleep(3)
#
# #产品列表组合筛选产品
#     def test_fr_group_select(self):
#         base1.group_select(u'王婷2223', u"预包装", 'sku0001')
#         time.sleep(3)
#         text1 = base1.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[9]').text
#         text2 = base1.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[6]').text
#         text3 = base1.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[3]').text
#         assert text1==u'王婷2223' and text2==u"预包装" and text3=='sku0001'
#
#
#
# ##根据其他信息搜索产品
#     def test_fs_search_goods(self):
#         base1.search_goods(u'产品名')
#         time.sleep(3)
#         text1=base1.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[4]').text
#         print text1
#         assert text1==u'产品名'
#
#
#
# #新增检测报告
#     def test_ga_add_testreport(self):
#         base1.add_testreport(base1.reportname, '112121231', u'王格必')
#         text=base1.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[2]').text
#         assert text == base1.reportname
#         time.sleep(3)
#
# #根据检测名称搜索检测报告
#     def test_gb_search_testreport2(self):
#         base1.search_testreport2(base1.reportname)
#         text=base1.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[2]').text
#         assert text == base1.reportname
#         time.sleep(3)
#
# #编辑检测报告
#     def test_gc_edit_report(self):
#         base1.edit_report(base1.reportname)
#         time.sleep(3)
#
# #删除检测报告
#     def test_gd_delete_report(self):
#         base1.delete_report(base1.reportname)
#         time.sleep(2)
#         base1.driver.find_element_by_xpath('//*[@id="searchbox"]').clear()
#         base1.driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(base1.reportname)
#         base1.driver.find_element_by_xpath('//*[@id="btnSearch"]').click()
#         time.sleep(2)
#         base1.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td')
#         time.sleep(3)
#
# #自定义时间搜索检测报告
#     def test_ge_search_SalesRecord1(self):
#         base1.search_testreport1('2019-08-13', '2020-10-13')
#         try:
#             time0=base1.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[6]').text #获取搜索结果的出库时间
#             time0 = datetime.datetime.strptime(time0, '%Y-%m-%d')
#             time1=datetime.datetime.strptime('2019-08-13', '%Y-%m-%d')
#             time2=datetime.datetime.strptime('2020-10-13', '%Y-%m-%d')
#             assert time1<=time0<=time2
#         except:
#             base1.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td')
#
#         time.sleep(3)
#
#
# #编辑检测报告选择产品列表sku升降序排列
#     def test_gf_edit_report1(self):
#         base1.edit_report1(base1.reportname)
#         sku1=base1.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[3]').text
#         sku2=base1.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[2]/td[3]').text
#         assert sku1<sku2
#         time.sleep(2)
#         base1.driver.find_element_by_xpath('//*[@id="submit"]').click()  # 点击保存
#         time.sleep(3)
#
# #预警信息导出（营业执照过期）
#     def test_ha_warning_query1(self):
#         base1.warning_query1()
#
# #预警信息导出（食品经营许可证过期）
#     def test_hb_warning_query2(self):
#         base1.warning_query2()
#         time.sleep(2)
#
# #预警信息按时间从大到小排序
#     def test_hc_orderby_time1(self):
#         base1.orderby_time1()
#         time.sleep(2)
#
#
#
# #预警信息按时间从小到大排序
#     def test_hd_orderby_time2(self):
#         base1.orderby_time2()
#         time.sleep(2)
#
# #查看营业执照过期的全部供应商
#     def test_he_warning_view0(self):
#         base1.warning_view0()
#         time.sleep(2)
#
# #查看营业执照即将在一个月内过期的供应商
#     def test_hf_warning_view1(self):
#         base1.warning_view1()
#         time.sleep(2)
#
# #查看营业执照即将在两个月内过期的供应商
#     def test_hg_warning_view2(self):
#         base1.warning_view2()
#         time.sleep(2)
#
# #查看营业执照即将在三个月内过期的供应商
#     def test_hh_warning_view3(self):
#         base1.warning_view3()
#         time.sleep(2)
#
# #查看食品经营许可证的全部供应商
#     def test_hi_warning_view4(self):
#         base1.warning_view4()
#         time.sleep(2)
#
# #查看食品经营许可证即将在一个月内过期的供应商
#     def test_hj_warning_view5(self):
#         base1.warning_view5()
#         time.sleep(2)
#
# #查看食品经营许可证即将在两个月内过期的供应商
#     def test_hk_warning_view6(self):
#         base1.warning_view6()
#         time.sleep(2)
#
# #查看食品经营许可证即将在三个月内过期的供应商
#     def test_hl_warning_view7(self):
#         base1.warning_view7()
#         time.sleep(2)
#
# #通过搜索供应商搜索预警信息
#     def test_hm_search_warning(self):
#         base1.search_warning()
#         time.sleep(2)
#         assert u'测试超市企业账号'==base1.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td[2]').text
#
#
#
# #新增销售记录
#     def test_ia_add_SalesRecord(self):
#         base1.add_SalesRecord(u'王格必')
#         time.sleep(3)
#
#
# #编辑销售记录
#     def test_ib_edit_SalesRecord(self):
#         # text=base.driver.find_element_by_css_selector('#tables tr:nth-child(1) > td:nth-child(6)').text
#         # print text
#         base1.edit_SalesRecord('17300000000')
#         time.sleep(3)
#
#
# #删除销售记录
#     def  test_ic_delete_SalesRecord(self):
#         base1. delete_SalesRecord()
#         time.sleep(3)
#
#
# #添加销售记录-文档导入
#     def test_id_import_txt(self):
#         base1.import_txt()
#         time.sleep(8)
#
#
#
# # 查找出库记录，自定义搜索时间范围
#     def test_ie_search_SalesRecord1(self):
#         base1.search_SalesRecord1('2019-08-13', '2019-10-16')
#         try:
#             time0=base1.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[3]').text #获取搜索结果的出库时间
#             time0 = datetime.datetime.strptime(time0, '%Y-%m-%d')
#             time1=datetime.datetime.strptime('2019-08-13', '%Y-%m-%d')
#             time2=datetime.datetime.strptime('2019-10-13', '%Y-%m-%d')
#             assert time1<=time0<=time2
#         except:
#             base1.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td')
#         time.sleep(3)
#
# #根据出库单号搜索销售记录
#     def test_if_search_SalesRecord2(self):
#         base1.search_SalesRecord2()
#
# #编辑产品出库时出库明细产品sku升、降序排列
#     def test_ig_orderby_sku(self):
#         base1.orderby_sku(u'F3115714612U2009000007')
#         sku1=base1.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[3]').text
#         sku2=base1.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[2]/td[3]').text
#         sku1>sku2
#         base1.driver.find_element_by_xpath('//*[@id="submit"]').click()  # 点击保存按钮
#         time.sleep(2)
# #
# #打印产品出库
#     def test_ih_print_outsale(self):
#         base1.print_outsale()
#
#
# #下载Excel导入的模板
#     def test_ii_download_salestemplete(self):
#         base1.download_salestemplete()
#         time.sleep(3)
#         base1.driver.find_element_by_xpath('//*[@id="newExcelModal"]/div/div/div[1]/button/span').click()
#         time.sleep(3)
#
#
#
#
# # 手动添加进货登记
#     def test_ja_stock_registration(self):
#         base1.stock_registration(u"配送系统测试0612", u'王格必')
#         time.sleep(4)
#
#
# # 编辑进货登记
#     def test_jb_edit_stock_registration(self):
#         base1.edit_stock_registration(100)
#         time.sleep(3)
#
#
# #编辑进货登记信息选择产品列表产品sku升、降序排列
#     def test_jc_goods_sort(self):
#         base1.goods_sort('F3115714612N1908000005')
#
# # 删除进货登记
#     def test_jd_delete_stock_registration(self):
#         base1.delete_stock_registration()
#         time.sleep(3)
#
# #下载Excel导入的模板
#     def test_je_download_template0(self):
#         base1.download_template0()
#
# #Excel导入进货登记信息
#     def test_jf_excel_import(self):
#         base1.excel_import()
#
#
# #下载导入标品的模板
#     def test_jg_download_templatebp(self):
#         base1.download_templatebp()
#
#
# # 标品导入
#     def test_jh_bp_import(self):
#         base1.bp_import()
#
#
#
# #自定义时间搜索进货登记
#     def test_ji_search_bytime(self):
#         base1.search_bytime('2019-08-13', '2019-10-13')
#         try:
#             time0=base1.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[4]').text #获取搜索结果的进货时间
#             time0 = datetime.datetime.strptime(time0[:10], '%Y-%m-%d')
#             time1=datetime.datetime.strptime('2019-08-13 ', '%Y-%m-%d')
#             time2=datetime.datetime.strptime('2019-10-13 ', '%Y-%m-%d')
#             print time0,time1,time2
#             assert time1<=time0<=time2
#         except:
#             base1.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td')
#         time.sleep(3)
#
# # #根据入库单或sku搜索进货登记信息
#     def test_jj_search_byothers(self):
#
#         base1.search_byothers()
#
# #批次管理
# # 下载预付码
#     def test_ka_download_Prepaidcode(self):
#         base1.download_Prepaidcode()
#
#
# #下载追溯码
#     def test_kb_download_Traceablity_code(self):
#         base1.download_Traceablity_code()
#
# #预览二维码
#     def test_kc_preview_ewm(self):
#         base1.preview_ewm()
#         time.sleep(2)
#         base1.driver.find_element_by_xpath('//*[@id="qrcodeModal"]/div/div/div[1]/button').click()
#
# #通过预览二维码下方的链接查看H5批次信息
#     def test_kd_preview_rq(self):
#         base1.preview_rq('001', u'姜')
#
# #自定义时间搜索检测报告
#     def test_ke_search_by_time1(self):
#         base1.search_by_time1('2019-08-13', '2019-10-13')
#         time.sleep(3)
#         try:
#             time0=base1.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[9]').text #获取搜索结果的出库时间
#             time0 = datetime.datetime.strptime(time0[:10], '%Y-%m-%d')
#             time1=datetime.datetime.strptime('2019-08-13', '%Y-%m-%d')
#             time2=datetime.datetime.strptime('2019-10-13', '%Y-%m-%d')
#             assert time1<=time0<=time2
#         except:
#
#             base1.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td')
#         time.sleep(3)
#
# #根据包装类型搜索批次信息
#     def test_kf_search_by_type(self):
#         base1.search_by_type()
#
# #根据其他字段搜索批次信息
#     def test_kg_search_by_others(self):
#         base1.search_by_others('1100')
#         time.sleep(2)
#         text = base1.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[2]').text
#         assert text==u'1100'
#
#
# #新增门店反馈
#     def test_la_add_store_feedback(self):
#         base1.add_store_feedback(u'这是我添加的一段反馈内容')
#         time.sleep(3)
#         text=base1.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[4]').text #获取列表中最新一条的反馈内容
#         assert text==u'这是我添加的一段反馈内容'
#
# #搜索门店反馈
#     def test_lb_search_feedback(self):
#         base1.search_feedback(u'这是我添加的')
#         time.sleep(2)
#         text = base1.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[4]').text #获取搜索到的反馈内容
#         assert  u'这是我添加的' in text
#
# #删除门店反馈
#     def test_lc_delete_feedback(self):
#         base1.delete_feedback(u'我添加的')
#         time.sleep(2)
#         base1.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td')


if __name__ == "__main__":
    unittest.main()



