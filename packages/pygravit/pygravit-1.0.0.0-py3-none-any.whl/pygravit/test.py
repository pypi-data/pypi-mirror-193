import _pygravit
from exceptions import NicknameLengthError, ClassDatabaseNotConnectionError

database = _pygravit.PyGravit(db = "s4_testing",user = "u4_nkJrO5tssr",passwd = "cs3uO9U!WQS@osp+UEd@QzeR", host = "node0-panel.frontalvlad.ml", table = "users")
database.player_get("FrontalvladMine", "password", "Testing2")
