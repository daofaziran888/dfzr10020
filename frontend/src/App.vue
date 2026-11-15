<template>
  <div class="app-shell">
    <aside class="app-side">
      <h1 class="app-title">道法自然非遗手工艺传习工坊管理平台</h1>
      <nav class="nav-list">
        <RouterLink v-for="item in navItems" :key="item.path" :to="item.path" class="nav-item">
          {{ item.label }}
        </RouterLink>
      </nav>
    </aside>
    <main class="app-main">
      <header class="app-head">
        <span class="head-desc">面向非遗手工艺传承的师徒带教、材料采备、工序流转、作品评审与工坊展销的一体化传习管理后台。</span>
        <span class="head-user">当前值班：{{ store.operator }} · {{ store.shiftLabel }}</span>
      </header>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { useSessionStore } from '@/stores/session'

const store = useSessionStore()

const navItems = [{ label: "运营概览", path: "/" }, { label: "传承项目", path: "/inheritance" }, { label: "传承人档案", path: "/master" }, { label: "学徒管理", path: "/apprentice" }, { label: "材料采备", path: "/material" }, { label: "工具管理", path: "/tool" }, { label: "作品工序", path: "/workpiece" }, { label: "工序标准", path: "/procedure" }, { label: "作品评审", path: "/review" }, { label: "展销活动", path: "/exhibition" }, { label: "奖项荣誉", path: "/award" }, { label: "培训课程", path: "/training" }, { label: "捐赠收藏", path: "/donation" }, { label: "合作机构", path: "/partner" }, { label: "项目经费", path: "/fund" }, { label: "文献资料", path: "/document" }, { label: "参观接待", path: "/visit" }, { label: "品质抽检", path: "/quality" }]
</script>
