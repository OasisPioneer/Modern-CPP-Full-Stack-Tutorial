# 常量

常量与变量大致类似，都是为内存中的数据进行命名标记。但不同的是常量一旦初始化后，不允许通过该名字修改对象。

常量的实现方式主要包括：

- 宏（#define，预处理阶段）
- const（运行期只读）
- constexpr（编译期常量）

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

定义语法: 

```CPP
const 数据类型 常量名称 = 常量的值;
```

可以理解为就是在变量的前面增加了 `const`。

普通常量有数据类型、作用域、编译器检查相比宏常量更加安全。

```{caution}
需要注意的是对于下方这种定义，编译器在编译的时候不保证知道常量的值。

```CPP
const int x = rand(); // rand() 随机数函数，返回伪随机数。
```

普通常量使用场景:

- 函数参数:

```CPP
void foo(const std::string& s); // 防止参数被修改
```

- 只读变量:

```CPP
const int max_users = 1000;
```

- 类成员 ……

## 编译期常量

自 C++ 11 起支持使用 **`constexpr`** 定义常量，它的本质就是在编译阶段就确定的值。

定义语法:

```CPP
constexpr 数据类型 常量名称 = 常量的值;
```

constexpr 必须编译期可计算，编译器可将其极限的优化。

使用场景:

- 编译期计算:

```CPP
constexpr int square(int x) {
    return x * x;
}

constexpr int a = square(5);
```

- 数组大小:

```CPP
constexpr int size = 100;
int arr[size];
```

从编译器视角看 const 与 constexpr 的实际区别:

- const 只保证值是只读不能修改的，而无法保证这个值在编译期一定存在。

例如:

```CPP
const int x = rand(); // 合法但 x 的值只有在运行期才知道
```

- constexpr 编译期就必须确定值

例如:

```CPP
constexpr int a = 10; // 能在编译阶段算出来否则直接报错
```

## 如何选择

1. 类型安全 + 普通常量: const
2. 追求性能 / 编译期优化: constexpr
3. 跨平台 / 编译控制: #define

优先级: 在现代 C++ 中，优先选择 constexpr，其次 const，尽量避免使用宏来定义常量。

- 能 constexpr 就 constexpr
- 需要运行时值但不希望修改 → const
- 宏只用于条件编译或平台适配