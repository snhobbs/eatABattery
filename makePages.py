from mezzanine.pages.models import Link
from django.db import models
class LinkData(object):
    def __init__(self, title, link, subtitle=None, subpages=None):
        self.title = title
        self.link=link
        self.subtitle = subtitle
        self.subpages = subpages

def assignLinkVals(linkData, parent = None):
    link = Link()
    link.title = linkData.title
    link.meta_title = linkData.title
    link.meta_description = linkData.subtitle
    link.set_parent(parent)
    link.set_slug(linkData.link)
    return link

pages = [
    LinkData("Home", "/"), 
    LinkData("Health Facts", "/Healthy_Living"),
    LinkData("Kirkland Corner", "/Kirkland_Corner"),
    LinkData("PJ", "/PJ")
]

def run():
    for page in pages:
        link = assignLinkVals(page)
        if page.subpages is not None:
            parent = link
            for subpage in page.subpages:
                link = assignLinkVals(subpage, parent)
                link.save()
