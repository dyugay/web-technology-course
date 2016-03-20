from django.db import models
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage
from django.http import Http404
from django.core.urlresolvers import reverse

# Create your models here.

class Question(models.Model):
  title = models.CharField(max_length=255)
  text = models.TextField()
  added_at = models.DateTimeField(auto_now_add=True)
  rating = models.IntegerField() 
  author = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)
  likes = models.ManyToManyField(User, related_name = 'likes_set')
  
  def get_url(self):
      return reverse('question-details',
                     kwargs = {'questionId': self.id} ) 

class Answer(models.Model):
  text = models.TextField()
  added_at = models.DateTimeField(auto_now_add=True)
  question = models.ForeignKey(Question)
  author = models.ManyToManyField(User)


#class qaShortcuts(object):   
    
 #    def __init__(self):
  #           pass
   
def paginate(request, querySet):
#shortcuts for pagination

            #gets and checks limit value
            try: 
                  limit =  int(request.GET.get('limit', 10))
            except ValueError:
                  limit = 10      
            if limit > 100:
                  limit = 10
           
            
            #gets and checks page value
            try:
                  page = int(request.GET.get('page', 1))
            except ValueError:
                  raise Http404
            
           
            paginator = Paginator(querySet, limit)             
            try:
                  page = paginator.page(page)   
            except EmptyPage:
                  page = paginator.page(paginator.num_pages)
            
            paginatorAttr = {'page': page,
                             'limit': limit,
                             'paginator': paginator }
            
            return paginatorAttr
      
           
            

 




             







    


 
