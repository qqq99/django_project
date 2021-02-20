from django.db import models
from tastypie.resources import ModelResource
from movies.models import Movie
# We use resource to differentiate the "APP data model" from the "REST resources"
# derive this class from the tastypie ModelResources class


class MovieResource(ModelResource):
    # tatsypie looks for an innerclass called Meta: which define some meta data about our movie rosources
    class Meta:
        queryset = Movie.objects.all()
        resource_name = 'movies'
