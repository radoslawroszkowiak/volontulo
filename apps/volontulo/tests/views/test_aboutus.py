# -*- coding: utf-8 -*-

u"""
.. module:: test_aboutus
"""
from django.test import Client
from django.test import TestCase

from apps.volontulo.tests import common

class TestAboutus(TestCase):
    u"""Class responsible for testing about us specific views."""

    # pylint: disable=invalid-name
    def test__about_us(self):
        u"""Test getting about us page as anonymous."""
        response = self.client.get('/about-us', follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about_us.html')
