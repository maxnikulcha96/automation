from framework.checkers.checkers import BaseWebsiteChecker


class MoiApplicationStatusChecker(BaseWebsiteChecker):
    def __init__(self, website):
        """
        Initializes a new MoiApplicationStatusChecker instance.

        :param website: The website to check.
        """

        self.website = website

        BaseWebsiteChecker.__init__(self, website)
