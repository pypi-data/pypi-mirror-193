import pytest

from atfdb.ophyd import ATFSignalNoConn, TimeoutException
from atfdb.utils import configure_logger, logger


def test_ophyd_atfsignal_never_sets(socket_server):
    test1 = ATFSignalNoConn(psname="test1", db="test", name="test1", tol=0.0, timeout=2.0)
    print(f"{test1.get() = }")
    print(f"{test1.read() = }")

    configure_logger(logger=logger)
    with pytest.raises(TimeoutException) as excinfo:
        test1.put(1)

    excinfo_value = excinfo.exconly()
    assert "ophyd object has not reached the setpoint" in excinfo_value, excinfo_value
    print(excinfo_value)

    print(f"{test1.get() = }")


def test_ophyd_atfsignal(socket_server):
    test2 = ATFSignalNoConn(psname="test2", db="test2", name="test2", tol=0.25, timeout=2.0)
    print(f"{test2.get() = }")
    print(f"{test2.read() = }")
    test2.put(1)
    print(f"{test2.get() = }")
