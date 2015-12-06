from django.conf.urls import url

from mailchimp.views import (
    webhook, dequeue, cancel, test_real, overview, campaign_information,
    schedule_campaign_for_object, test_campaign_for_object
)

urlpatterns = [
    url(r'^$', overview, name='mailchimp_overview', kwargs={'page': '1'}),
    url(r'^(?P<page>\d+)/$', overview, name='mailchimp_overview'),
    url(r'^send/(?P<content_type>\d+)/(?P<pk>\d+)/$', schedule_campaign_for_object, name='mailchimp_schedule_for_object'),
    url(r'^test/(?P<content_type>\d+)/(?P<pk>\d+)/$', test_campaign_for_object, name='mailchimp_test_for_object'),
    url(r'^test/(?P<content_type>\d+)/(?P<pk>\d+)/real/$', test_real, name='mailchimp_real_test_for_object'),
    url(r'^info/(?P<campaign_id>\w+)/$', campaign_information, name='mailchimp_campaign_info'),
    url(r'^dequeue/(?P<id>\d+)/', dequeue, name='mailchimp_dequeue'),
    url(r'^cancel/(?P<id>\d+)/', cancel, name='mailchimp_cancel'),
    url(r'^webhook/(?P<key>\w+)/', webhook, name='mailchimp_webhook'),
]
