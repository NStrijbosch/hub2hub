.. _section_install:

############
Installation
############


The following steps guide you through the process to install the ``hub2hub`` library. This installation is only required on the LEGO Eduction SPIKE Prime hub or the LEGO MINDSTORMS Robot Inventor hub. For the PoweredUP hubs used in your project it is sufficient to update them with the latest official firmware via the PoweredUP app. 


Step 1
------

If you did not update your SPIKE Prime software yet, install one of the latest versions of the SPIKE Prime app (1.3.4 or 1.3.3) and connect your device. If the app asks for a hub update, perform the hub update.

.. warning::
	This library does not work when using the MINDSTORMS Robot Inventor app. Due to a firmware difference, the Bluetooth module is not available when using the MINDSTORMS Robot Inventor App and corresponding firmware. Luckily you can just connect your MINDSTORMS hub to the SPIKE Prime app and update the SPIKE PRIME Firmware on the hub.
	
Step 2
------

Download and open the project: 'Instal_hub2hub_v010.llsp <https://github.com/NStrijbosch/hub2hub/blob/main/install/Install_hub2hub_v010.llsp?raw=true>'

Step 3
------

Set the SPIKE Prime execution mode in download mode, and select an unused project slot.

image:: /images/app_download_mode.png
	:height: 100
	:alt: app download mode


Step 4
------

image:: /images/app_run.png
	:height: 100
	:alt: app run
	
Step 5
------
Installation is successful. The hub2hub library is now installed on your hub. You can now safely use the slot you used for this installation for a new project.

.. warning::
	Firmware updates of the hub are likely to remove the library from the filesystem of the hub. Hence, this procedure should be repeated if a firmware update removed the library from the hub.

