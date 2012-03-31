#ifndef GNUSTEP
#include <GNUstepBase/GNUstep.h>
#endif

#import "DirectAction.h"

@implementation DirectAction

- (GSWComponent *)helloAction {
  return [self pageWithName: @"Main"];
}

@end
