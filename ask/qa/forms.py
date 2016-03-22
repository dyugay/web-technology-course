from django import forms
from qa.models import Answer, Question
from django.contrib.auth.models import User

class AskForm(forms.Form):
   title = forms.CharField(max_length=100)
   text = forms.CharField(widget=forms.Textarea)
  
   def clean_title(self):
       title = self.cleaned_data['title']
       if is_empty(title):
            raise forms.ValidationError(u'Title is empty!')
       return title

   def clean_text(self):
       text = self.cleaned_data['text']
       if is_empty(text):
            raise forms.ValidationError(u'Text is empty!') 
       return text   

  
   def save(self):
       question = Question(**self.cleaned_data)
       question.save()
       return question

class AnswerForm(forms.Form):
  
   #def __init__(self, *args, **kwargs):
   #   super(AnswerForm,self).__init__(*args, **kwargs)


  # question = forms.IntegerField()
   question = forms.IntegerField(widget=forms.HiddenInput())
   text = forms.CharField(widget=forms.Textarea)
   
   def clean_text(self):
       text = self.cleaned_data['text']
       if is_empty(text):
          raise forms.ValidationError(u'Answer is empty!')
       return text  

   def save(self):
       question = Question.objects.get(id = self.cleaned_data['question'])
       
      # if not question.id:
      #    return HttpResponse('question id is empty')
       answer = Answer(text=self.cleaned_data['text'],
                      question=question)
       answer.save()
       return answer          
 



def is_empty(text):
    return(text.isspace())

