"""The framework to write SCOS instance consistency/integrity checkers

To implement a new checker, subclass ``SCOSTableChecker`` and overwrite
at least the ``check_row`` function and the ``ACCEPTED_TABLES`` property to
select the tables that you wish to run this checker on.
"""
ALL_CHECKERS = []


class SCOSTableChecker:
    """The very basic visitor for SCOS table instances

    Subclasses are automatically registered in the global ``ALL_CHECKERS`` list
    to make it easier to just run all existing checkers on your SCOS instance.

    Parameters
    ----------
    scos : pyscos2000.SCOS2000
        is the instance of the SCOS-2000 that will be tested
    reporter : pyscos2000.Reporter
        the reporter to use for warnings, errors, etc.
    """
    ACCEPTED_TABLES = tuple()
    """The tables that this checker will be run on

    Must be an iterable of ``TableDefinition`` (not their instances).
    """

    def __init_subclass__(cls):
        ALL_CHECKERS.append(cls)

    def __init__(self, scos, reporter, pedantic=False):
        self.scos = scos
        self.reporter = reporter
        self.table = None
        self._cur_row = None
        self.pedantic = pedantic

    def visit(self, table):
        """Called when visiting a table"""
        if not self.accept(table):
            return

        self.table = table
        for row in table.rows:
            self._cur_row = row
            self.check_row(row)

    def accept(self, table):
        """Whether or not this table can be checked by this visitor

        The default implementation will use ``self.ACCEPTED_TABLES``, but you
        can overwrite this function to implement your own way of checking
        whether or not you want to run this checker on the given ``table``.

        Parameters
        ----------
        table : pyscos2000.Table
            Instance of a ``pyscos2000.instance.Table`` from the ``pyscos2000.SCOS``
            instance that's being checked
        """
        return isinstance(table.definition, self.ACCEPTED_TABLES)

    def check_row(self, row):
        """Called when a row is being visited"""

    def error(self, description):
        """Report an error in the current table and row"""
        assert self.reporter is not None
        assert self.table is not None
        assert self._cur_row is not None
        self.reporter.error(self.table.name,
                            self._cur_row.linenr,
                            description)

    def warning(self, description):
        """Report a warning in the current table and row"""
        assert self.reporter is not None
        assert self.table is not None
        assert self._cur_row is not None
        self.reporter.warning(self.table.name,
                              self._cur_row.linenr,
                              description)

    def info(self, description):
        """Report an informational statement in the current table and row"""
        assert self.reporter is not None
        assert self.table is not None
        assert self._cur_row is not None
        self.reporter.info(self.table.name,
                           self._cur_row.linenr,
                           description)
