from ..linking import (
    change_db_name,
    check_duplicate_codes,
    check_internal_linking,
    link_internal,
)
from bw2data import databases
from bw2io.importers.base_lci import LCIImporter


class WurstImporter(LCIImporter):
    def __init__(self, db_name, data):
        self.db_name = db_name
        self.data = data
        for act in self.data:
            act['database'] = self.db_name

    def write_database(self):
        assert not self.statistics()[2], "Not all exchanges are linked"
        assert self.db_name not in databases, "This database already exists"
        super().write_database()


def write_brightway2_database(data, name):
    """Write a new database (``data``) as a new Brightway2 database named ``name``.

    You should be in the correct project already.

    This function will do the following:

    * Change the database name for all activities and internal exchanges to ``name``. All activities will have the new ``name``, even if the original data came from multiple databases.
    * Relink exchanges using the default fields: ``('activity', 'product', 'location', 'unit')``.
    * Check that all internal links resolve to actual activities, If the ``input`` value is ``('foo', 'bar')``, there must be an activity with the code ``bar``.
    * Check to make sure that all activity codes are unique
    * Write the data to a new Brightway2 SQLite

    Will raise an assertion error is ``name`` already exists.

    Doesn't return anything."""
    assert name not in databases, "This database already exists"

    change_db_name(data, name)
    link_internal(data)
    check_internal_linking(data)
    check_duplicate_codes(data)
    WurstImporter(name, data).write_database()
