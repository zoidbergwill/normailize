class Provider(object):
    # # Public: Set on or more domains for a provider
    # #
    # # *domains - one or more domains
    # #
    # # Returns nothing
    # def set_domains(*domains)
    #   @domains = domains
    # end

    # # Public: Set one or more modifications to be performed on email address
    # # belonging to the provider
    # #
    # # *modifications - One or more modification symbols
    # #
    # # Currently, the following modifications are supported:
    # #
    # #   - :lowercase         Lowercase characthers in username part
    # #   - :remove_dots       Removes all dots in username part
    # #   - :remove_plus_part  Removes everything after the first occurrence of
    # #                        a plus sign
    # #
    # # Returns nothing
    # def set_modifications(*modifications)
    #   self.modifications = modifications.map(&:to_sym)

    # Internal: Get domains that are associated with the provider
    #
    # Returns an array of domains
    @classmethod
    def domains(self):
        return self.domains or []

    # # Public: Class initializer
    # #
    # # domain - A domain like gmail.com
    # #
    # # Returns nothing
    # def initialize(domain)
    #   @domain = domain
    # end

    # # Internal: Get all modification rules for the provider
    # #
    # # Returns symbols that tell the email class how to normalize an address
    # # for the provider
    # def modifications
    #   self.class.modifications || []
    # end

    # Internal: Get the domain that the provider was instantiated with
    #
    # Returns domain
    def domain(self):
        return self.domain

    # Internal: Determine if a provider is generic or not
    #
    # Returns true if generic or false if not
    def generic(self):
        return type(self) == Provider

    # Internal: Determine if two providers are the same or not
    #
    # provider - An instance of another provider class
    #
    # Returns true if providers are the same or false if not
    def same_as(self, provider):
        if self.generic or provider.generic():
            return self.domain == provider.domain
        else:
            return type(self) == type(provider)


class Gmail(Provider):
    # Gmail addresses work on both gmail.com and googlemail.com
    domains = ('gmail.com', 'googlemail.com')

    # A normalized Gmail address is lowercased, dots and everything after a
    # plus sign is removed from the username part
    modifications = ('lowercase', 'remove_dots', 'remove_plus_part')


class Hotmail(Provider):
    # A hotmail account only works on the hotmail.com domain
    domains = ('hotmail.com',)

    # A normalized hotmail address is lowercased and everything after a plus
    # sign is removed
    modifications = ('lowercase', 'remove_plus_part')


class Live(Provider):
    # A Live account only works on the live.com domain
    domains = ('live.com',)

    # A mormalized Live address is lowercased and everything after a plus sign
    # is removed
    modifications = ('lowercase', 'remove_plus_part')


def create_provider(domain):
    """Internal: Create a provider instance from a domain

    domain - A domain for an email provider, like gmail.com

    Returns an instance of a provider that recognizes the domain or a
    generic provider
    """
    if domain in Gmail.domains:
        return Gmail(domain)
    elif domain in Live.domains:
        return Live(domain)
    elif domain in Hotmail.domains:
        return Hotmail(domain)
    return Provider(domain)

# def self.included(base)
#   class << base; attr_accessor :domains, :modifications end
#   base.extend(ClassMethods)
# end
