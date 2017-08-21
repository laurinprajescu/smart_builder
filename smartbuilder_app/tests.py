# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from .models import PostAJob

class PostAJobTests(TestCase):

    def test_str(self):
        test_title = PostAJob(title='My first Job Post')
        self.assertEqual(str(test_title),
                         'My first Job Post')
