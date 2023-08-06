import subprocess
import time as ttime

import pytest

from atfdb.atfdb import host_connect, host_disconnect

SERVER_ADDRESS = "localhost"
SERVER_PORT = 5000


"""
:param scope:
    The scope for which this fixture is shared; one of ``"function"``
    (default), ``"class"``, ``"module"``, ``"package"`` or ``"session"``.

    This parameter may also be a callable which receives ``(fixture_name, config)``
    as parameters, and must return a ``str`` with one of the values mentioned above.

    See :ref:`dynamic scope` in the docs for more information.
"""


@pytest.fixture(scope="session")
def socket_server():
    p = subprocess.Popen(
        "test-socket-server".split(),
        start_new_session=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        shell=True,
    )
    ttime.sleep(2.0)

    # Connect to the test socket server with the client
    host_connect(SERVER_ADDRESS, SERVER_PORT)

    yield

    # Disconnect the client from the test socket server
    host_disconnect()

    # Print logs
    # print(f"{logfile[-1] = }")
    std_out, std_err = p.communicate()
    std_out = std_out.decode()
    print(std_out)
    p.terminate()
