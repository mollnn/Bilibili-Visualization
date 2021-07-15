<template>
  <div>
    <h2 id="xxx5" class="text-muted mb-0 mr" style = "font-size : 13px"><small>fuck</small></h2>
  </div>
</template>

<script>
export default {
  name: "label2",
  data() {
    return {};
  },
  methods: {
    draw() {
      var elem1 = document.getElementById("xxx5");
      this.$http
        .get("http://131.mollnn.com:5000/api/v/info/BV1144y1q7ve/", {
          headers: { "Access-Control-Allow-Origin": "*" },
        })
        .then((res) => {
          elem1.textContent = res.data[0].descs;
        });
    },
  },
  mounted() {
    this.draw();
  },
};
</script>

<style></style>