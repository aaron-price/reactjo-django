from tests.config_mock import setup_config, teardown_config
from helpers.path_manager import mkdir, parse_shortcuts
import os

def test_parse_shortcuts():
    setup_config()
    from helpers.config_manager import get_cfg
    cfg = get_cfg()

    actual = parse_shortcuts('$su')
    expected = os.getcwd()
    assert(actual == expected)

    actual = parse_shortcuts('$su/some/path')
    expected = os.path.join(os.getcwd(), 'some/path')
    assert(actual == expected)

    actual = parse_shortcuts('$rc')
    expected = os.path.join(cfg['paths']['super_root'], 'reactjorc')
    assert(actual == expected)

    actual = parse_shortcuts('$prj')
    expected = cfg['paths']['project_root']
    assert(actual == expected)

    actual = parse_shortcuts('$out')
    expected = os.path.join(cfg['paths']['project_root'], 'your_output_home_here')
    assert(actual == expected)

    actual = parse_shortcuts('$ext')
    expected = os.path.join(
        cfg['paths']['super_root'],
        'reactjorc/extensions/your_rc_home_here')
    assert(actual == expected)

    actual = parse_shortcuts('$assets')
    expected = os.path.join(
        cfg['paths']['super_root'],
        'reactjorc/extensions/your_rc_home_here',
        'assets')
    assert(actual == expected)

    actual = parse_shortcuts('$assets/test.txt')
    expected = os.path.join(
        cfg['paths']['super_root'],
        'reactjorc/extensions/your_rc_home_here',
        'assets/test.txt')
    assert(actual == expected)




def test_mkdir():
    from helpers.config_manager import get_cfg
    mkdir('$su/tests/sandbox/path_manager', 'pm')
    assert(os.path.exists('tests/sandbox/path_manager'))
    assert('pm' in get_cfg()['paths'].keys())

    # Teardown.
    os.rmdir(parse_shortcuts('$su/tests/sandbox/path_manager'))
    teardown_config()
