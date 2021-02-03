from django.db import models
from django.utils.text import slugify
from django.conf import settings
from django.urls import reverse


class Towns(models.Model):
    class Meta:
        verbose_name = _('town')
        verbose_name_plural = _('towns')
        ordering = ['order']

    town_name = models.CharField(max_length=100, default='', blank=True)
    mayor = models.CharField(max_length=100, default='', blank=True)
    town_clerk = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE,
                                   related_name='clerks_towns')
    staff_members = models.ManyToManyField(settings.AUTH_USER_MODEL, default=1, related_name='staff_towns')

    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    active = models.NullBooleanField(default=False)
    description = PlaceholderField('department_description')
    image = FilerImageField(blank=True, null=True, on_delete=models.SET_NULL)

    slug = models.SlugField(_('slug'), blank=False, default='', db_index=True,
                            help_text=_('Please supply the course slug.'), max_length=128)

    def get_absolute_url(self):
        return reverse('towns:town', kwargs={'slug': self.slug, })

    def __str__(self):
        return self.town_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.town_name)
        super(Towns, self).save(*args, **kwargs)