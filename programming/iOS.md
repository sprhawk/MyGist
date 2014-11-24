iOS
===


1.  layer需要在View里手动调整frame (- layoutSubviews())

2. UIViewController里可以override - viewDidLayoutSubviews() 方法

3. Circle Mask
```swift
func circleImageMask(#radius:CGFloat) -> UIImage {
    let l = radius * 2
    UIGraphicsBeginImageContextWithOptions(CGSizeMake(l, l), false, UIScreen.mainScreen().scale)
    UIColor(red: 0.0, green: 0.0, blue: 0.0, alpha: 0.0).setFill()
    let r = CGRectMake(0, 0, l, l)
    UIRectFill(r)
    UIColor(red: 1.0, green: 1.0, blue: 1.0, alpha: 1.0).setFill()
    let b = UIBezierPath(ovalInRect: r)
    b.fill()
    let i = UIGraphicsGetImageFromCurrentImageContext()
    UIGraphicsEndImageContext()
    
    return i
}
```
