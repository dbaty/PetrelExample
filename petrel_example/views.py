from pyramid.renderers import get_renderer

from petrel.views.utils import TemplateAPI as Base


class TemplateAPI(Base):

    def __init__(self, request):
        Base.__init__(self, request)
        self.layout = get_renderer(
            'petrel_example:templates/layout.pt').implementation()
