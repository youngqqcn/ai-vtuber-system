## 效果展示
- Youtube直播回放: https://www.youtube.com/watch?v=SoXnqO0KOpo&ab_channel=yqqyoung

![](https://raw.githubusercontent.com/youngqqcn/repo4picgo/master/img/vtuber_cami.jpg)


## 技术方案
> 原始项目: https://github.com/AIVTDevPKevin/AI-VTuber-System

![](https://raw.githubusercontent.com/youngqqcn/repo4picgo/master/img/ai-vtuber-output.jpg)

- 硬件配置
  - GPU 是必须的， VTube Studio 和 OBS 都需要用到显卡进行视频渲染
  - 外网服务器(Windows)
    - 要做7*24直播，最好使用境外Windows服务器,延迟低,直播稳定

- 实施步骤
  - 使用Live2D软件制作VTuber的形象模型
    - Live2D: https://www.live2d.com/zh-CHS/
    - Live3D:https://live3d.io/
    - 可以使用AI工具：https://www.phot.ai/ai-vtuber-maker
  - 用 VTube Studio 录制视频
  - 接入大模型
  - 接入 TTS 文本转语音，将回复的文本转为语音，自动播放，并与视频画面融合
    - 使用OBS
  - 制作直播字幕（透明的），背后循环播放视频
    - 使用OBS(Websocket字幕)
    - 也可以使用 streamlabs的插件
    - https://streamlabs.com/
  - Youtube/Twitch直播

- 开源方案：AI-VTuber-System
  - https://github.com/AIVTDevPKevin/AI-VTuber-System
    - 文档：https://docs.google.com/document/d/1na16cbaTVYin16BhvMQmeYYAZPwSyCoQ9sfcie3K-FQ/

- 其他方案
  - https://github.com/Ikaros-521/AI-Vtuber
  - https://github.com/Open-LLM-VTuber/Open-LLM-VTuber
  - https://github.com/ardha27/AI-Waifu-Vtuber
  - https://github.com/worm128/AI-YinMei


- Live2D模型资源：
  - 翠虚俙伶(白色女巫) Live2D 動畫設定檔&表情配置文件 Animation&Expression configuration files
    - https://drive.google.com/file/d/1GeiQ1aAaDv-ud5Lk7qiySvlZ04szMAC7/view?usp=sharing
  - https://github.com/Eikanya/Live2d-model


- 示例Twich直播
  - https://www.twitch.tv/cowi


----

# AI-VTuber-System
A graphical system program that allows you to quickly create your own AI VTuber for free.
![00_程式視窗](https://github.com/AIVTDevPKevin/AI-VTuber-System/assets/161304793/6f3bbb2b-a2f2-46b0-b1ce-49e47a7ae285)

## Tutorial Video
https://www.youtube.com/watch?v=Hwss_p2Iroc

## User Manual
https://docs.google.com/document/d/1na16cbaTVYin16BhvMQmeYYAZPwSyCoQ9sfcie3K-FQ/edit?usp=sharing

## Installation Guide
Python >= 3.8, install the main dependencies:
```
pip3 install -r requirements.txt
```
For the specific PyTorch packages which require a special handling, use the following command:
```
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```
## Nvidia
Latest GPU Driver
https://www.nvidia.com.tw/Download/index.aspx?lang=tw

CUDA Toolkit 12.1.1
https://developer.nvidia.com/cuda-12-1-1-download-archive

cuDNN
https://developer.nvidia.com/cudnn-downloads

## Whisper Model Download Links
tiny.en: https://openaipublic.azureedge.net/main/whisper/models/d3dd57d32accea0b295c96e26691aa14d8822fac7d9d27d5dc00b4ca2826dd03/tiny.en.pt

tiny: https://openaipublic.azureedge.net/main/whisper/models/65147644a518d12f04e32d6f3b26facc3f8dd46e5390956a9424a650c0ce22b9/tiny.pt

base.en: https://openaipublic.azureedge.net/main/whisper/models/25a8566e1d0c1e2231d1c762132cd20e0f96a85d16145c3a00adf5d1ac670ead/base.en.pt

base: https://openaipublic.azureedge.net/main/whisper/models/ed3a0b6b1c0edf879ad9b11b1af5a0e6ab5db9205f891f668f8b0e6c6326e34e/base.pt

small.en: https://openaipublic.azureedge.net/main/whisper/models/f953ad0fd29cacd07d5a9eda5624af0f6bcf2258be67c92b79389873d91e0872/small.en.pt

small: https://openaipublic.azureedge.net/main/whisper/models/9ecf779972d90ba49c06d968637d720dd632c55bbf19d441fb42bf17a411e794/small.pt

medium.en: https://openaipublic.azureedge.net/main/whisper/models/d7440d1dc186f76616474e0ff0b3b6b879abc9d1a4926b7adfa41db2d497ab4f/medium.en.pt

medium: https://openaipublic.azureedge.net/main/whisper/models/345ae4da62f9b3d59415adc60127b97c714f32e89e936602e85993674d08dcb1/medium.pt

large-v1: https://openaipublic.azureedge.net/main/whisper/models/e4b87e7e0bf463eb8e6956e646f1e277e901512310def2c24bf0e11bd3c28e9a/large-v1.pt

large-v2: https://openaipublic.azureedge.net/main/whisper/models/81f7c96c852ee8fc832187b0132e569d6c3065a3252ed18e56effd0b6a73e524/large-v2.pt

large-v3: https://openaipublic.azureedge.net/main/whisper/models/e5b1a55b89c1367dacf97e3e19bfd829a01529dbfdeefa8caeb59b3f1b81dadb/large-v3.pt
