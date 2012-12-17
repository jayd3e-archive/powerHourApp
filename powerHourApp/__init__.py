from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker
from powerHourApp.models import initialize_base
from pyramid.session import UnencryptedCookieSessionFactoryConfig


def get_db(request):
    maker = request.registry.settings['db.sessionmaker']
    return maker()


def main(global_config, **settings):
    '''Main config function'''

    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_base(engine)
    maker = sessionmaker(bind=engine)
    settings['db.sessionmaker'] = maker

    my_session_factory = UnencryptedCookieSessionFactoryConfig('itsaseekreet')
    config = Configurator(settings=settings,
                          session_factory=my_session_factory)

    config.set_request_property(get_db, 'db', reify=True)

    #Static routes
    config.add_static_view('style', 'powerHourApp:dependencies/')

    # Routes
    # HOME
    config.add_route('index', '/')

    config.scan('powerHourApp')
    return config.make_wsgi_app()
