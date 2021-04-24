.. include:: hubs_image.rst

####
Hubs
####

Technic Hub
===========

|technic_hub_large|

.. class:: TechnicHub(bt_handler)
 
   Class to control a Technic Hub. 
   
   :param bt_handler: The bluetooth handler. 
	  
   .. attribute:: led
           
      Led
 
   .. attribute:: motion
           
      Motion
	  
   .. attribute:: port.A.device
   .. attribute:: port.B.device
   .. attribute:: port.C.device
   .. attribute:: port.D.device
           
      Device
	  
   .. attribute:: port.A.motor
   .. attribute:: port.B.motor
   .. attribute:: port.C.motor
   .. attribute:: port.D.motor
           
      Motor
	  
Example	
-------

.. literalinclude:: ../../examples/TechnicHub/technic_hub.py
	  
City Hub
===========

|city_hub_large|

.. class:: CityHub(bt_handler)
 
   Class to control a Technic Hub. 
   
   :param bt_handler: The bluetooth handler. 
	  
   .. attribute:: led
           
      Led
           	  
   .. attribute:: port.A.device
   .. attribute:: port.B.device
           
      Device
	  
   .. attribute:: port.A.motor
   .. attribute:: port.B.motor
           
      Motor
	  
Example	
-------

.. literalinclude:: ../../examples/CityHub/city_hub.py
	  
Remote
===========

|remote_large|

.. class:: Remote(bt_handler)
 
   Class to control a PoweredUP remote
   
   :param bt_handler: The bluetooth handler. 
	  
   .. attribute:: led
           
      Led
 
   .. attribute:: left.plus
   .. attribute:: left.red
   .. attribute:: left.min
   .. attribute:: right.plus
   .. attribute:: right.red
   .. attribute:: right.min
           
      Button
	  
Example	
-------

.. literalinclude:: ../../examples/Remote/remote.py

Mario
===========

|mario_large|

.. class:: Mario(bt_handler)
 
   Class to control a LEGO Mario
   
   :param bt_handler: The bluetooth handler. 
	  
   .. attribute:: barcode
           
      Barcode
	  
   .. attribute:: motion
   
      MotionMario
	  
   .. attribute:: pants
   
      Pants
	  
Example	
-------

.. literalinclude:: ../../examples/Mario/mario.py
