<template>
    <div class="person">
        <h2>一辆{{ car.brand }}, 价值{{ car.price }}万</h2>
        <button @click="changePrice">修改汽车的价格</button>
        <ul>
            <li v-for="g in games" :keys="g.id">{{ g.name }}</li>
        </ul>
        <button @click="changeFirstGame">修改第一个游戏的名字</button>
    </div>
  
</template>
  
<script lang='ts' setup name ="Person">
    import { reactive } from 'vue';

    //数据
    let car = reactive({brand:'奔驰', price:100})
    let games = reactive([
        {id:'sadasa1',name:'1111'},
        {id:'sasass2',name:'2222'},
        {id:'sasas3s',name:'3333'}
    ])
    //方法
    function changePrice(){
        car.price += 10
    }
    function changeFirstGame(){
        games[0].name = '6666'

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