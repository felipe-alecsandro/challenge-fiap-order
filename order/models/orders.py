from django.db import models
import os
import re


class Order(models.Model):
    order_id = models.CharField(max_length=600, blank=True, null=True)
    transaction = models.CharField(max_length=600, blank=True, null=True)
    products = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=20,verbose_name="status", choices=(("em aberto", "em aberto"), ("recebido", "recebido"), ('em preparacao','em preparacao'), ('pronto','pronto'), ('finalizado','finalizado'), ('cancelado','cancelado')), default='em aberto')
    created_at = models.DateTimeField(auto_now=True, verbose_name="criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="atualizado em", null=True, blank=True,)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return f"{self.order_id}"

 
    def save(self,*args,**kwargs):
        kwargs['using'] = 'default'
        return super().save(*args,**kwargs)

