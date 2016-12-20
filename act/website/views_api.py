# act_project/act/website/views_api.py
from django.http import Http404

from rest_framework.response import Response
from rest_framework.generics import (
    GenericAPIView, ListAPIView, RetrieveAPIView, CreateAPIView,
)
from rest_framework.mixins import (
    CreateModelMixin, UpdateModelMixin,
)
from rest_framework.pagination import (
    LimitOffsetPagination, PageNumberPagination,
)

from django_filters import rest_framework as django_filters

from .models import (
    IntroContent,
    Sponsor, Social, Activity,
    ProjectArea, Project,
    EventCategory, Event,
    City, Participant, Contact,
    Centre,
    Worksheet,
)
from .serializers import (
    IntroContentSerializer,
    SponsorSerializer, SocialSerializer, ActivitySerializer,
    ProjectAreaSerializer, ProjectSerializer,
    EventCategorySerializer, EventSerializer,
    CitySerializer, ParticipantSerializer, ContactSerializer,
    CentreListSerializer, CentreDetailSerializer,
    CentreCitySerializer, CentreProjectsSerializer, CentreEventsSerializer,
    WorksheetSerializer,
)


# IntroContent

class IntroContentSingular(GenericAPIView):
    '''
    This view is tricky, as it overrides common behavior of `get_object()`
    method. It does not require positional `pk` argument, because it's
    intention is to return first & only one object of a given queryset
    '''
    queryset = IntroContent.objects.all()
    serializer_class = IntroContentSerializer

    def get_object(self):
        instance = self.get_queryset().first()
        return instance

    def get(self, request):
        intro_content = self.get_object()

        if not intro_content:
            raise Http404

        serializer = IntroContentSerializer(intro_content)
        return Response(serializer.data)


# Sponsor

class SponsorList(ListAPIView):
    serializer_class = SponsorSerializer
    queryset = Sponsor.objects.all()


class SponsorDetail(RetrieveAPIView):
    serializer_class = SponsorSerializer
    queryset = Sponsor.objects.all()


# Social

class SocialList(ListAPIView):
    serializer_class = SocialSerializer
    queryset = Social.objects.all()


class SocialDetail(RetrieveAPIView):
    serializer_class = SocialSerializer
    queryset = Social.objects.all()


# Social

class ActivityList(ListAPIView):
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()


class ActivityDetail(RetrieveAPIView):
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()


# ProjectArea

class ProjectAreaList(ListAPIView):
    serializer_class = ProjectAreaSerializer
    queryset = ProjectArea.objects.all()


class ProjectAreaDetail(RetrieveAPIView):
    serializer_class = ProjectAreaSerializer
    queryset = ProjectArea.objects.all()


# Project

class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = Project.LIMIT['default']
    max_limit = Project.LIMIT['max']

    limit_query_param = 'limit'


class ProjectPageNumberPagination(PageNumberPagination):
    page_size = Project.PAGE_SIZE['default']
    max_page_size = Project.PAGE_SIZE['max']

    page_query_param = 'page'


class ProjectFilter(django_filters.FilterSet):
    class Meta:
        model = Project
        fields = ['project_area', 'centres']


class ProjectList(ListAPIView):
    serializer_class = ProjectSerializer

    pagination_class = ProjectPageNumberPagination

    filter_backends = (django_filters.DjangoFilterBackend,)
    filter_class = ProjectFilter

    def get_queryset(self):
        queryset = Project.objects.order_by('-started_at')

        limit = self.request.query_params.get('limit', None)

        if limit is not None:
            self.pagination_class = ProjectLimitOffsetPagination

        return queryset


class ProjectDetail(RetrieveAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


# EventCategory

class EventCategoryList(ListAPIView):
    serializer_class = EventCategorySerializer
    queryset = EventCategory.objects.all()


class EventCategoryDetail(RetrieveAPIView):
    serializer_class = EventCategorySerializer
    queryset = EventCategory.objects.all()


# Event

class EventLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 3
    limit_query_param = 'limit'
    max_limit = 100


class EventPageNumberPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'page'
    max_page_size = 100


class EventFilter(django_filters.FilterSet):
    class Meta:
        model = Event
        fields = ['event_category', 'project', 'centres']


class EventList(ListAPIView):
    serializer_class = EventSerializer

    pagination_class = EventPageNumberPagination

    filter_backends = (django_filters.DjangoFilterBackend,)
    filter_class = EventFilter

    def get_queryset(self):
        queryset = Event.objects.order_by('-created_at')

        limit = self.request.query_params.get('limit', None)

        if limit is not None:
            self.pagination_class = EventLimitOffsetPagination

        return queryset


class EventDetail(RetrieveAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()


# City

class CityList(ListAPIView):
    serializer_class = CitySerializer
    queryset = City.objects.all()


# Participant

class ParticipantList(ListAPIView):
    serializer_class = ParticipantSerializer
    queryset = Participant.objects.all()


# Contact

class ContactList(ListAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


class ContactDetail(RetrieveAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


# Centre

class CentreList(ListAPIView):
    '''
    You can use `related` quary parameter to specify singular relation that
    should be included in serialized objects list. Available options are:

    1. 'related=city', to include only nested city object
    2. 'related=projects', to include projects as well as city
    3. 'related=events', to include events as well as city
    '''
    serializer_class = CentreListSerializer

    def get_queryset(self):
        queryset = Centre.objects.all()

        related = self.request.query_params.get('related')

        if related == 'city':
            self.serializer_class = CentreCitySerializer
        elif related == 'projects':
            self.serializer_class = CentreProjectsSerializer
        elif related == 'events':
            self.serializer_class = CentreEventsSerializer

        return queryset


class CentreDetail(RetrieveAPIView):
    serializer_class = CentreDetailSerializer
    queryset = Centre.objects.all()


# Worksheet

class WorksheetList(CreateModelMixin, GenericAPIView):
    serializer_class = WorksheetSerializer
    queryset = Worksheet.objects.all()

    def perform_create(self, serializer):
        '''
        Send an e-mail notification on succesfull serializer save
        '''
        serializer.save()
        serializer.send_email()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)