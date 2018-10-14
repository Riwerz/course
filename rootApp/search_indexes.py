from haystack import indexes
from .models import Conspect


class ConspectIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    body = indexes.CharField(model_attr='body')
    pub_date = indexes.DateTimeField(model_attr='published_date')



    def get_model(self):
        return Conspect

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

