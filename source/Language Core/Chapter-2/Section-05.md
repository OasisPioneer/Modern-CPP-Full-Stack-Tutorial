# 类型推导

类型推导是一种能让编译器根据初始化或表达式推断变量类型的机制

## 自动类型推导

自 C++ 11 开始新增 **`auto`** 关键字，主要是用来解决变量在显式指定数据类型可能导致的复杂或冗长,`auto` 的作用是根据初始化表达式自动推导变量的类型

使用语法:

```CPP
auto 变量名称 {值};
```

代码演示:

```CPP
auto x = 10;      // int
auto y = 3.14;    // double
auto z = 'A';     // char
```

```{attention}

auto 必须设定一个初始值，因为编译器需要通过初始化表达式才能推导出类型

```CPP
auto x; // 编译错误，auto 必须有初始值
```

auto 在推导时默认会丢弃 const 属性，如果需要保留常量属性，需要显式添加 const。

```CPP
// 常量代码演示
const int a{10};

auto b{a};        // b 的类型是 int（const 被丢弃）
const auto c{a};  // c 的类型是 const int
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

表达式类型推导 `decltype` 同样是 C++ 11 引入的关键字，它用于根据表达式本身推导类型，并完整保留类型信息

使用语法:

```CPP
decltype(表达式) 变量名称;
```

代码演示:

```CPP
int x{10};

decltype(x) y{20}; // y 的类型是 int
```

与 auto 不同的是 decltype 会保留 const 属性。

```CPP
const int a{10};

decltype(a) b = 10; // b 的类型是 const int
```

decltype 会完整保留 const 属性，如果赋值不符合 const 要求将导致编译错误。

## 使用建议

- 类型复杂时优先使用 auto
- 类型明显时可直接使用具体类型
- 涉及引用或 const 时使用 decltype
- 避免在简单场景中滥用 decltype