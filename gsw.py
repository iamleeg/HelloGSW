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

def addGSWComponentToMakefile(name):
    appName = ":-("
    outFile=tempfile.NamedTemporaryFile()
    for line in fileinput.input("GNUmakefile"):
        strippedLine=line[0:-1]
        if line.startswith("GSWAPP_NAME"):
            appName = strippedLine.split("=")[1]
    if appName == ":-(":
        print "Skipping GNUmakefile changes, couldn't find the app name"
    else:
        objcFilesVar = appName+"_OBJC_FILES"
        objcFileName = name+".m"
        componentsVar = appName+"_COMPONENTS"
        componentName = name+".wo"
        for line in fileinput.input("GNUmakefile"):
            if line.startswith(objcFilesVar):
                if line.find(objcFileName) == -1:
                    changedLine = line[0:-1] + " " + objcFileName + "\n"
                    outFile.write(changedLine)
                else:
                    print objcFileName + " is already in the target"
                    outFile.write(line)
            elif line.startswith(componentsVar):
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
            
def createGSWComponent(name):
    createGSWComponentInterface(name)
    createGSWComponentImplementation(name)
    createGSWComponentFolder(name)
    createGSWComponentHTML(name)
    createGSWComponentWOD(name)
    createGSWComponentWOO(name)
    addGSWComponentToMakefile(name)

def usage():
    print "usage: gsw.py addComponent <component>"
    sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) == 3 and sys.argv[1] == "addComponent":
        createGSWComponent(sys.argv[2])
    else:
        usage()
