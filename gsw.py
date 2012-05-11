#!/usr/bin/python
import os
import sys
import fileinput
import tempfile
import shutil

def informSkipped(path):
    print "Skipped " + path + ": file exists"

def writeToFile(path, content):
    file = open(path, 'w')
    file.write(content)
    file.close()

def createGSWComponentInterface(name):
    interfacePath = name + ".h"
    if not os.path.exists(interfacePath):
        interface = """#include <WebObjects/WebObjects.h>

@interface ###name###:GSWComponent

@end""".replace("###name###", name)
        writeToFile(interfacePath, interface)
    else:
        informSkipped(interfacePath)
    

def createGSWComponentImplementation(name):
    implementationPath = name + ".m"
    if not os.path.exists(implementationPath):
        implementation = """#ifndef GNUSTEP
#include <GNUstepBase/GNUstep.h>
#endif

#import "###name###.h"

@implementation ###name###

@end
""".replace("###name###", name)
        writeToFile(implementationPath, implementation)
    else:
        informSkipped(implementationPath)

def GSWComponentFolderName(componentName):
    return componentName + ".wo"

def createGSWComponentFolder(name):
    folderPath = GSWComponentFolderName(name)
    if not os.path.exists(folderPath):
        os.mkdir(folderPath)
    else:
        print "Folder exists: " + folderPath

def createGSWComponentHTML(name):
    htmlPath = GSWComponentFolderName(name) + os.sep + name + ".html"
    if not os.path.exists(htmlPath):
        html = """<!DOCTYPE HTML>
<html>
  <head>
    <title>###name###</title>
  </head>
  <body>
  </body>
</html>""".replace("###name###", name)
        writeToFile(htmlPath, html)
    else:
        informSkipped(htmlPath)

def createGSWComponentWOD(name):
    wodPath = GSWComponentFolderName(name) + os.sep + name + ".wod"
    if not os.path.exists(wodPath):
        open(wodPath, "w")
    else:
        informSkipped(wodPath)

def createGSWComponentWOO(name):
    wooPath = GSWComponentFolderName(name) + os.sep + name + ".woo"
    if not os.path.exists(wooPath):
        woo = '{"WebObjects Release" = "WebObjects 5.0"; encoding = NSUTF8StringEncoding; }'
        writeToFile(wooPath, woo)
    else:
        informSkipped(wooPath)

def GSWAppName():
    appName = ":-("
    for line in fileinput.input("GNUmakefile"):
        strippedLine=line[0:-1]
        if line.startswith("GSWAPP_NAME"):
            appName = strippedLine.split("=")[1]
    return appName

def addClassToMakefile(name):
    appName = GSWAppName()
    outFile=tempfile.NamedTemporaryFile()
    if appName == ":-(":
        print "Skipping GNUmakefile changes, couldn't find the app name"
    else:
        objcFilesVar = appName+"_OBJC_FILES"
        objcFileName = name+".m"
        for line in fileinput.input("GNUmakefile"):
                if line.startswith(objcFilesVar):
                    if line.find(objcFileName) == -1:
                        changedLine = line[0:-1] + " " + objcFileName + "\n"
                        outFile.write(changedLine)
                    else:
                        print objcFileName + " is already in the target"
                        outFile.write(line)
                else:
                    outFile.write(line)
        outFile.flush()
        shutil.copyfile(outFile.name, "GNUmakefile")


def addGSWComponentToMakefile(name):
    addClassToMakefile(name)
    appName = GSWAppName()
    outFile=tempfile.NamedTemporaryFile()
    if appName == ":-(":
        print "Skipping GNUmakefile changes, couldn't find the app name"
    else:
        componentsVar = appName+"_COMPONENTS"
        componentName = name+".wo"
        for line in fileinput.input("GNUmakefile"):
            if line.startswith(componentsVar):
                if line.find(componentName) == -1:
                    changedLine = line[0:-1] + " " + componentName + "\n"
                    outFile.write(changedLine)
                else:
                    print componentName + " is already in the target"
                    outFile.write(line)
            else:
                outFile.write(line)
        outFile.flush()
        shutil.copyfile(outFile.name, "GNUmakefile")

def createFolder(name):
    os.mkdir(name)

