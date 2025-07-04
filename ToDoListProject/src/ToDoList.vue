<script setup>
import {ref, onMounted, createApp,} from 'vue'
import moment from 'moment'
import Task from './components/Task.vue'
import FormCreateTask from './components/FormCreateTask.vue'
import FormEditTask from './components/FormEditTask.vue'
import { useToast } from "vue-toastification";

const toast=useToast();
const tasks = ref([]);
let ascend_Date=true;
let ascend_Prio=true;
let shownCreateTaskForm=ref(false);
let shownEditTaskForm = ref(false);
let editTaskId = ref(null);
let lastSort=ref(0); //0 => Date else=>Prio
let filterBy=ref([])
let categories=ref([]);
let priorities=["Basse","Moyenne","Haute"];
let filterValuesCategory=ref([]);
let filterValuesPriority=ref([]);
let tasksUnfiltered=[];

async function fetchAll(){
    const response = await fetch('http://localhost:8000/tasks')
    tasks.value = await response.json();
    sortWrapper(tasks.value,lastSort.value);

}


function sortWrapper(list,methodId){
    console.log(lastSort.value);
    console.log(ascend_Date,ascend_Prio);
    list.sort(methodId === 0 ? sortbyDate : sortbyPriority);
    lastSort.value=methodId;
}

function sortbyDate(a,b){
    console.log("sort by Date" + ascend_Date ? "asc" : "desc")
    const A=moment(a.date,"DD/MM/YYYY HH:mm",true);
    const B=moment(b.date,"DD/MM/YYYY HH:mm",true);
    if(A.isBefore(B,"second")){
        return ascend_Date ? -1 : 1;
    }else{
        if(A.isSame(B,"second")){
            return 0;
        }
        return ascend_Date ? 1 : -1;
    }
}

function sortbyPriority(a,b){
    console.log("sort by Date" + ascend_Date ? "asc" : "desc")
    const A=a.priority;
    const B=b.priority;
    if (A<B){
        return ascend_Prio ? -1 : 1;

    }else{
        if(A === B){
            return 0
        }
        return ascend_Prio ? 1: -1;
    }
}

function showCreateTaskForm(){
    shownCreateTaskForm.value=true;
}
function closeTaskForm(){
    shownCreateTaskForm.value=false;
}

function mountEditTaskForm(id) {
  shownEditTaskForm.value = true;
  editTaskId.value = id;
}

function closeEditTaskForm() {
  shownEditTaskForm.value = false;
  editTaskId.value = null;
}

async function removeTask(id){
    const response = await fetch(`http://localhost:8000/tasks/${id}`,{method:"DELETE"});
    const out=await response.json();
    const temp=[];
    tasks.value.forEach((task)=>{
            if(task.id != out.id){
                temp.push(task);
                console.log(temp);
            }
        });
    tasks.value=temp;
    successNotify("Tâche supprimée");
}

function successNotify(msg){
    toast.success(msg+" avec succès", {
    position: "bottom-left",
    timeout: 5000,
    closeOnClick: true,
    pauseOnFocusLoss: true,
    pauseOnHover: true,
    draggable: true,
    draggablePercent: 0.6,
    showCloseButtonOnHover: false,
    hideProgressBar: false,
    closeButton: "button",
    icon: true,
    rtl: false
});
}

function created(name){
    fetchAll();
    successNotify(name+" crée");
}

function edited(name){
    fetchAll();
    successNotify(name+" modifié");
}

function applyFilters(){
    if(tasksUnfiltered.length === 0){
        tasksUnfiltered=tasks.value;
    }
    tasks.value=[];
    tasks.value=tasksUnfiltered.filter((task)=>validedByFilters(task))
    successNotify("Filtres appliqués");
}

function removeFilters(){
    tasks.value=tasksUnfiltered;
    tasksUnfiltered=[];
    filterBy=ref([]);
    filterValuesCategory=ref([]);
    filterValuesPriority=ref([]);
    successNotify("Suppression des filtres effectuée");
}

function validedByFilters(task){
    return (!filterBy.value.includes("category") || 
            filterBy.value.includes("category") && filterValuesCategory.value.includes(task.category)) 
            && 
            (!filterBy.value.includes("priority") ||
            filterBy.value.includes("priority") && filterValuesPriority.value.includes(task.priority));
            
}

