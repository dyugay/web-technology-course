from django.db import models
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage
from django.http import Http404
from django.core.urlresolvers import reverse

# Create your models here.

class Question(models.Model):
  title = models.CharField(max_length=255)
  text = models.TextField(null=True)
  added_at = models.DateTimeField(auto_now_add=True)
  rating = models.IntegerField(null=True) 
  author = models.ForeignKey(User, null=True)
  likes = models.ManyToManyField(User, related_name = 'likes_set')
  
  def get_url(self):
      return reverse('question-details',
                     kwargs = {'questionId': self.id} ) 

class Answer(models.Model):
  text = models.TextField()
  added_at = models.DateTimeField(auto_now_add=True)
  question = models.ForeignKey(Question)
  author = models.ForeignKey(User, null=True)




  
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
      
           
            

def dbQuestionInit():
    for id in range(1,25):
     author = User(username = 'NewUserAgain'+ str(id))
     author.save()
     print author.username     
    
     question = Question(title = 'title' + str(id), 
                         text = 'text' + str(id),
                         rating = id,
                         author = author,
                         )
     question.save()
     print question.title

def dbAnswerInit():
    
    for id in range(1, 25):
      print id
      author = User.objects.get(id = id)
      print author.username    
  
      question = Question.objects.get(id = id)

      answer = Answer(text = 'answer' + str(id),
                      question = question,
                      author = author,
                      )
      answer.save()                        
 

   
 
    
    author = User(username = 'Nikolas')
    author.save()
    question = Question.objects.get(id = 3)
    answer = Answer(text = 'answer from Nikolas' + str(id),
                    question = question,
                     )
    answer.save()

    answer.author.add(author)
    answer.save()
 
    author = User(username = 'Jane')
    author.save()
    question = Question.objects.get(id = 3)
    answer = Answer(text = 'answer from Jane' + str(id),
                    question = question,
                     )
    answer.save()

    answer.author.add(author)
    answer.save()




    author = User(username = 'Silivia')
    author.save()
    question = Question.objects.get(id = 4)
    answer = Answer(text = 'answer from Silivia' + str(id),
                    question = question,
                     )
    answer.save()

    answer.author.add(author)
    answer.save()

    author = User(username = 'Frodo')
    author.save()
 
    answer = Answer(text = 'answer from Frodo' + str(id),
                    question = question,
                     )
    answer.save()

    answer.author.add(author)
    answer.save()









             







    


 
