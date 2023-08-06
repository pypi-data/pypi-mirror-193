from clockify_api_client_adgstudios.factories.abstract_factory import AbstractFactory
from clockify_api_client_adgstudios.models.time_entry import TimeEntry


class TimeEntryFactory(AbstractFactory):
    class Meta:
        model = TimeEntry

    api_key = None
