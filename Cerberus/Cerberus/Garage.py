from gpiozero import *

class Garage(object):
    garageActivatePin = LED(4)

    def activateGarage():
         status = "Failed"
         try:
             garageActivatePin.on()
             sleep(2)
             garageActivatePin.off()
             sleep(2)
         except :
             pass

    def checkStatus():
        garageStatusPin = MotionSensor(18)
        if(garageStatusPin.is_active):
            return "Open"
        else:
            return "Closed"
        


        #garageStatusPin.

#            GpioPin pin = null;
#            GpioController gpio = null;
#            try
#            {
#                gpio = GpioController.GetDefault();
#                GpioOpenStatus pinStatus;
#                if (gpio.TryOpenPin(GARAGE_ACTIVATE_PIN, GpioSharingMode.Exclusive, out pin, out pinStatus))
#                {
#                    if (pinStatus == GpioOpenStatus.PinOpened)
#                    {
#                        pin.Write(GpioPinValue.Low);
#                        var task = Task.Run(() => pin.SetDriveMode(GpioPinDriveMode.Output));
#                        if (!task.Wait(2000))
#                        {
#                            status = "GPIO drive mode timed out";
#                        }
#                        else
#                        {
#                            status = "Success";
#                        }
#                    }
#                }
#            }
#            catch (Exception e)
#            {
#                status = e.Message;
#            }
#            return status;

        
#    using Windows.Devices.Gpio;
#using System.Threading.Tasks;
#using System;
#using System.Threading;
#using Windows.Foundation;

#namespace WebService
#{
#    public sealed class GarageDoorInteraction
#    {
#  

#        public string ActivateGarage()
#        {
#            string status = "Failed";
#            GpioPin pin = null;
#            GpioController gpio = null;
#            try
#            {
#                gpio = GpioController.GetDefault();
#                GpioOpenStatus pinStatus;
#                if (gpio.TryOpenPin(GARAGE_ACTIVATE_PIN, GpioSharingMode.Exclusive, out pin, out pinStatus))
#                {
#                    if (pinStatus == GpioOpenStatus.PinOpened)
#                    {
#                        pin.Write(GpioPinValue.Low);
#                        var task = Task.Run(() => pin.SetDriveMode(GpioPinDriveMode.Output));
#                        if (!task.Wait(2000))
#                        {
#                            status = "GPIO drive mode timed out";
#                        }
#                        else
#                        {
#                            status = "Success";
#                        }
#                    }
#                }
#            }
#            catch (Exception e)
#            {
#                status = e.Message;
#            }
#            return status;
#        }

#        public string CheckGarageStatus()
#        {
#            string messageToReturn = "Unknown";
#            GpioPin pin = null;
#            GpioController gpio = null;
#            try
#            {
#                gpio = GpioController.GetDefault();
#                GpioOpenStatus pinStatus;
#                if (gpio.TryOpenPin(GARAGE_STATUS_PIN, GpioSharingMode.Exclusive, out pin, out pinStatus))
#                {
#                    var task = Task.Run(() => pin.SetDriveMode(GpioPinDriveMode.InputPullUp));
#                    if (!task.Wait(3000))
#                    {
#                        messageToReturn = "GPIO drive mode timed out";
#                    }
#                    else
#                    {
#                        var returned = pin.Read();
#                        if (returned == GpioPinValue.High)
#                        {
#                            messageToReturn = "Closed";
#                        }
#                        else
#                        {
#                            messageToReturn = "Open";
#                        }
#                        pin.Dispose();
#                    }
#                }
#                else
#                {
#                    messageToReturn = "Unknown";
#                }
#            }
#            catch (Exception e)
#            {
#                messageToReturn = e.Message;
#            }

#            return messageToReturn;
#        }

#    }
#}


