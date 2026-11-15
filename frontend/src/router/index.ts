import { createRouter, createWebHistory } from 'vue-router'

import Dashboard from '@/views/Dashboard.vue'
const Inheritance = () => import('@/views/inheritance/index.vue')
const Master = () => import('@/views/master/index.vue')
const Apprentice = () => import('@/views/apprentice/index.vue')
const Material = () => import('@/views/material/index.vue')
const Tool = () => import('@/views/tool/index.vue')
const Workpiece = () => import('@/views/workpiece/index.vue')
const Procedure = () => import('@/views/procedure/index.vue')
const Review = () => import('@/views/review/index.vue')
const Exhibition = () => import('@/views/exhibition/index.vue')
const Award = () => import('@/views/award/index.vue')
const Training = () => import('@/views/training/index.vue')
const Donation = () => import('@/views/donation/index.vue')
const Partner = () => import('@/views/partner/index.vue')
const Fund = () => import('@/views/fund/index.vue')
const Document = () => import('@/views/document/index.vue')
const Visit = () => import('@/views/visit/index.vue')
const Quality = () => import('@/views/quality/index.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'dashboard', component: Dashboard },
    { path: '/inheritance', name: 'inheritance', component: Inheritance },
    { path: '/master', name: 'master', component: Master },
    { path: '/apprentice', name: 'apprentice', component: Apprentice },
    { path: '/material', name: 'material', component: Material },
    { path: '/tool', name: 'tool', component: Tool },
    { path: '/workpiece', name: 'workpiece', component: Workpiece },
    { path: '/procedure', name: 'procedure', component: Procedure },
    { path: '/review', name: 'review', component: Review },
    { path: '/exhibition', name: 'exhibition', component: Exhibition },
    { path: '/award', name: 'award', component: Award },
    { path: '/training', name: 'training', component: Training },
    { path: '/donation', name: 'donation', component: Donation },
    { path: '/partner', name: 'partner', component: Partner },
    { path: '/fund', name: 'fund', component: Fund },
    { path: '/document', name: 'document', component: Document },
    { path: '/visit', name: 'visit', component: Visit },
    { path: '/quality', name: 'quality', component: Quality },
  ],
})

export default router
