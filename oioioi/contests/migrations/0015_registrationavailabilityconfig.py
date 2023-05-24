# Generated by Django 3.2.18 on 2023-04-17 21:51

from django.db import migrations, models
import django.db.models.deletion
import oioioi.base.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0014_contest_enable_editor'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationAvailabilityConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', oioioi.base.fields.EnumField(default='YES', help_text='If set to Open, the registration will be opened always.If set to Closed, the registration will be closed always.If set to Configuration, the registration will be opened according to the following settings.', max_length=64, verbose_name='Registration vailability')),
                ('registration_available_from', models.DateTimeField(blank=True, help_text='If set, the registration will be opened automatically at the specified date.', null=True, verbose_name='available from')),
                ('registration_available_to', models.DateTimeField(blank=True, help_text='If set, the registration will be closed automatically at the specified date.', null=True, verbose_name='available to')),
                ('contest', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='contests.contest')),
            ],
            options={
                'verbose_name': 'Registration availability config',
                'verbose_name_plural': 'open registration configs',
            },
        ),
    ]