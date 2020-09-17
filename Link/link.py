#coding=utf-8

import base01
import unittest
import time


# 追溯链条1
# 1、种植系统：添加供应商-添加产品-采收-出库
# 2、商超门店：扫码入库（检测产品是否添加、是否有新增的供应商、检查入库明细是否正确）
# 3、超市系统：扫码入库（检测产品是否添加、是否有新增的供应商、检查入库明细是否正确）--出库
# 4、检测h5追溯链条:种植出库-超市入库-超市出库-商超入库
# #
class Testlink_1(unittest.TestCase):
#登录种植系统
    def test_1aa_login(self):
        try:
            base01.login(base01.planting)
            print 'test_1aa_login test pass'
        except:
            print 'test_1aa_login test fail'

#种植 新增产品
    def test_1ab_add_goods_planting(self):
        try:
            base01.add_goods_planting(base01.sku,base01.goods_name,u"大品牌",'1823849',u"企业名称","180",'23')
            print 'test_1ab_add_goods_planting test pass'
        except:
            print 'test_1ab_add_goods_planting test fail'


#种植采收
    def test_1ac_recovery(self):
        try:
            base01.recovery()
            print 'test_1ac_recovery test pass'
        except:
            print 'test_1ac_recovery test fail'
        time.sleep(2)
#
#  种植系统添加销售记录(出库)、登录商超系统、商超门店添加进货登记
    def test_1ad(self):
        try:
            base01.add_SalesRecord_planting('sku00000/000')
            print 'test_1ad_add_SalesRecord_planting test pass'
        except:
            print 'test_1ad_add_SalesRecord_planting test fail'

        code = base01.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[2]').text  # 获取出库单号
        base01.driver.find_element_by_xpath('//*[@id="passwordFrom"]/div/ul/li[2]/a').click()  # 退出种植系统

        try:
            base01.login(base01.store) #登录商超系统
            print 'test_1ad_login test pass'
        except:
            print 'test_1ad_login test fail'
        try:
            base01.stock_registration_store(code)
            print 'test_1ad_stock_registration_store test pass'
        except:
            print 'test_1ad_stock_registration_store test pass'
        time.sleep(3)

#商超门店 查看产品管理列表是否添加了该产品
    def test_1ba_check_goods_store(self):
        try:
            base01.check_goods_store(base01.sku)
            time.sleep(2)
            text=base01.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[3]').text
            assert text==base01.sku
            print 'test_1ba_check_goods_store test pass'
        except:
            print 'test_1ba_check_goods_store test fail'


#商超门店 查看是否添加了供应商
    def test_1bb_check_supplier_sotre(self):
        try:
            base01.check_supplier_sotre(base01.supplier)
            time.sleep(2)
            text=base01.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td[2]').text
            assert text==base01.supplier
            print 'test_1bb_check_supplier_sotre test pass'
        except:
            print 'test_1bb_check_supplier_sotre test fail'


#商超门店查看批次信息是否正确
    def test_1bc_check_batch_sotre(self):
        try:
            base01.check_batch_sotre(base01.sku)
            time.sleep(3)
            sku=base01.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[2]').text
            name=base01.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[3]').text
            supplier=base01.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[4]').text
            number=base01.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[5]').text
            assert sku==base01.sku and name==base01.goods_name and supplier==base01.supplier and number==u'2000(-)'
            print 'test_1bc_check_batch_sotre test pass'
        except:
            print 'test_1bc_check_batch_sotre test fail'


# 商超添加销售记录(出库)、登录超市系统、超市添加进货登记
    def test_1bd(self):
        try:
            base01.add_SalesRecord_store(base01.sku)
            print 'test_1bd_add_SalesRecord1 test pass'
        except:
            print 'test_1bd_add_SalesRecord1 test fail'
        time.sleep(2)
        code = base01.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[2]').text  # 获取出库单号
        base01.driver.find_element_by_xpath('//*[@id="passwordFrom"]/div/ul/li[2]/a').click()  # 退出商超系统
        try:
            base01.login(base01.supermarket) #登录超市系统
            print 'test_1bd_login test pass'
        except:
            print 'test_1bd_login test fail'
        try:
            base01.stock_registration_supermarket(code)
            print 'test_1bd_stock_registration_supermarket test pass'
        except:
            print 'test_1bd_stock_registration_supermarket test pass'
        time.sleep(3)

