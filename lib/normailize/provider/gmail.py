from .provider import Provider

class Gmail(Provider):
      # Gmail addresses work on both gmail.com and googlemail.com
      domains = 'gmail.com', 'googlemail.com'

      # A normalized Gmail address is lowercased, dots and everything after a
      # plus sign is removed from the username part
      modifications = 'lowercase', 'remove_dots', 'remove_plus_part'
