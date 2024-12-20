<template>
    <div class="person">

    </div>
</template>
  
<script lang='ts' setup name ="Person">
    import {ref} from 'vue'
    import { type PersonInter,type Persons } from '@/types';


    let person:PersonInter = {id:'232321323',name:'张三',age:60}

    let PersonList:Persons = [
        {id:'232321323',name:'张三',age:60},
        {id:'232321323',name:'张三',age:60},
        {id:'232321323',name:'张三',age:60}
    ]
</script>
  
<style>
    .person{
      background-color: aliceblue;
      box-shadow: 0 0 10px;
      border-radius: 10px;
      padding: 20px;
    }
    button{
        margin: 0 10px;
    }
   
</style>