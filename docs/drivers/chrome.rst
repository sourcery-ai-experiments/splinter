.. Copyright 2012 splinter authors. All rights reserved.
   Use of this source code is governed by a BSD-style
   license that can be found in the LICENSE file.

.. meta::
    :description: How to use splinter with Chrome WebDriver
    :keywords: splinter, python, tutorial, how to install, installation, chrome, selenium

++++++++++++++++
Chrome WebDriver
++++++++++++++++

Installation
------------

Chrome automation is provided via Selenium WebDriver.
To use it, the following applications are required:

- `Google Chrome <http://google.com/chrome>`_
- `ChromeDriver <https://chromedriver.chromium.org/>`_

Google Chrome
+++++++++++++

Download and install the application from `<http://google.com/chrome>`_

ChromeDriver
++++++++++++

Download the application from `<https://chromedriver.chromium.org/>`_,
select the correct version for your operating system,
and place it in a directory that is in your operating system's ``PATH``.

Alternatively, use a package manager:

Mac OS X
========

Via `Homebrew <http://mxcl.github.com/homebrew/>`_:

.. code-block:: console

    brew install chromedriver

Windows
=======

Via `Chocolatey <https://chocolatey.org/>`_:

.. code-block:: console

    choco install chromedriver

Usage
-----

To use Chrome, use the string ``chrome`` when you create
the ``Browser`` instance:

.. code-block:: python

    from splinter import Browser
    browser = Browser('chrome')

Headless mode
+++++++++++++

**Note:** if you have trouble with ``$HOME/.bash_profile``, you can try ``$HOME/.bashrc``.

Headless mode
+++++++++++++

Starting with Chrome 59, Chrome can run in a headless mode.
Further Information: `google developers updates <https://developers.google.com/web/updates/2017/05/nic59#headless>`_

To use headless mode, pass the `headless` argument
when creating a new Browser instance.

.. code-block:: python

    from splinter import Browser
    browser = Browser('chrome', headless=True)

Incognito mode
++++++++++++++

To use Chrome's incognito mode, pass the `incognito` argument
when creating a Browser instance.

.. code-block:: python

    from splinter import Browser
    browser = Browser('chrome', incognito=True)

Emulation mode
++++++++++++++

Since Chrome options can be passed to customize Chrome's behaviour;
it's possible to leverage the experimental emulation mode.

.. code-block:: python

    from selenium import webdriver
    from splinter import Browser

    mobile_emulation = {"deviceName": "Google Nexus 5"}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option(
        "mobileEmulation", mobile_emulation)
    browser = Browser('chrome', options=chrome_options)


See: `chrome driver documentation <https://sites.google.com/a/chromium.org/chromedriver/mobile-emulation>`_


Custom executable path
++++++++++++++++++++++

WebDriver can also use a version of Chrome installed at a custom path.
To do this, pass the executable path as a dictionary to the `**kwargs` argument.
The dictionary should be set up with `executable_path` as the key and the value set to the path to the executable file.

.. code-block:: python

    from splinter import Browser
    executable_path = {'executable_path': '</path/to/chrome>'}

    browser = Browser('chrome', **executable_path)

Custom executable path
++++++++++++++++++++++

Chrome can also be used from a custom path.
Pass the executable path as a dictionary to the `**kwargs` argument.
The dictionary should be set up with `executable_path` as the key and
the value set to the path to the executable file.

.. code-block:: python

    from splinter import Browser
    executable_path = {'executable_path':'</path/to/chrome>'}

    browser = Browser('chrome', **executable_path)


API docs
--------

.. autoclass:: splinter.driver.webdriver.chrome.WebDriver
   :members:
   :inherited-members:
