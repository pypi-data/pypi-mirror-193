Archivist
=========

*Easily build a logger with various usual templates : console, rotating
and file.*

Installation
------------

.. code:: bash

   pip install archivist

Usage
-----

Build and use the logger
~~~~~~~~~~~~~~~~~~~~~~~~

There’s really only object that is to be used, that configures and
returns a logger with one of the available configuration templates.

.. code:: python

   from archivist import LoggerBuilder

   logger = LoggerBuilder().build()

   message = "Hello"
   logger.info("An info saying %s", message)

The default behaviour is to log only to console. To change this
behaviour and log to files ontop of logging to console, use one of the
built-in templates by specifying the ``template`` argument :
``LoggerBuilder().build(template="rotating")``. See the details section
for more information about the available templates.

*Note that you should instanciate a logger as above only once for the
whole program*, usually in the main. Logger instances in modules are to
be accessed with ``logger = logging.getLogger(__name__)``, so that the
program from which the logger was called always appears in the log
statement.

Details
-------

Setting log level
~~~~~~~~~~~~~~~~~

The main feature of this package, compared to the usual
``logging.getLogger(__name__)``, is to choose the level of logging from
an environment variable rather than hard-setting it in the code.

The level (for both console and file handlers) is read from variable
``LOGGER_LEVEL``, and defaulted to ``CRITICAL`` if it is not found. The
level is applied both to the console handler and the optional file
handler.

Logging templates
~~~~~~~~~~~~~~~~~

There are three logging behaviours available that must be chosen when
building a logger : *console*, *rotating* or *scheduled*.

Template *console*
^^^^^^^^^^^^^^^^^^

When building the logger with ``template="console"``, the returned
logger will only log statements to the console. When using this template
on aws lambda functions, these statements are automatically redirected
to cloudwatch.

Template *rotating*
^^^^^^^^^^^^^^^^^^^

When building the logger with ``template="rotating"``, log files will be
written using ``logging.handlers.RotatingFileHandler``, which means that
each log file has a size limit, and when the size limit is reached,
another log file is created. See the documentation
`here <https://docs.python.org/3/library/logging.handlers.html#logging.handlers.RotatingFileHandler>`__
for details.

The size limit for a single file is set to 1MB, and the maximum number
of files is 20. This mode is appropriate for programs that handles a lot
of requests

Template *scheduled*
^^^^^^^^^^^^^^^^^^^^

When building the logger with ``template="scheduled"``, a single log
file is written per program execution. The launch date and time is
appended to the log file name, so that each execution can be uniquely
retrieved by its log file. The format is
``activity-20200101-00h00m00s.log``.

This mode is appropriate for periodically triggered programs, where one
wants to be able to identify then investigate a specific execution.

Logfiles name and location
~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, when log files are written, they are at the module’s
location, with a default filename ``activity.log`` (with variations
according to the template used). It is generally a bad idea to keep log
files there since they won’t be easily accessible in a python
environment. Defining custom location and filename is made with
(``.log`` extension is automatically appended to the given filename) :

.. code:: python

   logger = LoggerBuilder().build(template="scheduled", folder="/home/here", filename="tracking")

Note that no log file is written when using the default behaviour which
is template *console*, so those arguments, if given, will be ignored.
