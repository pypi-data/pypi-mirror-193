from onlinesimru import FreeNumbersService, NumbersService, ProxyService, RentNumbersService, UserService
from .api import API


class Driver(API):
    def free(self):
        return FreeNumbersService(self.apikey, self.lang, self.lang)

    def numbers(self):
        return NumbersService(self.apikey, self.lang, self.lang)

    def proxy(self):
        return ProxyService(self.apikey, self.lang, self.lang)

    def rent(self):
        return RentNumbersService(self.apikey, self.lang, self.lang)

    def user(self):
        return UserService(self.apikey, self.lang, self.lang)
