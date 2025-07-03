<script setup>
import {ref, onMounted, createApp,} from 'vue'
import moment from 'moment'
import Task from './components/Task.vue'
import FormCreateTask from './components/FormCreateTask.vue'
import FormEditTask from './components/FormEditTask.vue'


const tasks = ref([])
let ascend_Date=true;
let ascend_Prio=true;
let shownCreateTaskForm=ref(false);
let shownEditTaskForm = ref(false)
let editTaskId = ref(null)
let lastSort=ref(0); //0 => Date else=>Prio

async function fetchAll(){
    const response = await fetch('http://localhost:8000/tasks')
    tasks.value = await response.json()
    console.log(lastSort.value);
    console.log(ascend_Date,ascend_Prio);
    sortWrapper(tasks.value,lastSort.value)
    console.log(tasks.value)
}

onMounted(async()=>{
    fetchAll()
});

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

function unmountEditTaskForm() {
  shownEditTaskForm.value = false;
  editTaskId.value = null;
}

async function removeTask(id){
    const response = await fetch(`http://localhost:8000/tasks/${id}`,{method:"DELETE"});
    const out=await response.json()
    const temp=[]
    tasks.value.forEach((task)=>{
            if(task.id != out.id){
                temp.push(task);
                console.log(temp);
            }
        });
    tasks.value=temp;
}


</script>

<template>
    <header class="utilities">
        <div>
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
        <FormCreateTask v-if="shownCreateTaskForm" @close="closeTaskForm" @refresh="fetchAll"/>
    </Suspense>

    <Suspense>
        <FormEditTask v-if="shownEditTaskForm" :id="editTaskId" @close="unmountEditTaskForm" @refresh="fetchAll"/>
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