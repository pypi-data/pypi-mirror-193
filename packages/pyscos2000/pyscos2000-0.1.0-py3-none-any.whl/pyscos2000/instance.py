"""SCOS Table instance classes"""
import csv


class TableCell:
    """A cell in an SCOS table"""
    def __init__(self, table, column, rawvalue):
        self.table = table
        self.column = column
        assert column in self.table.definition.columns

        self.columnidx = self.table.definition.columns.index(column)
        self.rawvalue = rawvalue
        if len(rawvalue) > 0:
            self._value = column.type.parse(rawvalue)
        else:
            self._value = column.type.parse(column.default)

    @property
    def value(self):
        """The parsed value of the cell"""
        return self._value

    @property
    def is_key(self):
        """Whether or not this cell is part of the row's primary key"""
        return self.column.is_key

    @property
    def type(self):
        """The column type of this cell"""
        return self.column.type

    def __eq__(self, other):
        if isinstance(other, TableCell):
            return self._value == other._value
        if isinstance(other, type(self._value)):
            return self._value == other
        raise ValueError(f"{type(other).__name__} not comparable to {type(self._value)}")

    def __lt__(self, other):
        if self._value is None:
            return True
        if isinstance(other, TableCell):
            return self._value < other._value
        if isinstance(other, type(self._value)):
            return self._value < other
        raise ValueError(f"{type(other).__name__} not comparable to {type(self._value)}")

    def __str__(self):
        return f'{self.column.name}: {self.value} ({self.rawvalue})'

    def __repr__(self):
        return str(self)


class TableRow:
    """A row in an SCOSTable"""

    def __init__(self, table, linenr):
        self.table = table
        self.items = []
        self.linenr = linenr

    def __len__(self):
        return len(self.items)

    def __getitem__(self, item):
        return self.get(item)

    def __iter__(self):
        yield from self.items

    @property
    def scos(self):
        """Convenience access to the SCOS instance"""
        return self.table.scos

    def key(self):
        """Return the primary key tuple identifying this row

        Will raise a ``RuntimeError`` if no primary key columns are defined
        """
        return tuple(cell.value
                     for cell in self.items
                     if cell.is_key)

    def get(self, item):
        """Obtain row item by index or column name"""
        if isinstance(item, int):
            return self.items[item]
        if isinstance(item, str):
            return self.items[self.table.definition.columnnames.index(item)]
        raise TypeError()

    def append(self, item):
        """Append this item to the end of the row"""
        self.items.append(item)

    def __lt__(self, other):
        return self.key() < other.key()

    def __str__(self):
        return str(self.items)

    def __repr__(self):
        return repr(self.items)


