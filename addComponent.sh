#!/bin/bash

COMPONENT_NAME=${1-"No Name"}

if [ "$COMPONENT_NAME" == "No Name" ]; then
    echo "Usage: addComponent.sh [name of component]"
    exit 1
fi

cat > "${COMPONENT_NAME}.h" <<-INTERFACE
  #include <WebObjects/WebObjects.h>

  @interface ${COMPONENT_NAME}:GSWComponent

  @end
INTERFACE

cat > "${COMPONENT_NAME}.m" <<-IMPLEMENTATION
  #ifndef GNUSTEP
  #include <GNUstepBase/GNUstep.h>
  #endif

  #import "${COMPONENT_NAME}.h"

  @implementation ${COMPONENT_NAME}

  @end
IMPLEMENTATION

mkdir "${COMPONENT_NAME}.wo"
touch "${COMPONENT_NAME}.wo/${COMPONENT_NAME}.wod"

cat > "${COMPONENT_NAME}.wo/${COMPONENT_NAME}.html" <<-HTML
  <!DOCTYPE HTML>
  <html>
    <head>
      <title>${COMPONENT_NAME}</title>
    </head>
    <body>
    </body>
  </html>
HTML

cat > "${COMPONENT_NAME}.wo/${COMPONENT_NAME}.woo" <<-WOO
  {"WebObjects Release" = "WebObjects 5.0"; encoding = NSUTF8StringEncoding; }
WOO

APP_NAME=`grep GSWAPP_NAME GNUmakefile | sed -E s/^GSWAPP_NAME[:space:]*=[:space:]*//`
COMPONENT_VAR="${APP_NAME}_COMPONENTS"
SED_COMPONENT_FUNCTION="/^${COMPONENT_VAR}/s/\$/ ${COMPONENT_NAME}.wo/"
sed -i '' "${SED_COMPONENT_FUNCTION}" GNUmakefile

OBJC_FILES_VAR="${APP_NAME}_OBJC_FILES"
SED_OBJC_FILES_FUNCTION="/^${OBJC_FILES_VAR}/s/\$/ ${COMPONENT_NAME}.m/"
sed -i '' "${SED_OBJC_FILES_FUNCTION}" GNUmakefile

echo "Added component ${COMPONENT_NAME}"
exit 0
