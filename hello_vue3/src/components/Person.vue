<template>
    <div class="person">
      <h2>姓名:{{ name }}</h2>
      <h2>年龄:{{ age }}</h2>
      <h2>地址:{{ address }}</h2>
      <button @click="changeAge">修改年龄</button>
      <button @click="changeName">修改姓名</button>
      <button @click="showTel">查看联系方式</button>
    </div>
  
  </template>
  
    <script lang='ts' setup name ="Person">
    import {ref} from 'vue'

    //数据
    let name = ref('张三')
    let age = ref(18)
    let tel = '1564156156'
    let address = '北京市'

    //方法
    function changeName() {
        name.value = 'zhang-san'
    }
    function changeAge() {
        age.value += 1
    }
    function showTel() {
        alert(tel)
    }
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