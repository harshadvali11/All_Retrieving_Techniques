from django.shortcuts import render

# Create your views here.
from app.models import *

from django.db.models import Q
from django.http import HttpResponse

def display_topics(request):
    topics=Topic.objects.all()
    d={'topics':topics}
    return render(request,'display_topics.html',d)

def display_webpages(request):
    webpages=Webpage.objects.all()
    webpages=Webpage.objects.filter(name__in=['rahul','Dhoni'])
    webpages=Webpage.objects.filter(name__regex='R\w+')
    webpages=Webpage.objects.all()
    webpages=Webpage.objects.filter(Q(name='Virat') | Q(url__startswith='https'))
    webpages=Webpage.objects.filter(Q(name='Rahul') & Q(url__startswith='https'))
    webpages=Webpage.objects.all()
    d={'webpages':webpages}
    return render(request,'display_webpages.html',d)


def display_access(request):
    LAO=AccessRecord.objects.all()

    LAO=AccessRecord.objects.filter(date='1995-01-18')
    LAO=AccessRecord.objects.filter(date__gt='1995-01-18')
    LAO=AccessRecord.objects.filter(date__lte='1995-01-18')
    LAO=AccessRecord.objects.filter(date__year='2021')
    LAO=AccessRecord.objects.filter(date__month='07')
    LAO=AccessRecord.objects.filter(date__day='12')
    LAO=AccessRecord.objects.filter(date__year__gte='2020')
    LAO=AccessRecord.objects.filter(date__year__lte='2020')
    LAO=AccessRecord.objects.filter(date__day__gt='12')
    
    

    
    
    

    
    
    
    d={'LAO':LAO}
    return render(request,'display_access.html',d)





def update_webpage(request):

    #Webpage.objects.filter(name='Dhoni').update(url='https://MSD.in')
    #Webpage.objects.filter(topic_name='Cricket').update(url='https://IndianTeam.in')
    #Webpage.objects.filter(name='Dhoni MSD').update(url='https://MSD.in')

    #Webpage.objects.filter(name='Dhoni').update(topic_name='BCCI Cricket')
    #Webpage.objects.filter(name='Dhoni').update(topic_name='Rugby')
    #Webpage.objects.update_or_create(name='Abc',defaults={'url':'http://ABCDE.com'})
    
    #Webpage.objects.update_or_create(topic_name='Rugby',defaults={'url':'http://Rugby.com'})
    #Webpage.objects.update_or_create(name='Abc',defaults={'url':'http://ABCDE.com'})
    CTO=Topic.objects.get(topic_name='Cricket')
    
    
    #Webpage.objects.update_or_create(name='Dhoni',defaults={'topic_name':CTO})
    Webpage.objects.update_or_create(name='Pandya',defaults={'topic_name':CTO,'url':'http://pandya.com'})
    



    
    
    webpages=Webpage.objects.all()
    d={'webpages':webpages}
    return render(request,'display_webpages.html',d)



def delete_webpage(request):
    #Webpage.objects.filter(name='Rahul').delete()

    Webpage.objects.all().delete()
    
    webpages=Webpage.objects.all()
    d={'webpages':webpages}
    return render(request,'display_webpages.html',d)












