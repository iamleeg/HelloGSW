#HelloGSW

This project demonstrates a very simple web app written in Objective-C and the GNUstepWeb framework. It's intended to be a sample application, to show people unfamiliar with the framework the various components involved.

##Building

Having installed [GNUstepWeb](http://wiki.gnustep.org/index.php/GNUstepWeb), build the app like this:

    $ make

##Running

    $ HelloGSW.gswa/Contents/MacOS/HelloGSW

This will print output like the following:

    2012-03-25 22:47:18.469 HelloGSW[4824:307] host address '::1'
    2012-03-25 22:47:18.471 HelloGSW[4824:307] cPortn '9001'
    2012-03-25 22:47:18.472 HelloGSW[4824:307] Thread XX Waiting for connections on localhost:9001.
    2012-03-25 22:47:18.474 HelloGSW[4824:307] Application running. To use direct connect enter
    http://localhost:9001/WebObjects/HelloGSW.woa/0/
    in your web Browser.
    Please make sure that this port is only reachable in a trusted network.

Visit the URL shown in the logs using your web browser.
