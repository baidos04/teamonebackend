from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

from .models import Card
from .serializers import CardSerializer


class CardList(generics.ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CardDetail(generics.RetrieveAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CardCreate(generics.CreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def perform_create(self, serializer):
        instance = serializer.save()

        send_email(instance)


class CardUpdate(generics.UpdateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def perform_update(self, serializer):
        updated_instance = serializer.save()

        send_email(updated_instance)


class CardDelete(generics.DestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


# Email
class EmailSuccessView(TemplateView):
    template_name = 'success.html'


def send_email(card):
    html_message = render_to_string('data.html', {'card': card})
    plain_message = strip_tags(html_message)

    email = EmailMultiAlternatives(
        subject=card.company_name,
        body=plain_message.strip(),
        from_email=settings.EMAIL_HOST_USER,
        to=[card.email_address],
    )

    # Attach the file
    if card.file:
        file = card.file
        email.attach(file.name, file.read())

    # Attach the signage
    if card.signage:
        signage = card.signage
        email.attach(signage.name, signage.read())

    # Attach HTML message
    email.attach_alternative(html_message, 'text/html')

    # Send email
    email.send()
