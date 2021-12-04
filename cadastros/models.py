from django.db import models


class Pais(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Países'


class Estado(models.Model):
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT)
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'
        ordering = ('nome', )


class Cidade(models.Model):

    estado = models.ForeignKey(Estado, on_delete=models.PROTECT, null=True, blank=False)
    nome = models.CharField(max_length=100, unique=True)
    capital = models.BooleanField(default=False, help_text=" Marcar se a cidade for capital.")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'
