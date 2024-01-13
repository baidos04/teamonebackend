from django.shortcuts import render
from rest_framework import generics
from .models import Card
from .serializers import CardSerializer
from django.views.generic import TemplateView
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


class CardList(generics.ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CardDetail(generics.RetrieveAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CardCreate(generics.CreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CardUpdate(generics.UpdateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CardDelete(generics.DestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


# Email
class EmailSuccessView(TemplateView):
    template_name = 'success.html'


def send_email(request, pk):
    card = Card.objects.get(pk=pk)

    html_message = render_to_string('data.html', {'card': card})
    plain_message = strip_tags(html_message)

    email = EmailMultiAlternatives(
        subject=card.company_name,
        body=plain_message.strip(),
        from_email=settings.EMAIL_HOST_USER,
        to=[card.email_address],
    )

    # Attach прикрепляем файл
    if card.file:
        file = card.file
        email.attach(file.name, file.read())

    # Attach прикрепляем рисунок
    if card.signage:
        signage = card.signage
        email.attach(signage.name, signage.read())

    # Attach прикрепляем HTML сообщение
    email.attach_alternative(html_message, 'text/html')

    # Отправляем email
    email.send()

    return render(request, 'success.html', )
