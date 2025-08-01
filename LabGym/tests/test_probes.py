import logging
import os
import re
import sys

from packaging import version

import pytest

from .exitstatus import exitstatus

from LabGym import probes


# basicConfig here isn't effective, maybe pytest has already configured logging?
#   logging.basicConfig(level=logging.DEBUG)
# so instead, use the root logger's setLevel method
logging.getLogger().setLevel(logging.DEBUG)

# the output from this debug statement is not accessible?
# instead, perform inside a test function.
#   logging.debug('%s: %r', 'dir(LabGym)', dir(LabGym))
#
# def test_inspect():
#     logging.debug('%s: %r', 'dir(LabGym)', dir(LabGym))
#     logging.debug('%s: %r', "os.getenv('PYTHONPATH')", os.getenv('PYTHONPATH'))


def test_probes(monkeypatch):
    # Arrange
    _config = {
        'anonymous': True, 
        'enable': {'registration': False, 'central_logger': False},
        }
    monkeypatch.setattr(probes.config, 'get_config', lambda: _config)
    logging.debug('%s: %r', '_config', _config)
    monkeypatch.setattr(probes.central_logging.config, 'get_config', lambda: _config)

    # Act
    probes.probes()

    # Assert
    # the probes were run and didn't raise an exception.


# def test_handshake_bad_cacert(monkeypatch):
#     # Arrange
#     monkeypatch.setenv('REQUESTS_CA_BUNDLE', os.path.join(os.getcwd(), 'cacert.fouled.pem'))
# 
#     # Act, and assert raises(SystemExit)
#     with pytest.raises(SystemExit) as e:
#         handshake.probe_url_to_verify_cacert()
# 
#     assert exitstatus(e.value) == 1
# 
# 
# def test_version_eq_pypi(monkeypatch, capsys):
#     # Arrange
#     return_values = [
#         version.Version('2.8.16'),  # version
#         version.Version('2.8.16'),  # version at pypi.org
#         ]
#     # monkeypatch the version.parse method to return return_values.pop(0)
#     monkeypatch.setattr('LabGym.handshake.version.parse', lambda self: return_values.pop(0))
# 
#     # Act
#     handshake.probe_pypi_check_freshness()
# 
#     # Assert
#     # assert re.match('Usage: ', capsys.readouterr().out)
# 
# 
# def test_version_lt_pypi(monkeypatch, capsys):
#     # Arrange
#     return_values = [
#         version.Version('2.0.16'),  # version
#         version.Version('2.8.16'),  # version at pypi.org
#         ]
#     # monkeypatch the version.parse method to return return_values.pop(0)
#     monkeypatch.setattr('LabGym.handshake.version.parse', lambda self: return_values.pop(0))
# 
#     # Act
#     handshake.probe_pypi_check_freshness()
# 
#     # Assert
#     assert re.match('You are using .*', capsys.readouterr().out)
# 
# 
# def test_version_gt_pypi(monkeypatch, capsys):
#     # Arrange
#     return_values = [
#         version.Version('2.8.16'),  # version
#         version.Version('2.0.16'),  # version at pypi.org
#         ]
#     # monkeypatch the version.parse method to return return_values.pop(0)
#     monkeypatch.setattr('LabGym.handshake.version.parse', lambda self: return_values.pop(0))
# 
#     # Act
#     handshake.probe_pypi_check_freshness()
# 
#     # Assert
#     # assert re.match('Usage: ', capsys.readouterr().out)
