# Use standard logging in this module.
import logging
import os

# Utilities.
from dls_utilpack.callsign import callsign
from dls_utilpack.require import require

# Exceptions.
from dls_servbase_api.exceptions import NotFound

# Class managing list of things.
from dls_servbase_api.things import Things

# Environment variables with some extra functionality.
from dls_servbase_lib.envvar import Envvar

logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------------------
__default_dls_servbase_configurator = None


def dls_servbase_configurators_set_default(dls_servbase_configurator):
    global __default_dls_servbase_configurator
    __default_dls_servbase_configurator = dls_servbase_configurator


def dls_servbase_configurators_get_default():
    global __default_dls_servbase_configurator
    if __default_dls_servbase_configurator is None:
        raise RuntimeError("dls_servbase_configurators_get_default instance is None")
    return __default_dls_servbase_configurator


def dls_servbase_configurators_has_default():
    global __default_dls_servbase_configurator
    return __default_dls_servbase_configurator is not None


# -----------------------------------------------------------------------------------------


class Configurators(Things):
    """
    Configuration loader.
    """

    # ----------------------------------------------------------------------------------------
    def __init__(self, name=None):
        Things.__init__(self, name)

    # ----------------------------------------------------------------------------------------
    def build_object(self, specification):
        """"""

        dls_servbase_configurator_class = self.lookup_class(
            require(f"{callsign(self)} specification", specification, "type")
        )

        try:
            dls_servbase_configurator_object = dls_servbase_configurator_class(
                specification
            )
        except Exception as exception:
            raise RuntimeError(
                "unable to instantiate dls_servbase_configurator object from module %s"
                % (dls_servbase_configurator_class.__module__)
            ) from exception

        return dls_servbase_configurator_object

    # ----------------------------------------------------------------------------------------
    def lookup_class(self, class_type):
        """"""

        if class_type == "dls_servbase_lib.dls_servbase_configurators.yaml":
            from dls_servbase_lib.configurators.yaml import Yaml

            return Yaml

        raise NotFound(
            "unable to get dls_servbase_configurator class for type %s" % (class_type)
        )

    # ----------------------------------------------------------------------------------------
    def build_object_from_environment(self, environ=None):

        # Get the explicit name of the config file.
        dls_servbase_configfile = Envvar(Envvar.DLS_BILLY_CONFIGFILE, environ=environ)

        # Config file is explicitly named?
        if dls_servbase_configfile.is_set:
            # Make sure the path exists.
            configurator_filename = dls_servbase_configfile.value
            if not os.path.exists(configurator_filename):
                raise RuntimeError(
                    f"unable to find {Envvar.DLS_BILLY_CONFIGFILE} {configurator_filename}"
                )
        # Config file is not explicitly named?
        else:
            raise RuntimeError(
                f"environment variable {Envvar.DLS_BILLY_CONFIGFILE} is not set"
            )

        dls_servbase_configurator = self.build_object(
            {
                "type": "dls_servbase_lib.dls_servbase_configurators.yaml",
                "type_specific_tbd": {"filename": configurator_filename},
            }
        )

        dls_servbase_configurator.substitute(
            {"configurator_directory": os.path.dirname(configurator_filename)}
        )

        return dls_servbase_configurator
