from unittest.mock import Mock

import pytest

from libypythonpro import github_api

@pytest.fixture
def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('renzo')
    assert ('%s' % avatar_url) == url


def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/402714?v=4'
    resp_mock.json.return_value = {
        'login': 'renzo', 'id': 402714, 'node_id': 'MDQ6VXNlcjQwMjcxNA==',
        'avatar_url': ('%s' % url)
    }
    get_mock=mocker.patch('libypythonpro.github_api.requests.get')
    get_mock.return_value =resp_mock
    return url

def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('renzo')
    assert 'https://avatars.githubusercontent.com/u/402714?v=4' == url


