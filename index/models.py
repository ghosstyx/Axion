from django.db import models

class User(models.Model):
    id = models.IntegerField(verbose_name="ID", primary_key=True)
    tap_count = models.IntegerField(verbose_name="Tap Count", default=0, null=True, blank=True)
    full_name = models.TextField(verbose_name="Full Name")
    rank = models.ForeignKey('Ranks', on_delete=models.SET_NULL, null=True, verbose_name="Rank",blank=True)
    profile_pic = models.FileField(upload_to="pfp/", verbose_name="Profile Picture", null=True, blank=True)
    date_of_birth = models.DateField(verbose_name="Date of Birth", null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = "User"
        verbose_name_plural = "Users"

    def save(self, *args, **kwargs):
        rank = Ranks.objects.filter(coin__gte=self.tap_count).first()
        self.rank = rank

        super().save(*args, **kwargs)

class Ranks(models.Model):
    id = models.IntegerField(auto_created=True, verbose_name="ID", primary_key=True)
    title = models.TextField(verbose_name="Title")
    coin = models.IntegerField(verbose_name="Coin")
    class Meta:
        verbose_name = "Rank"
        verbose_name_plural = "Ranks"
    def __str__(self):
        return self.title