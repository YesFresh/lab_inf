from typing import Annotated

from connstans import T_BIG_GREW, T_SMALL_GREW

def det_t(
    t1: Annotated[float, "1 температура"],
    t2: Annotated[float, "2 температура"], 
    ): return t2-t1

def Q_raschet(
        m:Annotated[float, "масса"],
        c:Annotated[float, "удельная теплоёмкость"],
    ):  return c*m*det_t()

