from pyramid.view import (
    view_config,
    )
from pyramid.httpexceptions import (
    HTTPFound
)
from pyramid.security import NO_PERMISSION_REQUIRED
from powerHourApp.models import (
    Song,
    User,
)


@view_config(route_name='index', renderer='powerHourApp:templates/index.mako', permission=NO_PERMISSION_REQUIRED)
def index(request):
    return {}
