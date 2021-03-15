from django.shortcuts import render
from .models import 加工產品, 加工廠商, 產銷履歷商品, 餐廳, 銷售通路, 生產者, 加工產品, 餐廳_加工產品, 加工產品_銷售通路, 產銷履歷商品_銷售通路, 加工產品_原料, 餐廳_產銷履歷
from django.db.models import Prefetch
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def index(request):
    """View function for home page of site."""
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'base_template.html')


def createPage(request):
    return render(request, 'create_template.html')


def createPage1(request):
    return render(request, 'create1.html')


def createPage2(request):
    return render(request, 'create2.html')


def createPage3(request):
    return render(request, 'create3.html')


def search(request):
    catagory = request.GET.get('catagory')
    query = request.GET.get('query')

    if(catagory == "1"):
        tgap = 產銷履歷商品.objects.filter(
            產品名稱__contains=query).select_related('生產者ID')

        farmer = []

        for p in tgap:
            # Without select_related(), this would make a database query for each
            # loop iteration in order to fetch the related blog for each entry.
            farmer.append(p.生產者ID)
        product_list = zip(tgap, farmer)
        return render(request, 'result1.html', context={'category': catagory, 'product_list': product_list, 'product_name': query})
    elif(catagory == "2"):
        tgap = 產銷履歷商品.objects.filter(追溯號碼=query).select_related('生產者ID')

        farmer = []

        for p in tgap:
            # Without select_related(), this would make a database query for each
            # loop iteration in order to fetch the related blog for each entry.
            farmer.append(p.生產者ID)
        product_list = zip(tgap, farmer)

        return render(request, 'result2.html', context={'category': catagory, 'product_list': product_list, 'product_code': query})
    elif(catagory == "3"):
        resturant = 餐廳.objects.filter(名稱=query)
        tgap = 產銷履歷商品.objects.filter(餐廳_產銷履歷__餐廳ID__名稱=query)
        product = 加工產品.objects.filter(餐廳_加工產品__餐廳ID__名稱=query)
        r_t = 餐廳_產銷履歷.objects.filter(餐廳ID__名稱=query)
        r_p = 餐廳_加工產品.objects.filter(餐廳ID__名稱=query)
        product_list = zip(tgap, r_t)
        p_product_list = zip(product, r_p)

        return render(request, 'result3.html', context={'resturant_list': resturant, 'product_list': product_list, 'p_product_list': p_product_list, 'resturant': query})
    elif(catagory == "4"):
        sales = 銷售通路.objects.filter(銷售通路名稱__contains=query)

        tgap = 產銷履歷商品.objects.filter(
            產銷履歷商品_銷售通路__銷售通路ID__銷售通路名稱__contains=query)
        product = 加工產品.objects.filter(
            加工產品_銷售通路__銷售通路ID__銷售通路名稱__contains=query)
        s_t = 產銷履歷商品_銷售通路.objects.filter(銷售通路ID__銷售通路名稱__contains=query)
        s_p = 加工產品_銷售通路.objects.filter(銷售通路ID__銷售通路名稱__contains=query)
        product_list = zip(tgap, s_t)
        p_product_list = zip(product, s_p)

        return render(request, 'result4.html', context={'sales_list': sales, "product_list": product_list, "p_product_list": p_product_list, 'sales': query})
    elif(catagory == "5"):
        farmer = 生產者.objects.filter(生產者名稱=query)
        tgap = 產銷履歷商品.objects.filter(生產者ID__生產者名稱=query)

        return render(request, 'result5.html', context={'category': catagory, 'product_list': tgap, 'producer_list': farmer, 'producer_name': query})
    elif(catagory == "6"):
        p_product = 加工產品.objects.filter(
            加工產品名稱__contains=query).select_related('加工廠商ID')

        factory = []

        for pp in p_product:
            # Without select_related(), this would make a database query for each
            # loop iteration in order to fetch the related blog for each entry.
            factory.append(pp.加工廠商ID)
        p_product_list = zip(p_product, factory)

        tgap = 產銷履歷商品.objects.filter(加工產品_原料__加工批號__加工產品名稱__contains=query)
        p_t = 加工產品_原料.objects.filter(加工批號__加工產品名稱__contains=query)
        product_list = zip(tgap, p_t)

        return render(request, 'result6.html', context={'category': catagory, 'p_product_list': p_product_list, 'product_list': product_list, 'p_product_name': query})
    else:
        return render(request, 'result6.html', context={'p_product_list': []})


def createForm1(request):
    code = request.POST.get("product-code")
    name = request.POST.get('product-name')
    farmerID = request.POST.get('product-farmer')
    origin = request.POST.get('product-origin')
    date = request.POST.get('product-date')
    certiBody = request.POST.get('product-certificate')
    tgap = request.POST.get('product-standard')

    success = 1
    try:
        farmer = 生產者.objects.get(生產者ID=farmerID)
    except ObjectDoesNotExist:
        success = 0
        return render(request, 'create1.html', context={'success': success})
    try:
        tap = 產銷履歷商品.objects.create(
            追溯號碼=code, 產品名稱=name, 生產者ID=farmer, 產地=origin, 包裝日期=date, 驗證機構=certiBody, 產銷作業基準=tgap)
    except IntegrityError:
        success = 0

    if success:
        return render(request, 'create1.html', context={'product': tap, 'success': success})
    else:
        return render(request, 'create1.html', context={'success': success})


