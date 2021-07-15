<template>
  <!-- 
  <h2 id="xxx1">4,332</h2>
  <h6 id="xxx2">+830</h6> -->
  <div>
    <div class="d-flex justify-content-between align-items-center mb-lg">
      <h2 id="xxx100">0</h2>
      <i class="la la-arrow-right text-primary la-lg rotate-315" />
    </div>
    <div class="d-flex flex-wrap justify-content-between">
      <div class="mt">
        <h6 id="xxx101">0</h6>
        <p class="text-muted mb-0 mr"><small>视频总数</small></p>
      </div>
      <div class="mt">
        <h6 id="xxx102">0</h6>
        <p class="text-muted mb-0"><small>总弹幕数</small></p>
      </div>
      <div class="mt">
        <h6 id="xxx103">0</h6>
        <p class="text-muted mb-0 mr"><small>总点赞数</small></p>
      </div>
    </div>
  </div>
</template>


<script>
// var tempuse = "BV1144y1q7ve";
// import Bus from '.././bus.js';
export default {
  name: "label6",
  data() {
    return {
    //   val:'',
    };
  },
  methods: {
    // ttt(){
    //   var elem4 = document.getElementById("xxx100");
    //   elem4.textContent = tempuse;
    //   this.draw();
    // },
    draw() {
      var elem1 = document.getElementById("xxx100");
      var elem2 = document.getElementById("xxx101");
      var elem3 = document.getElementById("xxx102");
      var elem4 = document.getElementById("xxx103");
      this.$http
        .get("http://131.mollnn.com:5000/api/sum/", {
          headers: { "Access-Control-Allow-Origin": "*" },
        })
        .then((res) => {
          elem1.textContent = res.data[0].sview;
          elem2.textContent = res.data[0].scnt;
          elem3.textContent = res.data[0].sdanmaku;
          elem4.textContent = res.data[0].slikes;
        });
    },
  },
    //   created (){
    //     Bus.$on('change',(val)=>{
    //     alert("fsadfads");
    //     this.val = val;
    //   });
    // },
  mounted() {
    // var that = this;      
    // Bus.$on('change',(val)=>{
    //     tempuse = val;
    //     this.ttt();
    //   });
    this.draw();
  },
};
</script>

<style></style>