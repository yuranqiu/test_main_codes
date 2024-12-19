<template>
    <div class="person">
    姓: <input type="text" v-model="firstName"> <br>
    名: <input type="text" v-model="lastName"> <br>
    全名: <span>{{fullName }}</span>
    <button @click="changeFullName">将全名修改为li -si</button>
    </div>
</template>
  
<script lang='ts' setup name ="Person">
    import {ref,computed} from 'vue'

    let firstName = ref('张')
    let lastName = ref('三')

    //此计算属性无法修改，是只读的
    // let fullName = computed(()=>{
    //     return firstName.value.slice(0,1).toUpperCase() + firstName.value.slice(1) + '-' + lastName.value
    // })

    //如此的计算属性是可以进行修改的，可读可写的。
    let fullName = computed({
       get(){
        return firstName.value.slice(0,1).toUpperCase() + firstName.value.slice(1) + '-' + lastName.value 
       },
       set(val){
        const [str1,str2] = val.split('-')
        firstName.value = str1
        lastName.value = str2
       }
        
    })

    function changeFullName(){
        fullName.value ='li-si'
    }
</script>
  
<style scoped>
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