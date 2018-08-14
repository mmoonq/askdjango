#blog/modles.py
import re
from django.db import models
from django.forms import ValidationError



def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')

class Post(models.Model):
    author = models.CharField(max_length=20,)
    title = models.CharField(max_length=100, verbose_name='제목',  # verbose를 안쓰면 필드이름으로 됨 지금 필드이름은 'title'임.
    help_text="포스팅 제목을 입력해주세요. 최대 100자 내외",) #길이 제한이 있는 문자열
    content = models.TextField(verbose_name="내용")    # 길이 제한이 없는 문자열
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50, blank=True, 
        validators=[lnglat_validator],
        help_text="경도/위도 포맷으로 입력하세요")
    created_at = models.DateTimeField(auto_now_add=True)   # 처음datetime이 생성될 때 자동 생성 Ture
    updated_at = models.DateTimeField(auto_now=True)    #  datetime이 저장될 때 마다.!
