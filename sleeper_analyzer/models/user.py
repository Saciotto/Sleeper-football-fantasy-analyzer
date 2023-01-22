from sleeper_analyzer.exceptions import UserNotFoundException


class User(dict):

    def __init__(self, db, name, league=None):
        super().__init__()
        self._db = db
        if league is not None:
            data = self._db.get_league_user(name, league)
        else:
            data = self._search_user_by_username(name)
        self.update(data)

    def _search_user_by_username(self, name):
        main_user = self._db.user_info
        if self.test_user_match(main_user, name):
            return main_user
        users = self._db.users
        for user in users:
            if self.test_user_match(user, name):
                return user
        raise UserNotFoundException('{} not found in users.json'.format(name))

    @staticmethod
    def test_user_match(user_info, name):
        if name == user_info['user_id']:
            return True
        if name.upper() == user_info['display_name'].upper():
            return True
        return False

    @property
    def id(self):
        return self['user_id']

    @property
    def name(self):
        return self['display_name']

    def __str__(self):
        return self.name

    __repr__ = __str__

    def __eq__(self, other):
        return other and self.id == other.id

    def __hash__(self):
        return hash(self.id)
