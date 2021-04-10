
The hub2hub's documentation!
===========================

.. toctree::
	:maxdepth: 1
	:caption: Getting started
	:hidden:
	
	install

.. toctree::
	:maxdepth: 0
	:caption: PoweredUP devices
	:hidden:
	
	hubs
	sensors
	motors
	
.. toctree::
	:maxdepth: 1
	:caption:  hub2hub modules
	:hidden:
	
	puphub
	led
	button
	motion
	device
	motor
	
The ``hub2hub`` library is not part of the original firmware of either the Robot Inventor hub or the SPIKE Prime hub. In the official SPIKE Prime firmware, a low-level ubluetooth library is available to be able to directly communicate over Bluetooth Low Energy (BLE). The documentation of this module can be found here: `ubluetooth documentation <https://docs.micropython.org/en/latest/library/ubluetooth.html>`_

The main goal of the ``hub2hub`` library is to simplify the python code required to setup and maintain a BLE connection between LEGO hubs. Installation of the library and writing programs that use it are both possible via the official LEGO Education SPIKE Prime app, as explained :ref:`here<section_install>`.

This library is still actively developed, at the moment two different versions are available that cannot be installed at the same time on a single hub. 

* The latest version: 0.1.0 supports communication between a LEGO SPIKE Prime or LEGO MINDSTORMS Robot Inventor hub with a PoweredUP hub. This version is documented on this page. 
* The previous version: 0.0.3/0.0.4 supports communication between LEGO SPIKE Prime and LEGO MINDSTORMS Robot Inventor hubs. This version is document `here <https://hubmodule.readthedocs.io/en/latest/hub2hub>`_

In a future release functionalities of both versions will be combined. 

