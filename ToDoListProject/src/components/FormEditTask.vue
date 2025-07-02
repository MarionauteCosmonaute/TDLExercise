<script setup>
import { computed, onMounted, ref } from 'vue';

const props=defineProps({
    id:{
        type : Number,
        required: true
    }
});
const task=ref(null);

const response = await fetch('http://localhost:8000/tasks/'+props.id);
task.value = await response.json()
console.log(task.value);


</script>
<template>
    <div class="modal">
        <div class="main-window">
            <div class="header">Modifier une tâche</div>
            <form>

            </form>
        </div>
        <button class="close-window" title="Fermer" @click="$emit('close')">X</button>
    </div>
</template>

<style scoped>
    .modal{
        position: fixed;
        top: 0; left: 0; right: 0; bottom: 0;
        background: rgba(0,0,0,0.5);
        z-index: 2;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .main-window{
        position: absolute;
        border: solid 10px rgb(55, 55, 158);
        width: 80vw;
        height: 80vh;
        overflow-y: scroll;
        top: 10vh;
        left: 10vw;
        background-color: white;
        z-index: 2;
        border-radius: 10px
    }

    .header{
        background-color: rgb(55, 55, 158);
        width: 100%;
        height: 10%;
        color: white;
        align-content: center;
        text-align: center;
        font-size: 30px;
        font-weight: 700;
    }

    .close-window{
        position: absolute;
        top: 8vh;
        right: 9vw;
        z-index: 3;
        border: none;
        background-color: black;
        color:white;
        width: 60px;
        height: 60px;
        cursor: pointer;
        font-size: 30px;
        font-weight: 700;
        border-radius: 80px;
        transition: all 300ms;
    }
    .close-window:hover{
        background-color: white;
        border: solid 3px red;
        color: red;
    }
</style>

