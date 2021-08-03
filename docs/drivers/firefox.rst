.. Copyright 2012 splinter authors. All rights reserved.
   Use of this source code is governed by a BSD-style
   license that can be found in the LICENSE file.

.. meta::
    :description: How to use splinter with Firefox WebDriver
    :keywords: splinter, python, tutorial, how to install, installation, firefox, selenium

+++++++++++++++++
Firefox WebDriver
+++++++++++++++++

Installation
------------

Firefox automation is provided via Selenium WebDriver.
To use it, the following applications are required:

- `Mozilla Firefox <http://firefox.com>`_
- `Geckodriver <https://github.com/mozilla/geckodriver/releases>`_

Mozilla Firefox
+++++++++++++++

Download and install the applications from `Firefox <https://mozilla.org/>`_

GeckoDriver
+++++++++++

Download the application from `<https://github.com/mozilla/geckodriver/releases>`_,
select the correct version for your operating system,
and place it in a directory that is in your operating system's ``PATH``.

Alternatively, use a package manager:

Mac OS X
========

Via `Homebrew <http://mxcl.github.com/homebrew/>`_:

.. code-block:: console

    brew install geckodriver

Windows
=======

Via `Chocolatey <https://chocolatey.org/>`_:

.. code-block:: console

    choco install geckodriver

Usage
-----

To use Firefox, use the string ``firefox`` when you create
the ``Browser`` instance:

.. code-block:: python

    from splinter import Browser
    browser = Browser('firefox')

Headless mode
+++++++++++++

Starting with Firefox 55, Firefox can run in a headless mode.

To use headless mode, pass the `headless` argument
when creating a new Browser instance.

.. code-block:: python

    from splinter import Browser
    browser = Browser('firefox', headless=True)

Incognito mode
++++++++++++++

To use Firefox's incognito mode, pass the `incognito` argument
when creating a Browser instance.

.. code-block:: python

    from splinter import Browser
    browser = Browser('firefox', incognito=True)

Specify Profile
+++++++++++++++

You can specify a `Firefox profile <http://support.mozilla.com/en-US/kb/Profiles>`_
using the ``profile`` keyword of the ``Browser`` function

.. code-block:: python

    from splinter import Browser
    browser = Browser('firefox', profile='my_profile')

If you don't specify a profile, a new temporary profile will be created (and deleted when you close the browser).

Firefox Extensions
++++++++++++++++++

An extension for Firefox is a .xpi archive.
To use an extension in Firefox WebDriver profile you need to give the path of the extension,
using the extensions keyword:

.. code-block:: python

    from splinter import Browser
    browser = Browser('firefox', extensions=['extension1.xpi', 'extension2.xpi'])

After the browser is closed, the extensions will be deleted from the profile, even if is not a temporary one.

Selenium Capabilities
+++++++++++++++++++++

.. code-block:: python

    from splinter import Browser
    browser = Browser('firefox', capabilities={'acceptSslCerts': True})

You can pass any selenium `read-write DesiredCapabilities parameters <https://code.google.com/p/selenium/wiki/DesiredCapabilities#Read-write_capabilities>`_ for Firefox.


API docs
--------

.. autoclass:: splinter.driver.webdriver.firefox.WebDriver
   :members:
   :inherited-members:
