from django.conf.urls import url

app_name = 'hostelmanagement'

urlpatterns = [
    url('allotedroom', views.alloted_room, name="allotedroom")
]