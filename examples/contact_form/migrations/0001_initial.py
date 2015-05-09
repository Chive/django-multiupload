# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(upload_to=b'attachments', verbose_name='Attachment')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author_name', models.CharField(max_length=255, verbose_name='Name')),
                ('author_email', models.EmailField(max_length=254, verbose_name='Email')),
                ('content', models.TextField(verbose_name='Content')),
            ],
        ),
        migrations.AddField(
            model_name='attachment',
            name='message',
            field=models.ForeignKey(verbose_name='Message', to='contact_form.Message'),
        ),
    ]
