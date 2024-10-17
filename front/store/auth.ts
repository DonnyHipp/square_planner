// import { defineStore } from 'pinia';
//
// import type { ApiAccountStatusOutSchema } from '~/@types/api';
//
// export const useAccountStore = defineStore('account', () => {
//     const { $api } = useNuxtApp();
//
//     const state = ref<ApiAccountStatusOutSchema>({
//         client_id: null,
//         is_authenticated: false,
//         username: '',
//         user_id: null,
//     });
//
//     const isAuthVerified = ref(false);
//
//     const setAccountData = (payload: ApiAccountStatusOutSchema) => {
//         state.value = payload;
//     };
//
//     const getStatusUser = async () => {
//         try {
//             const data = await $api.account(api => api.checkAuthorization());
//
//             setAccountData(data);
//
//             isAuthVerified.value = true;
//         } catch (err) {
//             console.warn('[Account] getStatusUser: request failed ', err);
//         }
//     };
//
//     return {
//         account: computed(() => state.value),
//         isAuthorized: computed(() => state.value.is_authenticated),
//         userId: computed(() => state.value.user_id),
//         userName: computed(() => state.value.username),
//         clientId: computed(() => state.value.client_id),
//
//         isAuthVerified: computed(() => isAuthVerified.value),
//
//         getStatusUser,
//     };
// });
