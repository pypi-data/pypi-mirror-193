"""Framework to report errors in an SCOS instance"""
import enum
import sys


class FindingType(enum.Enum):
    INFO = 50
    WARNING = 40
    ERROR = 30


class Reporter:
    """Generic error report interface"""
    def error(self, table, line, description):
        """When an error was found in ``table``'s ``line``"""
        return self.report(FindingType.ERROR, table, line, description)

    def warning(self, table, line, description):
        """When a warning was found in ``table``'s ``line``"""
        return self.report(FindingType.WARNING, table, line, description)

    def info(self, table, line, description):
        """When an information statement should be reported about ``table``'s ``line``"""
        return self.report(FindingType.INFO, table, line, description)

    def report(self, finding, table, line, description):
        """A ``finding`` in ``table``'s ``line``"""
        raise NotImplementedError("Implement in a subclass")


class StdErrReporter(Reporter):
    """Simple report that just prints to stderr"""
    def report(self, finding, table, line, description):
        print(f"[{finding.name}] {table} Line {line}: {description}",
              file=sys.stderr)
