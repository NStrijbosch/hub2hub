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