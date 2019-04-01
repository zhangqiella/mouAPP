from django.shortcuts import render

# Create your views here.


def handle_index(req):
    # print('前端数据',req.GET)
    print('前端数据', req.POST)
    print('上传文件',req.FILES)

    for item in req.FILES:
        #这里取字典的值，最好用get，这样如果没有值，可以返回定义的值，比如这里的None。
        #而不是返回错误
        obj= req.FILES.get(item,None)
        filename = obj.name

        f=open(filename,'wb')
        #chunks 就是从内存中取出一部分数据，不会一次取很多。
        for line in obj.chunks():
            f.write(line)

        f.close()
    # print(req.POST)
    return render(req,'index.html')