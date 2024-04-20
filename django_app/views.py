from django.shortcuts import render
from django_app import models
from django.core.paginator import Paginator


def home(request):
    search = request.POST.get("search", "")
    posts = models.Currency.objects.all().filter(title__icontains=search)
    limit_post_by_page = 9  # Увеличьте количество постов на странице до 9
    selected_page = request.GET.get(key="page", default=1)
    paginator = Paginator(posts, limit_post_by_page)
    current_page = paginator.get_page(selected_page)

    # Разделение постов на группы по 3
    first_three_posts = current_page[:3]
    second_three_posts = current_page[3:6]
    third_three_posts = current_page[6:9]

    return render(request, 'home.html', context={"search": search,
                                                 "first_three_posts": first_three_posts,
                                                 "second_three_posts": second_three_posts,
                                                 "third_three_posts": third_three_posts})

def vyper(request):

    return render(request, 'crypto/vyper.html')

def posts(request):
    search = request.POST.get("search", "")
    posts = models.Currency.objects.all().filter(title__icontains=search)
    limit_post_by_page = 10
    selected_page = request.GET.get(key="page", default=1)
    paginator = Paginator(posts, limit_post_by_page)
    current_page = paginator.get_page(selected_page)

    return render(request, 'posts.html',context={"current_page": current_page,"search": search})
def nav(request):
    search = request.POST.get("search", "")
    posts = models.Currency.objects.all().filter(title__icontains=search)
    limit_post_by_page = 10
    selected_page = request.GET.get(key="page", default=1)
    paginator = Paginator(posts, limit_post_by_page)
    current_page = paginator.get_page(selected_page)

    return render(request, 'components/nav.html',context={"current_page": current_page,"search": search})

def money(request):
    return render(request, 'money.html')
def solidity(request):
    return render(request, 'crypto/solidity.html')
def defi(request):
    return render(request, 'crypto/defi.html')
def coins(request):
    return render(request, 'crypto/coins.html')
def blockchain(request):
    return render(request, 'crypto/blockchain.html')
def exchanges(request):
    return render(request, 'crypto/exchanges.html')

def post1(request, pk: str):
    post = models.Currency.objects.get(id=int(pk))
    return render(request, f'posts/post{pk}_detail.html')

