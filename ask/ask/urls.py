from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from qa.views import test, getNewQuestionsList, questionDetails, getPopularQuestions


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)), 
    url(r'^$', getNewQuestionsList, name = 'home'),
    url(r'^login/.*$', 'qa.views.test'),
    url(r'^signup/.*$', 'qa.views.test'),
    url(r'^question/(?P<questionId>\d+)*/*$', questionDetails, name = 'question-details'),
    url(r'^ask/.*$', 'qa.views.test'),
    url(r'^popular/.*$', getPopularQuestions, name = 'popular-questions' ),
    url(r'^new/.*$', 'qa.views.test'), 
)
