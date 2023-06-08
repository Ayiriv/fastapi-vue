import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue';
import RegisterView from '@/views/RegisterView.vue';
import LoginView from '@/views/LoginView.vue';
import DashboardView from '@/views/DashboardView.vue';
import ProfileView from '@/views/ProfileView.vue';
import NoteView from '@/views/NoteView.vue';
import EditNoteView from '@/views/EditNoteView.vue';
import PharmacyView from '@/views/PharmacyView.vue';
import AddPharmacy from '@/views/AddPharmacyView.vue';
import EditPharmacy from '@/views/EditPharmacyView.vue';
import SearchView from '@/views/SearchView.vue';
import MedicineView from '@/views/MedicineView.vue';
import EditOnsale from '@/views/EditOnsaleView.vue';
import AddOnsaleMedicine from '@/views/AddOnSaleMedicineView.vue';
import EditPresale from '@/views/EditPresaleView.vue';
import AddPresaleMedicine from '@/views/AddPreSaleMedicineView.vue';
import store from '@/store'; // NEW


const routes = [
  {
    path: '/',
    name: "Home",
    component: HomeView,
  },
  {
    path: '/register',
    name: 'Register',
    component: RegisterView,
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginView,
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: DashboardView,
    meta: { requiresAuth: true },
  },
  {
    path: '/pharmacy',
    name: 'Pharmacy',
    component: PharmacyView,
    meta: { requiresAuth: true },
  },
  {
    path: '/profile',
    name: 'Profile',
    component: ProfileView,
    meta: { requiresAuth: true },
  },
  {
    path: '/note/:id',
    name: 'Note',
    component: NoteView,
    meta: { requiresAuth: true },
    props: true,
  },
  {
    path: '/editnote/:id',
    name: 'EditNote',
    component: EditNoteView,
    meta: { requiresAuth: true },
    props: true,
  },
  {
    path: '/editpharmacy/:id',
    name: 'EditPharmacy',
    component: EditPharmacy,
    meta: { requiresAuth: true },
    props: true,
  },
  {
    path: '/addpharmacy',
    name: 'AddPharmacy',
    component: AddPharmacy,
    meta: { requiresAuth: true },
  },
  {
    path: '/search/:type/:query',
    name: 'Search',
    component: SearchView,
  },
  {
    path: '/medicine/:id',
    name: 'Medicine',
    component: MedicineView,
    meta: { requiresAuth: true },
  },
  {
    path: '/editonsale/:id',
    name: 'EditOnsale',
    component: EditOnsale,
    meta: { requiresAuth: true },
    props: true,
  },
  {
    path: '/addonsalemedicine/:id',
    name: 'AddOnsaleMedicine',
    component: AddOnsaleMedicine,
    meta: { requiresAuth: true },
  },
  {
    path: '/editpresale/:id',
    name: 'EditPresale',
    component: EditPresale,
    meta: { requiresAuth: true },
    props: true,
  },
  {
    path: '/addpresalemedicine/:id',
    name: 'AddPresaleMedicine',
    component: AddPresaleMedicine,
    meta: { requiresAuth: true },
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to, _, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (store.getters.isAuthenticated) {
      next();
      return;
    }
    next('/login');
  } else {
    next();
  }
});

export default router;
