#ifndef GNUSTEP
#include <GNUstepBase/GNUstep.h>
#endif

#import "ClickDelay.h"

@implementation ClickDelay

@synthesize startDate;

- (NSString *)delay {
  NSDate *now = [NSDate date];
  NSTimeInterval interval = [now timeIntervalSinceDate: startDate];
  return [NSString stringWithFormat: @"%.0f", interval];
}

- (void)dealloc {
  [startDate release]; startDate = nil;
  [super dealloc];
}

@end
