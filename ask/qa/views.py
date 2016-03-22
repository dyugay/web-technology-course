from django.shortcuts import render, get_object_or_404
from qa.models import Question, Answer, paginate
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from qa.forms import AskForm, AnswerForm

def test(request, *args, **kwargs):
    return HttpResponse('OK')

#get questions list at home page
def getNewQuestionsList(request, *args, **kwargs):
    questionsList = Question.objects.all()
    questionsList = questionsList.order_by('-added_at')
    paginatorAttr = paginate(request, questionsList) 
   # shortcut = qaShortcuts()
   # page = paginate(request, questionsList)['page']
   # numPage = page = request.GET.get('page', 1)
   # limit = request.GET.get('limit', 10)
   # paginator = Paginator(questionsList, limit)
   # page = paginator.page(page)
    url = '/?page='  
   # questionUrl = reverse('question-details')  

    return render(request, 'qa/questionsList.html', {
             # 'questionsList': paginatorAttr['page'].object_list,
              'paginator': paginatorAttr['paginator'],
              'page': paginatorAttr['page'], 
              'url': url,                
           })
           

def getPopularQuestions(request, *args, **kwargs):
    questionsList = Question.objects.all()
    questionsList = questionsList.order_by('-rating')
    paginatorAttr = paginate(request, questionsList)
    url = '/popular/?page='
    return render(request, 'qa/questionsList.html', {
             # 'questionsList': paginatorAttr['page'].object_list,
              'paginator': paginatorAttr['paginator'],
              'page': paginatorAttr['page'],
              'url': url,
           })


 #   return HttpResponse('popular')


def questionDetails(request, *args, **kwargs):
    questionId = kwargs['questionId']
    question = get_object_or_404(Question, id = questionId)
    answers = Answer.objects.filter(question = question)
    
    if request.method == 'POST':
      form = AnswerForm(request.POST)
      if form.is_valid():
         form.save() 
         url = question.get_url()
         return HttpResponseRedirect(url)
    else:   
      form = AnswerForm(initial={'question':questionId}) 
    return render(request, 'qa/AnswerForm.html', {
                        'question': question,                       
                        'answers': answers,
                        'form': form, 
                         })


 
def askQuestion(request, *args, **kwargs):
    if request.method == 'POST':
      form = AskForm(request.POST)  
      if form.is_valid():
        question = form.save()
        url = question.get_url()
        return HttpResponseRedirect(url) 
    else:
      form = AskForm()
 
    #return HttpResponse('question input form')
    return render(request,
                  'qa/AskForm.html',
                   {
                   'form': form,
                    })



def postAnswer(request, *args, **kwargs):
    if request.method == 'POST':
       form = AnswerForm(request.POST)
       if form.is_valid():
          answer = form.save()
          question = Question.objects.get(id = form.cleaned_data['question'])
          url = question.get_url()
          return HttpResponseRedirect(url)
    #   return HttpResponse('answer form post') 
    else:
       form = AnswerForm()
    
    return render( request,
                   'qa/AnswerOnlyForm.html',
                   {
                     'form':form,
                     })           

 



    