#超市系统 查看产品管理列表是否添加了该产品
    def test_1ca_check_goods_supermarket(self):
        try:
            base01.check_goods_supermarket(base01.sku)
            time.sleep(2)
            text=base01.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[3]').text
            assert text==base01.sku
            print 'test_1ca_check_goods test pass'
        except:
            print 'test_1ca_check_goods test fail'


#超市系统查看是否添加了供应商
    def test_1cb_check_supplier_supermarket(self):
        try:
            base01.check_supplier_supermarket(base01.supplier)
            time.sleep(2)
            text=base01.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td[2]').text
            assert text==base01.supplier
            print 'test_1cb_check_supplier_supermarket test pass'
        except:
            print 'test_1cb_check_supplier_supermarket test fail'



#查看批次信息是否正确
    def test_1cc_check_batch_supermarket(self):
        try:
            base01.check_batch_supermarket(base01.sku)
            time.sleep(3)
            sku=base01.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[2]').text
            name=base01.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[3]').text
            supplier=base01.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[4]').text
            number=base01.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[5]').text
            assert sku==base01.sku and name==base01.goods_name and supplier==base01.supplier1 and number==u'2000(-)'
            print 'test_1cc_check_batch_supermarket test pass'
        except:
            print 'test_1cc_check_batch_supermarket test fail'


#查看超市H5信息
    def test_1cd_preview_H5_supermarket(self):
        try:
            base01.preview_H5_supermarket(base01.sku)
            text1 =base01.driver.find_element_by_xpath('//*[@id="div2"]/ul/li[4]/div[2]').text
            text2 =base01.driver.find_element_by_xpath('//*[@id="div2"]/ul/li[3]/div[2]').text
            text3 =base01.driver.find_element_by_xpath('//*[@id="div2"]/ul/li[2]/div[2]').text
            text4 =base01.driver.find_element_by_xpath('//*[@id="div2"]/ul/li[1]/div[2]').text
            assert u'在种植系统测试0612出库' in text1 and u'在商超门店测试企业入库' in text2 and u'在商超门店测试企业出库' in text3 and u'在超市系统测试0612入库' in text4
            print 'test_1cd_preview_H5_supermarket test pass'

        except:
            print 'test_1cd_preview_H5_supermarket test fail'
        base01.driver.get(base01.supermarket['url'])
        time.sleep(3)

#删除超市系统数据
    def test_1da_delete_supermarket(self):
        try:
            base01.delete_registration_supermarket(base01.sku) #删除进货登记
            print 'test_1da_delete_registration_supermarket test pass'
        except:
            print 'test_1da_delete_registration_supermarket test fail'
        time.sleep(2)
        try:
            base01.delete_goods_supermarket()  #删除产品
            print 'test_1da_delete_goods_supermarket test pass'
        except:
            print 'test_1da_delete_goods_supermarket test test fail'
        time.sleep(2)
        try:
            base01.delete_supplier_supermarket() #删除供应商
            print 'test_1da_delete_supplier_supermarket test pass'
        except:
            print 'test_1da_delete_supplier_supermarket test fail'
        base01.driver.find_element_by_xpath('//*[@id="passwordFrom"]/div/ul/li[2]/a').click()  # 退出超市系统


#删除商超系统数据
    def test_1db_delete_store(self):
        base01.login(base01.store)
        try:
            base01.delete_stock_store(base01.sku) #删除进货登记
            print 'test_1db_delete_stock_store test pass'
        except:
            print 'test_1db_delete_stock_store test fail'
        time.sleep(2)
        try:
            base01.delete_goods_store(base01.sku) #删除产品
            print 'test_1db_delete_goods_store test pass'
        except:
            print 'test_1db_delete_goods_store test fail'
        time.sleep(2)
        try:
            base01.delete_supplier_store(base01.supplier) #删除供应商
            print 'test_1db_delete_supplier_store test pass'
        except:
            print 'test_1db_delete_supplier_store test fail'
        base01.driver.find_element_by_xpath('//*[@id="passwordFrom"]/div/ul/li[2]/a').click()  # 退出商超系统


