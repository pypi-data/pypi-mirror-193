from viggocore.common import subsystem
from viggofiscal.subsystem.parametrizacao.serial_fiscal import resource, manager

subsystem = subsystem.Subsystem(resource=resource.SerieFiscal,
                                manager=manager.Manager)
