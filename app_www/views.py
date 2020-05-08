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
                    'img_name': 'deck',
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
                'url': 'https://www.aaronhastings.me'
            },
            'luas_at_a_glance': {
                'title': 'Luas at a Glance',
                'text': 'My Android app for Dublin\'s light rail',
                'img_name': 'laag',
                'url': 'https://play.google.com/store/apps/details?id=org.thecosmicfrog.luasataglance'
            }
        }
    }

    card_profile = cards['profile']

    return render(request, 'home.html', locals())

