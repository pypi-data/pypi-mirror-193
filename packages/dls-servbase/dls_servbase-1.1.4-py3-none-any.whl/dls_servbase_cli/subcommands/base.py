import logging
import os
import tempfile

# Utilities.
from dls_utilpack.visit import get_visit_year

# Configurator.
from dls_servbase_lib.configurators.configurators import (
    Configurators,
    dls_servbase_configurators_set_default,
)

logger = logging.getLogger(__name__)


class Base:
    """
    Base class for femtocheck subcommands.  Handles details like configuration.
    """

    def __init__(self, args):
        self._args = args

        self.__temporary_directory = None

    # ----------------------------------------------------------------------------------------
    def get_configurator(self):

        dls_servbase_configurator = Configurators().build_object_from_environment()

        # For convenience, make a temporary directory for this test.
        self.__temporary_directory = tempfile.TemporaryDirectory()

        # Make the temporary directory available to the configurator.
        dls_servbase_configurator.substitute(
            {"temporary_directory": self.__temporary_directory.name}
        )

        substitutions = {
            "APPS": "/dls_sw/apps",
            "CWD": os.getcwd(),
            "HOME": os.environ.get("HOME", "HOME"),
            # Provide the PYTHONPATH at the time of service start
            # to the (potentially remote) process where the dls_servbase_task.run is called.
            "PYTHONPATH": os.environ.get("PYTHONPATH", "PYTHONPATH"),
        }

        if hasattr(self._args, "visit") and self._args.visit != "VISIT":
            BEAMLINE = os.environ.get("BEAMLINE")
            if BEAMLINE is None:
                raise RuntimeError("BEAMLINE environment variable is not defined")
            year = get_visit_year(BEAMLINE, self._args.visit)
            substitutions["BEAMLINE"] = BEAMLINE
            substitutions["VISIT"] = self._args.visit
            substitutions["YEAR"] = year

        dls_servbase_configurator.substitute(substitutions)

        # Set this as the default configurator so it is available everywhere.
        dls_servbase_configurators_set_default(dls_servbase_configurator)

        return dls_servbase_configurator
