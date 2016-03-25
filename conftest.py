import pytest
import django_webtest
import os

from django.core.urlresolvers import reverse

from ideascube.tests.factories import UserFactory
from ideascube.search.utils import create_index_table


@pytest.fixture()
def cleansearch():
    create_index_table(force=True)


@pytest.fixture()
def user():
    return UserFactory(short_name="Hello", password='password')


@pytest.fixture()
def staffuser():
    return UserFactory(short_name="Hello", password='password', is_staff=True)


@pytest.fixture
def setup_dirs(monkeypatch, tmpdir, settings):
    storage_root = tmpdir.mkdir('storage')
    settings.STORAGE_ROOT = storage_root.strpath
    settings.BACKUPED_ROOT = storage_root.mkdir('main').strpath
    settings.MEDIA_ROOT = storage_root.mkdir('main', 'media').strpath

    cache_root = tmpdir.mkdir('cache')
    settings.CATALOG_CACHE_BASE_DIR = cache_root.mkdir('catalog').strpath

    install_root = tmpdir.mkdir('installs')
    settings.CATALOG_HANDLER_INSTALL_DIR = (
        install_root.mkdir('handler').strpath)
    settings.CATALOG_KIWIX_INSTALL_DIR = (
        install_root.mkdir('kiwix').strpath)
    settings.CATALOG_NGINX_INSTALL_DIR = (
        install_root.mkdir('nginx').strpath)

    # Change also the location of the default_storage as this is cached
    # and not updated when settings changed.
    monkeypatch.setattr(
        'django.core.files.storage.default_storage.location',
        settings.MEDIA_ROOT
    )
    monkeypatch.setattr(
        'django.core.files.storage.default_storage.base_location',
        settings.MEDIA_ROOT
    )


@pytest.yield_fixture()
def app(request):
    wtm = django_webtest.WebTestMixin()
    wtm._patch_settings()
    yield django_webtest.DjangoTestApp()
    wtm._unpatch_settings()


@pytest.fixture()
def loggedapp(app, user):
    """Return an app with an already logged in user."""
    form = app.get(reverse('login')).forms['login']
    form['username'] = user.serial
    form['password'] = 'password'
    form.submit().follow()
    setattr(app, 'user', user)  # for later use, if needed
    return app


@pytest.fixture()
def staffapp(app, staffuser):
    """Return an app with an already logged in staff user."""
    form = app.get(reverse('login')).forms['login']
    form['username'] = staffuser.serial
    form['password'] = 'password'
    form.submit().follow()
    setattr(app, 'user', staffuser)  # for later use, if needed
    return app


@pytest.fixture()
def testdatadir(request):
    datadir = request.fspath.dirpath().join('data')

    assert datadir.check(dir=True)
    return datadir
