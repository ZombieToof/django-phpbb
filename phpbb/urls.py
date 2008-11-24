# -*- coding: utf-8 -*-
# This file is part of django-phpbb, integration between Django and phpBB
# Copyright (C) 2007-2008  Maciej Bliziński
# 
# django-phpbb is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# django-phpbb is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with django-phpbb; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor,
# Boston, MA  02110-1301  USA

from django.conf.urls.defaults import *
# import django.contrib.phpbb
import django.contrib.phpbb.views
import models

# forumqs = models.ForumForum.objects.filter(auth_read = 0).
# exclude(forum_name = 'INDEX PAGE').exclude(forum_name = 'MEMBERLIST')
forumqs = (models.ForumForum.objects.exclude(forum_name='INDEX PAGE').
	       exclude(forum_name='MEMBERLIST').
           # FIXME: hardcoded forum IDs
	       exclude(forum_id=15).
	       exclude(forum_id=6))

urlpatterns = patterns('',
    # Example:
    # (r'^atopowe/', include('atopowe.apps.foo.urls.foo')),

    (r'^$', 'django.views.generic.list_detail.object_list',
        {'queryset': forumqs, }),
    (r'^topics/(?P<topic_id>[0-9]+)/(?P<slug>[\w-]*)/page(?P<page_no>[0-9]+)/$',
        'django.contrib.phpbb.views.topic', ),
    (r'^topics/(?P<topic_id>[0-9]+)/(?P<slug>[\w-]*)/$',
        'django.contrib.phpbb.views.topic', ),
    (r'^(?P<forum_id>[0-9]+)/(?P<slug>[\w-]*)/$',
        'django.contrib.phpbb.views.forum_index', ),
    (r'^(?P<forum_id>[0-9]+)/(?P<slug>[\w-]*)/page(?P<page_no>[0-9]+)/$',
        'django.contrib.phpbb.views.forum_index', ),
    (r'^(?P<forum_id>[0-9]+)/$',
        'django.contrib.phpbb.views.forum_index', {'slug': ''}),
    (r'^unanswered/$', 'django.contrib.phpbb.views.unanswered', ),
    (r'^viewtopic.php$', 'django.contrib.phpbb.views.handle_viewtopic', ),
    # (r'^(?P<slug>[0-9]+)/[\w-]/$',
    #   'django.views.generic.list_detail.object_list', ),

    # (r'^forum/$', 'django.views.generic.simple.redirect_to',
    #   {'url': 'http://www.atopowe-zapalenie.pl/forum/'}),
    # (r'^forum/(?P<path>.*)$', 'django.views.generic.simple.redirect_to',
    #   {'url': 'http://www.atopowe-zapalenie.pl/forum/%(path)s'}),
    # (r'^accounts/$', 'atopowe.portal.views.redirect_to_main', ),
)