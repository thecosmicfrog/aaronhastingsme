"""
Copyright © 2020 Aaron Hastings

This file is part of aaronhastings.me.

aaronhastings.me is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

aaronhastings.me is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with aaronhastings.me.  If not, see <http://www.gnu.org/licenses/>.
"""

from django.shortcuts import render


def home(request):
    cards = {
        'profile': {
            'title': 'About me',
            'text': {
                'location': {
                    'img_name': 'place',
                    'text': 'Dublin, Ireland'
                },
                'career': {
                    'img_name': 'work',
                    'text': 'Systems Engineer by day',
                },
                'personal': {
                    'img_name': 'couch',
                    'text': 'Developer by night',
                },
                'interest1': {
                    'img_name': 'code',
                    'text': 'Linux and open source enthusiast'
                },
                'interest2': {
                    'img_name': 'flight',
                    'text': 'Aviation and transport geek'
                },
                'interest3': {
                    'img_name': 'settings',
                    'text': 'I automate things'
                }
            },
            'img_name': 'profile_photo'
        },
        'row_top': {
            'linkedin': {
                'title': 'LinkedIn',
                'text': 'Connect with me on LinkedIn',
                'img_name': 'li',
                'url': 'https://www.linkedin.com/in/hastingsaaron'
            },
            'code': {
                'title': 'Code',
                'text': 'My code and contributions',
                'img_name': 'code',
                'url': 'https://github.com/thecosmicfrog'
            }
        },
        'row_bottom': {
            'blog': {
                'title': 'Blog',
                'text': 'My blog',
                'img_name': 'blog',
                'url': 'https://blog.aaronhastings.me'
            },
            'luas_at_a_glance': {
                'title': 'Luas at a Glance',
                'text': 'Android app for Dublin\'s light rail',
                'img_name': 'laag',
                'url': 'https://play.google.com/store/apps/details?id=org.thecosmicfrog.luasataglance'
            }
        }
    }

    card_profile = cards['profile']

    return render(request, 'home.html', locals())

