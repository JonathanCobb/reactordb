"""
from service.models import sheets
sheet = sheets.MasterSheet("/home/richard/Code/External/reactordb/service/tests/resources/MasterSheet.csv")
obs = [o for o in sheet.objects()]
"""

"""
from service.models import Reactor
r = Reactor()
r.reactor_name = "richard"
link = {"url" : "a", "text" : "b"}
r.wna_links = [link]
r.wna_links
r.wnn_links = [link]
r.wnn_links
r.reactor_name
print "hello"
"""

"""
from octopus.core import initialise
initialise()

from service.tests import fixtures
from service.lib import importer
master_path = fixtures.SheetFactory.master_sheet_path()
pris_path = fixtures.SheetFactory.pris_sheet_path()
importer.import_reactordb(master_path, pris_path, None)
"""

"""
from octopus.core import initialise
initialise()

from service.tests import fixtures
from service.lib import importer
master_path = fixtures.SheetFactory.master_sheet_path()
pris_path = fixtures.SheetFactory.pris_sheet_path()
history_path = fixtures.SheetFactory.history_sheet_path()
importer.import_reactordb(master_path, pris_path, history_path)
"""


"""
from octopus.core import initialise
initialise()

from service import models
r = models.Reactor()
r.reactor_name = "richard-1"
r.save()
"""

"""
from octopus.core import initialise
initialise()
"""

from octopus.core import initialise
initialise()

from service.lib import pageScraper
pageScraper.scrape_all_pages(100)