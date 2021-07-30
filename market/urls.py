from django.urls import path
from . import views

urlpatterns = [
    path('fabric/<str:market_name>/', views.market_fabrics_view, name='market_fabrics'),
    path('footwear/<str:market_name>/', views.market_footwear_view, name='market_footwear'),
    path('watches/<str:market_name>/', views.market_watch_view, name='market_watches'),
    path('category/<str:market_name>/', views.market_category, name='market_category'),
    path('grain/<str:market_name>/', views.market_grain_view, name='market_grain'),
    path('livestock/<str:market_name>/', views.market_livestock_view, name='market_livestock'),
    path('poultry/<str:market_name>/', views.market_poultry_view, name='market_poultry'),
    path('tuber/<str:market_name>/', views.market_tuber_view, name='market_tuber'),
    path('grocery/<str:market_name>/', views.market_grocery_view, name='market_grocery'),
    path('vegetable/<str:market_name>/', views.market_vegetable_view, name='market_vegetable'),
    path('frozen/<str:market_name>/', views.market_frozen_view, name='market_frozen'),
]