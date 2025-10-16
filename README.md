# CloudFlare IP优选自动化工具

## 功能简介

这是一个自动化的CloudFlare IP优选工具，通过GitHub Actions每3小时自动执行，获取最优的CF IP地址。

## 主要特性

- 🤖 **全自动化**：GitHub Actions定时执行，无需手动干预
- ⚡ **高效优选**：使用在线优选工具进行延迟测试
- 🎯 **精准测试**：专注CF官方列表+443端口组合
- 📊 **智能保存**：自动追加保存优选IP到文件
- 🔄 **双重保障**：主测试+备用收集，确保IP获取

## 工作原理

1. **在线优选**：访问 [https://t1.y130.icu/t1/bestip](https://t1.y130.icu/t1/bestip)
2. **自动测试**：选择CF官方列表+443端口进行延迟测试
3. **结果保存**：自动追加保存优选IP到 `ip.txt` 文件
4. **备用收集**：同时运行传统IP收集作为备份

## 文件说明

- `cf_ip_automation.py` - 主要自动化脚本
- `collect_ips.py` - 备用IP收集脚本
- `requirements.txt` - Python依赖包
- `ip.txt` - 输出文件，包含优选IP列表
- `.github/workflows/auto-update.yml` - GitHub Actions工作流

## 使用方法

### 自动运行（推荐）
1. Fork此仓库到您的GitHub账户
2. 启用GitHub Actions
3. 系统会自动每3小时执行一次

### 手动运行
```bash
# 安装依赖
pip install -r requirements.txt

# 安装Chrome和ChromeDriver
# 参考详细文档

# 运行自动化脚本
python cf_ip_automation.py
```

## 输出格式

```
# CF官方列表优选IP - 2024-01-01 12:00:00
# 获取到 16 个优选IP
# ==================================================
104.18.79.150
104.16.226.60
162.159.48.156
...
```

## 重要提醒

- ⚠️ **关闭代理**：确保未使用代理或VPN，否则测试结果不准确
- ⏱️ **执行时间**：每次执行约3-5分钟
- 🔄 **更新频率**：每3小时自动更新一次

## 详细文档

更多详细信息请参考：[COMBINATIONS_AUTOMATION.md](COMBINATIONS_AUTOMATION.md)

## 许可证

MIT License