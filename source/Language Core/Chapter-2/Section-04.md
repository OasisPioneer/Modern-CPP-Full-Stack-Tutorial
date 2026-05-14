# 数据类型转换

在 C++ 中，不同的数据类型之间无法始终直接进行操作，因此需要进行类型转换。

C++ 中的类型转换分为：

- 隐式类型转换（编译器自动完成）
- 显式类型转换（程序员主动指定）

## 隐式类型转换

隐式类型转换（Implicit Conversion）是指编译器自动完成的数据类型转换。

```cpp
#include <iostream>

int main() {
    int Int1 = 42;
    double DouBle1 = Int1; // int 隐式转换为 double
    std::cout << "DouBle1 = " << DouBle1 << std::endl;
    
    double DouBle2 = 3.14;
    int Int2 = DouBle2; // double 隐式转换为 int（小数部分被截断）
    std::cout << "Int2 = " << Int2 << std::endl;
    
    // 算术转换：不同类型的操作数会转换为相同类型
    double DouBle3 = Int1 + DouBle1; // i被转换为double，然后与pi相加
    std::cout << "DouBle3 = " << DouBle3 << std::endl;
}
```

## 显示类型转换

通过强制类型转换运算符手动进行的转换。

```cpp
#include <iostream>

int main() {
    double doubleValue = 3.14159;
    
    int intValue = (int)doubleValue;    // C风格转换
    int modernIntValue = static_cast<int>(doubleValue);  // C++风格转换

    std::cout << "原始浮点值: " << doubleValue << std::endl;
    std::cout << "转换为整数: " << intValue << std::endl;
    std::cout << "使用static_cast: " << modernIntValue << std::endl;
}
```