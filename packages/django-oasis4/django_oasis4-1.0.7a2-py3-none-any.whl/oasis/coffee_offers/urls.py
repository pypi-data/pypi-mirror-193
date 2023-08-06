# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2023. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2023. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         23/02/23 10:12
# Project:      CFHL Transactional Backend
# Module Name:  urls
# Description:
# ****************************************************************
from oasis.coffee_offers.api import services
from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter

routers = DefaultRouter()

urlpatterns = [
    path(r"warehouse/list/", services.CoffeeWareHouse.as_view({"post": "list"}))
]
