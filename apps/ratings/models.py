from django.db import models
from django.db.models.deletion import SET_NULL
from django.utils.translation import gettext_lazy as _ 
from django_rest_api.settings.base import AUTH_USER_MODEL 
from apps.common.models import TimeStampedUUIDMpdel
from apps.profiles.models import Profile

class Rating(TimeStampedUUIDMpdel):

    class Range(models.IntegerChoices):
        RATING_1 = 1, _("Poor")
        RATING_2 = 2, _("Fair")
        RATING_3 = 3, _("Good")
        RATING_4 = 4, _("Very Good")
        RATING_5 = 5, _("Excellent")

    rater = models.ForeignKey(AUTH_USER_MODEL, verbose_name=_("User Providing the rating"), on_delete=SET_NULL, null=True)
    agent = models.ForeignKey(Profile, verbose_name=_("Agent being rating"), related_name="agent_review", on_delete=SET_NULL, null=True)
    rating = models.IntegerField(verbose_name=_("Rating"), choices=Range.choices, help_text="1 = Poor, 2 = Fair, 3 = Good , 4 = Good, 5 = Excelent", default=0,)
    comment = models.TextField(verbose_name=_("Comment..."))

    class Meta:
        unique_together = ["rater", "agent"]

    def __str__(self):
        return f"{self.agent} rate at {self.rating}"
    
            

