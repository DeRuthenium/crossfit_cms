from cms.models import CMSPlugin, models


class NadpisSFonomPluginSetting(CMSPlugin):
    class Meta:
        verbose_name = 'HTML вставка'
        verbose_name_plural = 'HTML вставка'

    nadpis = models.CharField('Надпись', max_length=255)
    fon = models.ImageField('Фон')
    visota = models.IntegerField('Высота', default=100, )
