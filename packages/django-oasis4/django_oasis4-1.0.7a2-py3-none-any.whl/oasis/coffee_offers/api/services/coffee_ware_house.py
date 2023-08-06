# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2023. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2023. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         23/02/23 10:02
# Project:      CFHL Transactional Backend
# Module Name:  coffee_ware_house
# Description:
# ****************************************************************
from oasis import models
from oasis.coffee_offers.api import serializers
from rest_framework.response import Response
from zibanu.django.rest_framework import viewsets


class CoffeeWareHouse(viewsets.ModelViewSet):
    model = models.CoffeeWareHouse
    serializer_class = serializers.CoffeeWareHouseListSerializer

    def list(self, request, *args, **kwargs) -> Response:
        if "order_by" not in kwargs.keys():
            kwargs["order_by"] = "location_name"
        return super().list(request, *args, **kwargs)

