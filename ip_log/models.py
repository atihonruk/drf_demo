from django.db import models
from django.utils.translation import ugettext_lazy as _


class LogEntry(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField()

    class Meta:
        ordering = ('timestamp',)
        verbose_name = _('log entry')
        verbose_name_plural = _('log entries')
