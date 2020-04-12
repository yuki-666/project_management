import Vue from 'vue'
import Router from 'vue-router'
// 导入刚才编写的组件
import AppIndex from '@/components/home/AppIndex'
import Login from '@/components/Login'
import Home from '../components/Home'
import LibraryIndex from '../components/library/LibraryIndex'
import MyIndex from '../components/home/MyIndex'
import MyAuidt from '../components/Audit/Audit_Index'
import ManagerRAuidt from '../components/Audit/Manager_Audit/Manager_r_audit.vue'
import ManagerRWorkTime from '../components/Audit/Manager_Audit/Manager_r_workTime.vue'
import ProDetail from '../components/Project_Details/ProDetail_Index.vue'
// import ProDetailINFO from '../components/Project_Details/ProDetail_Info.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/home',
      name: 'Home',
      component: Home,
      // home页面并不需要被访问
      redirect: '/index',
      children: [
        {
          path: '/ManagerRAuidt',
          name: 'ManagerRAuidt',
          component: ManagerRAuidt,
          meta: {
            requireAuth: true
          }
        },
        {
          path: '/ManagerRWorkTime',
          name: 'ManagerRWorkTime',
          component: ManagerRWorkTime,
          meta: {
            requireAuth: true
          }
        },
        {
          path: '/index',
          name: 'AppIndex',
          component: AppIndex,
          meta: {
            requireAuth: true
          }
        },
        {
          path: '/library',
          name: 'Library',
          component: LibraryIndex,
          meta: {
            requireAuth: true
          }
        },
        {
          path: '/my_audit',
          name: 'MyAuidt',
          component: MyAuidt,
          meta: {
            requireAuth: true
          }
        },
        {
          path: '/project_Detail',
          name: 'ProDetail',
          component: ProDetail,
          meta: {
            requireAuth: true
          }
        },
        {
          path: '/MyIndex',
          name: 'MyIndex',
          component: MyIndex,
          meta: {
            requireAuth: true
          }
        }
      ]
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    }
  ]
})
// export default new Router({
//   mode: 'history',
//   routes: [
//   // 下面都是固定的写法
//     {
//       path: '/login',
//       name: 'Login',
//       component: Login
//     },
//     {
//       path: '/index',
//       name: 'AppIndex',
//       component: AppIndex,
//       meta: {
//         requireAuth: true
//       }
//     }
//   ]
// })
