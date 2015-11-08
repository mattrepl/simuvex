
import logging
l = logging.getLogger('simuvex.plugins.uc_manager')

from .plugin import SimStatePlugin

class SimUCManager(SimStatePlugin):
    def __init__(self, man=None):

        SimStatePlugin.__init__(self)

        if man:
            self._uc_region_base = man._uc_region_base
            self._uc_pos = man._uc_pos
        else:
            self._uc_region_base = 0xd0000000
            self._uc_pos = 0

    def assign(self):
        """
        Assign a new region for under-constrained symbolic execution

        :return: as ast of memory address that points to a new region
        """

        ptr = self.state.se.BVV(self._uc_region_base + self._uc_pos, self.state.arch.bits)
        self._uc_pos += 0x1000
        return ptr

    def copy(self):
        return SimUCManager(man=self)

SimStatePlugin.register_default('uc_manager', SimUCManager)