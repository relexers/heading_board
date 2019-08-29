from django.db import models


class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='title')
    content = models.TextField(null=True, blank=True, verbose_name='about')
    price = models.FloatField(null=True, blank=True, verbose_name='cost')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='date published')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Heading')

    class Meta:
        verbose_name_plural = 'Boards'
        verbose_name = 'Board'
        ordering = ['-published']


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='title')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Headings'
        verbose_name = 'Heading'
        ordering = ['name']
