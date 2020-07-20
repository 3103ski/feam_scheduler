from enum import IntEnum


class AppointmentStatusTypes(IntEnum):
    NOT_STARTED = 1
    IN_PROGRESS = 2
    COMPLETED = 3

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
