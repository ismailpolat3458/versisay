from django.urls import path
from . import views
urlpatterns=[
    path("/",views.root),
    path("/cpu",views.cpu),
    path("cpu/percent",views.cpu_percent),
    path("/cpu/count",views.cpu_count),
    path("/cpu/freq",views.cpu_freq),
    path("/cpu/times",views.cpu_times),
    path("/cpu/times/user",views.cpu_times_user()),
    path("/cpu/times/system",views.cpu_times_system),
    path("/cpu/times/idle",views.cpu_times_idle),
    path("/ram",views.ram),
    path("/ram/total",views.ram_total),
    path("/ram/available",views.ram_available),
    path("/ram/used",views.ram_used),
    path("/ram/percent",views.ram_percent),
    path("/disk",views.disk),
    path("/disk/total",views.disk_total),
    path("/disk/free",views.disk_free),
    path("/disk/used",views.disk_used),
    path("/disk/percent",views.disk_percent),
    path("/network",views.network),
    path("network(bytes_sent",views.net_bytes_sent),
    path("/network/bytes_recv",views.net_bytes_recv),











]