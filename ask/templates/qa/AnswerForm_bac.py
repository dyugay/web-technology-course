{%extends "qa/questionDetails.html" %}

{%block question%}{{block.super}} {% endblock %}

{% block answer %}
<h3>Answer Form:</h3>


 {% for e in form.non_field_errors%}
    <div>{{e}}</div>
 {% endfor %}

 <form method= "post" action="/question/{{question.id}}">
  <fieldset>
   {% for field in form%}
    
    <label> {{field.label}} </label> 
    <div>
       {{field}}
    </div>
    {% if field.errors %}
     <div> 
      {{field.errors}}
     </div>
    {% endif %}
   {% endfor %}
  </fieldset>

  <div>
   <button type="submit">submit answer</button>
  </div>
  {% csrf_token %}
 </form>

{% endblock %}
