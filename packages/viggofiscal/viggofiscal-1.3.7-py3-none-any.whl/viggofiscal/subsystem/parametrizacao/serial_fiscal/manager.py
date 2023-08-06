from viggocore.common.subsystem import operation
from viggocore.common.subsystem import manager


class Manager(manager.Manager):

    def __init__(self, driver):
        super(Manager, self).__init__(driver)
