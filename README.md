# Remote FlatPanel to help with taking calibration frames.

This flat panel is going to be an open source, dimmable flat panel for astronomy.

## Features
- Dimmable flat panel
- Optional dew heater
- Flat panel acts like lens cap
- AsiAir remote controlable (both for heater and panel)
- oLed display for local control
- Wifi remote control
- Ascom Alpaca control
- Temperature and humidity sensor
- Fully automatic mode for dew heater

Above is the fully list of features that I'm planning.  Some of the features will cancel out other features. For example Fully Automatic mode will be available for the dew heater, to use the minimum power so that it keeps away dew without human interaction, however I want to have the ability to overrride this in several ways - Using an output from the AsiAir, a dedicated web page, Ascom Alpaca or manually via the display.

The plan is that this is going to be a full solution for any size scope, however, my initial project is based on creating a Panel for my SpaceCat 51 Scope.   Once that is working, I'll be looking at how to modify the project to work with my Meade LX-90.

## Discord

[cjdSkunkWorks/FlatPanel](https://discord.com/channels/800391513091211284/1350925191181631498)


## Todo list
- ~~Upload Display board design prototype~~ (done)
- ~~Upload Mainboard design prototype~~ (done)
- Finish designing 3D files for the SpaceCat51
  ![3D Design Progress](3D%20Models/FlatPanelDesignProgress.png)
- Upload 3d models for the SpaceCat51
- Finalise PCB Layout for Display Board
- Finalise PCB Layout for Mainboard
- Figure out display controls for manual mode
- Create micropython source oode for Pico
- Upgrade MicroPython code to support Pico W, for Web access
- Upgrade MicroPyton code to implement ASCOM Alpaca support
