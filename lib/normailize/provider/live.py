from .provider import Provider


class Live(Provider):
    """Internal: A provider to represent Live
    """
    # A Live account only works on the live.com domain
    domains = 'live.com'

    # A mormalized Live address is lowercased and everything after a plus sign is removed
    modifications = 'lowercase', 'remove_plus_part'

