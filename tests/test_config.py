from tests.config_mock import setup_config, teardown_config
import os
from helpers.config_manager import get_cfg, set_cfg

def test_get_cfg():
	setup_config()
	cfg = get_cfg()
	assert('paths' in cfg)

def test_set_cfg():
	cfg = get_cfg()
	cfg['foo'] = 'bar'
	set_cfg(cfg)

	another_cfg = get_cfg()
	assert('foo' in another_cfg)

	teardown_config()
