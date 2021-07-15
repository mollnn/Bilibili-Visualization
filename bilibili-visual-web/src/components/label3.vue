<template>
  <div>
    <img id="xxx6" src = "javacrip:;">fuck>
  </div>
</template>

<script>
export default {
  name: "label3",
  data() {
    return {};
  },
  methods: {
    draw() {
      var elem1 = document.getElementById("xxx6");
      this.$http
        .get("http://131.mollnn.com:5000/api/v/info/BV1144y1q7ve/", {
          headers: { "Access-Control-Allow-Origin": "*" },
        })
        .then((res) => {
            elem1.setAttribute("src",res.data[0].pic);
        //   elem1.src = res.data[0].pic;
        });
    },
  },
  mounted() {
    this.draw();
  },
};
</script>

<style></style>