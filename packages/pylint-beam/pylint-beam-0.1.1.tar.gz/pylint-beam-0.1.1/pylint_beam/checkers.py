"""Pylint rules for Apache Beam."""
import astroid
from pylint.checkers import BaseChecker


class WriteToBQChecker(BaseChecker):
    """Checks calls to beam.io.WriteToBigQuery.

    1. Warns against usage of write_disposition=WRITE_TRUNCATE.
    """

    name = "write-to-bq"
    msgs = {
        # refer to
        # https://pylint.readthedocs.io/en/latest/development_guide/how_tos/custom_checkers.html#defining-a-message
        "W5001": (  # message id
            # template of the message
            "write_disposition=WRITE_TRUNCATE is not allowed",
            "write-to-bq-write-truncate",  # message symbol
            # message description
            "write_disposition=WRITE_TRUNCATE is not allowed because its behavior is "
            "buggy / misleading. In apache-beam 2.28.0 (not verified in later versions)"
            " WriteToBigQuery may spawn multiple load or copy jobs based on how big the"
            " dataset being uploaded is, and the write_disposition gets configured on "
            "all of these jobs. This means that all of the jobs will truncate each "
            "other and only data from one of the jobs will be present in the table.",
        ),
    }

    def visit_call(self, node):
        """Checks if the function is WriteToBigQuery."""
        if isinstance(node.func, astroid.Attribute):
            if node.func.attrname == "WriteToBigQuery":
                if node.keywords:
                    for keyword in node.keywords:
                        if keyword.arg == "write_disposition":
                            if keyword.value.attrname == "WRITE_TRUNCATE":
                                self.add_message("write-to-bq-write-truncate", node=node)


def register(linter):
    """Register the checker."""
    linter.register_checker(WriteToBQChecker(linter))
