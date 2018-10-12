# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
 
from TestModel.models import Test
 

# 添加数据
def testdb1(request):
    # 添加值为runoob的数据
    v = 'runoob'
    test1 = Test(name=v)
    test1.save()
    s = '添加数据 %s 成功' % v
    return HttpResponse("<p> %s </p>" % s)

# 获取数据
def testdb2(request):
    # 显示所有数据

    # filter相当于SQL中的WHERE，可设置条件过滤结果
    response1 = Test.objects.filter(id=3) 
    
    # 获取单个对象
    response2 = Test.objects.get(id=3) 
    
    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    Test.objects.order_by('name')[3:5]
    
    #数据排序
    Test.objects.order_by("id")
    
    # 上面的方法可以连锁使用
    Test.objects.filter(name="runoob").order_by("id")
    
    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = Test.objects.all()
    response = ""
    response3 = ""

    # 输出所有数据
    for var in list:
        response3 += var.name + ", "
    response = '所有数据为：%s' % response3
    return HttpResponse("<p> %s </p>" % response)

# 更新数据
def testdb3(request):
    # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
    k = 1
    v = 'Google'
    test1 = Test.objects.get(id=k)
    test1.name = v
    test1.save()
    
    # 另外一种方式
    #Test.objects.filter(id=1).update(name='Google')
    
    # 修改所有的列
    # Test.objects.all().update(name='Google')
    s = '修改键：%d, 值为：%s ' % (k,v)
    return HttpResponse("<p>%s</p>" % s)


# 删除数据
def testdb4(request):
    # 删除id=1的数据
    k = 2
    
    test1 = Test.objects.get(id=k)
    test1.delete()
    
    # 另外一种方式
    # Test.objects.filter(id=1).delete()
    
    # 删除所有数据
    # Test.objects.all().delete()
    s = '删除 %s 成功' % k
    return HttpResponse("<p>%s</p>" % s)