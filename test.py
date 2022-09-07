#!/usr/bin/python

from framework.web.browsers import FirefoxBrowser


def setUp():
    global browser

    browser = FirefoxBrowser()


def test():
    browser.load_url("https://www.google.com")


    import os
    home_directory = os.path.expanduser( '~' )
    print( home_directory )

    browser.take_screenshot("test.png".format(home_directory))

    import os
    import shutil

    # os.rename("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
    os.replace("test.png", "/Users/maximnikulcha/tmp/test.png")
    # shutil.move("path/to/current/file.foo", "path/to/new/destination/for/file.foo")


def tearDown():
    browser.close()

    print("------------------------------------------------")


def main():
    setUp()
    test()
    tearDown()


if __name__ == "__main__":
    main()
