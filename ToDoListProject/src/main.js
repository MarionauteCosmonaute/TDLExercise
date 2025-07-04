import './assets/main.css'
import { createApp } from 'vue'
import ToDoList from './ToDoList.vue'
import Toast from 'vue-toastification'
import 'vue-toastification/dist/index.css'



const app=createApp(ToDoList);
app.mount('#todolist');
app.use(Toast,
    {transition: "Vue-Toastification__bounce",
    maxToasts: 5,
    newestOnTop: true
    });
