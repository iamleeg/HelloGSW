#ifndef GNUSTEP
#include <GNUstepBase/GNUstep.h>
#endif

#import "HelloGSW.h"

@implementation HelloGSW

- (id)init
{
  if (self = [super init]) {
    [WOMessage setDefaultEncoding: NSUTF8StringEncoding];
  }
  return self;
}

+ (NSNumber *)sessionTimeOut
{
  return [NSNumber numberWithInt:60];
}

@end
