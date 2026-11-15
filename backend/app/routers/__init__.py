"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import inheritance as router_inheritance
from app.routers import master as router_master
from app.routers import apprentice as router_apprentice
from app.routers import material as router_material
from app.routers import tool as router_tool
from app.routers import workpiece as router_workpiece
from app.routers import procedure as router_procedure
from app.routers import review as router_review
from app.routers import exhibition as router_exhibition
from app.routers import award as router_award
from app.routers import training as router_training
from app.routers import donation as router_donation
from app.routers import partner as router_partner
from app.routers import fund as router_fund
from app.routers import document as router_document
from app.routers import visit as router_visit
from app.routers import quality as router_quality

ROUTERS = [router_inheritance, router_master, router_apprentice, router_material, router_tool, router_workpiece, router_procedure, router_review, router_exhibition, router_award, router_training, router_donation, router_partner, router_fund, router_document, router_visit, router_quality]
