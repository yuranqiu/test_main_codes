<template>
    <div class="person">
      <h2>姓名:{{ name }}</h2>
      <h2>年龄:{{ age }}</h2>
      <button @click="changeName">修改名字</button>
      <button @click="changeAge">修改年龄</button>
      <button @click="showTel">查看联系方式</button>
    </div>
  
  </template>
  
  <script>
    export default{
      name:'Person',
      setup(){
        //数据
        let name = '张三'
        let age = 18
        let tel = '11231564564'
        
        //方法
        function changeAge(){
            name = 'zhang-san'
        }
        function changeName(){
            age += 1  
        }
        function showTel(){
            alert(tel)
        }

        return {name,age,changeAge,changeName,showTel}
      }
      
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
        margin:0 5px;
    }
   
  </style>