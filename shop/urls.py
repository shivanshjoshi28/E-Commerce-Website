from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="BlogHome"),
    path("test/",views.test,name="test"),
    path("about/",views.about,name="About Us"),
    path("contact/",views.contact,name="Contact"),
    path("tracker/",views.tracker,name="Tracking The Order"),
    path("search/",views.search,name="Search"),
    path("products/<int:myid>",views.products,name="BlogHome"),
    path("checkOut/",views.checkout,name="BlogHome"),
    path("handlerequest/", views.handlerequest, name="HandleRequest"),

]
