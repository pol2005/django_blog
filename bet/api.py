from __future__ import unicode_literals

from django.http import HttpResponse
from tastypie.resources import ModelResource
from tastypie.utils.mime import build_content_type

from .models import Article
from tastypie.api import Api
from django.utils.html import strip_tags
from templatetags.bet_tags import remove_whitespace

class ArticleResource(ModelResource):
    class Meta:
        queryset = Article.published.all()
        resource_name = 'post'
        include_absolute_url = True
        fields = [u'title',u'body','image','created']
        allowed_methods = ['get']

    def dehydrate(self, bundle):
        bundle.data['body'] = remove_whitespace(strip_tags(bundle.data['body']))
        return bundle

    def create_response(self, request, data, response_class=HttpResponse, **response_kwargs):
        desired_format = self.determine_format(request)
        serialized = self.serialize(request, data, desired_format)
        response = response_class(content=serialized, content_type=build_content_type(desired_format),
                                  **response_kwargs)
        response['Content-Type'] = ' application/json;charset=utf-8'
        return response
    # def dehydrate(self, bundle):
    #     bundle.data['my_field'] = bundle.data['get_absolute_url']
    #     return bundle


v1_api = Api(api_name='v1')
v1_api.register(ArticleResource())