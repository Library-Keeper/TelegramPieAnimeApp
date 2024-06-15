import logging
from pathlib import Path
from db import *
import flet_easy as fs
from core.config import ConfigApp

logging.basicConfig(level=logging.INFO)

app = fs.FletEasy(
    route_init="/",
    path_views=Path(__file__).parent / "views"
    )

ConfigApp(app)

with db:
    db.create_tables([User, Anime])

# We run the application
app.run()
