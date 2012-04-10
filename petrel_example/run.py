from petrel.config import get_default_config

from petrel_example.views import TemplateAPI


def app(global_config, **settings):
    from petrel.content.document import Document
    from petrel.content.file import File
    from petrel.content.file import file_info
    from petrel.content.folder import Folder
    from petrel.content.image import Image
    from petrel.content.site import Site
    ## FIXME: perhaps we should rather use 'Configuration.include()'
    ## and the 'includeme()' pattern.
    config = get_default_config(global_config, **settings)
    config.customize_content_type(
        Document,
        display_templates=[{'id': 'default',
                            'template': 'petrel_example:templates/document.pt'}])
    config.customize_content_type(
        File,
        extra_views=[{'name': 'info',
                      'context': File,
                      'view': file_info,
                      'renderer': 'petrel_example:templates/file.pt'}])
    config.customize_content_type(
        File,
        extra_views=[{'name': 'info',
                      'context': Image,
                      'view': file_info,
                      'renderer': 'petrel_example:templates/image.pt'}])
    config.customize_content_type(
        Folder,
        display_templates=[
            {'id': 'default',
             'label': 'Default',
             'description': 'Shows the body text',
             'template': 'petrel_example:templates/folder.pt'},
            {'id': 'listing',
             'label': 'Listing',
             'description': 'Shows a list of contained items.',
             'template': 'petrel_example:templates/folder_listing.pt'}])
    config.customize_content_type(
        Site,
        display_templates=[{'id': 'default',
                            'template': 'petrel_example:templates/folder.pt'}])
    config.add_static_view(name='static', path='petrel_example:static')
    config.register_template_api(TemplateAPI)
    return config.make_wsgi_app()
