from __future__ import annotations

import os
import sys
from dataclasses import dataclass

IMPORTED = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.pardir
))
sys.path.append(IMPORTED)

from data.abstract import *
from utils.errorhandler import Error


@dataclass
class Domain:

    domain: str
    interfaces: List[str]

    def data(self) -> dict:
        return {self.domain: self.interfaces}

    def update(self, domain, interfaces) -> None:
        self.domain = str(domain)
        if isinstance(interfaces, list):
            self.interfaces = interfaces
        elif not hasattr(interfaces, "__iter__"):
            self.interfaces = [str(interfaces)]


@dataclass
class GasCompressor:

    name: str
    ctype: str
    inlet: str
    outlet: str
    blade: str
    nblades: int = 1
    axis: str = 'Z'
    rpm: float = 0.0
    tooltip: str = ''

    def data(self) -> dict:
        return {
            'name': self.name, 'type': self.ctype,
            'inlet': self.inlet, 'outlet': self.outlet,
            'blade': self.blade, 'nblades': self.nblades,
            'axis': self.axis, 'rpm': self.rpm, 'tooltip': self.tooltip
        }
    
    def update(self, data: dict) -> None:

        if name := data.get('name'): self.name = name
        if ctype := data.get('type'): self.ctype = ctype
        if blade := data.get('blade'): self.throat = blade
        if inlet := data.get('inlet'): self.inlet = inlet
        if outlet := data.get('outlet'): self.outlet = outlet
        if nblades := data.get('nblades') and isinstance(nblades, int):
            self.nblades = nblades
        if tooltip := data.get('tooltip'): self.tooltip = tooltip
        if axis := data.get('axis'): self.axis = axis
        if rpm := data.get('rpm') and isinstance(rpm, float): self.rpm = rpm


@dataclass
class GCPerformance:

    name: str
    inlet: str
    outlet: str
    tooltip: str = ''
    ctype: str = 'Performance Map'

    def data(self) -> dict:
        return {
            'name': self.name, 'type': self.ctype,
            'inlet': self.inlet, 'outlet': self.outlet,
            'tooltip': self.tooltip
        }

    def update(self, data: dict) -> None:

        if name := data.get('name'): self.name = name
        if ctype := data.get('type'): self.ctype = ctype
        if inlet := data.get('inlet'): self.inlet = inlet
        if outlet := data.get('outlet'): self.outlet = outlet
        if tooltip := data.get('tooltip'): self.tooltip = tooltip


@dataclass
class PipeDiffuser:

    name: str
    throat: str
    inlet: str
    outlet: str
    nblades: int
    ctype: str = 'Pipe Diffuser'
    tooltip: str = ''

    def data(self) -> dict:
        return {
            'name': self.name, 'type': self.ctype,
            'inlet': self.inlet, 'outlet': self.outlet,
            'nblades': self.nblades, 'tooltip': self.tooltip
        }
    
    def update(self, data: dict) -> None:

        if name := data.get('name'): self.name = name
        if ctype := data.get('type'): self.ctype = ctype
        if throat := data.get('throat'): self.throat = throat
        if inlet := data.get('inlet'): self.inlet = inlet
        if outlet := data.get('outlet'): self.outlet = outlet
        if nblades := data.get('nblades') and isinstance(nblades, int):
            self.nblades = nblades
        if tooltip := data.get('tooltip'): self.tooltip = tooltip


macroses = [
    GasCompressor, GCPerformance, PipeDiffuser
]


class Macros(AbstractDataModel):

    def __init__(self) -> None:
        super(Macros, self).__init__()
        
        self._macros = None

    def setMacros(self, macros) -> bool:
        
        if not isinstance(macros, any(macroses)):
            return False
        
        self._macros = macros

    @property
    def macros(self):
        return self._macros
    
    def data(self) -> dict:
        return self._macros.data

    def update(self, data: dict) -> bool:
        
        if not isinstance(data, dict): return False
        self._macros.update(data)
        return True
    
    def view(self) -> str:
        return f'{self._macros.ctype}: {self._macros.name}\n'
    

class DataCache(AbstractDataCache):

    pass
