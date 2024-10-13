from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sorting = request.GET.get('sort')
    template = 'catalog.html'
    sorting_list = ['name', 'min_price', 'max_price']
    sorting_tuple = ('name', 'price', '-price')
    if sorting:
        num_sort = sorting_list.index(sorting)
        phone_obj = Phone.objects.order_by(sorting_tuple[num_sort])
        context = {'phones': phone_obj}
    else:
        phone_obj = Phone.objects.all()
        context = {'phones': phone_obj}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
