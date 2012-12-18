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
    db = request.db
    songs = db.query(Song).all()
    db.flush()
    db.commit()
    if request.POST.get('search', False):
        search_item = request.POST['search']
        if db.query(Song).filter(Song.genre.ilike(search_item)).first():
            result = db.query(Song).filter(Song.genre.ilike(search_item)).first()
            return{
                'result': result,
                'songs': songs
            }
        else:
            message = "No Seach Result!"
            return dict(message=message, songs=songs)
    return {'songs': songs}
