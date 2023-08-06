import contextlib
import getpass

from bluesky import RunEngine
from bluesky.plans import count
import pytest
from tiled.client import from_config

from ..mongo_normalized import MongoAdapter, SimpleAccessPolicy


@pytest.fixture
def enter_password(monkeypatch):
    """
    Return a context manager that overrides getpass, used like:

    >>> with enter_password(...):
    ...     # Run code that calls getpass.getpass().
    """

    @contextlib.contextmanager
    def f(password):
        original = getpass.getpass
        monkeypatch.setattr("getpass.getpass", lambda: password)
        yield
        monkeypatch.setattr("getpass.getpass", original)

    return f


def test_access_policy_pass_through():
    # Ensure access_policy is propagated to __init__.

    access_policy = SimpleAccessPolicy({}, key="...", provider="...")

    class InstrumentedMongoAdapter(MongoAdapter):
        def __init__(self, *args, **kwargs):
            assert kwargs["access_policy"] is not None

    InstrumentedMongoAdapter.from_uri(
        "mongodb://localhost:27017/dummy",  # never actually connects
        access_policy=access_policy,
    )
    InstrumentedMongoAdapter.from_mongomock(access_policy=access_policy)


def test_access_policy_example(tmpdir, enter_password):

    config = {
        "authentication": {
            "providers": [
                {
                    "provider": "toy",
                    "authenticator": "tiled.authenticators:DictionaryAuthenticator",
                    "args": {"users_to_passwords": {"alice": "secret"}},
                }
            ],
        },
        "trees": [
            {
                "path": "/",
                "tree": "databroker.mongo_normalized:MongoAdapter.from_mongomock",
                "access_control": {
                    "access_policy": "databroker.mongo_normalized:SimpleAccessPolicy",
                    "args": {
                        "provider": "toy",
                        "key": "color",
                        "access_lists": {
                            "alice": ["blue", "red"],
                        },
                    },
                },
            }
        ],
    }
    with enter_password("secret"):
        client = from_config(config, username="alice", token_cache=tmpdir)

    def post_document(name, doc):
        client.post_document(name, doc)

    RE = RunEngine()
    RE.subscribe(post_document)
    (red_uid,) = RE(count([], md={"color": "red"}))
    (blue_uid,) = RE(count([], md={"color": "green"}))
    (blue_uid,) = RE(count([], md={"color": "blue"}))

    # alice can see red and blue but not green
    assert set(client.keys()) == {red_uid, blue_uid}
