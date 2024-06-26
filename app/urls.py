from django.urls import path
from app import views



urlpatterns = [
     path('',views.home,name='home'),
     path('shop',views.shop,name="shop"),
     
     path('adminhome',views.adminhome,name='adminhome'),
     path('logouts',views.logouts,name='logouts'),
     path('contact',views.contact,name='contact'),
     path('about',views.about,name='about'),
     path('log',views.logins,name='logins'),
     path('signup',views.signup,name='signup'),
     path('productregistartion',views.register_product,name='register_product'),
     path('viewproductadmin',views.viewproductadmin,name='viewproductadmin'),
     path('backtoadmin',views.backtoadmin,name='backtoadmin'),
     path('deleteproduct/<int:id>',views.deleteproduct,name='deleteproduct'),
     path('editproduct/<int:id>',views.editproduct,name='editproduct'),
     path('updateproduct/<int:id>',views.updateproduct,name='updateproduct'),
     path('feedback',views.feed_back,name='feed_back'),
     path('place_order/<int:product_id>/', views.place_order, name='place_order'),
     path('order_sucess',views.order_sucess,name='order_sucess'),
     path('approve',views.vieworder_details,name='vieworder_details'),
     path('order_success',views.order_sucess,name='order_success'),
     path('editprofile',views.editprofile,name='editprofile'),
     path('updateprofile',views.updateprofile,name='updateprofile'),
     path('ordercustomer_view',views.ordercustomer_view,name='ordercustomer_view'),
     path('deleteorder/<int:id>',views.deleteorder,name='deleteorder'),
     path('cancelorder',views.canceluserorder,name='canceluserorder'),
     path('approvereject',views.approvereject,name='approvereject'),
     path('orderpending',views.orderpending,name='orderpending'),
     path('approve_order/<int:id>',views.approve_order,name='approve_order'),
     path('orderstatus/<int:id>',views.orderstatus,name='orderstatus'),
     path('orderdeletecustomer/<int:id>',views.orderdeletecustomer,name='orderdeletecustomer'),


     
     
]