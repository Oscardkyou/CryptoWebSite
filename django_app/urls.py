from django.urls import path
from django_app import views
urlpatterns = [
path("", views.home, name="home"),
path("nav/", views.nav, name="nav"),
path("home/posts/", views.posts, name="posts"),
path("home/money/", views.money, name="money"),
path("home/blockchain/", views.blockchain, name="blockchain"),
path("home/defi/", views.defi, name="defi"),
path("home/coins/", views.coins, name="coins"),
path("home/solidity/", views.solidity, name="solidity"),
path("home/exchanges/", views.exchanges, name="exchanges"),
path("home/vyper/", views.vyper, name="vyper"),

#TODO
    path("home/posts/<str:pk>/", views.post1, name="post1"),
    ]