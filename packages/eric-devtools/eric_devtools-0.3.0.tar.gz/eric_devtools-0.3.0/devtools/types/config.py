from enum import Enum


class Env(str, Enum):
    DEV = 'dev'
    HML = 'hml'
    TEST = 'test'
    PRD = 'prd'

    def is_test(self):
        return self in [Env.TEST]
