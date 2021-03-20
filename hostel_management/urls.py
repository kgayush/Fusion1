from django.conf.urls import url

app_name = 'hostelmanagement'

urlpatterns = [
    url('allotedroom', views.alloted_room, name="allotedroom"),
    url('upload', views.add_hall_room, name="upload"),
]