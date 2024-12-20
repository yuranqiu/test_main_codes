<template>
    <div class="person">
    <h1>情况三:监视【reactive】定义的【对象】数据</h1>
    <h2>姓名：{{ person.name }}</h2>
    <h2>年龄:{{ person.age }}</h2>
    <button @click="changeName">修改名字</button>
    <button @click="changeAge">修改年龄</button>
    <button @click="changePerson">修改对象</button>
    </div>
</template>
  
<script lang='ts' setup name ="Person">
    import {reactive,watch} from 'vue'
    //数据
    let person = reactive({
        name:"zhangsan",
        age:18
    })
    //方法
    function changeName(){
        person.name += '~'
    }
    function changeAge(){
        person.age += 1
    }
    function changePerson(){
       Object.assign(person,{name:'李四', age:90})
    }
    
    //监视,情况三:监视reactive定义的【对象类型】数据，且默认是开启深度监视的
    //watch的第一个参数:被监视的数据，第二个参数:监视的回调,第三个参数:配置对象
    watch(person,(newValue,oldValue)=>{
        console.log('person变化了',newValue,oldValue)
    },{deep:true,immediate:true})
    
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