# Open Codex Micro — 简体中文

[English](README.md) · [العربية](README.ar.md) · **简体中文** · [Español](README.es.md)

### 让编程工作流触手可及。

Open Codex Micro 是一个小巧、可维修、开源的宏键盘控制面板，用来把编码
代理和开发工具中的重复操作变成实体按键：启动任务、暂停、批准修改、切换
会话、查看差异，或快速回到终端。

![Open Codex Micro 示意图](docs/assets/open-codex-micro.svg)

## 你将获得

- 13 个可编程按键
- 带按压功能的双轴摇杆
- 带按压功能的旋转编码器
- 可选电容触摸输入
- RGB 状态灯
- 无需专用驱动的 USB HID 输出
- 适用于 Raspberry Pi Pico / RP2040 的 CircuitPython 固件

## 快速开始

1. 阅读[硬件清单与接线说明](hardware/README.md)。
2. 按照[构建检查清单](docs/BUILD-CHECKLIST.md)组装。
3. 将[固件文件](firmware/circuitpython/README.md)复制到 `CIRCUITPY`。
4. 在 [`config.py`](firmware/circuitpython/config.py) 中修改快捷键。

> 第一次通电时请先只连接按键，再逐个添加摇杆、编码器、触摸输入和灯光。
> RP2040 GPIO 不能接入 5V。

这是一个独立的开源项目，不隶属于 OpenAI 或 Work Louder。项目由 **Qusai Al Bahri**
创建，并在构思和审阅过程中使用了 AI 工具协助。

项目主页：[albahri.org](https://albahri.org)