onMounted(async()=>{
    fetchAll();
    const response= await fetch("http://localhost:8000/categories");
    categories=await response.json();
});

</script>

<template>
    
    <header class="utilities">
        <div class="options">
            <div>Trier par:</div>
            <select>
                <option @click="lastSort === 0 ?
                            ascend_Date = !ascend_Date : ascend_Date =ascend_Date;
                            sortWrapper(tasks,0);">Date {{ ascend_Date ?  "↓" : "↑"}}</option>
                <option @click="lastSort === 1 ?
                            ascend_Prio = !ascend_Prio : ascend_Prio = ascend_Prio;
                            sortWrapper(tasks,1); ">Priorité {{ ascend_Prio ? "↓" : "↑" }}</option>
            </select>
        </div>
        <div class="options">
            <div>Filtres :</div>
            <input type="checkbox" v-model="filterBy" value="category" id="category"><label for="category">Catégories</label>
            <input type="checkbox" v-model="filterBy" value="priority" id="priority"><label for="priority">Priorités</label>
        </div>
        <div class="options" v-if="filterBy.includes('category')">
            <div>Catégories:</div>
            <div v-for="category,index in categories" class="filter-options">
                <input type="checkbox" v-model="filterValuesCategory" :id="category" :value="index">
                <label :for="category">{{ category }}</label>
            </div>
        </div>
        <div class="options" v-if="filterBy.includes('priority')">
            <div>Priorités:</div>
            <div v-for="priority,index in priorities" class="filter-options">
                <input type="checkbox" v-model="filterValuesPriority" :id="priority" :value="index">
                <label :for="priority">{{ priority }}</label>
            </div>
        </div>
        <button v-if="filterBy.length>0" @click="applyFilters">Appliquer</button>
        <button v-if="tasksUnfiltered.length!=0" @click="removeFilters">Supprimer filtres</button>
    </header>
    <div class="todolist">
        <Task @edit="mountEditTaskForm"
            @remove="removeTask"
            v-for="task in tasks"
            :id="task.id"
            :title="task.name"
            :date="task.date"
            :desc="task.desc"
            :priority="task.priority"

            
        />
    </div>
    <button class="add-task-show-form" @click="showCreateTaskForm" title="Créer une nouvelle tâche">+</button>
    <Suspense>
        <FormCreateTask v-if="shownCreateTaskForm" @close="closeTaskForm" @refresh="created"/>
    </Suspense>

    <Suspense>
        <FormEditTask v-if="shownEditTaskForm" :id="editTaskId" @close="closeEditTaskForm" @refresh="edited"/>
    </Suspense>
</template>

<style scoped>
.add-task-show-form{
    z-index: 1;
    position: absolute;
    bottom: 5vh;
    right: 5vw;
    font-size: 40px;
    width: 70px;
    height: 70px;
    border-radius: 10px;
    background-color: rgb(55, 55, 158);
    color: white;
    border: none;
    transition: all 300ms;
    cursor: pointer;
}

.add-task-show-form:hover{
    background-color: white;
    color: rgb(55, 55, 158);
    border: solid rgb(55, 55, 158) 3px;
}

.utilities{
    display: flex;
    flex-direction: row;
    font-size: 20px;
    align-content: center;
    position:absolute;
    top:0;
    left:0;
    width: 100%;
    padding-left: 10px;
    padding-right: 10px;
    z-index: 1;
    background-color: white;
    height: 10vh;
    box-shadow:  0 2px 5px rgba(0, 0, 0, 0.1); ;
}

.utilities .options{
    margin: 0px 10px;
}

.utilities .options .filter-options{
    display: inline;
}

.utilities select{
    font-size: 20px;
    
}
.todolist{
    padding-top: 12vh;
    width: 100vw;
    height: 100vh;
    position: relative;
    top: 0;
    left: 0;
    bottom: 0;
    right: 0;
    background-color: antiquewhite;
    display: grid;
    grid-template-columns: 1fr;
    grid-auto-rows: min-content;
    gap: 2vh; 
    overflow-y: scroll;
}
</style>