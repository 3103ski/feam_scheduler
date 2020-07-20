from django.db import models


class DaySchedule(models.Model):
    briefingTime = models.TimeField(null=True)
    reminders = models.TextField(null=True, blank=True)
    # rampCrew = StaffMember
    date = models.DateField(null=True)

    def serialize(self):
        return {
            "briefingTime": self.briefingTime,
            "reminders": self.reminders,
            "date": self.date
        }

    def __str__(self):
        return self.reminders
