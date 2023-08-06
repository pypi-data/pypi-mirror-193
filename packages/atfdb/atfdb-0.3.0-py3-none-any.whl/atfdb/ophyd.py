import time as ttime

from ophyd import Signal
from ophyd.sim import NullStatus

from . import atfdb
from .utils import logger


def open_close_conn(socket_server=None, socket_port=None):
    """Decorator to open/close socket connections before and after ophyd calls."""

    def inner_decorator(f):
        def wrapped(*args, **kwargs):
            atfdb.host_connect(socket_server, socket_port)
            response = f(*args, **kwargs)
            atfdb.host_disconnect()
            return response

        return wrapped

    return inner_decorator


class TimeoutException(Exception):
    ...


class ATFSignalNoConn(Signal):
    def __init__(
        self,
        psname,
        db,
        *args,
        tol=0.0,
        read_suffix="RAS;RB_CURRENT_SETPT",
        write_suffix="CDS;SET_CURRENT_SETPT",
        timeout=2.0,
        dtype="real",
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self._psname = psname
        self._db = db
        self._tol = tol
        self._read_suffix = read_suffix
        self._write_suffix = write_suffix
        self._timeout = timeout  # seconds
        self._dtype = dtype  # 'real', 'integer', etc. corresponding to the get_<dtype> functions from atf_db.

        self._setpoint = None
        self._readback = None

        self._update_readback_setpoint()  # update setpoint and readback on init

    def _get_readback(self):
        self._readback = getattr(atfdb, f"get_{self._dtype}")(
            atfdb.get_channel_index(f"{self._db}::{self._psname};{self._read_suffix}")
        )
        return self._readback

    def _get_setpoint(self):
        self._setpoint = getattr(atfdb, f"get_{self._dtype}")(
            atfdb.get_channel_index(f"{self._db}::{self._psname};{self._write_suffix}")
        )
        return self._setpoint

    def get(self):
        return self._get_readback()

    def get_setpoint(self):
        return self._get_setpoint()

    def _update_readback_setpoint(self):
        self._get_readback()
        self._get_setpoint()

    def put(self, value):
        self._setpoint = float(value)

        start_time = ttime.monotonic()
        getattr(atfdb, f"put_{self._dtype}")(
            atfdb.get_channel_index(f"{self._db}::{self._psname};{self._write_suffix}"),
            value,
        )
        while True:
            waited_time = ttime.monotonic() - start_time
            how_far = self._get_readback() - value
            logger.debug(f"{waited_time = :.3f}s  {how_far = :.6f}")
            if waited_time < self._timeout:
                if abs(how_far) < self._tol:
                    break
                else:
                    # not reached yet, wait a bit
                    ttime.sleep(0.1)
            else:
                raise TimeoutException(
                    f"'{self.name}' ophyd object has not reached the setpoint={self._setpoint} "
                    f"within the timeout of {self._timeout} seconds (waited {waited_time:.3f}s).\n"
                    f"Current position: {self._get_readback():.6f}\n\n"
                    f"Details:\n  db='{self._db}'\n  psname='{self._psname}'\n"
                    f"  read_suffix='{self._read_suffix}'\n  write_suffix='{self._write_suffix}'\n"
                    f"  tolerance={self._tol}"
                )

    def set(self, *args, **kwargs):
        self.put(*args, **kwargs)
        return NullStatus()


class ReadOnlyException(Exception):
    ...
