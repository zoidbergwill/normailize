from .provider import Provider

class Hotmail(Provider):
    # A hotmail account only works on the hotmail.com domain
    domains = 'hotmail.com'

    # A normalized hotmail address is lowercased and everything after a plus sign is removed
    modifications = 'lowercase', 'remove_plus_part'
