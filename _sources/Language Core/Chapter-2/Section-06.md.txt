# 类型推导

类型推导是一种能让编译器根据初始化或表达式推断变量类型的机制，它能减少代码冗余，提高可维护性。

C++ 提供了多种类型推导机制：

- auto（C++11）：根据初始化表达式推导变量类型
- decltype（C++11）：根据表达式推导类型，保留完整类型信息
- decltype(auto)（C++14）：结合auto和decltype的特性
- 函数返回类型推导（C++14）
- 结构化绑定（C++17）

## 自动类型推导

自 C++ 11 开始新增 **`auto`** 关键字，主要是用来解决变量在显式指定数据类型可能导致的复杂或冗长,`auto` 的作用是根据初始化表达式自动推导变量的类型

使用语法:

```CPP
auto 变量名称 {值};
```

代码演示:

```CPP
auto x{10};      // int
auto y{3.14};    // double
auto z{'A'};     // char
```

```{attention}

auto 必须设定一个初始值，因为编译器需要通过初始化表达式才能推导出类型

```CPP
auto x; // 编译错误，auto 必须有初始值
```

### auto 与 const、引用的交互

auto 在推导时默认会丢弃 const 属性和引用属性，如果需要保留，需要显式添加。

```CPP
// 常量代码演示
const int a{10};

auto b{a};        // b 的类型是 int（const 被丢弃）
const auto c{a};  // c 的类型是 const int（显式添加 const）
```

处理引用

```CPP
int x{10};
int& ref = x;

auto a{ref};   // a 是 int（引用被丢弃）
auto& b{ref};  // b 是 int&（显式添加 & 保留引用）
```

同时处理 const 和引用

```CPP
const int& cref = x;

auto d{cref};        // d 是 int（const 和引用都被丢弃）
const auto& e{cref}; // e 是 const int&（保留 const 和引用）
```

### 函数返回类型推导

C++14 起，auto 也可以用于推导函数返回类型

```CPP
auto add(int a, int b) {
    return a + b;  // 推导返回类型为 int
}

// 也可以结合 trailing return type
auto multiply(int a, int b) -> int {
    return a * b;
}
```

优点:

- 减少代码冗余
- 提高代码可维护性
- 避免手写类型错误

缺点:

- 可读性下降（类型不直观）
- 容易丢失 const 和引用
- 某些情况下可能导致隐式类型错误

## 表达式类型推导

表达式类型推导 decltype 同样是 C++ 11 引入的关键字，它用于根据表达式本身推导类型，并完整保留类型信息（包括 const 和引用）

使用语法:

```CPP
decltype(表达式) 变量名称;
```

代码演示:

```CPP
int x{10};

decltype(x) y{20}; // y 的类型是 int
```

### decltype 的推导规则

decltype 的推导规则比 auto 更复杂，取决于表达式的形式

1. 如果表达式是标识符或类成员访问，则推导为该实体的类型
2. 如果表达式是函数调用，则推导为函数返回类型
3. 如果表达式是左值表达式（且不是规则 1 的情况），则推导为 T&
4. 如果表达式是纯右值表达式，则推导为 T

代码演示:

```CPP
int x = 10;
int& ref = x;
const int& cref = x;

// 规则1：标识符
decltype(x) a = 20;        // int
decltype(ref) b = x;        // int&
decltype(cref) c = x;       // const int&

// 规则2：函数调用
int func();
decltype(func()) d = 10;     // int

// 规则3：左值表达式（非标识符）
decltype((x)) e = x;         // int&（注意双括号！）
decltype(x = 5) f = x;       // int&（赋值表达式返回左值）

// 规则4：纯右值表达式
decltype(10) g = 20;         // int
decltype(x + 5) h = 20;      // int
```

与 auto 不同的是 decltype 会保留 const 属性。

```CPP
const int a{10};

decltype(a) b{10}; // b 的类型是 const int（完整保留 const）
```

decltype 会完整保留 const 属性，如果赋值不符合 const 要求将导致编译错误。

```CPP
int x{10};

decltype(x) a{x};   // int
decltype((x)) b{x}; // int&（注意双括号，被视为左值表达式）
```

## decltype(auto)（C++14）

C++14 引入了 decltype(auto)，它结合了 auto 的简洁性和 decltype 的类型保留能力

代码演示:

```CPP
int x = 10;
int& ref = x;
const int& cref = x;

decltype(auto) a = x;        // int（类似 auto）
decltype(auto) b = ref;      // int&（保留引用，类似 decltype）
decltype(auto) c = cref;     // const int&（保留 const 和引用）
decltype(auto) d = (x);       // int&（注意双括号，类似 decltype((x))）
```

decltype(auto) 特别适合用于函数返回类型推导，当需要保留引用或 const 属性时

代码演示:

```CPP
// 返回引用
decltype(auto) getRef(int& x) {
    return x;  // 返回 int&
}

// 返回值
decltype(auto) getValue(int x) {
    return x;  // 返回 int
}
```

## 结构化绑定（C++17）

C++17 引入了结构化绑定，可以同时推导多个变量的类型

代码演示:

```CPP
#include <tuple>
#include <map>

std::tuple<int, double, std::string> getPerson() {
    return {25, 75.5, "Alice"};
}

int main() {
    // 结构化绑定，自动推导类型
    auto [age, weight, name] = getPerson();
    
    // 也可以使用 decltype(auto)
    decltype(auto) [a, w, n] = getPerson();
    
    // 与 map 一起使用
    std::map<int, std::string> myMap = {{1, "one"}, {2, "two"}};
    for (const auto& [key, value] : myMap) {
        // key 是 int，value 是 std::string
    }
    
    return 0;
}
```

## auto 与 decltype 对比

| 特性 | auto | decltype |
|------|------|----------|
| 推导依据 | 初始化表达式 | 任意表达式 |
| const 处理 | 默认丢弃 | 完整保留 |
| 引用处理 | 默认丢弃 | 完整保留 |
| 初始化要求 | 必须初始化 | 不需要（仅推导类型） |
| 适用场景 | 变量声明 | 类型推导、泛型编程 |
| 语法复杂度 | 简单 | 较复杂（有特殊规则） |

## 使用建议

- 类型复杂时优先使用 auto：如迭代器、lambda 返回类型、模板类型等
- 类型明显时可直接使用具体类型：如 int、double 等简单类型，提高可读性
- 涉及引用或 const 时使用 decltype：当需要完整保留类型信息时
- 避免在简单场景中滥用 auto：过度使用会降低代码可读性
- C++14 起，考虑使用 decltype (auto)：特别是在函数返回类型推导中
- 注意 auto 与列表初始化的交互：避免意外得到 std::initializer_list
- 使用结构化绑定处理多返回值：C++17 起，这是处理元组、pair 等的优雅方式