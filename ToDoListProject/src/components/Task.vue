<script setup>
import moment from 'moment';
import {ref, computed, onMounted} from 'vue'
    const props = defineProps({

        title: {
            type: String,
            required: true,
        },
        date :{
            type : String,
            required: true,
        },
        desc :{
            type : String,
            required : false
        },
        id: {
            type : Number,
            required : true 
        },
        priority: {
            type : Number,
            required : true
        },
        category:{
            type : Number,
            required :true
        }
    })
    let checked= ref(false);

    let showEditBtns= ref(false);
    let categories=ref([]);

    const priorityClass = computed(() => {
        return `priority-${props.priority}`
    })

    const priorityKey = computed(()=>{
        switch (props.priority) {
            case 0:
                return "Priorité Basse"
            case 1:
                return  "Priorité Moyenne"
            case 2: 
                return "Priorité Haute"
            default:
                return "This priority doesn't exist";
        }
    })

    const closeDeadline= computed(()=>{
        return moment(props.date,"DD/MM/YYYY HH:mm",true).diff(moment(),'days') < 2;
    });

    const overdue=computed(()=>{
        return moment(props.date,"DD/MM/YYYY HH:mm",true).diff(moment(),'seconds') <0;;
    })


    onMounted(async()=>{
        const response= await fetch("http://localhost:8000/categories");
        categories=await response.json();
    })

</script>

<template>
    <div class="todo" @mouseenter="showEditBtns=true" @mouseleave="showEditBtns=false">
                <input class="checkbox" type="checkbox" :id="{ id }" v-model="checked" />
                <div class="priority-indicator" :class="priorityClass" :title="priorityKey"></div>
                <div class="details">
                    <div class="title">{{ title }}
                        <div>
                            <img class="category-icon" src="../assets/perso.svg" :title="categories[category]" v-if="category === 0">
                            <img class="category-icon" src="../assets/pro.svg" :title="categories[category]" v-if="category===1">
                            <img class="category-icon" src="/src/assets/medical.svg" :title="categories[category]" v-if="category===2">
                            <img class="category-icon" src="/src/assets/loisir.svg" :title="categories[category]" v-if="category===3">
                        </div>
                    </div>
                    <div class="date" :title="overdue ? 'Deadline Dépassée' : closeDeadline ? 'Deadline Proche' : '' ">{{ date }}
                        <div :class="overdue ? 'overdue' : 'warn'" v-if="closeDeadline" src="../assets/warn.png">
                            !
                        </div>
                    </div>
                    <div class="desc">{{ desc ? desc : " "}}</div>
                </div>
                <div class="modif-btns" v-if="showEditBtns">
                    <button class="edit-btn" title="Modifier" @click="$emit('edit',id)" >
                        <img class="edit-img" src="../assets/edit-button-svgrepo-com.svg">
                    </button>
                    <button class="del-btn" @click="$emit('remove',id)" :id="{ id }" title="Supprimer">X</button>
                </div>
    </div>
</template>

<style scoped>

.category-icon{
    width: 25px;
    height: 25px;
}


.modif-btns{
    display:flex;
    flex-direction: row;
}

.edit-btn{
    background: none;
    border: solid 2px gray;
    border-radius: 5px;
    margin-right: 5px;
    cursor: pointer;
    transition: all 300ms;
}

.edit-btn:hover{
    background-color: gray;
}

.edit-img{
    width: 30px;
    height: 30px;
}

.warn,
.overdue{
    cursor:default;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    width: 25px;
    height: 25px;
    color:white;
    border: solid 2px white ;
    border-radius: 25px;
}

.warn{
    background-color:orange;
}
.overdue{
    background-color:red;
}
.todo{
    max-height: 20vh; 
    height: auto;
    display:flex;
    margin-left: 5vw;
    margin-right: 5vw;
    background-color: white;
    justify-content: space-between;
    box-shadow:  0 4px 20px rgba(0, 0, 0, 0.2);
    border-radius: 10px;
    padding: 2vh 2vw;
    align-items: center;
    overflow: hidden;
    transition: translateY 300ms;
}

.todo .details{
    width: 100%;
    margin-left: 15px;

}

.todo .title{
    font-size: 30px;
    font-weight: 500;
}

.todo .date{
    font-size: 20px;
    font-weight: 200;
}

.todo .desc{
    font-size: 15px;
    font-weight: 100;
    word-wrap: break-word;
}


.todo:hover{
    transform: translateY(-1vh);
}

.todo .del-btn{
    width: 40px;
    height: 40px;
    font-weight: 700;
    font-size: 20px;
    background-color: red;
    color: white;
    border: solid 0px;
    transition: all 300ms;
    border-radius: 5px;
    opacity: 1;
}

.todo .del-btn:hover{
    cursor: pointer;
    background-color: white;
    border: solid 3px red;
    color: red;
}

.checkbox{
    background:none;
    padding: 10px 10px;
    border: solid 2px black;
    cursor: pointer;
    transform: scale(2);

}

.todo .priority-indicator{
    height: 200%;
    width: 10px;
    margin-right: 3px;
    margin-left: 20px;
    border-radius: 5px;
}
.priority-0 {
    background-color: green;
}

.priority-1 {
    background-color: orange;
}

.priority-2 {
    background-color: red;
}
</style> 