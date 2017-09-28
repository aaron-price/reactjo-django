from textwrap import dedent
from helpers.ui import paint
from helpers.file_manager import file_manager as f

def production():

    print(paint(dedent("""\
        To deploy the backend to heroku, run these commands:
        1. > cd {}

        2. > git init

        3. > git add -A

        4. > git commit -m "Initialize"

        5. > heroku login                             # Enter your login credentials

        6. > heroku create                            # Copy the URL it gives you

        7. Add that URL (as a string) to the ALLOWED_HOSTS list of each file
            in the settings/ directory. Leave off the 'https://' and the trailing slash

        8. > heroku config:set DISABLE_COLLECTSTATIC=1

        9. > heroku addons:create heroku-postgresql   # Create a database

        10. > git add -A

        11. > git commit -m "Updated ALLOWED_HOSTS"

        12. > git push heroku master

        (Optionally, if you want a superuser in production)
        13. > heroku run bash

        14. > python manage.py createsuperuser


        Note that if you visit the URL, the site is an unstyled mess. This is
        because it's not serving the static files. You can set that up yourself
        if you want, however, if this is being used as a backend api server,
        you probably won't ever want your end user visiting it anyway, so it
        doesn't matter as long as the API works.

    """.format(f('$out', '$'))), 'yellow'))
