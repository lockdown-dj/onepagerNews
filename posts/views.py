from django.shortcuts import render
from posts.models import News
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect

# Create your views here.

# def index(request):
#     return render(request,'index.html')

def index(request):

    # to get latest post
    get_data = News.objects.filter(is_news=False).values('id','date','heading_one','heading_two','heading_three','image_one','image_two','image_three','image_four','image_five','image_six','image_seven','image_eight','image_nine','para_one','para_two','para_three','para_four','para_five','para_six','para_seven','para_eight','para_nine').order_by('-id')[:1]
    # to get all news
    get_news_data = News.objects.filter(is_news=True).values('id','date','heading_one','heading_two','heading_three','image_one','image_two','image_three','image_four','image_five','image_six','image_seven','image_eight','image_nine','para_one','para_two','para_three','para_four','para_five','para_six','para_seven','para_eight','para_nine').order_by('-id')[1:]
    # to get latest news
    latest_news = News.objects.filter(is_news=True).values('id','date','heading_one','heading_two','heading_three','image_one','image_two','image_three','image_four','image_five','image_six','image_seven','image_eight','image_nine','para_one','para_two','para_three','para_four','para_five','para_six','para_seven','para_eight','para_nine').order_by('-id')[:1]

    return render(request,'index.html',{'data':get_data , 'news_data':get_news_data,'latest_news':latest_news})


def preview(request, id =None):

    objData = News.objects.get(pk=id)
    return render(request,'preview.html',{"objData":objData})