def createGSWMakefile(name):
    if not os.path.exists("GNUmakefile"):
        GNUmakefile = """include $(GNUSTEP_MAKEFILES)/common.make
include $(GNUSTEP_MAKEFILES)/Auxiliary/gsweb_wo.make

GSWAPP_NAME=###name###
###name###_HAS_GSWCOMPONENTS=YES
###name###_PRINCIPAL_CLASS=###name###
###name_GSWAPP_INFO_PLIST=Resources/Info.plist

###name###_OBJC_FILES=
###name###_COMPONENTS=

ifneq ($(FOUNDATION_LIB),gnu)
AUXILIARY_GSW_LIBS = -framework WebObjects -framework WOExtensions
else
AUXILIARY_GSW_LIBS += -lWebObjects -lWOExtensions
endif


-include Makefile.preamble

include $(GNUSTEP_MAKEFILES)/gswapp.make

-include Makefile.postamble
""".replace("###name###", name)
        writeToFile("GNUmakefile", GNUmakefile)
    else:
        informSkipped("GNUmakefile")

def createInfoPlist(name):
    infoPlistPath = "Resources/Info.plist"
    if not os.path.exists(infoPlistPath):
        infoPlist="""defaults = {
  GSWAdaptor = GSWDefaultAdaptor;
  GSWDebugSetConfigFilePath = "/etc/gsweb/###name###.logstate";
  GSWHost = "localhost";
  GSWPort = 9001;
  GSWApplicationBaseURL = "/GSW";
  GSWFrameworksBaseURL = "/GSW/frameworks";
  GSWLoadFrameworks = (
    "GSWExtensionsGSW",
    "GSWExtensions"
  );
  GSWMonitorAppConfFilePath = "/etc/httpd/conf/GSWebMonitor.conf";
  GSWSessionTimeOut = 1200;
};
""".replace("###name###", name)
        writeToFile(infoPlistPath, infoPlist)
    else:
        informSkipped(infoPlistPath)

def createWOAppSubclass(name):
    headerPath = name + ".h"
    if not os.path.exists(headerPath):
        header = """#include <WebObjects/WebObjects.h>
            
@interface ###name### : GSWApplication
@end
""".replace("###name###", name)
        writeToFile(headerPath, header)
    else:
        informSkipped(headerPath)
    implementationPath = name + ".m"
    if not os.path.exists(implementationPath):
        implementation = """#ifndef GNUSTEP
#include <GNUstepBase/GNUstep.h>
#endif

#import "###name###.h"

@implementation ###name###

- (id)init
{
  if ((self = [super init])) {
    [WOMessage setDefaultEncoding: NSUTF8StringEncoding];
    NSString *directActionHandlerKey = [[self class] directActionRequestHandlerKey];
    WORequestHandler *directActionHandler = [self requestHandlerForKey: directActionHandlerKey];
    [self setDefaultRequestHandler: directActionHandler];
  }
  return self;
}

+ (NSNumber *)sessionTimeOut
{
  return [NSNumber numberWithInt:60];
}

@end
""".replace("###name###", name)
        writeToFile(implementationPath, implementation)
    else:
        informSkipped(implementationPath)
    addClassToMakefile(name)

def createGSWMain(name):
    mainFile = name + "_main"
    mainPath = mainFile + ".m"
    if not os.path.exists(mainPath):
        mainContent = """#ifndef GNUSTEP
#include <GNUstepBase/GNUstep.h>
#endif

#include <WebObjects/WebObjects.h>

int main(int argc, const char *argv[])
{
  int ret=0;
  NSAutoreleasePool *arp = [NSAutoreleasePool new];
  ret=WOApplicationMain(@"###name###", argc, argv);
  [arp release];
  return ret;
}
""".replace("###name###", name)
        writeToFile(mainPath, mainContent)
    else:
        informSkipped(mainPath)
    addClassToMakefile(mainFile)

def createGSWComponent(name):
    createGSWComponentInterface(name)
    createGSWComponentImplementation(name)
    createGSWComponentFolder(name)
    createGSWComponentHTML(name)
    createGSWComponentWOD(name)
    createGSWComponentWOO(name)
    addGSWComponentToMakefile(name)

def createGSWApp(name):
    createFolder(name)
    os.chdir(name)
    createFolder("Resources")
    createGSWMakefile(name)
    createInfoPlist(name)
    createWOAppSubclass(name)
    createGSWComponent("Main")
    createGSWMain(name)
    os.chdir("..")

def usage():
    print "usage: gsw.py addComponent <component>"
    print "       gsw.py newApp <appname>"
    sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) == 3:
        if sys.argv[1] == "addComponent":
            createGSWComponent(sys.argv[2])
        elif sys.argv[1] == "newApp":
            createGSWApp(sys.argv[2])
        else:
            usage()
    else:
        usage()
