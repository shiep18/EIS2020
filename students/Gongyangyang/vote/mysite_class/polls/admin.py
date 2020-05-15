from django.contrib import admin
from .models import Question,Choice

# Register your models here.

admin.site.register(Question)
admin.site.register(Choice)

# python manage.py shell # 打开shell
# from polls.models import Question
# from django.utils import timezone
# q = Question(question_text='text', pub_date=timezone.now())
# q.save()