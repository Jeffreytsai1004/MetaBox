
## Config

有两种方法可以创建自定义配置。

1. 您可以在此目录中创建一个 config.json 文件。
   config.json 文件将覆盖 [default.json](../src/studiolibrary/config/default.json) 文件中的任何键，并将被 git 忽略。

2. 另一种方法是创建一个名为 STUDIO_LIBRARY_CONFIG_PATH 的环境变量。该变量的值应为 config.json 文件的完整路径。

配置使用 json 文件类型，基本支持使用 "//" 进行注释。

##### Example：

```javascript
// config.json
{
  // The maximum walking depth from the root directory
  "recursiveSearchDepth": 4
}
```
