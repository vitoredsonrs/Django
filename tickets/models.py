from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db import models

from proj import settings, settings_dev


class Categoria(models.Model):
    descricao = models.CharField(max_length=255)
    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ('descricao',)
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


    def __str__(self):
        return self.descricao


class Solicitacao(models.Model):

    STATUS_NEW = 'new'
    STATUS_ONGOING = 'ongoing'
    STATUS_CLOSED = 'closed'
    STATUS_CANCELED = 'canceled'

    STATUS_CHOICES = (
        (STATUS_NEW, 'Novo'),
        (STATUS_ONGOING, 'Em andamento'),
        (STATUS_CLOSED, 'Fechado'),
        (STATUS_CANCELED, 'Cancelado'),
    )

    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    nome = models.CharField(max_length=120)
    email = models.EmailField(verbose_name='E-mail')
    assunto = models.CharField(max_length=85, verbose_name='Assunto')
    descricao = models.TextField(verbose_name='Descrição')
    arquivo = models.FileField(upload_to='solicitacoes', null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=STATUS_NEW)
    atendente = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    data_solicitacao = models.DateTimeField(auto_now_add=True, verbose_name='Data da solicitação')
    ultima_atualizacao = models.DateTimeField(auto_now=True, verbose_name='Última atualização.')

    class Meta:
        ordering = ('ultima_atualizacao',)
        verbose_name = 'Solicitação'
        verbose_name_plural = 'Solicitações'

    def __str__(self):
        return f'TICKTES{self.pk:04d}'

    # def save(self, *args, **kwargs):
    #     if self.pk:
    #         pass
    #
    #     super().save(*args, **kwargs)
    #


class Interacao(models.Model):

    TIPO_ASSIGNED = 0
    TIPO_TEAM_RESPONSE = 1
    TIPO_REQUESTER_RESPONSE = 2
    TIPO_STATUS_CHANGE = 3

    TIPO_CHOICES = (
        (TIPO_ASSIGNED, 'Designado para o atendente'),
        (TIPO_TEAM_RESPONSE, 'Resposta da equipe'),
        (TIPO_REQUESTER_RESPONSE, 'Resposta do solicitante'),
        (TIPO_STATUS_CHANGE, 'Mudança de status'),

    )

    solicitacao = models.ForeignKey(Solicitacao, on_delete=models.CASCADE, related_name='interacoes')
    tipo = models.PositiveSmallIntegerField(choices=TIPO_CHOICES)
    descricao=models.TextField()
    atendente = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    data_interacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('data_interacao',)
        verbose_name = 'Interação'
        verbose_name_plural = 'Interações'

    def __str__(self):
        return f'{self.pk}'

    def send_mail_message(self):
        send_mail(
            subject=f'{self.solicitacao} - Nova interação -{self.get_tipo_display()}',
            message=self.descricao,
            from_email=settings_dev.DEFAULT_FROM_EMAIL,
            recipient_list=[self.solicitacao.email],
        )
