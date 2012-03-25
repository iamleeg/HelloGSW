#ifndef GNUSTEP
#include <GNUstepBase/GNUstep.h>
#endif

#import "Main.h"

@implementation Main

- (NSString *)now {
  NSDate *theDate = [NSDate date];
  return [theDate description];
}

@end
