# APP 项目测试

- 瀑布模型： 将一个项目作为整体，下一个环节依赖上一个环节的完成（传统行业）
- 敏捷模型：将一个项目拆分成多个子项目，每一个迭代周期完成一个子项目（现在大多数使用）

# 敏捷开发（scrum) 模型

Scruml: 是一个敏捷的开发框架，是一个增量，迭代的开发过程

- 迭代（sprint) 项目开发过程中最小的周期，每个sprint 周期建议为2-4周  在整个开发周期包括若干个小迭代周期
- 产品功能列表（Backlog)： 在Scruml中，将产品Backlog 按照商业价值排除需求



产品规划产品功能列表（backlog) ---- 产品组织迭代计划会（拆分需求，确认迭代周期）--迭代开发（需求评审\开发\测试）---- 发布评审会（反思会）





## 面试题目

100 台服务器，发布新版本时，一次性更新100台好还，还是更新几台验证一段实时间好？

灰度发布： 由于一个项目，一般线上部署时有多台服务器运行，所有灰度 1台至 3台，看看新功能是否ok 如果失败则只需要回滚几台，比较方便

### app 如何发布？

app软件包的类型

- app 开发完成后，相关的开发人员会打出应用程序包，由测试人员安装测试
- 安卓 xxx.apk  ios  xxx.ipa





# app 项目测试内容介绍

- 功能测试
- 专项测试
- 性能测试

设置用例：

1. 熟悉需求
2. 设计测试点(测试点评审)
3. 编写测试用例（用例评审）