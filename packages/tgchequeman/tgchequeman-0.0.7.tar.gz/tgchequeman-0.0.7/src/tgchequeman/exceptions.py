class UnknownError(Exception):
    def __init__(self, txt: str = None):
        self.txt = txt


class ChequeFullyActivatedOrNotFound(Exception):
    def __init__(self, txt: str = None):
        self.txt = txt


class ChequeActivated(Exception):
    def __init__(self, txt: str = None):
        self.txt = txt


class ChequeForPremiumUsersOnly(Exception):
    def __init__(self, txt: str = None):
        self.txt = txt


class CannotActivateOwnCheque(Exception):
    def __init__(self, txt: str = None):
        self.txt = txt


class PasswordError(Exception):
    def __init__(self, txt: str = None):
        self.txt = txt
