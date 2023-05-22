from __future__ import annotations

import os
import sys


from abc import ABCMeta, abstractmethod, abstractproperty
from copy import deepcopy
from typing import List

DIR_IMP = os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.pardir
))
sys.path.append(DIR_IMP)

from utils.errorhandler import Error


class AbstractDataModel(metaclass=ABCMeta):

    def __init__(self) -> None:
        pass

    @abstractproperty
    def data(self) -> dict:
        pass

    @abstractmethod
    def update(self, data: dict) -> bool:
        pass

    @abstractmethod
    def view(self) -> str:
        pass

    def clone(self) -> AbstractDataModel:
        return deepcopy(self)
    
    def __str__(self) -> str:

        out = f'{self.__class__.__name__}:\n'
        for k, v in self.data.items():
            out += f'\t{k} = {v}\n'
        return out
    

class AbstractDataCache(metaclass=ABCMeta):

    def __init__(self) -> None:
        self.cache: List[AbstractDataModel] = []
    
    def data(self) -> list:
        return self.cache

    def add(self, data: AbstractDataModel) -> bool:

        if not isinstance(data, AbstractDataModel): 
            TypeError(Error.TYPEERR.value.format(
                AbstractDataModel.__class__.__name__, type(data).__class__.__name__
            ))
        
        try:
            self.cache.append(data)
            return True
        except KeyError:
            raise KeyError(Error.DATAERROR.value.format(data.datatype))
        except AttributeError:
            raise AttributeError(Error.ATTRERROR.value.format(data.__class__.__name__))
        except Exception:
            return False
        
    def insert(self, data: AbstractDataModel, idx: int) -> bool:

        if not isinstance(data, AbstractDataModel):
            raise TypeError(Error.NOTSTR.value.format('Data type', type(data).__class__.__name__))
        
        if not isinstance(idx, int):
            raise TypeError(Error.NOTINT.value.format('ID', type(idx).__class__.__name__))

        try:
            self.cache.insert(idx, data)
            return True
        except Exception:
            return False

    def moveDown(self, idx: int) -> bool:

        if not isinstance(idx, int):
            raise TypeError(Error.NOTINT.value.format('ID', type(idx).__class__.__name__))

        if idx < 0 or idx > len(self.cache): return False

        try:
            pop = self.cache.pop(idx)
            self.cache.insert(idx+1, pop)
            return True
        except:
            return False

    def moveUp(self, idx: int) -> bool:

        if not isinstance(idx, int):
            raise TypeError(Error.NOTINT.value.format('ID', type(idx).__class__.__name__))

        if idx < 0 or idx > len(self.cache): return False

        try:
            pop = self.cache.pop(idx)
            self.cache.insert(idx-1, pop)
            return True
        except:
            return False

    def get(self, idx: int) -> AbstractDataModel | None:

        if not isinstance(idx, int):
            raise TypeError(Error.NOTINT.value.format('ID', type(idx).__class__.__name__))

        try:
            return self.cache[idx].clone()
        except IndexError:
            return None
        except Exception:
            return None

    def delete(self, idx: int):

        if not isinstance(idx, int):
            raise TypeError(Error.NOTINT.value.format('ID', type(idx).__class__.__name__))

        try:
            return self.cache.pop(idx)
        except IndexError:
            return None
        except Exception:
            return None

    def update(self, idx: int, data: dict) -> bool:
        if not isinstance(idx, int):
            raise TypeError(Error.NOTINT.value.format('ID', type(idx).__class__.__name__))
        if not isinstance(data, dict) : raise TypeError(Error.DATAERROR.value.format(type(data)))

        try:
            model: AbstractDataModel = self.cache[idx]
            model.update(data)
            return True
        except IndexError:
            return False
        except Exception:
            return False

    def view(self) -> list | None:

        try:
            return [data.view() for data in self.data]
        except (TypeError, AttributeError):
            None

    def __str__(self) -> str:
        out = ''
        for item in self.cache:
            out += str(item) + '\n'
        return out
