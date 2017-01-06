# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from random import choice, randint
from faker import Factory
from django.contrib.auth.models import User
from rip_app.models import OfficeModel


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-n',
                            action="store",
                            dest='number',
                            default=5, )

    def handle(self, *args, **options):
        fake = Factory.create()
        number = int(options['number'])
        users = User.objects.all()

        for i in range(0, number):
            n = OfficeModel()
            n.named = fake.sentence(nb_words=randint(2, 5), variable_nb_words=True)
            n.location = u"%s" % (
                    fake.paragraph(nb_sentences=randint(5, 15), variable_nb_sentences=True),
                    )
            n.member = choice(users)
            n.save()
            self.stdout.write('created offices [%d]' % n.id)