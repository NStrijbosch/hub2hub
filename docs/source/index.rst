
The hub2hub's documentation!
===========================

.. toctree::
	:maxdepth: 1
	:caption: Getting started
	
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