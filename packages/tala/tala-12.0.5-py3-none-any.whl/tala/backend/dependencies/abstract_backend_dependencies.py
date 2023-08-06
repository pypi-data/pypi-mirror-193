from tala.config import BackendConfig

INACTIVE_SECONDS_ALLOWED_MIN = 60 * 60
INACTIVE_SECONDS_ALLOWED_MAX = 60 * 60 * 24 * 30


class InvalidConfigValue(Exception):
    pass


class AbstractBackendDependencies(object):
    def __init__(self, args):
        super(AbstractBackendDependencies, self).__init__()

        self._overridden_ddd_config_paths = args.overridden_ddd_config_paths
        self._raw_config = BackendConfig(args.config).read()
        self._path = args.config or BackendConfig.default_name()
        self._repeat_questions = self._raw_config["repeat_questions"]
        self._ddd_names = self._raw_config["ddds"]
        self._rerank_amount = self._raw_config["rerank_amount"]
        self._inactive_seconds_allowed = self._raw_config["inactive_seconds_allowed"]
        self._validate_inactive_seconds_allowed()
        self._response_timeout = self._raw_config["response_timeout"]
        self._confidence_thresholds = self._raw_config["confidence_thresholds"]
        self._confidence_prediction_thresholds = self._raw_config["confidence_prediction_thresholds"]
        self._short_timeout = self.raw_config["short_timeout"]
        self._medium_timeout = self.raw_config["medium_timeout"]
        self._long_timeout = self.raw_config["long_timeout"]

    def _validate_inactive_seconds_allowed(self):
        if self._inactive_seconds_allowed < INACTIVE_SECONDS_ALLOWED_MIN \
           or self._inactive_seconds_allowed > INACTIVE_SECONDS_ALLOWED_MAX:
            raise InvalidConfigValue(
                "Expected inactive_seconds_allowed to be in the range %d-%d, but it was %d." %
                (INACTIVE_SECONDS_ALLOWED_MIN, INACTIVE_SECONDS_ALLOWED_MAX, self._inactive_seconds_allowed)
            )

    @property
    def raw_config(self):
        return self._raw_config

    @property
    def overridden_ddd_config_paths(self):
        return self._overridden_ddd_config_paths

    @property
    def ddds(self):
        return self._ddds

    @ddds.setter
    def ddds(self, ddds):
        self._ddds = ddds

    @property
    def repeat_questions(self):
        return self._repeat_questions

    @property
    def ddd_names(self):
        return self._ddd_names

    @property
    def rerank_amount(self):
        return self._rerank_amount

    @property
    def inactive_seconds_allowed(self):
        return self._inactive_seconds_allowed

    @property
    def response_timeout(self):
        return self._response_timeout

    @property
    def path(self):
        return self._path

    @property
    def short_timeout(self):
        return self._short_timeout

    @property
    def medium_timeout(self):
        return self._medium_timeout

    @property
    def long_timeout(self):
        return self._long_timeout
