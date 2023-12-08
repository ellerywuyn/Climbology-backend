from django.urls import path
from . import views

urlpatterns = [
    # path("/", views.route_operations, name="route_operations"),
    path("update_hold/", views.update_hold, name="update_hold"),
    path("delete_hold/", views.delete_hold, name="delete_hold"),
    path("delete_move/", views.delete_move, name="delete_move"),
    path("find_holds_by_property/", views.find_holds_by_property, name="find_holds_by_property"),
    path("find_routes_by_property/", views.find_routes_by_property, name="find_routes_by_property"),
    # path("/", views.register_user, name="register")
]