import logging
import logging.config
from os import makedirs
from pathlib import Path

from yaml import safe_load

from .definitions import LOGGER_LEVEL, MODULE_PATH, LAUNCH_TIME


class LoggerBuilder:
    """Constructor for a logger with the desired template."""
    templates = {
        "console": MODULE_PATH / "templates" / "logging_console.yml",
        "rotating": MODULE_PATH / "templates" / "logging_rotating.yml",
        "scheduled": MODULE_PATH / "templates" / "logging_scheduled.yml"
    }

    def __init__(self):
        self.config = None

    def build(
        self,
        template: str = "console",
        folder: str or Path = MODULE_PATH / "logs",
        filename: str = "activity"
    ) -> logging.Logger:
        """Initiate a logger instance with the given template.

        The method returns an instanciated logger, which is the result of a call
        to ``logging.getLogger("root")``. This method should only be called once
        per execution. Access to the logger should otherwise be made with
        ``logging.getLogger(__name__)``.

        :param template: template to use, one of console, rotating, scheduled
        :param folder: folder to put log file(s) into, defaulted to ``logs`` at
          the module's location
        :param filename: default ``"activity"`` — name for log file(s)

        Details
        =======

        The logger can be set up from three templates : console, rotating or scheduled.

        + *console* logger simply writes output to console with ``sys.stdout``.
        + *scheduled* logger writes one log file per execution, with the execution
          date and time appended to the log filename, such as
          ``activity-20200101-00h00m00s.log``.
        + *rotating* logger uses ``logging`` built-in ``RotatingFileHandler`` to
          write log files with a size limit. Limit per file is set to 1MB for a
          maximum of 20 files. When the maximum is reached, the oldest log file
          is overwritten.
        """
        config_file = LoggerBuilder._dispatch_config_path(template=template)
        self._read_config(config_file=config_file)

        filename = LoggerBuilder._consolidate_filename(template, filename)
        self._set_logger_parameters(folder=folder, filename=filename)
        logging.config.dictConfig(self.config)
        return logging.getLogger("root")

    @classmethod
    def __validate_template(cls, template: str) -> None:
        if template not in cls.templates.keys():
            raise ValueError(f"template must be one of {cls.templates.keys()}, was {template}.")

    @classmethod
    def _dispatch_config_path(cls, template: str) -> Path:
        """Find logger configuration file for given template."""
        cls.__validate_template(template)
        return LoggerBuilder.templates[template]

    @classmethod
    def _consolidate_filename(cls, template: str, filename: str = "activity") -> str:
        """Alter if necessary the log file name.

        :param template: One of console, scheduled or rotating
        :param filename: default ``"activity"`` — name for log file, None if using console template
        :return: the modified log file name according to template

        * for template ``console``, filename is overriden and ``None`` is always returned
        * for template ``scheduled``, the launch time is appended to the given filename
        * for template ``rotating``, the filename is returned as such
        """
        cls.__validate_template(template)
        if template == "console":
            result = None
        elif template == "scheduled":
            result = f"{filename}-{LAUNCH_TIME}"
        else:
            result = filename
        return result

    def _read_config(self, config_file: Path) -> None:
        """Read logger configuration from yaml templates."""
        with open(config_file, "r") as f:
            log_config = safe_load(f)
        self.config = log_config

    def _set_logger_parameters(self, folder: str = None, filename: str = None) -> None:
        """Set logger parameters : levels and filename if it is not ``None``.

        :param folder: default ``None`` — folder to put log files into, created if
          it does not exist
        :param filename: default ``None`` — name of log file(s)

        Both folder and filename are ignored when using the ``console`` template.
        """
        self.config["root"]["level"] = LOGGER_LEVEL
        if filename:
            makedirs(folder, exist_ok=True)
            log_file = f"{folder}/{filename}.log"
            self.config["handlers"]["logfile"]["filename"] = log_file
