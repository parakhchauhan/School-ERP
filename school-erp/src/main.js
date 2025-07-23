import { createApp } from 'vue';
import App from './App.vue';
import './assets/tailwind.css';
import router from './router';
import { AllCommunityModule, ModuleRegistry } from 'ag-grid-community'; 
import 'ag-grid-community/styles/ag-grid.css'
import 'ag-grid-community/styles/ag-theme-alpine.css'

// Register all Community features
ModuleRegistry.registerModules([AllCommunityModule]);


// createApp(App).mount('#app')
const app = createApp(App);
app.use(router);
app.mount('#app');

