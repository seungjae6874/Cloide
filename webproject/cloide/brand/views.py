from django.shortcuts import render
from .models import Brand, Agesex
# Create your views here.

def brand(request):
    brand = Brand.objects.all()
    agesex = Agesex.objects.all()
    current_url = request.get_full_path()
    token = current_url.split('?')
    sex = token[1]
    if sex == 'Man':
        sex = 1
    else:
        sex = 0
    style = token[2]
    
    age = int(token[3])


    #1. views 안에서 모든 처리, html에서는 쿼리해서 받아온 브랜드들을 보여주기만한다.
    #2. 토큰을 html에 넘겨줘서 html안에서 모델에 접근해서 보여준다.
    return render(request,'brand.html',{'current_url' : current_url, 'sex' : sex,'age':age, 'style':style,'brand':brand,'agesex':agesex})
