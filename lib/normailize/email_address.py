"""Public: Class to represent an email address.

Normalizes email addresses according to the rules given by the provider.

Examples

  # Compare two Gmail accounts
  address1 = Normailize::EmailAddress.new('Jo.Hn+sneaky@gmail.com')
  address2 = Normailize::EmailAddress.new('j.o.h.n@googlemail.com')
  address1.same_as?(address2) # => true

  # Get normalized email address
  address = Normailize::EmailAddress.new('Jo.Hn+sneaky@gmail.com')
  address.normalized_address # => john@gmail.com
"""
import re

from .provider import create_provider

"""Private: Simple regex to validate format of an email address

We're deliberately ignoring a whole range of special and restricted chars
for the sake of simplicity. This should match 99.99% of all the email
addresses out there. If you allow comments (parentheses enclosed) in the
local or domain part of your email addresses, make sure to strip them for
normalization purposes. For '@' in the local part to be allowed, split
local and domain part at the _last_ occurrence of the @-symbol.
"""
EMAIL_ADDRESS_REGEX = r'\A([a-z0-9_\-][a-z0-9_\-\+\.]{,62})?[a-z0-9_\-]@(([a-z0-9]|[a-z0-9][a-z0-9\-]*[a-z0-9])\.)+[a-z]{2,}\z'
EMAIL_MATCHER = re.compile(EMAIL_ADDRESS_REGEX, flags=re.I)


class EmailAddress(object):
    # attr_reader :address, :username, :domain

    # Public: Class initializer
    #
    # address - An email address
    #
    # Raises ArgumentError if email address does not have correct format
    def __init__(self, address):
        if not EMAIL_MATCHER.match(address):
            raise TypeError("Does not look like a valid email address")

        self.address = address
        self.username, self.domain = self.address.split('@', 2)
        self.normalize()

    # Internal: Remove all dots from username parts
    #
    # Returns nothing
    def remove_dots(self):
        self.username = self.username.replace('.', '')

    # Internal: Removes everything after the first occurrence of a plus sign in the username parts
    #
    # Returns nothing
    def remove_plus_part(self):
        self.username = self.username.split('+', 2)[0]

    # Internal: Lowercase characthers in username part
    #
    # Returns nothing
    def lowercase(self):
        self.username = self.username.lower()

    # Internal: Get provider instance for email address
    #
    # If provider is known, it returns a specific provider instance,
    # otherwise a generic provider instance is returned
    #
    # Returns Normailize::Provider
    def provider(self):
        create_provider(self.domain)

    # Public: Get normalized email address
    #
    # Returns normalized address according to the rules specified by the provider.
    def normalized_address(self):
        return "{username}@{domain}".format(username=self.username, domain=self.domain)

    # Public: Determine if two email addresses are the same
    #
    # Performs a comparison of the normalized username and provider
    #
    # Returns true if same or false if not
    def same_as(self, address):
        return (self.username == address.username) and self.provider.same_as(address.provider)

    # private

    # Internal: Normalize email address according to rules specified by the provider
    #
    # Returns nothing
    def normalize(self):
        self.domain = self.domain.lower()
        for modification in self.provider.modifications:
            # if self.respond_to(modification):
            #     self.send(m)
            getattr(self, modification)()
