#include <WebObjects/WebObjects.h>

/**
 * This is the first component a visitor will see.
 */
@interface Main:GSWComponent 
{ 
  NSDate *accessedAt;
}

- (NSString *)now;
- (GSWComponent *)nextPage;

@end
