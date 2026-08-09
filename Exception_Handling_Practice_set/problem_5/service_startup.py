def get_json_parser():
    """Use the faster 'orjson' library if installed, else fall back."""
    # TODO: 'import orjson' raises ImportError (ModuleNotFoundError) when it
    # isn't installed. Handle it, print "orjson not available -- falling
    #back to standard json", and import the built-in json instead.
    try:

        import orjson
        return orjson
    except ImportError:
        print("orjson not available -- falling back to standard json")
        import json


class ReportService:
    def __init__(self):
        self.connected = False
    
    def run_query(self):
        try:
            if not self.connected:
                raise RuntimeError("Database connection not established.")
            return "query results"
        except RuntimeError:
            print("Looks like we are having a bad connection at the moment.")
            return None


def generate_report(service):
# connection not opened yet

    """TODO: call service.run_query() inside try/except RuntimeError,
    print the error message, and keep the program running."""
    pass

# --- Test cases --
get_json_parser()  # handled -> standard json fallbac
generate_report(ReportService()) # RuntimeError handled, no crash