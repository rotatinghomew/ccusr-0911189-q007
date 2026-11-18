# captions · 图书馆片头字幕抽看与发行版对照

使用 Python 3.11 标准库，不需要联网、第三方包或数据库。输入示例使用本地合成记录。

```sh
python3 -m captions intake data/sample.json
python3 -m unittest discover -s tests -v
```

输出为 UTF-8 JSON。输入文件不可读、业务引用无效或记录不符合口径时退出码为 2，同时报告原因。

## 记录口径

`editions` 的 `caption` 和 `revision` 标识实际引用的资源和稿次，`clip` 是字幕时轴上左闭右开的毫秒区间；冻结发行版标记 `frozen`。
`draws` 是按抽看计划抽中的发行版，记录 `stratum` 与 `probability`；`verification` 可以是 missing、clean 或 defect。抽看计划内各层独立，以发行版为抽样单元，层内等概率无放回；`frame` 记录分层规模。视频复用同一资源不代表抽中同一个发行版。`findings` 是缺陷区间；`complaints` 是主动报障，`views` 为按当时发行版确认的累计观看秒数。
