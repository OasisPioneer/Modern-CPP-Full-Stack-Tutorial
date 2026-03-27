# 常量

常量与变量大致类似，都是为内存中的数据进行命名标记。但不同的是常量一旦初始化后，不允许通过该名字修改对象。

常量的实现方式主要包括：

- 宏（#define，预处理阶段）
- const（运行期只读）
- constexpr（编译期常量）
- consteval
- constinit
- 枚举常量

## 宏常量

宏常量事实上并不算是一个常量而是在预处理阶段的文本替换。

```CPP
#define PI 3.14 // 在预处理阶段代码中的 PI 会被替换为 3.14
```

```CPP
double x = PI * 2;
// 替换
double x = 3.14 * 2;
```

```{caution}
宏常量没有类型也就是说编译器根本不知道你定义的数据到底是什么类型的数据。

同时宏常量也没有作用域极大可能造成全局污染。
```

在什么情况下需要使用宏常量?

- 条件编译:

```CPP
#define DEBUG

#ifdef DEBUG
    // 在调试模式下执行特定内容
#endif
```

- 系统适配:

```CPP
#ifdef _WIN32
// Windows 平台执行特定代码
#elif defined(__linux__)
// Linux 平台执行特定代码
#endif
```

- 编译器适配
- 架构适配 ……

## 普通常量

普通常量其实就是一个只读的变量，定义普通常量需要使用 **`const`** 关键字。

普通常量语法: 

```CPP
const 数据类型 常量名称 = 值;
```

现代常量语法:

```CPP
const 数据类型 常量名称{值};
```

常量可以理解为就是在变量的前面增加了 `const` 关键字然后让变量从读写变成了只读。

普通常量有数据类型、作用域、编译器检查相比宏替换更加安全。

普通常量的常见使用场景:

- 参数保护:

```CPP
void foo(const std::string& s); // 防止函数内部修改参数
```

- 只读变量:

```CPP
const int max_users{1000};
```

## 编译期常量

自 C++ 11 起支持使用 **`constexpr`** 定义常量，用于定义必须在编译期就能确定值的常量。

定义语法:
```CPP
constexpr 数据类型 常量名称{值};
```

```CPP
constexpr int a{10};
```

constexpr 必须是编译期可计算的表达式，允许编译器在编译阶段完成计算，从而避免运行时开销。

使用场景:

- 编译期计算:

```CPP
constexpr int square(int x) {
    return x * x;
}

constexpr int a{square(5)};
```

- 数组大小:

```CPP
constexpr int size{100};
int arr[size];
```

从编译器视角看 const 与 constexpr 的实际区别:

- const 只保证值是只读不能修改的，而无法保证这个值在编译期一定存在。

例如:

```CPP
const int x{rand()}; // 合法但 x 的值只有在运行期才知道
```

- constexpr 编译期就必须确定值

例如:

```CPP
constexpr int a{10}; // 能在编译阶段算出来否则直接报错

constexpr int x{rand()}; // 编译失败，rand() 函数只有在运行期才会有返回值
```

## consteval

自 C++ 20 起引入了consteval，用于定义必须在编译期执行的函数

代码演示:

```CPP
consteval int square(int x) {
    return x * x;
}

constexpr int a = square(5);  // OK，编译期计算
// int b = square(rand());  // 错误：square必须在编译期计算
```

与 constexpr 不同，consteval 函数总是在编译期执行，不能用于运行期计算。

## constinit

constinit 同样是 C++ 20 引入的，用于确保变量在编译期初始化

代码演示:

```CPP
constinit int x = 42;  // 编译期初始化

// constinit int y = rand();  // 错误：必须编译期初始化
```

与 const 和 constexpr 不同，constinit 变量在运行期可以修改

代码演示:

```CPP
constinit int x = 42;
x = 100;  // constinit不影响运行期修改
```

## 枚举常量

枚举（Enumeration）是 C++ 中一种用户自定义类型，用于定义一组命名的整型常量。它能让代码更具可读性、类型更安全，特别适合表示一组相关的离散值（如状态、方向、选项等）。

C++ 提供了两种枚举形式：