#删除种植系统数据
    def test_1dc_delete_planting(self):
        base01.login(base01.planting)
        try:
            base01.delete_batch_planting(base01.sku)
            print 'test_1dc_delete_batch_planting test pass'
        except:
            print 'test_1dc_delete_batch_planting test fail'
        time.sleep(3)
        try:
            base01.delete_goods_planting(base01.sku)
            print 'test_1dc_delete_goods_planting test pass'
        except:
            print 'test_1dc_delete_goods_planting test fail'

        base01.driver.find_element_by_xpath('//*[@id="passwordFrom"]/div/ul/li[2]/a').click()  # 退出种植系统



# #追溯链条二
# # 1、种植系统：添加供应商-添加产品-采收-出库
# # 2、加工系统：扫码添加（检测原辅料管理产品是否添加、是否有新增的供应商、检查入库明细是否正确）-新增加工品-加工品添加到bom管理-加工品入库-出库
# # 3、检测h5追溯链条:种植出库-加工入库-加工出库
# # 4.农贸：扫码入库（检测产品是否添加、是否有新增的供应商、检查入库明细是否正确）
# class Testlink_2(unittest.TestCase):
# #登录种植系统
#     def test_2aa_login(self):
#         try:
#             base01.login(base01.planting)
#             print 'test_2aa_login test pass'
#         except:
#             print 'test_2aa_login test fail'
#     #种植采收
#     def test_2ab_recovery(self):
#         try:
#             base01.recovery()
#             print 'test_2ab_recovery test pass'
#         except:
#             print 'test_2ab_recovery test fail'
#         time.sleep(2)
#
# #  种植系统添加销售记录(出库)、登录加工系统、加工系统添加进货登记
#     def test_2ac(self):
#         try:
#             base01.add_SalesRecord_planting('sku00000/000')
#             print 'test_2ac_add_SalesRecord_planting test pass'
#         except:
#             print 'test_2ac_add_SalesRecord_planting test fail'
#
#         code = base01.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[2]').text  # 获取出库单号
#         base01.driver.find_element_by_xpath('//*[@id="passwordFrom"]/div/ul/li[2]/a').click()  # 退出种植系统
#
#         try:
#             base01.login(base01.machining) #登录加工系统
#             print 'test_2ac_login test pass'
#         except:
#             print 'test_2ac_login test fail'
#         try:
#             base01.stock_registration_machining(code)
#             print 'test_2ac_stock_registration_store test pass'
#         except:
#             print 'test_2ac_stock_registration_store test pass'
#         time.sleep(3)
#
# #加工系统检测原辅料管理产品是否添加
#     def test_2ba_check_goods_machining(self):
#         base01.check_goods_machining(base01.sku)
#         try:
#             text=base01.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[3]').text
#             assert text==base01.sku
#             print 'test_2ba_check_goods_machining test pass'
#         except:
#             print 'test_2ba_check_goods_machining test fail'
#
#         time.sleep(2)
#
# #加工系统 检测供应商是否添加
#     def test_2bb_check_supplier_machining(self):
#         base01.check_supplier_machining(base01.supplier)
#         try:
#             text=base01.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td[2]').text
#             assert text==base01.supplier
#             print 'test_2bb_check_supplier_machining test pass'
#         except:
#             print 'test_2bb_check_supplier_machining test fail'
#         time.sleep(2)
#
# #加工查看批次信息是否正确
#     def test_2bc_check_batch_machining(self):
#         base01.check_batch_machining(base01.sku)
#         try:
#             text=base01.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td[2]').text
#             assert text==base01.sku
#             print 'test_2bc_check_batch_machining test pass'
#         except:
#             print 'test_2bc_check_batch_machining test fail'
#         time.sleep(2)
#
#
# #加工系统加工品添加到bom管理
#     def test_2be_add_bom_machining(self):
#         base01.add_bom_machining(base01.sku1,base01.sku)
#         try:
#             text=base01.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[1]').text
#             assert text==base01.sku1
#             print 'test_2be_add_bom_machining test pass'
#         except:
#             print 'test_2be_add_bom_machining test fail'
#
# #加工系统加工品入库
#     def test_2bf_add_batch_machining(self):
#         base01.add_batch_machining(base01.sku1)
#         try:
#             text=base01.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[2]').text
#             assert text==base01.sku1
#             print 'test_2bf_add_batch_machining test pass'
#         except:
#             print 'test_2bf_add_batch_machining test fail'
#
#
# #加工添加销售记录、登录农贸系统、农贸扫码入库
#     def test_2bg(self):
#         try:
#             base01.add_SalesRecord_machining(base01.sku1) #加工添加销售记录
#             print 'test_2bg_add_SalesRecord_machining test pass'
#         except:
#             print 'test_2bg_add_SalesRecord_machining test fail'
#         code = base01.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[2]').text  # 获取出库单号
#         base01.driver.find_element_by_xpath('//*[@id="passwordFrom"]/div/ul/li[2]/a').click()  # 退出加工系统
#         try:
#             base01.login(base01.farmersmarket) #登录农贸系统
#             print 'test_2bg_login test pass'
#         except:
#             print 'test_2bg_login test fail'
#         try:
#             base01.stock_registration_farmersmarket(code) #农贸系统扫码入库
#             print 'test_2bg_stock_registration_farmersmarket test pass'
#         except:
#             print 'test_2bg_stock_registration_farmersmarket test pass'
#
#         time.sleep(3)
#
# #加工系统查看H5
#     def test_2bh_preview_H5_machining(self):
#         base01.driver.find_element_by_xpath('//*[@id="passwordFrom"]/div/ul/li[2]/a').click()  # 退出农贸系统
#         base01.login(base01.machining) #登录加工系统
#         try:
#             base01.preview_H5_machining(base01.sku1)  # 获取H5信息
#             text=base01.driver.find_element_by_xpath('//*[@id="productIntroduction"]/div/ul/li[2]/span').text
#             assert '000' == text
#             print 'test_2bh_preview_H5_machining test pass'
#         except:
#             print 'test_2bh_preview_H5_machining test fail'
#         time.sleep(2)
#
#
# #删除bom管理里该产品
#     def test_2bi_delete_bom_machining(self):
#         base01.driver.get(base01.machining['url'])
#         try:
#             base01.delete_bom_machining(base01.sku1)
#             print 'test_2bi_delete_bom_machining test pass'
#         except:
#             print 'test_2bi_delete_bom_machining test fail'

