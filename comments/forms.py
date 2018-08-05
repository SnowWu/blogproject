# -*- coding: utf-8 -*-
__author__ = 'Snow'

from django import forms
from .models import Comment

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'text']