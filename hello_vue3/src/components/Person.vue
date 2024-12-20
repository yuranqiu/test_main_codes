<template>
    <div class="person">
    <h1>情况三:监视【reactive】定义的【对象】数据</h1>
    <h2>姓名：{{ person.name }}</h2>
    <h2>年龄:{{ person.age }}</h2>
    <h2>汽车:{{ person.car.c1}}、{{ person.car.c2 }}</h2>
    <button @click="changeName">修改名字</button>
    <button @click="changeAge">修改年龄</button>
    <button @click="changeC1">修改第一台车</button>
    <button @click="changeC2">修改第二台车</button>
    <button @click="changeCar">修改整个车</button>
    </div>
</template>
  
<script lang='ts' setup name ="Person">
    import {reactive,watch} from 'vue'
    //数据
    let person = reactive({
        name:"张三",
        age:18,
        car:{
            c1:'bench',
            c2:'bmw'
        }
    })
    //方法
    function changeName(){
        person.name += '~'
    }
    function changeAge(){
        person.age += 1
    }
    function changeC1(){
       person.car.c1 = 'aodi'
    }
    function changeC2(){
       person.car.c2 = 'auto'
    }
    function changeCar(){
        person.car = {c1:'雅迪',c2:'艾玛'}
    }
    
    //监视,情况四:监视响应式对象中的某个属性，且该属性是基本类型，要写成函数式
    //watch的第一个参数:被监视的数据，第二个参数:监视的回调,第三个参数:配置对象
    watch(()=>person.car,(newValue,oldValue)=>{
        console.log('person.car变化了',newValue,oldValue)
    },{deep:true})
    
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