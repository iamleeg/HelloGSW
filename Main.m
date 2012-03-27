#ifndef GNUSTEP
#include <GNUstepBase/GNUstep.h>
#endif

#import "Main.h"

@implementation Main
{
  NSDate *accessedAt;
}

- (id)init {
  if ((self = [super init])) {
    accessedAt = [[NSDate date] retain];
  }
  return self;
}

- (NSString *)now {
  return [accessedAt description];
}

- (void)dealloc {
  [accessedAt release];
  [super dealloc];
}

@end
