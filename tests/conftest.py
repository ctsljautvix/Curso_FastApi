from fast_zero.models import table_registry
import pytest
from fastapi.testclient import TestClient

from fast_zero.app import app
from sqlalchemy import create_engine, table
from sqlalchemy.engine import create


@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def session():
    engine = create_engine('sqlite:///:memory:')
    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    table_registry.metadata.drop_all(engine)