<script setup>
import { computed, ref } from 'vue';
import moment from 'moment';
    const emit=defineEmits(['close','refresh']);
    const servURL="http://localhost:8000"
    let categories=ref([]);
    let priorities=["Basse","Moyenne","Haute"];
    const response= await fetch(servURL+"/categories");
    categories=await response.json();

    const userInput=ref({
        name:"",
        category:"",
        priority: "",
        date: { day :"", hour: ""},
        desc :""
    })
    const now= ref("");
    now.value= {date:moment().format("YYYY-MM-DD"),time:moment().format("HH:mm")};
    setInterval(()=>{now.value.date=moment().format("YYYY-MM-DD")},1000*60*60);
    setInterval(()=>{now.value.time=moment().format("HH:mm")},1000*60);
    const minHour = computed(() => {
        return moment(userInput.value.date.day,"YYYY-MM-DD",true).isSame(moment(now.value.date,"YYYY-MM-DD",true),"day") ? now.value.time : '00:00'
    })

    async function sendRequest(){
        const newDeadLine=moment(userInput.value.date.day+" "+userInput.value.date.hour,"YYYY-MM-DD HH:mm",true).format("DD/MM/YYYY HH:mm");
        const request={
                            method : "POST",
                            headers: { "Content-Type": "application/json" },
                            body : JSON.stringify({
                                id : userInput.value.id,
                                name : userInput.value.name,
                                category : userInput.value.category,
                                priority : userInput.value.priority,
                                date : newDeadLine,
                                desc : userInput.value.desc
                            })
                        };
        console.log(request)
        await fetch(servURL+"/tasks",request)
        emit('refresh')
        emit('close')
        
    }

</script>
<template>
    <div class="modal">
        <div class="main-window">
            <div class="header">Créer une tâche</div>
            <form @submit.prevent="sendRequest">
                <div>
                    <label for="name">Nom de la tâche: </label>
                    <input type="text" name="name" id="name" required v-model="userInput.name" minlength="3">
                </div>
                <div>
                    <label for="category" name="category" id="category" >Catégorie de la tâche:</label>
                    <select v-model="userInput.category" required>
                        <option disabled value="">Selectionnez une catégorie</option>
                        <option v-for="category,index in categories" :value="index">
                        {{ category }}
                        </option>
                    </select>
                </div>
                <div>
                    <label for="priority" name="priority" id="priority">Priorité :</label>
                    <select v-model="userInput.priority" required>
                        <option disabled value="">Selectionnez une priorité</option>
                        <option v-for="priority,index in priorities" :value="index">
                        {{ priority }}
                        </option>
                    </select>
                </div>
                <div><label for="date" name="date" id="date">Date et Heure :</label>
                    <input type="date" :min="now.date" v-model="userInput.date.day" required>
                    <input type="time" :min="minHour" v-model="userInput.date.hour" required>
                </div>
                <div>
                    <label for="desc" name="desc" id="desc"> Description :</label>
                    <textarea v-model="userInput.desc" placeholder="Vous pouvez écrire une description de votre tâche ici (facultative)"></textarea>
                </div>
                <div>
                    <input type="submit" value="Créer">
                </div>
                
            </form>
        </div>
        <button class="close-window" title="Fermer" @click="$emit('close')">X</button>
    </div>
    
</template>
<style scoped>

    form div{
        font-size: 20px;
        margin: 10px 5px;
        display: flex;
        align-items: center;
    }
    form label{
        width: 20%;
    }
    form input,
    form option,
    form select,
    form textarea{
        font-size: 20px;
        margin: 0px 5px;
        border-radius: 5px;
        border: solid black 1px;
        width: 100%;
    }
    form input:invalid,
    form option:invalid,
    form select:invalid{
        border: solid red 2px
    }

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
        border-radius: 10px;
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