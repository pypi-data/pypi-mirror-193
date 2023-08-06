import logging

import structlog
from tala.backend.dependencies.abstract_backend_dependencies import AbstractBackendDependencies

from tala.ddd.ddd_component_manager import DDDComponentManager
from tala.ddd.loading.component_set_loader import ComponentSetLoader
from tala.log.formats import TIS_LOGGING_COMPACT, TIS_LOGGING_NONE, TIS_LOGGING_AUTO


class UnknownActiveDddException(Exception):
    pass


class BackendDependenciesForRunning(AbstractBackendDependencies):
    def __init__(self, args, logger=None):
        self._logger = logger or structlog.get_logger(__name__)
        super(BackendDependenciesForRunning, self).__init__(args)
        self.ddds = self.load_ddds(self._raw_config["ddds"])
        self.active_ddd = self.get_active_ddd(self.ddds)
        self._should_greet = args.should_greet
        self._logged_tis_format = args.logged_tis_format
        self._logged_tis_update_format = args.tis_update_format
        self._log_to_stdout = args.log_to_stdout
        self._log_level = args.log_level
        if self._logged_tis_format == TIS_LOGGING_AUTO:
            log_level = logging.getLevelName(args.log_level)
            self._logged_tis_format = self._generate_tis_format_from_log_level(log_level)

    @staticmethod
    def _generate_tis_format_from_log_level(log_level):
        if log_level == logging.DEBUG:
            return TIS_LOGGING_COMPACT
        return TIS_LOGGING_NONE

    def get_active_ddd(self, ddds):
        active_ddd_name = self._raw_config["active_ddd"]
        ddd_names = [ddd.name for ddd in ddds]
        if not active_ddd_name and len(ddd_names) == 1:
            active_ddd_name = ddd_names[0]

        if active_ddd_name is None:
            raise UnknownActiveDddException(
                "Expected active_ddd to be defined in backend config when using more than one DDD (%s), "
                "but active_ddd was undefined." % ddd_names
            )
        if active_ddd_name not in ddd_names:
            raise UnknownActiveDddException(
                "Expected active_ddd as one of %s, but got %r." % (ddd_names, active_ddd_name)
            )

        return active_ddd_name

    def load_ddds(self, ddd_names):
        ddd_component_manager = DDDComponentManager()
        component_set_loader = ComponentSetLoader(ddd_component_manager, self.overridden_ddd_config_paths)
        ddds = component_set_loader.ddds_as_list(ddd_names, rerank_amount=self.rerank_amount, logger=self._logger)
        return ddds

    @property
    def logger(self):
        return self._logger

    @property
    def active_ddd(self):
        return self._active_ddd

    @active_ddd.setter
    def active_ddd(self, active_ddd):
        self._active_ddd = active_ddd

    @property
    def should_greet(self):
        return self._should_greet

    @property
    def logged_tis_format(self):
        return self._logged_tis_format

    @property
    def logged_tis_update_format(self):
        return self._logged_tis_update_format

    @property
    def log_to_stdout(self):
        return self._log_to_stdout

    @property
    def log_level(self):
        return self._log_level

    @property
    def confidence_thresholds(self):
        return self._confidence_thresholds

    @property
    def confidence_prediction_thresholds(self):
        return self._confidence_prediction_thresholds
