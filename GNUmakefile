include $(GNUSTEP_MAKEFILES)/common.make
include $(GNUSTEP_MAKEFILES)/Auxiliary/gsweb_wo.make

GSWAPP_NAME=HelloGSW
HelloGSW_HAS_GSWCOMPONENTS=YES
HelloGSW_PRINCIPAL_CLASS=HelloGSW
HelloGSW_GSWAPP_INFO_PLIST=Resources/Info-HelloGSW.plist

HelloGSW_OBJC_FILES=HelloGSW_main.m HelloGSW.m Main.m Session.m ClickDelay.m
HelloGSW_COMPONENTS=Main.wo ClickDelay.wo

ifneq ($(FOUNDATION_LIB),gnu)
AUXILIARY_GSW_LIBS = -framework WebObjects -framework WOExtensions
else
AUXILIARY_GSW_LIBS += -lWebObjects -lWOExtensions
endif


-include Makefile.preamble

include $(GNUSTEP_MAKEFILES)/gswapp.make

-include Makefile.postamble

