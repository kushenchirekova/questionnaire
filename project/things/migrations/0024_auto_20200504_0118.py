# Generated by Django 2.2.5 on 2020-05-03 19:18

from django.db import migrations


def create_through_relations(apps, schema_editor):
    TestInfo = apps.get_model('things', 'TestInfo')
    TestResult = apps.get_model('things', 'TestResult')
    for test in TestInfo.objects.all():
        for student in test.students.all():
            TestResult(
                student=student,
                test=test,
            ).save()


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0023_auto_20200504_0118'),
    ]

    operations = [
        migrations.RunPython(create_through_relations, reverse_code=migrations.RunPython.noop),
    ]
