#ifndef GNUSTEP
#include <GNUstepBase/GNUstep.h>
#endif

#import "Main.h"
#import "ClickDelay.h"

@implementation Main

- (id)init {
  if ((self = [super init])) {
    accessedAt = [[NSDate date] retain];
  }
  return self;
}

- (NSDate *)now {
  return accessedAt;
}

- (GSWComponent *)nextPage {
  ClickDelay *nextComponent = (ClickDelay *)[self pageWithName: @"ClickDelay"];
  nextComponent.startDate = accessedAt;
  return nextComponent;
}

- (void)dealloc {
  [accessedAt release];
  [super dealloc];
}

@end
