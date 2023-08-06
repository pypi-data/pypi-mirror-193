# Copyright 2023 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from django.urls import re_path
from grade_conversion_calculator.views import DemoView


urlpatterns = [
    re_path(r'^calculator-demo', DemoView.as_view(), name='calculator_demo'),
]
