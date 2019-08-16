from django.db import models


class DoubanMovie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    img_url = models.URLField()
    rate = models.DecimalField(decimal_places=1, max_digits=3)
    detail_url = models.URLField()

    class Meta:
        managed = True
        db_table = 'douban_movie'