def createForm2(request):
    index = request.POST.get('farmer-id')
    name = request.POST.get('farmer-name')
    tel = request.POST.get('farmer-phone')
    address = request.POST.get('farmer-address')
    operator = request.POST.get('farmer-business')
    success = 1
    try:
        farmer = 生產者.objects.create(
            生產者ID=index, 生產者名稱=name, 電話=tel, 地址=address, 農產品經營業者=operator)
        # return render(request, 'create1.html', context = {'farmer':farmer, 'success':success})
    except IntegrityError:
        success = 0
        return render(request, 'create2.html', context={'success': success})
    else:
        return render(request, 'create2.html', context={'farmer': farmer, 'success': success})


def createForm3(request):
    index = request.POST.get('factory-id')
    name = request.POST.get('factory-name')
    tel = request.POST.get('factory-phone')
    address = request.POST.get('factory-address')
    success = 1
    try:
        factory = 加工廠商.objects.create(
            加工廠商ID=index, 加工廠商名稱=name, 地址=address, 電話=tel)
    except IntegrityError:
        success = 0
        return render(request, 'create3.html', context={'success': success})
    else:
        return render(request, 'create3.html', context={'factory': factory, 'success': success})


def deleteEntry(request):
    category = request.POST.get('category')
    entry = request.POST.get('entry')

    if(category == "5"):  # 生產者 (id)
        success = 1
        try:
            farmer = 生產者.objects.get(生產者ID=entry)
        except ObjectDoesNotExist:
            success = 0
        else:
            farmer.delete()
        return render(request, 'base_template.html', context={'success': success})
    elif(category == "6"):  # 加工產品批號
        success = 1
        try:
            product = 加工產品.objects.get(加工批號=entry)
        except ObjectDoesNotExist:
            success = 0
        else:
            product.delete()
        return render(request, 'base_template.html', context={'success': success})

    elif(category == "1" or category == "2"):  # 產銷履歷商品(追溯號碼)
        success = 1
        try:
            tap = 產銷履歷商品.objects.get(追溯號碼=entry)
        except ObjectDoesNotExist:
            success = 0
        else:
            tap.delete()
        return render(request, 'base_template.html', context={'success': success})


def rerouteUpdate(request):
    category = request.GET.get('category')
    entry = request.GET.get('entry')

    if(category == "1"):
        tap = 產銷履歷商品.objects.get(追溯號碼=entry)
        return render(request, 'update1.html', context={'product': tap})
    elif(category == "5"):
        farmer = 生產者.objects.get(生產者ID=entry)
        return render(request, 'update2.html', context={'farmer': farmer})
    elif(category == "6"):
        p_product = 加工產品.objects.get(加工批號=entry)
        return render(request, 'update3.html', context={'p_product': p_product})
    else:
        return render(request, 'update1.html', context={'product': []})


def updateForm1(request):
    code = request.POST.get('product-code')
    name = request.POST.get('product-name')
    origin = request.POST.get('product-origin')
    certiBody = request.POST.get('product-certificate')
    tgap = request.POST.get('product-standard')

    success = 1
    try:
        tap = 產銷履歷商品.objects.filter(追溯號碼=code)
    except ObjectDoesNotExist:
        success = 0
        return render(request, 'update1.html', context={'success': success})
    else:
        tap.update(產品名稱=name, 產地=origin, 驗證機構=certiBody, 產銷作業基準=tgap)
        return render(request, 'update1.html', context={'product': tap, 'success': success})


def updateForm2(request):
    index = request.POST.get('farmer-id')
    name = request.POST.get('farmer-name')
    tel = request.POST.get('farmer-phone')
    address = request.POST.get('farmer-address')
    operator = request.POST.get('farmer-business')
    success = 1
    try:
        farmer = 生產者.objects.filter(生產者ID=index)
    except ObjectDoesNotExist:
        success = 0
        return render(request, 'update2.html', context={'success': success})
    else:
        farmer.update(生產者名稱=name, 電話=tel, 地址=address, 農產品經營業者=operator)
        return render(request, 'update2.html', context={'farmer': farmer, 'success': success})


def updateForm3(request):
    productID = request.POST.get("pproduct-code")
    name = request.POST.get("pproduct-name")
    amount = request.POST.get("pproduct-quantity")

    success = 1

    try:
        product = 加工產品.objects.filter(加工批號=productID)
    except ObjectDoesNotExist:
        success = 0
        return render(request, 'update3.html', context={'success': success})
    # else:
    product.update(加工產品名稱=name, 產量=amount)
    return render(request, 'update3.html', context={'p_product': product, 'success': success})
