#include <WebObjects/WebObjects.h>

@interface Main:GSWComponent 
{ 
  NSDate *accessedAt;
}

- (NSString *)now;
- (GSWComponent *)nextPage;

@end
