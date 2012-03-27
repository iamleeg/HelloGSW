#include <WebObjects/WebObjects.h>

@interface ClickDelay:GSWComponent

@property (nonatomic, retain) NSDate *startDate;
@property (nonatomic, readonly) NSString *delay;

@end
