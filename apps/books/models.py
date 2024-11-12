from django.utils.translation import gettext as _
from django.db import models

class Author(models.Model):
    full_name = models.CharField(_("Full name"), max_length=255)
    bio = models.TextField(_("Bio"))

    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")


class Book(models.Model):
    title = models.CharField(_("Title"), max_length=255)
    description = models.TextField(_("Description"))
    cover = models.ImageField(_("Cover"), upload_to="covers")
    
    author = models.ForeignKey(
        to="Author", 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="books",
        verbose_name=_("Author")
    )

    quantity = models.IntegerField(_("Quantity"), default=0)
    price = models.DecimalField(_("Price"), decimal_places=2, max_digits=12)

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")


