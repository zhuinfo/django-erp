# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-13 20:58
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organ', '0001_initial'),
        ('basedata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin', models.DateField(blank=True, null=True, verbose_name='begin date')),
                ('end', models.DateField(blank=True, null=True, verbose_name='end date')),
                ('creator', models.CharField(blank=True, max_length=20, null=True, verbose_name='creator')),
                ('modifier', models.CharField(blank=True, max_length=20, null=True, verbose_name='modifier')),
                ('creation', models.DateTimeField(auto_now_add=True, null=True, verbose_name='creation')),
                ('modification', models.DateTimeField(auto_now=True, null=True, verbose_name='modification')),
                ('begin_time', models.DateTimeField(verbose_name='begin time')),
                ('end_time', models.DateTimeField(verbose_name='end time')),
                ('enroll_deadline', models.DateTimeField(blank=True, null=True, verbose_name='enroll deadline')),
                ('code', models.CharField(blank=True, max_length=20, null=True, verbose_name='code')),
                ('title', models.CharField(max_length=120, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('host', models.CharField(blank=True, max_length=80, null=True, verbose_name='host')),
                ('speaker', models.CharField(blank=True, max_length=80, null=True, verbose_name='speaker')),
                ('accept_enroll', models.BooleanField(default=1, verbose_name='accept enroll')),
                ('location', models.CharField(blank=True, max_length=80, null=True, verbose_name='location')),
                ('classification', models.CharField(blank=True, choices=[(b'T', 'Train'), (b'M', 'Meeting'), (b'G', 'Community')], default=b'M', max_length=2, null=True, verbose_name='classification')),
                ('mail_list', models.TextField(blank=True, null=True, verbose_name='mail list')),
                ('mail_notice', models.BooleanField(default=1, verbose_name='mail notice')),
                ('short_message_notice', models.BooleanField(default=1, verbose_name='short message notice')),
                ('weixin_notice', models.BooleanField(default=1, verbose_name='weixin notice')),
                ('status', models.BooleanField(default=0, verbose_name='published')),
                ('publish_time', models.DateTimeField(blank=True, null=True, verbose_name='publish time')),
                ('attach', models.FileField(blank=True, null=True, upload_to=b'activity', verbose_name='attach')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='selfhelp.Activity', verbose_name='parent')),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='basedata.Material', verbose_name='room')),
            ],
            options={
                'verbose_name': 'activity',
                'verbose_name_plural': 'activities',
            },
        ),
        migrations.CreateModel(
            name='Enroll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enroll_time', models.DateTimeField(auto_now_add=True, verbose_name='enroll time')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='selfhelp.Activity')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed_time', models.DateTimeField(auto_now_add=True, verbose_name='feedback time')),
                ('rank', models.CharField(blank=True, choices=[(b'A', b'A'), (b'B', b'B'), (b'C', b'C'), (b'D', b'D')], default=b'B', max_length=2, null=True, verbose_name='rank')),
                ('comment', models.CharField(blank=True, max_length=80, null=True, verbose_name='suggest')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='selfhelp.Activity')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin', models.DateField(blank=True, null=True, verbose_name='begin date')),
                ('end', models.DateField(blank=True, null=True, verbose_name='end date')),
                ('creator', models.CharField(blank=True, max_length=20, null=True, verbose_name='creator')),
                ('modifier', models.CharField(blank=True, max_length=20, null=True, verbose_name='modifier')),
                ('creation', models.DateTimeField(auto_now_add=True, null=True, verbose_name='creation')),
                ('modification', models.DateTimeField(auto_now=True, null=True, verbose_name='modification')),
                ('code', models.CharField(blank=True, max_length=10, null=True, verbose_name='loan code')),
                ('title', models.CharField(max_length=120, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('status', models.CharField(blank=True, choices=[(b'N', 'NEW'), (b'I', 'IN PROGRESS'), (b'A', 'APPROVED'), (b'P', 'PAYED')], default=b'N', max_length=2, null=True, verbose_name='status')),
                ('logout_time', models.DateTimeField(blank=True, null=True, verbose_name='logout time')),
                ('loan_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='loan amount')),
                ('logout_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='logout amount')),
                ('pay_user', models.CharField(blank=True, max_length=40, null=True, verbose_name='pay user')),
                ('pay_time', models.DateTimeField(blank=True, null=True, verbose_name='pay time')),
                ('is_clear', models.BooleanField(default=False, verbose_name='is clear')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basedata.Project', verbose_name='project')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'loan',
                'verbose_name_plural': 'loans',
                'permissions': (('financial_pay', 'financial pay'),),
            },
        ),
        migrations.CreateModel(
            name='Reimbursement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin', models.DateField(blank=True, null=True, verbose_name='begin date')),
                ('end', models.DateField(blank=True, null=True, verbose_name='end date')),
                ('creator', models.CharField(blank=True, max_length=20, null=True, verbose_name='creator')),
                ('modifier', models.CharField(blank=True, max_length=20, null=True, verbose_name='modifier')),
                ('creation', models.DateTimeField(auto_now_add=True, null=True, verbose_name='creation')),
                ('modification', models.DateTimeField(auto_now=True, null=True, verbose_name='modification')),
                ('code', models.CharField(blank=True, max_length=10, null=True, verbose_name='fee code')),
                ('title', models.CharField(max_length=120, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('bank_account', models.CharField(blank=True, max_length=120, null=True, verbose_name='bank account')),
                ('status', models.CharField(blank=True, choices=[(b'N', 'NEW'), (b'I', 'IN PROGRESS'), (b'A', 'APPROVED'), (b'P', 'PAYED')], default=b'N', max_length=2, null=True, verbose_name='status')),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='amount of money')),
                ('loan_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='loan amount')),
                ('logout_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='logout amount')),
                ('pay_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='pay amount')),
                ('pay_time', models.DateTimeField(blank=True, null=True, verbose_name='pay time')),
                ('pay_user', models.CharField(blank=True, max_length=40, null=True, verbose_name='pay user')),
                ('loan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='selfhelp.Loan', verbose_name='loan record')),
                ('org', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organ.OrgUnit', verbose_name='cost center')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basedata.Project', verbose_name='project')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'reimbursement',
                'verbose_name_plural': 'reimbursements',
                'permissions': (('financial_pay', 'financial pay'),),
            },
        ),
        migrations.CreateModel(
            name='ReimbursementItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin', models.DateField(default=datetime.date.today, verbose_name='occur date')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='amount of money')),
                ('memo', models.CharField(blank=True, max_length=40, null=True, verbose_name='memo')),
                ('expense_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basedata.ExpenseAccount', verbose_name='expenses account')),
                ('reimbursement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='selfhelp.Reimbursement', verbose_name='reimbursement')),
            ],
            options={
                'verbose_name': 'fee item',
                'verbose_name_plural': 'fee items',
            },
        ),
        migrations.CreateModel(
            name='WOExtraValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('param_value', models.CharField(blank=True, max_length=40, null=True, verbose_name='param value')),
                ('param_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basedata.ExtraParam', verbose_name='extra param')),
            ],
            options={
                'verbose_name': 'extra value',
                'verbose_name_plural': 'extra values',
            },
        ),
        migrations.CreateModel(
            name='WOItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True, verbose_name='amount')),
                ('price', models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True, verbose_name='price')),
                ('material', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='basedata.Material', verbose_name='material')),
                ('measure', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='basedata.Measure', verbose_name='measure')),
            ],
            options={
                'verbose_name': 'workorder item',
                'verbose_name_plural': 'workorder items',
            },
        ),
        migrations.CreateModel(
            name='WorkOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin', models.DateField(blank=True, null=True, verbose_name='begin date')),
                ('end', models.DateField(blank=True, null=True, verbose_name='end date')),
                ('creator', models.CharField(blank=True, max_length=20, null=True, verbose_name='creator')),
                ('modifier', models.CharField(blank=True, max_length=20, null=True, verbose_name='modifier')),
                ('creation', models.DateTimeField(auto_now_add=True, null=True, verbose_name='creation')),
                ('modification', models.DateTimeField(auto_now=True, null=True, verbose_name='modification')),
                ('code', models.CharField(blank=True, max_length=10, null=True, verbose_name='workorder code')),
                ('title', models.CharField(max_length=120, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('business_domain', models.CharField(default=b'OT', max_length=4, verbose_name='business domain')),
                ('classification', models.CharField(default=b'D', max_length=4, verbose_name='classification')),
                ('status', models.CharField(blank=True, default=b'NEW', max_length=6, null=True, verbose_name='status')),
                ('answer', models.TextField(blank=True, null=True, verbose_name='answer')),
                ('attach', models.FileField(blank=True, help_text='\u5de5\u5355\u9644\u4ef6\uff0c\u4e0d\u5bfc\u5165\u660e\u7ec6\u3002', null=True, upload_to=b'', verbose_name='attach')),
                ('detail', models.FileField(blank=True, help_text='\u60a8\u53ef\u5bfc\u5165\u9700\u6c42\u660e\u7ec6\uff0c\u6a21\u677f\u8bf7\u53c2\u8003\u6587\u6863FD0007', null=True, upload_to=b'', verbose_name='to be imported detail')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='basedata.Project', verbose_name='project')),
                ('refer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='selfhelp.WorkOrder', verbose_name='refer wo')),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='basedata.Material', verbose_name='service name')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'workorder apply',
                'verbose_name_plural': 'workorder apply',
            },
        ),
        migrations.AddField(
            model_name='woitem',
            name='workorder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='selfhelp.WorkOrder', verbose_name='workorder'),
        ),
        migrations.AddField(
            model_name='woextravalue',
            name='workorder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='selfhelp.WorkOrder', verbose_name='workorder'),
        ),
        migrations.AddField(
            model_name='reimbursement',
            name='wo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='selfhelp.WorkOrder', verbose_name='work order'),
        ),
    ]
