
## 配置

创建自定义配置有两种方法。

1. 您可以在此目录中创建一个 config.json 文件。
   config.json 文件将覆盖 [default.json](../src/studiolibrary/config/default.json) 文件中的任何键，并将被 git 忽略。

2. 另一种方法是创建一个名为 STUDIO_LIBRARY_CONFIG_PATH 的环境变量。
   该变量的值应为您的 config.json 文件的完整路径。

配置使用 json 文件类型，并基本支持使用 "//" 的注释。

##### 示例：

```javascript
// config.json
{
  // 从根目录开始的最大搜索深度
  "recursiveSearchDepth": 4
}
```