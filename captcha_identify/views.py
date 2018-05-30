
from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def apis(request):
    data = {'name': '你爹'}  # 返<span style="color:#ff0000;">回给客户端的数据</span>
    if request.method == "POST":
        print(request.POST)     # <span style="color:#ff0000;">查看客户端发来的请求内容</span>
    return JsonResponse(data)       # <span style="color:#ff0000;">通过 django内置的Json格式 丢给客户端数据</span>
