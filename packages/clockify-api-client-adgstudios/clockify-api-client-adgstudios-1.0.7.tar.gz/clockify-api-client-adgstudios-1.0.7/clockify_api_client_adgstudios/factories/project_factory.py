from clockify_api_client_adgstudios.factories.abstract_factory import AbstractFactory
from clockify_api_client_adgstudios.models.project import Project


class ProjectFactory(AbstractFactory):
    class Meta:
        model = Project

    api_key = None