#追溯链条3
# 1、商超门店：新增产品-入库-出库
# 2、批发系统：扫码入库-（检测产品管理里面新增该产品、新增供应商、入库明细）-出库
# 3、团体采购：扫码入库（检测产品是否添加、是否有新增的供应商、检查入库明细是否正确）
# 4.检测h5追溯链条：商超门店-团体采购-批发系统
#
# class Testlink_3(unittest.TestCase):
#     #商超门店添加进货登记（手动登记）
#     def test_3ab_stock_registration_store1(self):
#         base01.login(base01.store)
#         try:
#             base01.stock_registration_store1()
#             print 'test_3ab_stock_registration_store1 test pass'
#         except:
#             print 'test_3ab_stock_registration_store1 test fail'
#
#     #商超门店出库、登录批发系统、批发系统扫码入库
#     def test_3ac(self):
#         try:
#             base01.add_SalesRecord_store(base01.sku2) #商超门店添加销售记录（出库）
#             print 'test_3ac_add_SalesRecord_store test pass'
#         except:
#             print 'test_3ac_add_SalesRecord_store test fail'
#         code = base01.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[2]').text  # 获取出库单号
#         base01.driver.find_element_by_xpath('//*[@id="passwordFrom"]/div/ul/li[2]/a').click()  # 退出商超系统
#
#         try:
#             base01.login(base01.wholesalemarket)  # 登录批发系统
#             base01.stock_registration_wholesalemarket(code) #批发系统扫码入库
#             print 'test_3ac_stock_registration_wholesalemarket test pass'
#         except:
#             print 'test_3ac_stock_registration_wholesalemarket test fail'
#
#     #批发系统出库、登录团体采购系统、团采扫码入库
#     def test_3ad(self):
#         try:
#             base01.add_SalesRecord_wholesalemarket(u'大苹果') #批发系统出库
#             print 'test_3ad_add_SalesRecord_wholesalemarket test pass'
#         except:
#             print 'test_3ad_add_SalesRecord_wholesalemarket test fail'
#
#         code = base01.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[1]').text  # 获取出库单号
#         base01.driver.find_element_by_xpath('//*[@id="passwordFrom"]/div/ul/li[2]/a').click()  # 退出批发系统
#         try:
#             base01.login(base01.grouppurchasing)
#             base01.stock_registration_grouppurchasing(code)
#             print 'test_3ad_stock_registration_grouppurchasing test pass'
#         except:
#             print 'test_3ad_stock_registration_grouppurchasing test fail'
#
#     #查看团采H5信息
#     def test_3ae_preview_H5_grouppurchasing(self):
#         try:
#             base01.preview_H5_grouppurchasing(base01.sku2)
#             text=base01.driver.find_element_by_xpath('//*[@id="div2"]').text
#             assert u'在供应商03出库' in text and u'在商超门店测试企业入库'in text and u'在梦梦批发入库' in text and u'在团体采购测试0612入库' in text
#             print 'test_3ae_preview_H5_grouppurchasing test pass'
#         except:
#             print 'test_3ae_preview_H5_grouppurchasing test fail'
#
#
#     #团采删除批次信息
#     def test_3af_delete_registration_grouppurchasing(self):
#         base01.driver.get(base01.grouppurchasing['url'])
#         try:
#             base01.delete_registration_grouppurchasing(base01.sku2)
#             print 'test_3af_delete_registration_grouppurchasing test pass'
#         except:
#             print 'test_3af_delete_registration_grouppurchasing test fail'
#
#     #团采删除供应商
#     def test_3ag_delete_supplier_grouppurchasing(self):
#         try:
#             base01.delete_supplier_grouppurchasing(u'梦梦批发')
#             print 'test_3ag_delete_supplier_grouppurchasing test pass'
#         except:
#             print 'test_3ag_delete_supplier_grouppurchasing test fail'
#
#
#     #批发系统删除批次信息
#     def test_3ah_delete_registration_wholesalemarket(self):
#         base01.driver.find_element_by_xpath('//*[@id="passwordFrom"]/div/ul/li[2]/a').click()  # 退出团采系统
#         base01.login(base01.wholesalemarket) #登录批发系统
#         try:
#             base01.delete_registration_wholesalemarket(base01.sku2)
#             print 'test_3ah_delete_registration_wholesalemarket test pass'
#         except:
#             print 'test_3ah_delete_registration_wholesalemarket test fail'
#
#     #批发删除供应商
#     def test_3ai_delete_supplier_wholesalemarket(self):
#         try:
#             base01.delete_supplier_wholesalemarket(u'商超门店测试企业')
#             print 'test_3ai_delete_supplier_wholesalemarket test pass'
#         except:
#             print 'test_3ai_delete_supplier_wholesalemarket test fail'
#
#
#     #商超门店删除进货登记
#     def test_3aj_delete_stock_store(self):
#         base01.driver.find_element_by_xpath('//*[@id="passwordFrom"]/div/ul/li[2]/a').click()  # 退出批发系统
#         base01.login(base01.store) #登录批发系统
#         try:
#             base01.delete_stock_store(base01.sku2)
#             print 'test_3aj_delete_stock_store test pass'
#         except:
#             print 'test_3aj_delete_stock_store test fail'
#




if __name__ =="__main__":
    unittest.main()

