#ifndef GNUSTEP
#include <GNUstepBase/GNUstep.h>
#endif

#include <WebObjects/WebObjects.h>

int main(int argc, const char *argv[])
{
  int ret=0;
  NSAutoreleasePool *arp = [NSAutoreleasePool new];
  ret=WOApplicationMain(@"HelloGSW", argc, argv);
  [arp release];
  return ret;
}
