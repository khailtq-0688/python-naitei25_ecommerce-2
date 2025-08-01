from __future__ import annotations

from django.db import models

from core.constants import DecimalSettings
from core.constants import FieldLengths
from core.models import BaseModel


class Category(BaseModel):
    name = models.CharField(
        max_length=FieldLengths.NAME,
        unique=True,
    )

    class Meta:
        db_table = 'categories'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = models.CharField(max_length=FieldLengths.DEFAULT)
    description = models.TextField(blank=True)
    price = models.DecimalField(
        max_digits=DecimalSettings.PRICE_MAX_DIGITS,
        decimal_places=DecimalSettings.PRICE_DECIMAL_PLACES,
    )
    image_urls = models.JSONField(default=list)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='products',
    )
    specification = models.JSONField(default=list)
    is_in_stock = models.BooleanField(default=True)

    class Meta:
        db_table = 'products'
        indexes = [
            models.Index(fields=['category'], name='idx_products_category_id'),
        ]

    def __str__(self):
        return self.name
