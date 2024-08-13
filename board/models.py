from django.conf import settings
from django.db import models


NULLABLE = {'blank': True,
            'null': True}


class Ad(models.Model):
    image = models.ImageField(
        upload_to="images/",
        verbose_name="Photo",
        help_text="Attach a photo of your product",
        **NULLABLE,
    )

    title = models.CharField(
        max_length=200,
        verbose_name="Product title",
        help_text="Type your product title here",
    )

    price = models.PositiveIntegerField(
        verbose_name="Price",
        help_text="Type your product price here"
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Ad author",
        help_text="Choose ads' author",
        default='Anonymous',
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Add creation date",
    )

    description = models.CharField(
        max_length=1000,
        verbose_name="Product description",
        help_text="Type your product description here",
        **NULLABLE,
    )

    class Meta:
        verbose_name = "Ad"
        verbose_name_plural = "Ads"
        ordering = ("-created_at", )


class Comment(models.Model):
    text = models.CharField(
        max_length=1000,
        verbose_name="Comment",
        help_text="Leave your comment here",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Comment add time",
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Comment author",
        help_text="Choose author",
    )
    ad = models.ForeignKey(
        Ad,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Ads",
        help_text="Ad to which you leave comment",
    )

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ("-created_at", )
