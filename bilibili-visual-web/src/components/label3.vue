<template>
  <div>
    <img id="xxx6" src = "javacrip:;" height = 180px>
  </div>
</template>

<script>
var tempuse = "BV1144y1q7ve";
import Bus from '.././bus.js';
export default {
  name: "label3",
  data() {
    return {};
  },
  methods: {
    ttt(){
      var elem1 = document.getElementById("xxx6");
      elem1.textContent = "...";
      this.draw();
    },
    draw() {
      var elem1 = document.getElementById("xxx6");
      this.$http
        .get("http://131.mollnn.com:5000/api/v/info/" + tempuse + "/", {
          headers: { "Access-Control-Allow-Origin": "*" },
        })
        .then((res) => {
            elem1.setAttribute("src","http://131.mollnn.com:5000/getrc/"+res.data[0].pic);
        });
    },
  },
  mounted() {
    Bus.$on('change',(val)=>{
        tempuse = val;
        this.ttt();
      });
    this.draw();
  },
};
</script>

<style></style>