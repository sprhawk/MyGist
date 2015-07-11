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

4. 使用 swift 的 IBDesignable 功能需要在 Storyboard 里选择正确的 module ( app 名称 )

5. Objective-C 也是可以使用 IBDesignable 的 ( IB_DESIGNABLE )

6. 在 Playground 里显示动画需要选择 run in full simulator

7. 在 Playground 里显示 View 还是要 import XCPlayground， 和XCPShowView() 方法
