from django import template

register = template.Library()

@register.simple_tag
def get_links():
    links =  [{
        'name': 'Home',
        'href': '/',
        'icon': 'fa-house',
    }, {
        'name': 'Contact',
        'href': '/contact',
        'icon': 'fa-paper-plane',
    }, {
        'name': 'About',
        'href': '/about',
        'icon': 'fa-address-card',
    },{
        'name': 'Marketplace',
        'href': '/marketplace/',
        'icon': 'fa-newspaper',
    },{
        'name': 'Forum',
        'href': '/forum',
        'icon': 'fa-comment', #look for your icon here https://fontawesome.com/search?ic=free
    }]

    return links

@register.simple_tag
def get_links_authenticated():
    links =  [{
        'name': 'Home',
        'href': '/',
        'icon': 'fa-house',
    }, {
        'name': 'Contact',
        'href': '/contact',
        'icon': 'fa-paper-plane',
    }, {
        'name': 'About',
        'href': '/about',
        'icon': 'fa-address-card',
    },{
        'name': 'Marketplace',
        'href': '/marketplace/',
        'icon': 'fa-newspaper',
    },{
        'name': 'Add post',
        'href': '/marketplace/create',
        'icon': 'fa-plus',
    },{
        'name': 'Forum',
        'href': '/forum',
        'icon': 'fa-comment', #look for your icon here https://fontawesome.com/search?ic=free
    }]
         
    return links
