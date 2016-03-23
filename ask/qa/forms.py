from django import forms
from qa.models import Answer, Question
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

class LoginForm(forms.Form):
   username = forms.CharField(max_length=30)
   password = forms.CharField(max_length=128)

   def clean(self):
     cleaned_data = super(LoginForm, self).clean()
     username = cleaned_data.get('username')
     password = cleaned_data.get('password')
     
     user = authenticate (username = username, password = password)
     if user is None:
         raise forms.ValidationError(u'user is not authentificated!')

     return cleaned_data

   def clean_username(self):
       username = self.cleaned_data['username']
       if is_empty(username):
            raise forms.ValidationError(u'Username is empty!')
       return username

   
   def clean_password(self):
       password = self.cleaned_data['password']
       if is_empty(password):
            raise forms.ValidationError(u'Password is empty')
       return password

   def logIn(self):
       
       return user
   
class SignUpForm(forms.Form):
   username = forms.CharField(max_length=30)
   email = forms.EmailField(max_length=75)
   password = forms.CharField(max_length=128)
    
   def clean_username(self):
       username = self.cleaned_data['username']
       if is_empty(username):
            raise forms.ValidationError(u'Username is empty!')
       try:
        if User.objects.get(username=username):
             raise forms.ValidationError(u'Username already exists')
       except User.DoesNotExist:
              pass
              
       return username


  
   def clean_email(self):
       email = self.cleaned_data['email']
       if is_empty(email):
            raise forms.ValidationError(u'E-mail is empty')
       return email    
 
   def clean_password(self):
       password = self.cleaned_data['password']
       if is_empty(password):
            raise forms.ValidationError(u'Password is empty')       
       return password 

   def save(self):
       username = str(self.cleaned_data['username'])
       email = self.cleaned_data['email']
       password = self.cleaned_data['password'] 
       user = User.objects.create_user(username, email, password) 
       user.save()
       return user




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
       self.cleaned_data['author'] = self._user
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
       self.cleaned_data['author'] = self._user 
       answer = Answer(text=self.cleaned_data['text'],
                       author = self.cleaned_data['author'],
                       question=question)
       #answer = Answer(**self.cleaned_data)
     
       answer.save()
       return answer          
 



def is_empty(text):
    return(text.isspace())

