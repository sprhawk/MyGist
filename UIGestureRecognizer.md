UIGestureRecognizer
==============

```objc
if (UIGestureRecognizerStateRecognized == gesture.state) {
}
```

* 在识别touch时忽略掉某些子view的response

```objc
- (BOOL)gestureRecognizer:(UIGestureRecognizer *)gestureRecognizer shouldReceiveTouch:(UITouch *)touch
{
  if ([touch.view isDescendantOfView:loginButton]) {
      return NO;
  }
  else if ([touch.view isDescendantOfView:tempCloseButton]) {
      return NO;
  }
      return YES;
}
```






