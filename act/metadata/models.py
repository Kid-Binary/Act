# act_project/act/metadata/models.py
from urllib.parse import urljoin

from django.db import models, transaction
from django.core.exceptions import ObjectDoesNotExist

from stdimage.models import StdImageField

# Notice overridden transmeta import!
from act.services.transmeta import TransMeta
from act.services.file_name import RandomFileName
from act.utils import get_default_URL

from .utils import truncate_description


class Metadata(models.Model, metaclass=TransMeta):
    IMAGE_PATH = 'metadata/images/'

    variations = {
        'open_graph': {'width': 1200, 'height': 630, 'crop': True},
        'twitter_card': {'width': 1120, 'height': 600, 'crop': True},
    }

    image = StdImageField(
        'Зображення',
        upload_to=RandomFileName(IMAGE_PATH),
        variations=variations)

    url_name = models.CharField('Роутінг', max_length=100)
    title = models.CharField('Назва сторінки', max_length=100)
    description = models.CharField('Опис сторінки', max_length=250)
    robots = models.CharField('Інформація для ботів', max_length=100)

    class Meta:
        verbose_name = 'Метадані'
        verbose_name_plural = 'Метадані'

        translate = ('title', 'description', )

    def __str__(self):
        return str(self.title) or self.__class__.__name__

    @staticmethod
    def build_metadata_from_dict(master_metadata, object_metadata_dict):
        metadata = Metadata(**object_metadata_dict)

        metadata.description_uk = truncate_description(
            metadata.description_uk, 250)

        if not metadata.image:
            metadata.image = master_metadata.image

        if not metadata.robots:
            metadata.robots = master_metadata.robots

        return metadata

    def image_preview(self):
        return '<img src="%s" width="300" max-width="300">' % (self.image.url)
    image_preview.allow_tags = True
    image_preview.short_description = 'Превʼю зображення'

    def provide_open_graph(self, open_graph_type):
        self.open_graph = OpenGraph(
            metadata=self, type=open_graph_type)

    def provide_twitter_card(self, twitter_card):
        self.twitter_card = TwitterCard(
            metadata=self, card=twitter_card)


class MetadataAttributeMixin():
    metadata = None

    def get_metadata_attribute(self, attribute):
        if not isinstance(self.metadata, Metadata):
            raise ImproperlyConfigured('Metadata object is not set correctly')

        return getattr(self.metadata, attribute)


class OpenGraph(MetadataAttributeMixin, models.Model):
    TYPE_WEBSITE = 'website'
    TYPE_ARTICLE = 'article'

    TYPES = [TYPE_WEBSITE, TYPE_ARTICLE]

    DESCRIPTION_LENGTH = 250

    _type = None

    def __init__(self, *args, **kwargs):
        self.metadata = kwargs.pop('metadata')

        open_graph_type = kwargs.pop('type', self.TYPE_WEBSITE)
        if open_graph_type in self.TYPES:
            self._type = open_graph_type

        super(OpenGraph, self).__init__(*args, **kwargs)

    def __str__(self):
        return str(self.__class__.__name__)

    @property
    def type(self):
        return self._type

    @property
    def url(self):
        return self.get_metadata_attribute('url_name')

    @property
    def title(self):
        return self.get_metadata_attribute('title')

    @property
    def description(self):
        return truncate_description(
            self.get_metadata_attribute('description'),
            self.DESCRIPTION_LENGTH)

    @property
    def image(self):
        return self.get_metadata_attribute('image')


class TwitterCard(MetadataAttributeMixin, models.Model):
    CARD_SUMMARY = 'summary'
    CARD_SUMMARY_LARGE_IMAGE = 'summary_large_image'

    CARDS = [CARD_SUMMARY, CARD_SUMMARY_LARGE_IMAGE]

    DESCRIPTION_LENGTH = 140

    _card = None

    def __init__(self, *args, **kwargs):
        self.metadata = kwargs.pop('metadata')

        twitter_card = kwargs.pop('card', self.CARD_SUMMARY)
        if twitter_card in self.CARDS:
            self._card = twitter_card

        super(TwitterCard, self).__init__(*args, **kwargs)

    def __str__(self):
        return str(self.__class__.__name__)

    @property
    def card(self):
        return self._card

    @property
    def title(self):
        return self.get_metadata_attribute('title')

    @property
    def description(self):
        return truncate_description(
            self.get_metadata_attribute('description'),
            self.DESCRIPTION_LENGTH)

    @property
    def image(self):
        return self.get_metadata_attribute('image')