- 传统枚举（enum，C++98 起）
- 枚举类（enum class / enum struct，C++11 起，推荐使用）

### 传统枚举

#### 基本定义与使用

代码演示:

```CPP
// 定义一个表示颜色的枚举
enum Color {
    Red,    // 默认值为 0
    Green,  // 自动递增为 1
    Blue    // 自动递增为 2
};

int main() {
    Color c = Red;  // 使用枚举值
    
    if (c == Red) {
        std::cout << "颜色是红色" << std::endl;
    }
}
```

#### 手动指定枚举值

你可以手动为枚举值指定底层整数值，未指定的会自动从最后一个指定值递增。

```CPP
enum Status {
    OK = 0,
    Warning = 1,
    Error = 2,
    FatalError  // 自动为 3
};

// 也可以不连续指定
enum Weekday {
    Monday = 1,
    Tuesday = 2,
    Wednesday = 3,
    Thursday = 4,
    Friday = 5,
    Saturday = 6,
    Sunday = 7
};
```

传统枚举虽然简单，但存在两个显著问题

作用域污染:

枚举值会直接暴露在枚举所在的作用域中，容易导致命名冲突

```CPP
enum Color { Red, Green, Blue };
enum TrafficLight { Red, Yellow, Green };  // 错误！Red 和 Green 重复定义
```

隐式转换为 int:

枚举值会隐式转换为整数，可能导致类型不安全

```CPP
enum Color { Red, Green, Blue };
Color c = Red;

int num = c;  // 隐式转换为 int（值为 0）
if (c == 0) {  // 直接和整数比较
    // ...
}
```

### 枚举类（enum class / enum struct）

为了解决传统枚举的问题，C++11 引入了枚举类（也叫 “强类型枚举”）。它是现代 C++ 中推荐使用的枚举形式。

#### 定义与使用

枚举类使用 enum class（或 enum struct，两者完全等价）

```CPP
// 定义枚举类
enum class Color {
    Red,
    Green,
    Blue
};

int main() {
    // 访问枚举值时必须加上枚举类名::前缀
    Color c = Color::Red;
    
    if (c == Color::Red) {
        std::cout << "颜色是红色" << std::endl;
    }
}
```

枚举类的优势

强作用域:

枚举值被封装在枚举类内部，不会污染外部作用域

```CPP
enum class Color { Red, Green, Blue };
enum class TrafficLight { Red, Yellow, Green };  // 没问题！

Color c = Color::Red;
TrafficLight t = TrafficLight::Red;  // 两者互不冲突
```

强类型（无隐式转换）:

枚举类不会隐式转换为 int，必须显式转换

```CPP
enum class Color { Red, Green, Blue };
Color c = Color::Red;

// int num = c;  // 错误！不能隐式转换
int num = static_cast<int>(c);  // 正确，显式转换为 int（值为 0）

// if (c == 0) {  // 错误！不能直接和整数比较
if (c == Color::Red) {  // 正确，只能和同类型枚举值比较
    // ...
}
```

### 指定底层类型

无论是传统枚举还是枚举类，都可以显式指定底层数据类型（默认是 int）。这在需要控制内存大小或与特定硬件 / 协议交互时很有用

```CPP
// 枚举类指定底层类型为 char（节省空间）
enum class Color : char {
    Red,
    Green,
    Blue
};

// 传统枚举也可以指定底层类型（C++11 起）
enum Status : unsigned int {
    OK = 0,
    Warning = 1,
    Error = 2
};

// 查看枚举大小
std::cout << sizeof(Color) << std::endl;  // 输出 1（char 的大小）
std::cout << sizeof(Status) << std::endl; // 输出 4（unsigned int 的大小）
```

## 如何选择

- 能在编译期确定的值 → 使用 constexpr
- 需要运行期确定但不希望修改 → 使用 const
- 仅用于编译控制（如平台 / 调试） → 使用 #define
- 表示一组相关常量 → 使用枚举
- 需要确保编译期初始化但运行期可修改 → 使用 constinit
- 函数必须在编译期执行 → 使用 consteval

优先级: 在现代 C++ 中，优先选择 constexpr，其次 const，在现代 C++ 中，应避免使用宏定义常量。