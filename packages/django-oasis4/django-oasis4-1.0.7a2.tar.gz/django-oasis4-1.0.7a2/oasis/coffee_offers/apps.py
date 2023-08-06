# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2023. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2023. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         22/02/23 9:18
# Project:      CFHL Transactional Backend
# Module Name:  apps
# Description:
# ****************************************************************
from django.apps import AppConfig
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class OasisCoffeeOffer(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "oasis.coffee_offers"
    label = "coffee_offer"
    verbose_name = _("Oasis4 Coffee Offer ")

    def ready(self):
        """
        Method loaded on ready event load application
        :return: None
        """
        settings.COFFEE_OFFERS_DOCUMENT = getattr(settings, "COFFEE_OFFERS_DOCUMENT", "OA")
        settings.COFFEE_OFFERS_CONCEPT = getattr(settings, "COFFEE_OFFERS_CONCEPT", "OA")
        settings.COFFEE_OFFERS_MOTIVE = getattr(settings, "COFFEE_OFFERS_MOTIVE", 9)