class BasicTable:
    """An instance of an SCOS table

    The table represents a parsed SCOS table with its rows
    available as the property ``rows``.
    The table definition is available as ``definition``, but you should
    never have to access it.
    Instead each row consists of a number of ``SCOSTableCell`` wich each contain
    the value in that column of that row, and have a reference to their
    column definition.
    """

    ROW_TYPE = TableRow
    CELL_TYPE = TableCell

    def __init__(self, scos, definition):
        self.scos = scos
        self.definition = definition
        self.rows = []

    @property
    def name(self):
        return self.definition.name

    def get(self, key):
        """Return the row of this key using the first few columns

        Depending on how many columns your ``key`` has, that many are used to
        identify a row.
        This is a close approximation to the primary key behaviour for tables
        that don't have a primary key.
        It will return the first found row. Which may or may not be the only
        row matching the ``key``.

        But all in all you're probably better off using ``find``.

        Returns ``None`` if entry is not found
        """
        if isinstance(key, list):
            key = tuple(key)
        if not isinstance(key, tuple):
            key = (key,)
        key = tuple(k.value if isinstance(k, self.CELL_TYPE) else k
                    for k in key)
        for row in self.rows:
            if all(row.items[i].value == key[i]
               for i in range(len(key))):
                return row
        return None

    def find(self, values):
        """Return a list of all matching rows given these ``values``

        - ``values`` can be a tuple or list to match against the columns in order,
        - ``values`` can also be a dictionary to match the respective named column
          against the given value
        """
        if isinstance(values, dict):
            for row in self.rows:
                matches = all(sval == row[name].value
                              for name, sval in values.items())
                if matches:
                    yield row

        if isinstance(values, (tuple, list)):
            for row in self.rows:
                matches = all(value == row[idx].value
                              for idx, value in enumerate(values))
                if matches:
                    yield row

    def parse(self):
        """Parse the table name"""
        context = self.scos.open_table(self.name)
        if context is not None:
            with context as tabbed:
                reader = csv.reader(tabbed, dialect=CSVDialect)
                self._parse_from_reader(reader)
        return self

    def _parse_from_reader(self, reader):
        """Parse the rows from the given csv.reader instance"""
        for linenr, row in enumerate(reader):
            self.rows.append(self.ROW_TYPE(self, linenr+1))
            for columnidx, field in enumerate(row):
                column = self.definition.columns[columnidx]
                self.rows[-1].append(self.create_cell(column, field))

    def create_cell(self, column, field):
        """Return a new instance of ``CELL_TYPE`` for this column"""
        return self.CELL_TYPE(self, column, field)

    def can_merge(self, other):
        """Whether or not the ``other`` table's content can be merged

        Conditions are:

        - no clashing entries in the primary keys
        - same table name
        """
        return self.definition.filename == other.definition.filename

    def merge(self, other):
        """Merge the ``other`` table's content into this table"""
        self.rows += other.rows
        self.rows.sort()

    def __iter__(self):
        yield from self.rows

    def sort(self, full=False):
        """Sort the rows of this table

        By default only the key column(s) are used for sorting.

        If there are no key columns or ``full`` is ``True``, all columns
        will be used for sorting.

        The rows are sorted in place, but the function returns this instance
        of the table, for convenience.
        """
        sortcolumns = self.definition.primary_key[:]
        if len(sortcolumns) == 0 or full:
            sortcolumns = range(len(self.definition.columns))

        self.rows.sort(key=lambda r: [r.items[i] for i in sortcolumns])

        return self


class Table(BasicTable):
    """The same as ``pyscos2000.instance.BasicTable``, but with an index

    There is also an index over the rows based on the definition's primary
    key. You can use the ``get`` method to obtain rows by their index.
    """
    def __init__(self, scos, definition):
        super().__init__(scos, definition)
        self.index = {}

    def get(self, key):
        """Return the row of this key using the index

        Usually ``key`` is of type ``tuple``, but for the lazy developer there
        are a few conveniences built in:

        - if a table has only one key column, you can just pass one ``key`` value
          and ``get`` will find it
        - if you pass a list instead of a tuple, ``get`` will convert the list
          and still find the correct entry
        - if key is or consists of ``TableCell`` instances, ``get`` will use their
          respective ``.value``

        Returns ``None`` if entry is not found
        """
        if isinstance(key, list):
            key = tuple(key)
        if not isinstance(key, tuple):
            key = (key,)
        key = tuple(k.value if isinstance(k, self.CELL_TYPE) else k
                    for k in key)
        return self.index.get(key, None)

    def build_index(self):
        """(Re-)build the index of the rows based on the key-columns"""
        if len(self.definition.primary_key) == 0:
            raise ValueError(f"No primary key for {type(self.definition).__name__}")
        self.index = {}
        for row in self.rows:
            self.index[row.key()] = row

    def parse(self):
        retval = super().parse()
        if len(self.definition.primary_key) > 0:
            self.build_index()
        return retval

    def can_merge(self, other):
        """Whether or not the ``other`` table's content can be merged

        Conditions are:

        - no clashing entries in the primary keys
        - same table name
        """
        return self.definition.filename == other.definition.filename \
           and len(set(self.index.keys()) & set(other.index.keys())) == 0

    def merge(self, other):
        """Merge the ``other`` table's content into this table"""
        self.rows += other.rows
        self.rows.sort()
        if len(self.definition.primary_key) > 0:
            self.build_index()

    def sort(self, full=False):
        super().sort(full)
        if len(self.definition.primary_key) > 0:
            self.build_index()
        return self


class CSVDialect(csv.Dialect):
    """CSV dialect for SCOS-style ``.dat`` files"""
    delimiter = '\t'
    doublequote = False
    escapechar = None
    lineterminator = '\r\n'
    quoting = csv.QUOTE_NONE
    skipinitialspace = False
    strict = True
