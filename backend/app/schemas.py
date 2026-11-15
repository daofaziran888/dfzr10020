"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class InheritanceEntry(BaseModel):
    """技艺项目明细结构。"""

    field_0: str | None = None  # 项目编号
    field_1: str | None = None  # 技艺名称
    field_2: str | None = None  # 所属名录
    field_3: str | None = None  # 传承级别
    field_4: str | None = None  # 代表性传承人
    field_5: str | None = None  # 立项日期
    field_6: str | None = None  # 保护单位
    field_7: str | None = None  # 项目状态

class MasterEntry(BaseModel):
    """传承人明细结构。"""

    field_0: str | None = None  # 传承人编号
    field_1: str | None = None  # 姓名
    field_2: str | None = None  # 技艺门类
    field_3: str | None = None  # 认定级别
    field_4: str | None = None  # 师承关系
    field_5: str | None = None  # 从艺年限
    field_6: str | None = None  # 代表作数量
    field_7: str | None = None  # 档案状态

class ApprenticeEntry(BaseModel):
    """学徒明细结构。"""

    field_0: str | None = None  # 学徒编号
    field_1: str | None = None  # 姓名
    field_2: str | None = None  # 师从何人
    field_3: str | None = None  # 入门日期
    field_4: str | None = None  # 学习阶段
    field_5: str | None = None  # 考核成绩
    field_6: str | None = None  # 出师日期
    field_7: str | None = None  # 学徒状态

class MaterialEntry(BaseModel):
    """原材料明细结构。"""

    field_0: str | None = None  # 材料编号
    field_1: str | None = None  # 材料名称
    field_2: str | None = None  # 材料类别
    field_3: str | None = None  # 产地来源
    field_4: str | None = None  # 采购日期
    field_5: str | None = None  # 采购数量
    field_6: str | None = None  # 存放区域
    field_7: str | None = None  # 品质等级

class ToolEntry(BaseModel):
    """手工工具明细结构。"""

    field_0: str | None = None  # 工具编号
    field_1: str | None = None  # 工具名称
    field_2: str | None = None  # 工具类别
    field_3: str | None = None  # 所属工坊
    field_4: str | None = None  # 保管人员
    field_5: str | None = None  # 保养周期
    field_6: str | None = None  # 使用状态
    field_7: str | None = None  # 最后一次保养

class WorkpieceEntry(BaseModel):
    """在制作品明细结构。"""

    field_0: str | None = None  # 作品编号
    field_1: str | None = None  # 作品名称
    field_2: str | None = None  # 技艺门类
    field_3: str | None = None  # 制作人
    field_4: str | None = None  # 当前工序
    field_5: str | None = None  # 开始日期
    field_6: str | None = None  # 预计完成日
    field_7: str | None = None  # 作品状态

class ProcedureEntry(BaseModel):
    """工序步骤明细结构。"""

    field_0: str | None = None  # 工序编号
    field_1: str | None = None  # 工序名称
    field_2: str | None = None  # 所属技艺
    field_3: str | None = None  # 前置工序
    field_4: str | None = None  # 标准工时
    field_5: str | None = None  # 所需工具
    field_6: str | None = None  # 所需材料
    field_7: str | None = None  # 质量控制点

class ReviewEntry(BaseModel):
    """评审记录明细结构。"""

    field_0: str | None = None  # 评审编号
    field_1: str | None = None  # 评审作品
    field_2: str | None = None  # 评审日期
    field_3: str | None = None  # 评审委员
    field_4: str | None = None  # 工艺评分
    field_5: str | None = None  # 创意评分
    field_6: str | None = None  # 评审意见
    field_7: str | None = None  # 评审结果

class ExhibitionEntry(BaseModel):
    """展销活动明细结构。"""

    field_0: str | None = None  # 活动编号
    field_1: str | None = None  # 活动名称
    field_2: str | None = None  # 活动类型
    field_3: str | None = None  # 举办地点
    field_4: str | None = None  # 开始日期
    field_5: str | None = None  # 结束日期
    field_6: str | None = None  # 参展作品数
    field_7: str | None = None  # 活动状态

class AwardEntry(BaseModel):
    """获奖记录明细结构。"""

    field_0: str | None = None  # 奖项编号
    field_1: str | None = None  # 奖项名称
    field_2: str | None = None  # 获奖作品
    field_3: str | None = None  # 获奖人
    field_4: str | None = None  # 颁奖单位
    field_5: str | None = None  # 获奖日期
    field_6: str | None = None  # 奖项级别
    field_7: str | None = None  # 记录状态

class TrainingEntry(BaseModel):
    """传习课程明细结构。"""

    field_0: str | None = None  # 课程编号
    field_1: str | None = None  # 课程名称
    field_2: str | None = None  # 授课传承人
    field_3: str | None = None  # 课程内容
    field_4: str | None = None  # 课时安排
    field_5: str | None = None  # 学员人数
    field_6: str | None = None  # 开课日期
    field_7: str | None = None  # 课程状态

class DonationEntry(BaseModel):
    """捐赠记录明细结构。"""

    field_0: str | None = None  # 捐赠编号
    field_1: str | None = None  # 捐赠人
    field_2: str | None = None  # 捐赠物品
    field_3: str | None = None  # 物品年代
    field_4: str | None = None  # 评估价值
    field_5: str | None = None  # 接收日期
    field_6: str | None = None  # 存放位置
    field_7: str | None = None  # 捐赠状态

class PartnerEntry(BaseModel):
    """合作单位明细结构。"""

    field_0: str | None = None  # 机构编号
    field_1: str | None = None  # 机构名称
    field_2: str | None = None  # 合作方向
    field_3: str | None = None  # 联系人
    field_4: str | None = None  # 联系电话
    field_5: str | None = None  # 签约日期
    field_6: str | None = None  # 合作期限
    field_7: str | None = None  # 合作状态

class FundEntry(BaseModel):
    """经费项目明细结构。"""

    field_0: str | None = None  # 项目编号
    field_1: str | None = None  # 经费来源
    field_2: str | None = None  # 批准金额
    field_3: str | None = None  # 已拨付金额
    field_4: str | None = None  # 已使用金额
    field_5: str | None = None  # 经费周期
    field_6: str | None = None  # 负责人
    field_7: str | None = None  # 经费状态

class DocumentEntry(BaseModel):
    """技艺文献明细结构。"""

    field_0: str | None = None  # 文献编号
    field_1: str | None = None  # 文献名称
    field_2: str | None = None  # 文献类型
    field_3: str | None = None  # 所属技艺
    field_4: str | None = None  # 作者/采集人
    field_5: str | None = None  # 录入日期
    field_6: str | None = None  # 文献载体
    field_7: str | None = None  # 文献状态

class VisitEntry(BaseModel):
    """来访记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 来访单位
    field_2: str | None = None  # 来访人数
    field_3: str | None = None  # 来访目的
    field_4: str | None = None  # 接待人员
    field_5: str | None = None  # 来访日期
    field_6: str | None = None  # 参观路线
    field_7: str | None = None  # 接待状态

class QualityEntry(BaseModel):
    """抽检记录明细结构。"""

    field_0: str | None = None  # 抽检编号
    field_1: str | None = None  # 抽检对象
    field_2: str | None = None  # 抽检日期
    field_3: str | None = None  # 检测维度
    field_4: str | None = None  # 检测结果
    field_5: str | None = None  # 检测人员
    field_6: str | None = None  # 不合格项
    field_7: str | None = None  # 抽检状态
